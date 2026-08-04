# D001 — De Novo Genome Assembly and Polishing

Batch **001** · 10 workstreams · 100 tasks

## 01. Project intake and execution constraints

### MYR-D001-T001 — Validate the assembly project manifest and enforce globally unique sample, library, and run identifiers

Validate the assembly project manifest and enforce globally unique sample, library, and run identifiers.

- **Routing name:** `validate-the-assembly-project-manifest-and-enforce-globally-unique-sample-library-and-run-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T002 — Verify read-file checksums, compression integrity, readability, and declared byte sizes before analysis

Verify read-file checksums, compression integrity, readability, and declared byte sizes before analysis.

- **Routing name:** `verify-read-file-checksums-compression-integrity-readability-and-declared-byte-sizes-before-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T003 — Reconcile library metadata with sequencing-platform tags and read-group headers

Reconcile library metadata with sequencing-platform tags and read-group headers.

- **Routing name:** `reconcile-library-metadata-with-sequencing-platform-tags-and-read-group-headers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T004 — Confirm organism ploidy, expected genome-size range, and known sex-chromosome system

Confirm organism ploidy, expected genome-size range, and known sex-chromosome system.

- **Routing name:** `confirm-organism-ploidy-expected-genome-size-range-and-known-sex-chromosome-system`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T005 — Record required nuclear, organellar, plasmid, and alternate-haplotype assembly outputs

Record required nuclear, organellar, plasmid, and alternate-haplotype assembly outputs.

- **Routing name:** `record-required-nuclear-organellar-plasmid-and-alternate-haplotype-assembly-outputs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T006 — Define the primary, alternate, haplotype-resolved, and unplaced sequence output contract

Define the primary, alternate, haplotype-resolved, and unplaced sequence output contract.

- **Routing name:** `define-the-primary-alternate-haplotype-resolved-and-unplaced-sequence-output-contract`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T007 — Validate the availability and pedigree consistency of parental or trio sequencing data

Validate the availability and pedigree consistency of parental or trio sequencing data.

- **Routing name:** `validate-the-availability-and-pedigree-consistency-of-parental-or-trio-sequencing-data`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T008 — Declare whether assembly must remain reference-free or may use reference-guided scaffolding

Declare whether assembly must remain reference-free or may use reference-guided scaffolding.

- **Routing name:** `declare-whether-assembly-must-remain-reference-free-or-may-use-reference-guided-scaffolding`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T009 — Estimate compute, memory, scratch-storage, and archival requirements from input yield

Estimate compute, memory, scratch-storage, and archival requirements from input yield.

- **Routing name:** `estimate-compute-memory-scratch-storage-and-archival-requirements-from-input-yield`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T010 — Freeze assembler, aligner, polishing-tool, container, and random-seed versions in a run manifest

Freeze assembler, aligner, polishing-tool, container, and random-seed versions in a run manifest.

- **Routing name:** `freeze-assembler-aligner-polishing-tool-container-and-random-seed-versions-in-a-run-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Raw-read quality control

### MYR-D001-T011 — Compute read-count, yield, length quantiles, N50, N90, and maximum-read-length statistics per library

Compute read-count, yield, length quantiles, N50, N90, and maximum-read-length statistics per library.

- **Routing name:** `compute-read-count-yield-length-quantiles-n50-n90-and-maximum-read-length-statistics-per-library`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T012 — Summarize per-read quality-score distributions and quantify yield above declared quality thresholds

Summarize per-read quality-score distributions and quantify yield above declared quality thresholds.

- **Routing name:** `summarize-per-read-quality-score-distributions-and-quantify-yield-above-declared-quality-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T013 — Calculate total sequence yield and provisional physical coverage against the expected genome-size range

Calculate total sequence yield and provisional physical coverage against the expected genome-size range.

- **Routing name:** `calculate-total-sequence-yield-and-provisional-physical-coverage-against-the-expected-genome-size-range`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T014 — Detect residual adapters, primers, barcodes, and ligation artefacts in long-read sequences

Detect residual adapters, primers, barcodes, and ligation artefacts in long-read sequences.

