---
name: score-variant-aware-crispr-offtargets
version: 1.0.0
description: >
  Activate when an agent must enumerate, annotate, compare, or rank potential CRISPR
  nuclease off-target sites while accounting for germline variants or sample-specific
  haplotypes; when requests mention Cas-OFFinder, CRISPRitz, SpCas9 NGG, PAM-aware
  search, CFD score, mismatch position weights, DNA or RNA bulges, personalized genome,
  VCF-aware guide specificity, GUIDE-seq candidate prioritization, or off-target risk tables.
parameters:
  type: object
  additionalProperties: false
  required:
    - guides
    - nuclease
    - reference_fasta
    - reference_build
    - output_directory
  properties:
    guides:
      type: array
      minItems: 1
      maxItems: 10000
      items:
        type: object
        additionalProperties: false
        required: [guide_id, spacer]
        properties:
          guide_id: {type: string, pattern: '^[A-Za-z0-9][A-Za-z0-9_.-]{0,79}$'}
          spacer: {type: string, pattern: '^[ACGTUacgtu]{17,24}$'}
    nuclease:
      type: object
      additionalProperties: false
      required: [name, spacer_length, pam_pattern, pam_side]
      properties:
        name: {type: string, pattern: '^[A-Za-z0-9_.+-]{2,50}$'}
        spacer_length: {type: integer, minimum: 15, maximum: 30}
        pam_pattern: {type: string, pattern: '^[ACGTRYSWKMBDHVNacgtryswkmbdhvn]{2,12}$'}
        pam_side: {enum: [3prime, 5prime]}
    reference_fasta:
      type: string
      pattern: '^.+\\.(fa|fasta|fna)(\\.gz)?$'
    reference_build:
      type: string
      minLength: 1
    sample_vcf:
      type: string
      pattern: '^.+\\.(vcf|vcf\\.gz|bcf)$'
    sample_id:
      type: string
      pattern: '^[A-Za-z0-9][A-Za-z0-9_.-]{0,99}$'
    gene_annotation:
      type: string
      pattern: '^.+\\.(gff|gff3|gtf)(\\.gz)?$'
    regulatory_annotation_bed:
      type: string
      pattern: '^.+\\.(bed|bed\\.gz)$'
    max_mismatches:
      type: integer
      minimum: 0
      maximum: 8
      default: 4
    max_dna_bulges:
      type: integer
      minimum: 0
      maximum: 3
      default: 0
    max_rna_bulges:
      type: integer
      minimum: 0
      maximum: 3
      default: 0
    scoring_models:
      type: array
      minItems: 1
      uniqueItems: true
      items:
        enum: [CFD, mismatch-count, pam-tier, consequence-tier]
      default: [CFD, mismatch-count, pam-tier, consequence-tier]
    output_directory:
      type: string
      minLength: 1
    threads:
      type: integer
      minimum: 1
      maximum: 512
      default: 16
outputs:
  type: object
  required: [status, guide_summaries, off_targets, provenance]
  properties:
    status: {enum: [PASS, REVIEW, FAIL]}
    guide_summaries: {type: array}
    off_targets: {type: array}
    provenance: {type: object}
runtime:
  operating_system: linux
  required_executables:
    - samtools
    - bcftools
    - tabix
  optional_executables:
    - cas-offinder
    - CRISPRitz.py
    - bedtools
  network_access: forbidden-after-reference-acquisition
  deterministic_environment: container-image-digest-required
safety:
  data_classification: genomic-data-sensitive
  execution_mode: prediction-and-prioritization-only
  clinical_use: prohibited-without-independent-validation
---

# Mission

Generate an auditable list of reference- and variant-created candidate off-target sites, apply only scientifically applicable scoring models, annotate genomic consequence, and rank loci for review without presenting computational predictions as experimental evidence.

# Activation conditions

Use for sequence-specificity analysis of declared CRISPR nucleases against a declared reference build. Do not use for guide synthesis, delivery design, wet-lab editing instructions, clinical release decisions, or autonomous experimental execution.

# Preconditions and fail-closed checks

1. Normalize every spacer to uppercase DNA alphabet by converting `U` to `T`.
2. Require spacer length to equal `nuclease.spacer_length`; reject rather than truncate or pad.
3. Expand IUPAC PAM symbols only for search matching. Preserve the original PAM expression in provenance.
4. Verify FASTA index integrity and calculate reference SHA-256.
5. Require a reference-build identifier and confirm VCF contig names are reconcilable to FASTA contigs through an explicit mapping. Never guess mappings such as adding or stripping `chr` without recording the rule.
6. If `sample_vcf` contains multiple samples, require `sample_id`. If phased haplotypes are requested but genotypes are unphased, mark personalized results `REVIEW_UNPHASED`; do not invent phase.
7. Reject symbolic variants, breakends, or variants exceeding the local augmentation capability unless they are separately handled and reported as not assessed.
8. Record tool versions, command lines, model versions, reference hashes, annotation hashes, and container digest.

