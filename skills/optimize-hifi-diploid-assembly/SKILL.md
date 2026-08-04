---
name: optimize-hifi-diploid-assembly
version: 1.0.0
description: >
  Activate when an agent must generate, compare, quality-control, or select a diploid
  PacBio HiFi de novo genome assembly using hifiasm; when requests mention HiFi read
  assembly, haplotype-resolved assembly, hifiasm parameter optimization, primary and
  alternate contigs, trio binning, Hi-C phasing, Merqury QV, k-mer completeness, BUSCO,
  QUAST, contamination screening, assembly Pareto ranking, or reproducible assembly QC.
parameters:
  type: object
  additionalProperties: false
  required:
    - hifi_reads
    - output_directory
    - expected_ploidy
    - genome_size_bp
    - busco_lineage
  properties:
    hifi_reads:
      type: array
      minItems: 1
      items:
        type: string
        minLength: 1
        pattern: '^.+\\.(fastq|fq)(\\.gz)?$'
      description: Absolute or workspace-relative PacBio HiFi FASTQ paths.
    output_directory:
      type: string
      minLength: 1
    expected_ploidy:
      type: integer
      const: 2
    genome_size_bp:
      type: integer
      minimum: 1000000
      maximum: 100000000000
    busco_lineage:
      type: string
      pattern: '^[A-Za-z0-9_.-]+_odb[0-9]+$'
    parental_kmer_databases:
      type: object
      additionalProperties: false
      required: [maternal, paternal]
      properties:
        maternal: {type: string, minLength: 1}
        paternal: {type: string, minLength: 1}
    hic_reads:
      type: object
      additionalProperties: false
      required: [read1, read2]
      properties:
        read1: {type: string, pattern: '^.+\\.(fastq|fq)(\\.gz)?$'}
        read2: {type: string, pattern: '^.+\\.(fastq|fq)(\\.gz)?$'}
    reference_fasta:
      type: string
      pattern: '^.+\\.(fa|fasta|fna)(\\.gz)?$'
    candidate_parameter_sets:
      type: array
      minItems: 1
      maxItems: 12
      items:
        type: object
        additionalProperties: false
        required: [id, purge_level]
        properties:
          id: {type: string, pattern: '^[a-z0-9][a-z0-9_-]{0,39}$'}
          purge_level: {type: integer, minimum: 0, maximum: 3}
          hom_cov: {type: integer, minimum: 1, maximum: 1000}
          low_q: {type: integer, minimum: 0, maximum: 100}
          high_q: {type: integer, minimum: 0, maximum: 100}
    threads:
      type: integer
      minimum: 1
      maximum: 512
      default: 32
    minimum_read_q:
      type: number
      minimum: 10
      maximum: 40
      default: 20
    max_total_input_gb:
      type: number
      exclusiveMinimum: 0
    hard_gates:
      type: object
      additionalProperties: false
      properties:
        minimum_merqury_qv: {type: number, minimum: 0, default: 30}
        minimum_kmer_completeness_percent: {type: number, minimum: 0, maximum: 100, default: 90}
        minimum_busco_complete_percent: {type: number, minimum: 0, maximum: 100, default: 90}
        maximum_busco_duplicated_percent: {type: number, minimum: 0, maximum: 100, default: 15}
        maximum_assembly_span_ratio: {type: number, minimum: 1, default: 1.25}
        minimum_assembly_span_ratio: {type: number, exclusiveMinimum: 0, maximum: 1, default: 0.75}
outputs:
  type: object
  required: [status, selected_candidate, candidate_metrics, provenance]
  properties:
    status: {enum: [PASS, REVIEW, FAIL]}
    selected_candidate: {type: [string, 'null']}
    candidate_metrics: {type: array}
    provenance: {type: object}
runtime:
  operating_system: linux
  required_executables:
    - hifiasm
    - seqkit
    - meryl
    - merqury.sh
    - quast.py
    - busco
    - minimap2
    - samtools
  network_access: forbidden-after-tool-installation
  deterministic_environment: container-image-digest-required
safety:
  data_classification: genomic-data-sensitive
  execution_mode: computational-only
  human_review_required: true
---

# Mission

Produce a reproducible, haplotype-aware diploid HiFi assembly comparison; select a candidate only when it passes declared quality gates; and emit complete provenance sufficient to rerun every command byte-for-byte.

# Activation conditions

Use this skill only for PacBio HiFi reads from a nominally diploid isolate or individual. Do not route metagenomes, pooled populations, tumor–normal mixtures, low-accuracy CLR-only reads, or polyploid genomes here. Route those to a different assembly workflow.