- **Routing name:** `detect-residual-adapters-primers-barcodes-and-ligation-artefacts-in-long-read-sequences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T015 — Identify candidate chimeric reads using split alignments, abrupt composition shifts, or adapter junctions

Identify candidate chimeric reads using split alignments, abrupt composition shifts, or adapter junctions.

- **Routing name:** `identify-candidate-chimeric-reads-using-split-alignments-abrupt-composition-shifts-or-adapter-junctions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T016 — Quantify low-complexity, homopolymer-dominated, and entropy-deficient read fractions

Quantify low-complexity, homopolymer-dominated, and entropy-deficient read fractions.

- **Routing name:** `quantify-low-complexity-homopolymer-dominated-and-entropy-deficient-read-fractions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T017 — Detect duplicated read identifiers and exact duplicate sequences across input files

Detect duplicated read identifiers and exact duplicate sequences across input files.

- **Routing name:** `detect-duplicated-read-identifiers-and-exact-duplicate-sequences-across-input-files`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T018 — Profile nucleotide composition by read position and flag systematic run-specific anomalies

Profile nucleotide composition by read position and flag systematic run-specific anomalies.

- **Routing name:** `profile-nucleotide-composition-by-read-position-and-flag-systematic-run-specific-anomalies`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T019 — Measure quality and length differences across flow cells, lanes, barcodes, or sequencing runs

Measure quality and length differences across flow cells, lanes, barcodes, or sequencing runs.

- **Routing name:** `measure-quality-and-length-differences-across-flow-cells-lanes-barcodes-or-sequencing-runs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T020 — Quarantine corrupted, truncated, malformed, or non-IUPAC read records with explicit reasons

Quarantine corrupted, truncated, malformed, or non-IUPAC read records with explicit reasons.

- **Routing name:** `quarantine-corrupted-truncated-malformed-or-non-iupac-read-records-with-explicit-reasons`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Genome-complexity estimation

### MYR-D001-T021 — Estimate genome size from k-mer spectra using multiple k values and reconcile model disagreement

Estimate genome size from k-mer spectra using multiple k values and reconcile model disagreement.

- **Routing name:** `estimate-genome-size-from-k-mer-spectra-using-multiple-k-values-and-reconcile-model-disagreement`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T022 — Estimate heterozygosity from k-mer multiplicity peaks and report model confidence intervals

Estimate heterozygosity from k-mer multiplicity peaks and report model confidence intervals.

- **Routing name:** `estimate-heterozygosity-from-k-mer-multiplicity-peaks-and-report-model-confidence-intervals`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T023 — Estimate repetitive-sequence fraction and repeat-copy complexity from k-mer spectra

Estimate repetitive-sequence fraction and repeat-copy complexity from k-mer spectra.

- **Routing name:** `estimate-repetitive-sequence-fraction-and-repeat-copy-complexity-from-k-mer-spectra`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T024 — Detect polyploid or aneuploid k-mer patterns inconsistent with the declared ploidy

Detect polyploid or aneuploid k-mer patterns inconsistent with the declared ploidy.

- **Routing name:** `detect-polyploid-or-aneuploid-k-mer-patterns-inconsistent-with-the-declared-ploidy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T025 — Classify taxonomic contamination in reads and quantify contaminant yield by candidate source

Classify taxonomic contamination in reads and quantify contaminant yield by candidate source.

- **Routing name:** `classify-taxonomic-contamination-in-reads-and-quantify-contaminant-yield-by-candidate-source`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T026 — Quantify mitochondrial, chloroplast, plasmid, or other organellar read abundance

Quantify mitochondrial, chloroplast, plasmid, or other organellar read abundance.

- **Routing name:** `quantify-mitochondrial-chloroplast-plasmid-or-other-organellar-read-abundance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T027 — Estimate haplotype divergence using phased k-mers or parental marker separation

Estimate haplotype divergence using phased k-mers or parental marker separation.

- **Routing name:** `estimate-haplotype-divergence-using-phased-k-mers-or-parental-marker-separation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T028 — Detect multimodal coverage distributions consistent with contamination, symbionts, or sex chromosomes

Detect multimodal coverage distributions consistent with contamination, symbionts, or sex chromosomes.

- **Routing name:** `detect-multimodal-coverage-distributions-consistent-with-contamination-symbionts-or-sex-chromosomes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T029 — Assess whether the read-length distribution spans the estimated repeat-length spectrum