# Deterministic procedure

## Step 1 — Canonicalize and validate inputs

For each guide, create:

- `spacer_dna`;
- reverse complement;
- length;
- GC fraction;
- homopolymer-run warning when any base run is 5 or more;
- duplicate-sequence group.

Duplicate guide sequences may be retained under multiple IDs, but compute search results once and fan out deterministically.

## Step 2 — Normalize variants

When a VCF/BCF is supplied:

```bash
bcftools norm -f reference.fa -m -any input.vcf.gz -Oz -o normalized.vcf.gz
tabix -p vcf normalized.vcf.gz
```

Then:

1. retain PASS variants by default; list non-PASS variants excluded;
2. restrict to the requested sample genotype;
3. split multiallelic records;
4. left-align and trim alleles;
5. verify REF alleles against FASTA;
6. classify SNVs, insertions, deletions, and unsupported structural alleles;
7. retain genotype and phase-set provenance.

A REF mismatch stops personalized analysis for the affected contig and produces `FAIL_VARIANT_REFERENCE_MISMATCH` for that contig.

## Step 3 — Enumerate reference candidates

Choose one approved engine:

- Cas-OFFinder for flexible mismatch/PAM enumeration;
- CRISPRitz when variant-aware and bulge-aware searching is required and the installed version is validated.

The engine configuration must explicitly encode spacer length, PAM side, PAM pattern, mismatch limit, DNA bulge limit, and RNA bulge limit. Search both strands. Coordinate output must be converted to 0-based half-open BED and 1-based human-readable coordinates, with strand and reference-build fields.

If neither engine is installed, a local exact enumerator may be used only for `max_mismatches <= 4` and no bulges. Its test suite must demonstrate equivalence on a fixed synthetic genome before use.

## Step 4 — Enumerate variant-created and variant-destroyed candidates

Preferred mode: use a validated variant-aware engine on the normalized VCF.

Fallback mode for SNVs and small indels:

1. identify every reference protospacer/PAM window intersecting a sample variant plus enough flank to cover the complete target window;
2. construct each observed allele sequence, and phased haplotype sequences when phase is available;
3. rescan the altered window for PAM-compatible sites;
4. label each site as `reference-retained`, `variant-created`, `variant-destroyed`, or `allele-score-changed`;
5. deduplicate by build, contig, start, end, strand, altered allele, guide ID, and bulge representation.

Do not project coordinates through unsupported large structural variants. Report them separately as `not_assessed_structural_variant`.

## Step 5 — Represent alignment features

For each candidate, store:

- guide and target sequence in guide orientation;
- PAM sequence and PAM class;
- mismatch count;
- ordered mismatch tuples `(guide_position_1_based, guide_base, target_base)`;
- DNA/RNA bulge count and positions;
- strand and genomic coordinates;
- reference or variant allele provenance;
- genotype, allele fraction if present, and phase set;
- whether the candidate overlaps multiple variant combinations.

Guide position 1 is PAM-distal and the last guide position is PAM-proximal for 3-prime PAM nucleases. For 5-prime PAM nucleases, define and document the orientation before scoring; do not reuse SpCas9 positional weights automatically.

## Step 6 — Apply scoring models with applicability gates

### CFD

Apply CFD only when all are true:

- nuclease is the validated SpCas9 model;
- spacer length is 20 nt;
- PAM model is compatible with the model's supported PAM table;
- candidate contains substitutions only, with no DNA or RNA bulge;
- every mismatch substitution and position has a defined weight.

Calculate the product of position/substitution mismatch weights and PAM weight using the pinned model table. Store the table version and every multiplicand. If any condition fails, set `cfd_score: null` and an explicit reason; never approximate CFD for unsupported nucleases or bulges.

### Mismatch-count tier

Assign deterministic tiers:

- `T0`: exact spacer match with accepted PAM;
- `T1`: 1 mismatch;
- `T2`: 2 mismatches;
- `T3`: 3 mismatches;
- `T4`: 4 or more mismatches;
- `TB`: any bulge.

This tier is descriptive, not a cleavage probability.

### PAM tier

Classify PAMs using a user- or nuclease-specific approved table. If no table is supplied beyond the IUPAC pattern, use only `accepted` versus `not-accepted`; do not invent relative activity.

### Consequence tier

Using supplied annotations, assign the most severe overlapping category in this order:

1. coding exon;
2. splice-region;
3. promoter or supplied regulatory element;
4. noncoding exon;
5. intron;
6. intergenic;
7. annotation unavailable.