# Preconditions and fail-closed checks

1. Resolve every input path and compute SHA-256 checksums before analysis.
2. Verify FASTQ syntax on all records. Reject files containing unequal sequence/quality lengths, truncated records, or non-IUPAC nucleotide symbols other than `N`.
3. Confirm the total input size does not exceed `max_total_input_gb` when supplied.
4. Record exact executable versions and the container image digest. If any required executable is absent or unversioned, stop with `FAIL_TOOLCHAIN`.
5. Require either no phasing auxiliary data, a complete maternal+paternal k-mer pair, or a complete Hi-C read pair. Reject half-specified phasing inputs.
6. Never infer `genome_size_bp`, ploidy, lineage, sex chromosomes, or expected organellar content from filename conventions.

# Deterministic procedure

## Step 1 — Create immutable run manifest

Write `run-manifest.json` containing normalized parameters, input checksums, UTC start time, hostname, CPU/RAM inventory, tool versions, container digest, and a randomly generated run UUID. The UUID identifies artifacts but must not affect algorithmic decisions.

## Step 2 — Profile reads

Run:

```bash
seqkit stats --all --tabular "$READS" > qc/seqkit-stats.tsv
```

For multiple files, process in lexical path order and aggregate only after per-file validation. Calculate:

- total bases and reads;
- read N50 and median length;
- mean and median Phred quality;
- fraction of bases below `minimum_read_q`;
- approximate sequence coverage = total bases / `genome_size_bp`.

Decision rules:

- coverage `< 10×`: stop `FAIL_INSUFFICIENT_COVERAGE`;
- coverage `10–15×`: continue but force final status no better than `REVIEW`;
- coverage `> 300×`: stop and require explicit downsampling strategy because extreme depth can distort compute and assembly behavior;
- more than 5% of bases below Q20: mark `READ_QUALITY_WARNING`.

Do not trim HiFi reads by default. Remove only structurally invalid records or explicitly supplied adapter contamination with a documented tool and rule.

## Step 3 — Build read k-mer database

Choose k deterministically:

- genome `< 500 Mb`: `k=21`;
- `500 Mb–3 Gb`: `k=31`;
- `> 3 Gb`: `k=31` unless the estimated unique k-mer count exceeds implementation limits, then stop for operator review.

Run `meryl count` with the selected k and record the command. Save the database and a histogram. If parental k-mer databases are supplied, verify they use the same k; otherwise stop `FAIL_KMER_SIZE_MISMATCH`.

## Step 4 — Define candidate parameter sets

When `candidate_parameter_sets` is supplied, use exactly those sets in ascending `id` order.

Otherwise create this bounded default sweep:

| Candidate | hifiasm purge level | `--hom-cov` |
|---|---:|---|
| `baseline-p2` | 2 | omitted |
| `conservative-p1` | 1 | omitted |
| `aggressive-p3` | 3 | omitted |

Add `homcov-observed` only when the primary homozygous peak is unambiguous in the k-mer histogram; set `--hom-cov` to the integer peak location and `-l 2`. Never guess a peak from a flat or multimodal histogram.

## Step 5 — Execute hifiasm candidates

For unphased assembly:

```bash
hifiasm -o "$PREFIX" -t "$THREADS" -l "$PURGE_LEVEL" ${HOM_COV_ARG} "$READS"
```

For trio binning, provide the verified parental k-mer inputs using the hifiasm version-specific trio arguments. For Hi-C phasing, provide the paired Hi-C files using version-specific arguments. Before execution, generate the final command from the installed version's help text; if required flags differ from the pinned command template, stop `FAIL_CLI_INCOMPATIBLE` instead of improvising.

Convert selected GFA segments to FASTA without reordering segment identifiers. Preserve primary and haplotype outputs separately. A command failure, empty GFA, duplicate segment ID, or zero-length sequence marks that candidate `INVALID`.

## Step 6 — Evaluate every valid candidate identically

For each candidate, run the following in this order:

1. sequence statistics and assembly span;
2. QUAST without reference, and additionally with `reference_fasta` when supplied;
3. Merqury against the read k-mer database;
4. BUSCO in genome mode using `busco_lineage`;
5. map HiFi reads back with minimap2, sort/index with samtools, and calculate breadth/depth summaries;
6. screen for suspicious taxonomic contamination using an approved local database workflow, if available. If no approved database is available, emit `CONTAMINATION_NOT_ASSESSED` and cap status at `REVIEW`.

Never optimize against N50 alone. Capture at least:

- total assembly span and span/genome-size ratio;
- contig count, N50, L50, longest contig;
- Merqury QV and k-mer completeness;
- BUSCO complete-single, complete-duplicated, fragmented, and missing percentages;
- mapped-read fraction, zero-coverage fraction, and extreme-depth fraction;
- reference-derived misassemblies only when a suitable reference is explicitly provided;
- haplotype switch/error metrics when phasing truth data are available.

## Step 7 — Apply hard gates

A candidate fails if any condition is true:

- Merqury QV below `minimum_merqury_qv`;
- k-mer completeness below `minimum_kmer_completeness_percent`;
- BUSCO complete below `minimum_busco_complete_percent`;
- BUSCO duplicated above `maximum_busco_duplicated_percent`, unless a taxonomically justified whole-genome duplication exception is supplied outside this skill;
- assembly span ratio outside the configured minimum/maximum range;
- more than 1% of assembly bases have zero mapped-read coverage, unless explicitly attributable to verified auxiliary sequences;
- contamination screen reports a critical contaminant above the locally approved threshold;
- output is structurally invalid.

A failed candidate remains in the report but cannot be selected.

## Step 8 — Rank passing candidates

Compute normalized metrics among passing candidates only. Higher is better for QV, completeness, BUSCO single-copy completeness, and contiguity; lower is better for duplicated BUSCO, span deviation, zero-coverage fraction, and reference-supported misassemblies.

Use this deterministic lexicographic ranking, not an opaque weighted score:

1. highest Merqury QV, rounded to 0.01;
2. highest k-mer completeness, rounded to 0.01%;
3. highest BUSCO complete-single percentage, rounded to 0.01%;
4. lowest absolute span-ratio deviation from 1.0, rounded to 0.001;
5. lowest BUSCO duplicated percentage, rounded to 0.01%;
6. highest contig N50;
7. lexical candidate ID.

Select the first candidate. If no candidate passes, emit `FAIL` and `selected_candidate: null`.

## Step 9 — Package outputs

Create:

```text
output_directory/
  run-manifest.json
  candidate-summary.tsv
  decision.json
  qc/
  candidates/<candidate-id>/
  selected/assembly.fasta
  selected/assembly.sha256
  selected/provenance.json
  logs/
```

`decision.json` must contain every gate result, ranking comparison, warning, and the exact reason the winner outranked the runner-up.

# Output contract

Return a JSON object with:

- `status`: `PASS`, `REVIEW`, or `FAIL`;
- `selected_candidate`: candidate ID or null;
- `selected_assembly_path`: path or null;
- `candidate_metrics`: complete metrics for all candidates;
- `hard_gate_results`: per-candidate booleans and reasons;
- `warnings`: ordered unique warning codes;
- `provenance`: hashes, commands, versions, and runtime manifest path.

# Error handling

- Never silently retry with changed biological parameters.
- A transient execution retry may occur once with identical command, inputs, environment, and seed; label it in provenance.
- Preserve partial logs and mark incomplete metrics null with an error code.
- Never select a candidate with missing required QC metrics.

# Validation tests

1. **Schema rejection:** non-diploid ploidy must fail before tool execution.
2. **Truncated FASTQ:** malformed record must produce `FAIL_INPUT_FORMAT`.
3. **No passing candidate:** selection must be null and status `FAIL`.
4. **Tie-break:** equal metrics must resolve by lexical candidate ID.
5. **Tool drift:** changed CLI flags must produce `FAIL_CLI_INCOMPATIBLE`.
6. **Provenance:** deleting any command or checksum must fail repository acceptance tests.

# Safety and scope

This skill analyzes genomic data and may handle sensitive human sequence information. Enforce local privacy, consent, retention, and access-control requirements. It does not make clinical interpretations, identify individuals, or authorize release of an assembly as a reference standard.

# Scientific basis

- Cheng H. et al. Haplotype-resolved de novo assembly using phased assembly graphs with hifiasm. *Nature Methods* 18, 170–175 (2021). DOI: 10.1038/s41592-020-01056-5.
- Rhie A. et al. Merqury: reference-free quality, completeness, and phasing assessment for genome assemblies. *Genome Biology* 21, 245 (2020). DOI: 10.1186/s13059-020-02134-9.
- Gurevich A. et al. QUAST: quality assessment tool for genome assemblies. *Bioinformatics* 29, 1072–1075 (2013). DOI: 10.1093/bioinformatics/btt086.
- Seppey M. et al. BUSCO: assessing genome assembly and annotation completeness. *Methods in Molecular Biology* 1962, 227–245 (2019). DOI: 10.1007/978-1-4939-9173-0_14.