Assess whether the read-length distribution spans the estimated repeat-length spectrum.

- **Routing name:** `assess-whether-the-read-length-distribution-spans-the-estimated-repeat-length-spectrum`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T030 — Emit an assembly-complexity risk profile covering repeats, heterozygosity, ploidy, and contamination

Emit an assembly-complexity risk profile covering repeats, heterozygosity, ploidy, and contamination.

- **Routing name:** `emit-an-assembly-complexity-risk-profile-covering-repeats-heterozygosity-ploidy-and-contamination`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Read preprocessing and partitioning

### MYR-D001-T031 — Filter reads below a declared minimum quality while retaining an auditable exclusion manifest

Filter reads below a declared minimum quality while retaining an auditable exclusion manifest.

- **Routing name:** `filter-reads-below-a-declared-minimum-quality-while-retaining-an-auditable-exclusion-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T032 — Filter reads below a declared minimum length and recalculate retained physical coverage

Filter reads below a declared minimum length and recalculate retained physical coverage.

- **Routing name:** `filter-reads-below-a-declared-minimum-length-and-recalculate-retained-physical-coverage`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T033 — Trim confirmed adapter and primer sequences without altering internal biological sequence

Trim confirmed adapter and primer sequences without altering internal biological sequence.

- **Routing name:** `trim-confirmed-adapter-and-primer-sequences-without-altering-internal-biological-sequence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T034 — Split high-confidence chimeric reads at validated junctions and preserve parent-child provenance

Split high-confidence chimeric reads at validated junctions and preserve parent-child provenance.

- **Routing name:** `split-high-confidence-chimeric-reads-at-validated-junctions-and-preserve-parent-child-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T035 — Downsample excessive sequence yield deterministically to a target coverage envelope

Downsample excessive sequence yield deterministically to a target coverage envelope.

- **Routing name:** `downsample-excessive-sequence-yield-deterministically-to-a-target-coverage-envelope`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T036 — Partition reads by library, run, molecule type, or platform for controlled assembly experiments

Partition reads by library, run, molecule type, or platform for controlled assembly experiments.

- **Routing name:** `partition-reads-by-library-run-molecule-type-or-platform-for-controlled-assembly-experiments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T037 — Partition offspring reads by parental k-mers and quantify assigned, ambiguous, and unassigned fractions

Partition offspring reads by parental k-mers and quantify assigned, ambiguous, and unassigned fractions.

- **Routing name:** `partition-offspring-reads-by-parental-k-mers-and-quantify-assigned-ambiguous-and-unassigned-fractions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T038 — Extract organellar-enriched reads using declared seed references or taxonomic classifiers

Extract organellar-enriched reads using declared seed references or taxonomic classifiers.

- **Routing name:** `extract-organellar-enriched-reads-using-declared-seed-references-or-taxonomic-classifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T039 — Create a machine-readable ledger for every excluded, trimmed, split, or reassigned read

Create a machine-readable ledger for every excluded, trimmed, split, or reassigned read.

- **Routing name:** `create-a-machine-readable-ledger-for-every-excluded-trimmed-split-or-reassigned-read`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T040 — Verify post-processing yield, quality, coverage, and identifier uniqueness before assembly

Verify post-processing yield, quality, coverage, and identifier uniqueness before assembly.

- **Routing name:** `verify-post-processing-yield-quality-coverage-and-identifier-uniqueness-before-assembly`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Assembler selection and parameter design

### MYR-D001-T041 — Select an assembler family compatible with read technology, ploidy, heterozygosity, and output requirements

Select an assembler family compatible with read technology, ploidy, heterozygosity, and output requirements.

- **Routing name:** `select-an-assembler-family-compatible-with-read-technology-ploidy-heterozygosity-and-output-requirements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T042 — Define a bounded assembly-parameter grid with explicit candidate count and stopping rules

Define a bounded assembly-parameter grid with explicit candidate count and stopping rules.

- **Routing name:** `define-a-bounded-assembly-parameter-grid-with-explicit-candidate-count-and-stopping-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T043 — Choose the haplotype-purging or haplotype-retention mode appropriate to the requested deliverable