This is a prioritization category, not a clinical pathogenicity assertion.

## Step 7 — Aggregate guide-level specificity

For each guide, report:

- count by mismatch tier, PAM tier, consequence tier, and variant status;
- maximum applicable CFD score among non-on-target candidates;
- sum of applicable CFD scores, clearly labeled a heuristic aggregate;
- number of exact alternate-locus matches;
- number of variant-created candidates;
- number of coding/splice candidates;
- fraction of candidates lacking a supported quantitative score.

Do not collapse exact alternate-locus matches into a benign aggregate. Any non-on-target exact match forces guide status `HIGH_RISK_EXACT_MATCH`.

## Step 8 — Rank off-target candidates

Use this lexicographic order:

1. exact alternate-locus match first;
2. coding exon, splice-region, regulatory, noncoding exon, intron, intergenic, unknown;
3. variant-created before reference-retained when genotype indicates the allele is present;
4. higher CFD score where applicable;
5. fewer mismatches;
6. accepted stronger PAM tier where a validated table exists;
7. fewer total bulges;
8. contig natural sort, coordinate, strand, target sequence.

Ranked output must preserve candidates without CFD rather than dropping them.

## Step 9 — Produce validation-prioritization panel

For each guide, propose an analysis panel containing:

- all exact alternate-locus matches;
- top ten ranked quantitative-risk candidates;
- all coding/splice candidates within search bounds;
- all variant-created candidates within the top fifty;
- at least one low-risk negative candidate when available;
- the intended on-target locus when supplied elsewhere by the caller.

Label this a computational prioritization panel. It is not evidence of cleavage and must not replace empirical off-target assessment.

# Quality gates

Status is `FAIL` when:

- reference or guide schema is invalid;
- VCF REF alleles disagree with FASTA for a material portion of analyzed regions;
- search engine exits nonzero or returns malformed coordinates;
- candidate enumeration omits a tested synthetic positive control;
- provenance lacks model/table versions.

Status is at most `REVIEW` when:

- variants are unphased but haplotype-specific interpretation matters;
- structural variants are not assessed;
- gene/regulatory annotation is absent;
- more than 20% of top fifty candidates lack an applicable quantitative model;
- only a mismatch-count fallback was available.

# Output contract

Write:

```text
output_directory/
  run-manifest.json
  normalized-guides.tsv
  normalized-variants.vcf.gz
  off-targets.tsv.gz
  off-targets.jsonl.gz
  guide-summary.json
  validation-prioritization.tsv
  logs/
```

Every off-target row must include guide ID, reference build, coordinates, strand, target, PAM, mismatch representation, bulges, allele status, genotype/phase, annotation, all scores with applicability reasons, rank, and provenance pointer.

# Error handling

- Do not silently discard malformed or unsupported candidates.
- Do not impute missing genotypes, phase, PAM activity, or quantitative scores.
- One deterministic retry with identical command is allowed for transient tool failure.
- Preserve raw engine output and parser error context.

# Validation tests

1. Perfect on-target and one-mismatch synthetic loci are both recovered.
2. A heterozygous SNV that creates an NGG PAM is labeled `variant-created`.
3. A REF mismatch in VCF causes a fail-closed result for that contig.
4. CFD is null for bulged candidates and unsupported nucleases.
5. Reverse-strand coordinates reproduce the original target sequence.
6. Duplicate engine rows collapse only when the complete biological identity key matches.
7. Exact alternate-locus match always ranks above lower-risk mismatched candidates.

# Safety and scope

Predictions may be incomplete and model performance is context-dependent. Results require independent experimental confirmation, especially for therapeutic, reproductive, environmental-release, or clinical applications. Protect sample-specific genomic data as sensitive personal data where applicable.

# Scientific basis

- Bae S., Park J., Kim J.-S. Cas-OFFinder: a fast and versatile algorithm that searches for potential off-target sites of Cas9 RNA-guided endonucleases. *Bioinformatics* 30, 1473–1475 (2014). DOI: 10.1093/bioinformatics/btu048.
- Cancellieri S. et al. CRISPRitz: rapid, high-throughput and variant-aware in silico off-target site identification for CRISPR genome editing. *Bioinformatics* 36, 2001–2008 (2020). DOI: 10.1093/bioinformatics/btz867.
- Doench J.G. et al. Optimized sgRNA design to maximize activity and minimize off-target effects of CRISPR-Cas9. *Nature Biotechnology* 34, 184–191 (2016). DOI: 10.1038/nbt.3437.
- Tsai S.Q. et al. GUIDE-seq enables genome-wide profiling of off-target cleavage by CRISPR-Cas nucleases. *Nature Biotechnology* 33, 187–197 (2015). DOI: 10.1038/nbt.3117.