Choose the haplotype-purging or haplotype-retention mode appropriate to the requested deliverable.

- **Routing name:** `choose-the-haplotype-purging-or-haplotype-retention-mode-appropriate-to-the-requested-deliverable`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T044 — Set genome-size and expected-coverage parameters from reconciled complexity estimates

Set genome-size and expected-coverage parameters from reconciled complexity estimates.

- **Routing name:** `set-genome-size-and-expected-coverage-parameters-from-reconciled-complexity-estimates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T045 — Configure optional ultra-long-read support only when sufficient yield and length criteria are met

Configure optional ultra-long-read support only when sufficient yield and length criteria are met.

- **Routing name:** `configure-optional-ultra-long-read-support-only-when-sufficient-yield-and-length-criteria-are-met`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T046 — Configure trio, Hi-C, Strand-seq, or linked-read phasing inputs with compatibility checks

Configure trio, Hi-C, Strand-seq, or linked-read phasing inputs with compatibility checks.

- **Routing name:** `configure-trio-hi-c-strand-seq-or-linked-read-phasing-inputs-with-compatibility-checks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T047 — Set repeat-resolution sensitivity while bounding graph complexity and memory use

Set repeat-resolution sensitivity while bounding graph complexity and memory use.

- **Routing name:** `set-repeat-resolution-sensitivity-while-bounding-graph-complexity-and-memory-use`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T048 — Set minimum overlap or seed-length parameters from the empirical read-length distribution

Set minimum overlap or seed-length parameters from the empirical read-length distribution.

- **Routing name:** `set-minimum-overlap-or-seed-length-parameters-from-the-empirical-read-length-distribution`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T049 — Calculate threads, memory, temporary storage, and wall-time limits for each candidate run

Calculate threads, memory, temporary storage, and wall-time limits for each candidate run.

- **Routing name:** `calculate-threads-memory-temporary-storage-and-wall-time-limits-for-each-candidate-run`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T050 — Generate immutable per-candidate run manifests containing inputs, parameters, tools, and seeds

Generate immutable per-candidate run manifests containing inputs, parameters, tools, and seeds.

- **Routing name:** `generate-immutable-per-candidate-run-manifests-containing-inputs-parameters-tools-and-seeds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Assembly execution and integrity checks

### MYR-D001-T051 — Launch each candidate assembly with fail-fast resource limits and isolated output directories

Launch each candidate assembly with fail-fast resource limits and isolated output directories.

- **Routing name:** `launch-each-candidate-assembly-with-fail-fast-resource-limits-and-isolated-output-directories`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T052 — Capture commands, environment, standard output, standard error, runtime, and peak memory per candidate

Capture commands, environment, standard output, standard error, runtime, and peak memory per candidate.

- **Routing name:** `capture-commands-environment-standard-output-standard-error-runtime-and-peak-memory-per-candidate`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T053 — Detect premature termination, silent truncation, and scheduler eviction from logs and output signatures

Detect premature termination, silent truncation, and scheduler eviction from logs and output signatures.

- **Routing name:** `detect-premature-termination-silent-truncation-and-scheduler-eviction-from-logs-and-output-signatures`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T054 — Verify that expected graph, contig, unitig, and haplotype files exist and are non-empty

Verify that expected graph, contig, unitig, and haplotype files exist and are non-empty.

- **Routing name:** `verify-that-expected-graph-contig-unitig-and-haplotype-files-exist-and-are-non-empty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T055 — Standardize contig identifiers while retaining source-candidate and graph-node provenance

Standardize contig identifiers while retaining source-candidate and graph-node provenance.

- **Routing name:** `standardize-contig-identifiers-while-retaining-source-candidate-and-graph-node-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T056 — Remove zero-length records and reject duplicate contig identifiers before downstream analysis

Remove zero-length records and reject duplicate contig identifiers before downstream analysis.

- **Routing name:** `remove-zero-length-records-and-reject-duplicate-contig-identifiers-before-downstream-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T057 — Validate FASTA alphabet, line formatting, sequence lengths, and checksum stability

Validate FASTA alphabet, line formatting, sequence lengths, and checksum stability.

- **Routing name:** `validate-fasta-alphabet-line-formatting-sequence-lengths-and-checksum-stability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T058 — Compute candidate contig count, total span, N50, NG50, L50, and maximum-contig statistics

Compute candidate contig count, total span, N50, NG50, L50, and maximum-contig statistics.

- **Routing name:** `compute-candidate-contig-count-total-span-n50-ng50-l50-and-maximum-contig-statistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T059 — Extract graph branching, bubble, tip, and unresolved-repeat metrics from assembler graph outputs

Extract graph branching, bubble, tip, and unresolved-repeat metrics from assembler graph outputs.

- **Routing name:** `extract-graph-branching-bubble-tip-and-unresolved-repeat-metrics-from-assembler-graph-outputs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T060 — Quarantine incomplete or structurally invalid candidate assemblies from polishing and ranking

Quarantine incomplete or structurally invalid candidate assemblies from polishing and ranking.

- **Routing name:** `quarantine-incomplete-or-structurally-invalid-candidate-assemblies-from-polishing-and-ranking`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Consensus polishing and error correction

### MYR-D001-T061 — Align source long reads back to each candidate assembly with technology-appropriate presets

Align source long reads back to each candidate assembly with technology-appropriate presets.

- **Routing name:** `align-source-long-reads-back-to-each-candidate-assembly-with-technology-appropriate-presets`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T062 — Detect low-support consensus regions using depth, allele balance, and local alignment quality

Detect low-support consensus regions using depth, allele balance, and local alignment quality.

- **Routing name:** `detect-low-support-consensus-regions-using-depth-allele-balance-and-local-alignment-quality`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T063 — Apply one long-read consensus-polishing iteration with fixed parameters and recorded evidence

Apply one long-read consensus-polishing iteration with fixed parameters and recorded evidence.

- **Routing name:** `apply-one-long-read-consensus-polishing-iteration-with-fixed-parameters-and-recorded-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T064 — Permit a second polishing iteration only when predefined consensus-quality gains are achieved

Permit a second polishing iteration only when predefined consensus-quality gains are achieved.

- **Routing name:** `permit-a-second-polishing-iteration-only-when-predefined-consensus-quality-gains-are-achieved`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T065 — Evaluate homopolymer-length errors separately from substitutions and non-homopolymer indels

Evaluate homopolymer-length errors separately from substitutions and non-homopolymer indels.

- **Routing name:** `evaluate-homopolymer-length-errors-separately-from-substitutions-and-non-homopolymer-indels`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T066 — Compare pre-polish and post-polish error spectra against mapped reads or trusted k-mers

Compare pre-polish and post-polish error spectra against mapped reads or trusted k-mers.

- **Routing name:** `compare-pre-polish-and-post-polish-error-spectra-against-mapped-reads-or-trusted-k-mers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T067 — Apply orthogonal short-read polishing only when contamination and mapping-bias gates pass

Apply orthogonal short-read polishing only when contamination and mapping-bias gates pass.

- **Routing name:** `apply-orthogonal-short-read-polishing-only-when-contamination-and-mapping-bias-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T068 — Prevent cross-haplotype correction by masking or partitioning confidently phased regions

Prevent cross-haplotype correction by masking or partitioning confidently phased regions.

- **Routing name:** `prevent-cross-haplotype-correction-by-masking-or-partitioning-confidently-phased-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T069 — Reject polishing changes that reduce k-mer completeness or increase switch-error indicators

Reject polishing changes that reduce k-mer completeness or increase switch-error indicators.

- **Routing name:** `reject-polishing-changes-that-reduce-k-mer-completeness-or-increase-switch-error-indicators`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T070 — Freeze the accepted polished assembly with content checksums and a change summary

Freeze the accepted polished assembly with content checksums and a change summary.

- **Routing name:** `freeze-the-accepted-polished-assembly-with-content-checksums-and-a-change-summary`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Phasing, deduplication, and scaffolding

### MYR-D001-T071 — Assign contigs or graph paths to parental haplotypes using informative trio markers

Assign contigs or graph paths to parental haplotypes using informative trio markers.

- **Routing name:** `assign-contigs-or-graph-paths-to-parental-haplotypes-using-informative-trio-markers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T072 — Phase contigs with Hi-C contact evidence while detecting trans-contact and repeat artefacts

Phase contigs with Hi-C contact evidence while detecting trans-contact and repeat artefacts.

- **Routing name:** `phase-contigs-with-hi-c-contact-evidence-while-detecting-trans-contact-and-repeat-artefacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T073 — Identify candidate haplotigs using sequence similarity, depth, and allelic correspondence

Identify candidate haplotigs using sequence similarity, depth, and allelic correspondence.

- **Routing name:** `identify-candidate-haplotigs-using-sequence-similarity-depth-and-allelic-correspondence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T074 — Detect collapsed repeats or collapsed homologous regions from abnormal depth and heterozygous k-mers

Detect collapsed repeats or collapsed homologous regions from abnormal depth and heterozygous k-mers.

- **Routing name:** `detect-collapsed-repeats-or-collapsed-homologous-regions-from-abnormal-depth-and-heterozygous-k-mers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T075 — Detect over-purged sequence by loss of single-copy k-mers, BUSCOs, or parental markers

Detect over-purged sequence by loss of single-copy k-mers, BUSCOs, or parental markers.

- **Routing name:** `detect-over-purged-sequence-by-loss-of-single-copy-k-mers-buscos-or-parental-markers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T076 — Scaffold contigs with Hi-C links under minimum support and conflict-resolution rules

Scaffold contigs with Hi-C links under minimum support and conflict-resolution rules.

- **Routing name:** `scaffold-contigs-with-hi-c-links-under-minimum-support-and-conflict-resolution-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T077 — Scaffold contigs with optical-map alignments while preserving unresolved structural conflicts

Scaffold contigs with optical-map alignments while preserving unresolved structural conflicts.

- **Routing name:** `scaffold-contigs-with-optical-map-alignments-while-preserving-unresolved-structural-conflicts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T078 — Detect and circularize organellar or plasmid contigs only when junction support is complete

Detect and circularize organellar or plasmid contigs only when junction support is complete.

- **Routing name:** `detect-and-circularize-organellar-or-plasmid-contigs-only-when-junction-support-is-complete`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T079 — Orient and name chromosome-scale scaffolds using declared evidence without overwriting uncertainty

Orient and name chromosome-scale scaffolds using declared evidence without overwriting uncertainty.

- **Routing name:** `orient-and-name-chromosome-scale-scaffolds-using-declared-evidence-without-overwriting-uncertainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T080 — Emit primary, alternate, haplotype-specific, unplaced, and excluded sequence sets separately

Emit primary, alternate, haplotype-specific, unplaced, and excluded sequence sets separately.

- **Routing name:** `emit-primary-alternate-haplotype-specific-unplaced-and-excluded-sequence-sets-separately`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Assembly evaluation and candidate ranking

### MYR-D001-T081 — Evaluate contiguity and structural consistency with reference-free and optional reference-based metrics

Evaluate contiguity and structural consistency with reference-free and optional reference-based metrics.

- **Routing name:** `evaluate-contiguity-and-structural-consistency-with-reference-free-and-optional-reference-based-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T082 — Estimate consensus quality value from trusted k-mer concordance and report excluded k-mer classes

Estimate consensus quality value from trusted k-mer concordance and report excluded k-mer classes.

- **Routing name:** `estimate-consensus-quality-value-from-trusted-k-mer-concordance-and-report-excluded-k-mer-classes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T083 — Measure k-mer completeness separately for maternal, paternal, shared, and assembly-specific k-mers

Measure k-mer completeness separately for maternal, paternal, shared, and assembly-specific k-mers.

- **Routing name:** `measure-k-mer-completeness-separately-for-maternal-paternal-shared-and-assembly-specific-k-mers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T084 — Assess conserved single-copy gene completeness, duplication, fragmentation, and missingness

Assess conserved single-copy gene completeness, duplication, fragmentation, and missingness.

- **Routing name:** `assess-conserved-single-copy-gene-completeness-duplication-fragmentation-and-missingness`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T085 — Screen assembled contigs for taxonomic contamination and anomalous nucleotide composition

Screen assembled contigs for taxonomic contamination and anomalous nucleotide composition.

- **Routing name:** `screen-assembled-contigs-for-taxonomic-contamination-and-anomalous-nucleotide-composition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T086 — Measure read-mapping completeness, depth uniformity, discordance, and uncovered sequence

Measure read-mapping completeness, depth uniformity, discordance, and uncovered sequence.

- **Routing name:** `measure-read-mapping-completeness-depth-uniformity-discordance-and-uncovered-sequence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T087 — Compare candidate structures against optical maps, linkage maps, or trusted references when available

Compare candidate structures against optical maps, linkage maps, or trusted references when available.

- **Routing name:** `compare-candidate-structures-against-optical-maps-linkage-maps-or-trusted-references-when-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T088 — Estimate switch error, haplotype block length, and parental-marker consistency

Estimate switch error, haplotype block length, and parental-marker consistency.

- **Routing name:** `estimate-switch-error-haplotype-block-length-and-parental-marker-consistency`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T089 — Assess telomere, centromere, rDNA, and other declared difficult-region completeness

Assess telomere, centromere, rDNA, and other declared difficult-region completeness.

- **Routing name:** `assess-telomere-centromere-rdna-and-other-declared-difficult-region-completeness`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T090 — Pareto-rank candidate assemblies across consensus, completeness, contiguity, phasing, and contamination metrics

Pareto-rank candidate assemblies across consensus, completeness, contiguity, phasing, and contamination metrics.

- **Routing name:** `pareto-rank-candidate-assemblies-across-consensus-completeness-contiguity-phasing-and-contamination-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Release, provenance, and review gates

### MYR-D001-T091 — Select the winning assembly using predefined hard gates and deterministic tie-breaking rules

Select the winning assembly using predefined hard gates and deterministic tie-breaking rules.

- **Routing name:** `select-the-winning-assembly-using-predefined-hard-gates-and-deterministic-tie-breaking-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T092 — Generate release FASTA, GFA, AGP, gap, and sequence-dictionary files required by downstream users

Generate release FASTA, GFA, AGP, gap, and sequence-dictionary files required by downstream users.

- **Routing name:** `generate-release-fasta-gfa-agp-gap-and-sequence-dictionary-files-required-by-downstream-users`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T093 — Produce a machine-readable assembly report containing metrics, thresholds, failures, and rationale

Produce a machine-readable assembly report containing metrics, thresholds, failures, and rationale.

- **Routing name:** `produce-a-machine-readable-assembly-report-containing-metrics-thresholds-failures-and-rationale`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T094 — Export excluded contigs with contamination, duplication, organellar, or low-support reason codes

Export excluded contigs with contamination, duplication, organellar, or low-support reason codes.

- **Routing name:** `export-excluded-contigs-with-contamination-duplication-organellar-or-low-support-reason-codes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T095 — Record full input, tool, container, parameter, environment, and checksum provenance

Record full input, tool, container, parameter, environment, and checksum provenance.

- **Routing name:** `record-full-input-tool-container-parameter-environment-and-checksum-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T096 — Generate a reproducibility command or workflow bundle for the selected assembly

Generate a reproducibility command or workflow bundle for the selected assembly.

- **Routing name:** `generate-a-reproducibility-command-or-workflow-bundle-for-the-selected-assembly`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T097 — Validate checksums and cross-file identifier consistency across all release artifacts

Validate checksums and cross-file identifier consistency across all release artifacts.

- **Routing name:** `validate-checksums-and-cross-file-identifier-consistency-across-all-release-artifacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T098 — Archive logs, candidate manifests, QC tables, and ranking evidence under retention rules

Archive logs, candidate manifests, QC tables, and ranking evidence under retention rules.

- **Routing name:** `archive-logs-candidate-manifests-qc-tables-and-ranking-evidence-under-retention-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T099 — Issue explicit human-review flags for unresolved ploidy, contamination, phasing, or structural conflicts

Issue explicit human-review flags for unresolved ploidy, contamination, phasing, or structural conflicts.

- **Routing name:** `issue-explicit-human-review-flags-for-unresolved-ploidy-contamination-phasing-or-structural-conflicts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D001-T100 — Release the assembly only when every mandatory gate passes or an authorized waiver is recorded

Release the assembly only when every mandatory gate passes or an authorized waiver is recorded.

- **Routing name:** `release-the-assembly-only-when-every-mandatory-gate-passes-or-an-authorized-waiver-is-recorded`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
