# D011 — Bulk RNA Sequencing and Differential Expression

Batch **002** · 10 workstreams · 100 tasks

## 01. Study intake and statistical design

### MYR-D011-T001 — Validate the bulk RNA-seq sample manifest and enforce unique sample, library, lane, and biological-replicate identifiers

Validate the bulk RNA-seq sample manifest and enforce unique sample, library, lane, and biological-replicate identifiers.

- **Routing name:** `validate-the-bulk-rna-seq-sample-manifest-and-enforce-unique-sample-library-lane-and-biological-replicate-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T002 — Reconcile declared conditions, batches, subjects, tissues, time points, and covariates against the experimental design

Reconcile declared conditions, batches, subjects, tissues, time points, and covariates against the experimental design.

- **Routing name:** `reconcile-declared-conditions-batches-subjects-tissues-time-points-and-covariates-against-the-experimental-design`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T003 — Distinguish biological replicates, technical replicates, repeated measures, and pooled specimens in the design matrix

Distinguish biological replicates, technical replicates, repeated measures, and pooled specimens in the design matrix.

- **Routing name:** `distinguish-biological-replicates-technical-replicates-repeated-measures-and-pooled-specimens-in-the-design-matrix`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T004 — Verify that every requested contrast is estimable from the declared groups and covariates

Verify that every requested contrast is estimable from the declared groups and covariates.

- **Routing name:** `verify-that-every-requested-contrast-is-estimable-from-the-declared-groups-and-covariates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T005 — Detect complete or near-complete confounding between biological conditions and technical batches

Detect complete or near-complete confounding between biological conditions and technical batches.

- **Routing name:** `detect-complete-or-near-complete-confounding-between-biological-conditions-and-technical-batches`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T006 — Record library preparation chemistry, strandedness, RNA selection method, read layout, and sequencing platform

Record library preparation chemistry, strandedness, RNA selection method, read layout, and sequencing platform.

- **Routing name:** `record-library-preparation-chemistry-strandedness-rna-selection-method-read-layout-and-sequencing-platform`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T007 — Validate reference genome and transcript annotation compatibility with organism, strain, assembly build, and gene identifiers

Validate reference genome and transcript annotation compatibility with organism, strain, assembly build, and gene identifiers.

- **Routing name:** `validate-reference-genome-and-transcript-annotation-compatibility-with-organism-strain-assembly-build-and-gene-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T008 — Define primary endpoints, effect-size thresholds, false-discovery targets, and independent-filtering policy before testing

Define primary endpoints, effect-size thresholds, false-discovery targets, and independent-filtering policy before testing.

- **Routing name:** `define-primary-endpoints-effect-size-thresholds-false-discovery-targets-and-independent-filtering-policy-before-testing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T009 — Estimate design-matrix rank and flag underpowered interaction, paired, or longitudinal terms

Estimate design-matrix rank and flag underpowered interaction, paired, or longitudinal terms.

- **Routing name:** `estimate-design-matrix-rank-and-flag-underpowered-interaction-paired-or-longitudinal-terms`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T010 — Freeze input checksums, software versions, random seeds, and contrast definitions in an immutable analysis manifest

Freeze input checksums, software versions, random seeds, and contrast definitions in an immutable analysis manifest.

- **Routing name:** `freeze-input-checksums-software-versions-random-seeds-and-contrast-definitions-in-an-immutable-analysis-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Raw-read quality and identity control

### MYR-D011-T011 — Verify FASTQ checksums, compression integrity, record pairing, and read-identifier synchronization

Verify FASTQ checksums, compression integrity, record pairing, and read-identifier synchronization.

- **Routing name:** `verify-fastq-checksums-compression-integrity-record-pairing-and-read-identifier-synchronization`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T012 — Summarize per-base sequence quality, read length, nucleotide composition, and ambiguous-base rates per library

Summarize per-base sequence quality, read length, nucleotide composition, and ambiguous-base rates per library.

- **Routing name:** `summarize-per-base-sequence-quality-read-length-nucleotide-composition-and-ambiguous-base-rates-per-library`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T013 — Detect adapter, primer, poly-G, poly-A, and other library-construction sequence contamination

Detect adapter, primer, poly-G, poly-A, and other library-construction sequence contamination.

- **Routing name:** `detect-adapter-primer-poly-g-poly-a-and-other-library-construction-sequence-contamination`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T014 — Quantify overrepresented sequences, low-complexity reads, and exact or near-exact duplicate fractions

Quantify overrepresented sequences, low-complexity reads, and exact or near-exact duplicate fractions.

- **Routing name:** `quantify-overrepresented-sequences-low-complexity-reads-and-exact-or-near-exact-duplicate-fractions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T015 — Screen reads for ribosomal RNA, mitochondrial RNA, vector, microbial, and cross-species contamination

Screen reads for ribosomal RNA, mitochondrial RNA, vector, microbial, and cross-species contamination.

- **Routing name:** `screen-reads-for-ribosomal-rna-mitochondrial-rna-vector-microbial-and-cross-species-contamination`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T016 — Infer library strandedness from a representative read subset and compare it with the declared protocol

Infer library strandedness from a representative read subset and compare it with the declared protocol.

- **Routing name:** `infer-library-strandedness-from-a-representative-read-subset-and-compare-it-with-the-declared-protocol`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T017 — Compare read-quality profiles across lanes, flow cells, sequencing runs, and experimental groups

Compare read-quality profiles across lanes, flow cells, sequencing runs, and experimental groups.

- **Routing name:** `compare-read-quality-profiles-across-lanes-flow-cells-sequencing-runs-and-experimental-groups`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T018 — Detect sample swaps or gross identity mismatches using expressed genotype markers when matched genotypes are available

Detect sample swaps or gross identity mismatches using expressed genotype markers when matched genotypes are available.

- **Routing name:** `detect-sample-swaps-or-gross-identity-mismatches-using-expressed-genotype-markers-when-matched-genotypes-are-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T019 — Estimate saturation and gene-detection curves from deterministic read subsampling

Estimate saturation and gene-detection curves from deterministic read subsampling.

- **Routing name:** `estimate-saturation-and-gene-detection-curves-from-deterministic-read-subsampling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T020 — Quarantine malformed, truncated, orphaned, or non-IUPAC records with explicit exclusion reason codes

Quarantine malformed, truncated, orphaned, or non-IUPAC records with explicit exclusion reason codes.

- **Routing name:** `quarantine-malformed-truncated-orphaned-or-non-iupac-records-with-explicit-exclusion-reason-codes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Read preprocessing and contamination control

### MYR-D011-T021 — Trim confirmed adapters and primers using chemistry-specific sequence definitions and minimum overlap rules

Trim confirmed adapters and primers using chemistry-specific sequence definitions and minimum overlap rules.

- **Routing name:** `trim-confirmed-adapters-and-primers-using-chemistry-specific-sequence-definitions-and-minimum-overlap-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T022 — Remove low-quality terminal bases while preserving a declared minimum retained read length

Remove low-quality terminal bases while preserving a declared minimum retained read length.

- **Routing name:** `remove-low-quality-terminal-bases-while-preserving-a-declared-minimum-retained-read-length`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T023 — Filter reads dominated by ambiguous bases or low sequence complexity using fixed thresholds

Filter reads dominated by ambiguous bases or low sequence complexity using fixed thresholds.

- **Routing name:** `filter-reads-dominated-by-ambiguous-bases-or-low-sequence-complexity-using-fixed-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T024 — Remove ribosomal RNA reads only when the protocol and analysis objective justify depletion

Remove ribosomal RNA reads only when the protocol and analysis objective justify depletion.

- **Routing name:** `remove-ribosomal-rna-reads-only-when-the-protocol-and-analysis-objective-justify-depletion`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T025 — Separate reads assigned to declared spike-ins before endogenous transcript quantification

Separate reads assigned to declared spike-ins before endogenous transcript quantification.

- **Routing name:** `separate-reads-assigned-to-declared-spike-ins-before-endogenous-transcript-quantification`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T026 — Partition mixed-species reads against a combined reference and quantify cross-mapping ambiguity

Partition mixed-species reads against a combined reference and quantify cross-mapping ambiguity.

- **Routing name:** `partition-mixed-species-reads-against-a-combined-reference-and-quantify-cross-mapping-ambiguity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T027 — Deduplicate UMI-tagged reads with protocol-appropriate directional or adjacency rules

Deduplicate UMI-tagged reads with protocol-appropriate directional or adjacency rules.

- **Routing name:** `deduplicate-umi-tagged-reads-with-protocol-appropriate-directional-or-adjacency-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T028 — Preserve non-UMI duplicates while reporting duplication metrics instead of deleting biological signal

Preserve non-UMI duplicates while reporting duplication metrics instead of deleting biological signal.

- **Routing name:** `preserve-non-umi-duplicates-while-reporting-duplication-metrics-instead-of-deleting-biological-signal`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T029 — Merge resequenced lanes for the same library only after read-group and metadata reconciliation

Merge resequenced lanes for the same library only after read-group and metadata reconciliation.

- **Routing name:** `merge-resequenced-lanes-for-the-same-library-only-after-read-group-and-metadata-reconciliation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T030 — Recompute retained read counts, yield, pair concordance, and contamination estimates after preprocessing

Recompute retained read counts, yield, pair concordance, and contamination estimates after preprocessing.

- **Routing name:** `recompute-retained-read-counts-yield-pair-concordance-and-contamination-estimates-after-preprocessing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Alignment and transcript quantification

### MYR-D011-T031 — Build or verify a splice-aware genome index from the frozen genome and annotation versions

Build or verify a splice-aware genome index from the frozen genome and annotation versions.

- **Routing name:** `build-or-verify-a-splice-aware-genome-index-from-the-frozen-genome-and-annotation-versions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T032 — Align reads with declared strandedness, read-group metadata, and maximum multimapping constraints

Align reads with declared strandedness, read-group metadata, and maximum multimapping constraints.

- **Routing name:** `align-reads-with-declared-strandedness-read-group-metadata-and-maximum-multimapping-constraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T033 — Quantify uniquely mapped, multimapped, unmapped, chimeric, and discordant read fractions per sample

Quantify uniquely mapped, multimapped, unmapped, chimeric, and discordant read fractions per sample.

- **Routing name:** `quantify-uniquely-mapped-multimapped-unmapped-chimeric-and-discordant-read-fractions-per-sample`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T034 — Measure exon, intron, intergenic, ribosomal, and mitochondrial alignment distributions

Measure exon, intron, intergenic, ribosomal, and mitochondrial alignment distributions.

- **Routing name:** `measure-exon-intron-intergenic-ribosomal-and-mitochondrial-alignment-distributions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T035 — Generate coordinate-sorted indexed alignments with validated headers and reference dictionaries

Generate coordinate-sorted indexed alignments with validated headers and reference dictionaries.

- **Routing name:** `generate-coordinate-sorted-indexed-alignments-with-validated-headers-and-reference-dictionaries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T036 — Quantify gene-level counts using a strandedness-aware exon assignment policy

Quantify gene-level counts using a strandedness-aware exon assignment policy.

- **Routing name:** `quantify-gene-level-counts-using-a-strandedness-aware-exon-assignment-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T037 — Quantify transcript-level abundance with bias correction and retained inferential uncertainty when supported

Quantify transcript-level abundance with bias correction and retained inferential uncertainty when supported.

- **Routing name:** `quantify-transcript-level-abundance-with-bias-correction-and-retained-inferential-uncertainty-when-supported`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T038 — Import transcript estimates to gene level using an explicit transcript-to-gene mapping

Import transcript estimates to gene level using an explicit transcript-to-gene mapping.

- **Routing name:** `import-transcript-estimates-to-gene-level-using-an-explicit-transcript-to-gene-mapping`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T039 — Compare alignment-based and lightweight-mapping abundance estimates on a bounded validation subset

Compare alignment-based and lightweight-mapping abundance estimates on a bounded validation subset.

- **Routing name:** `compare-alignment-based-and-lightweight-mapping-abundance-estimates-on-a-bounded-validation-subset`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T040 — Reject or flag samples with incompatible annotation overlap, extreme multimapping, or insufficient assigned reads

Reject or flag samples with incompatible annotation overlap, extreme multimapping, or insufficient assigned reads.

- **Routing name:** `reject-or-flag-samples-with-incompatible-annotation-overlap-extreme-multimapping-or-insufficient-assigned-reads`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Expression matrix quality control

### MYR-D011-T041 — Validate count-matrix dimensions, integer constraints, sample ordering, and gene-identifier uniqueness

Validate count-matrix dimensions, integer constraints, sample ordering, and gene-identifier uniqueness.

- **Routing name:** `validate-count-matrix-dimensions-integer-constraints-sample-ordering-and-gene-identifier-uniqueness`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T042 — Remove annotation rows lacking valid genomic or transcript mappings while preserving an exclusion ledger

Remove annotation rows lacking valid genomic or transcript mappings while preserving an exclusion ledger.

- **Routing name:** `remove-annotation-rows-lacking-valid-genomic-or-transcript-mappings-while-preserving-an-exclusion-ledger`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T043 — Summarize library size, detected genes, zero fraction, and abundance distribution per sample

Summarize library size, detected genes, zero fraction, and abundance distribution per sample.

- **Routing name:** `summarize-library-size-detected-genes-zero-fraction-and-abundance-distribution-per-sample`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T044 — Calculate sample-to-sample correlations on variance-stabilized expression values

Calculate sample-to-sample correlations on variance-stabilized expression values.

- **Routing name:** `calculate-sample-to-sample-correlations-on-variance-stabilized-expression-values`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T045 — Perform principal-component analysis and quantify association of leading components with known covariates

Perform principal-component analysis and quantify association of leading components with known covariates.

- **Routing name:** `perform-principal-component-analysis-and-quantify-association-of-leading-components-with-known-covariates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T046 — Detect expression outliers using robust distance, connectivity, and replicate-consistency metrics

Detect expression outliers using robust distance, connectivity, and replicate-consistency metrics.

- **Routing name:** `detect-expression-outliers-using-robust-distance-connectivity-and-replicate-consistency-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T047 — Assess sex-linked, tissue-specific, and lineage-marker expression for sample-identity plausibility

Assess sex-linked, tissue-specific, and lineage-marker expression for sample-identity plausibility.

- **Routing name:** `assess-sex-linked-tissue-specific-and-lineage-marker-expression-for-sample-identity-plausibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T048 — Quantify mitochondrial, ribosomal, immunoglobulin, and other dominant biotype fractions

Quantify mitochondrial, ribosomal, immunoglobulin, and other dominant biotype fractions.

- **Routing name:** `quantify-mitochondrial-ribosomal-immunoglobulin-and-other-dominant-biotype-fractions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T049 — Identify genes with sample-specific count spikes suggestive of mapping or contamination artefacts

Identify genes with sample-specific count spikes suggestive of mapping or contamination artefacts.

- **Routing name:** `identify-genes-with-sample-specific-count-spikes-suggestive-of-mapping-or-contamination-artefacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T050 — Issue pass, warning, or fail status per sample using predefined multimetric QC gates

Issue pass, warning, or fail status per sample using predefined multimetric QC gates.

- **Routing name:** `issue-pass-warning-or-fail-status-per-sample-using-predefined-multimetric-qc-gates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Normalization and model construction

### MYR-D011-T051 — Filter genes with insufficient counts using a design-aware expression threshold

Filter genes with insufficient counts using a design-aware expression threshold.

- **Routing name:** `filter-genes-with-insufficient-counts-using-a-design-aware-expression-threshold`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T052 — Estimate sample-specific size factors using a method robust to library-depth differences

Estimate sample-specific size factors using a method robust to library-depth differences.

- **Routing name:** `estimate-sample-specific-size-factors-using-a-method-robust-to-library-depth-differences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T053 — Evaluate whether composition bias violates the selected normalization assumptions

Evaluate whether composition bias violates the selected normalization assumptions.

- **Routing name:** `evaluate-whether-composition-bias-violates-the-selected-normalization-assumptions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T054 — Construct the full-rank statistical design matrix with explicit reference levels and interaction terms

Construct the full-rank statistical design matrix with explicit reference levels and interaction terms.

- **Routing name:** `construct-the-full-rank-statistical-design-matrix-with-explicit-reference-levels-and-interaction-terms`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T055 — Encode paired or repeated-measure structure without treating technical replicates as independent subjects

Encode paired or repeated-measure structure without treating technical replicates as independent subjects.

- **Routing name:** `encode-paired-or-repeated-measure-structure-without-treating-technical-replicates-as-independent-subjects`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T056 — Estimate gene-wise dispersions and fit the declared mean-dispersion trend

Estimate gene-wise dispersions and fit the declared mean-dispersion trend.

- **Routing name:** `estimate-gene-wise-dispersions-and-fit-the-declared-mean-dispersion-trend`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T057 — Apply empirical-Bayes dispersion shrinkage and retain diagnostic estimates

Apply empirical-Bayes dispersion shrinkage and retain diagnostic estimates.

- **Routing name:** `apply-empirical-bayes-dispersion-shrinkage-and-retain-diagnostic-estimates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T058 — Detect genes with convergence failures, boundary estimates, or non-identifiable coefficients

Detect genes with convergence failures, boundary estimates, or non-identifiable coefficients.

- **Routing name:** `detect-genes-with-convergence-failures-boundary-estimates-or-non-identifiable-coefficients`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T059 — Define independent filtering, outlier replacement, and Cook-distance policies before contrast extraction

Define independent filtering, outlier replacement, and Cook-distance policies before contrast extraction.

- **Routing name:** `define-independent-filtering-outlier-replacement-and-cook-distance-policies-before-contrast-extraction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T060 — Store normalized counts and transformed expression separately from raw counts used for inference

Store normalized counts and transformed expression separately from raw counts used for inference.

- **Routing name:** `store-normalized-counts-and-transformed-expression-separately-from-raw-counts-used-for-inference`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Differential-expression testing

### MYR-D011-T061 — Test the primary pairwise condition contrast with the frozen model and coefficient definition

Test the primary pairwise condition contrast with the frozen model and coefficient definition.

- **Routing name:** `test-the-primary-pairwise-condition-contrast-with-the-frozen-model-and-coefficient-definition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T062 — Test multi-level factors using an omnibus likelihood-ratio or equivalent nested-model comparison

Test multi-level factors using an omnibus likelihood-ratio or equivalent nested-model comparison.

- **Routing name:** `test-multi-level-factors-using-an-omnibus-likelihood-ratio-or-equivalent-nested-model-comparison`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T063 — Test condition-by-time interaction terms for differential temporal response

Test condition-by-time interaction terms for differential temporal response.

- **Routing name:** `test-condition-by-time-interaction-terms-for-differential-temporal-response`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T064 — Test genotype-by-treatment interactions while preserving main-effect interpretability

Test genotype-by-treatment interactions while preserving main-effect interpretability.

- **Routing name:** `test-genotype-by-treatment-interactions-while-preserving-main-effect-interpretability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T065 — Test paired contrasts using subject blocking and verify within-pair sample completeness

Test paired contrasts using subject blocking and verify within-pair sample completeness.

- **Routing name:** `test-paired-contrasts-using-subject-blocking-and-verify-within-pair-sample-completeness`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T066 — Extract log2 fold changes, standard errors, test statistics, raw P values, and adjusted P values

Extract log2 fold changes, standard errors, test statistics, raw P values, and adjusted P values.

- **Routing name:** `extract-log2-fold-changes-standard-errors-test-statistics-raw-p-values-and-adjusted-p-values`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T067 — Apply the declared multiple-testing procedure to the eligible gene universe

Apply the declared multiple-testing procedure to the eligible gene universe.

- **Routing name:** `apply-the-declared-multiple-testing-procedure-to-the-eligible-gene-universe`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T068 — Classify genes by statistical significance and minimum absolute effect-size threshold

Classify genes by statistical significance and minimum absolute effect-size threshold.

- **Routing name:** `classify-genes-by-statistical-significance-and-minimum-absolute-effect-size-threshold`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T069 — Return no-call status for non-estimable contrasts, singular designs, or insufficient residual degrees of freedom

Return no-call status for non-estimable contrasts, singular designs, or insufficient residual degrees of freedom.

- **Routing name:** `return-no-call-status-for-non-estimable-contrasts-singular-designs-or-insufficient-residual-degrees-of-freedom`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T070 — Generate contrast-specific diagnostic plots without reusing transformed values for count-model inference

Generate contrast-specific diagnostic plots without reusing transformed values for count-model inference.

- **Routing name:** `generate-contrast-specific-diagnostic-plots-without-reusing-transformed-values-for-count-model-inference`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Effect-size estimation and robustness analysis

### MYR-D011-T071 — Shrink noisy log2 fold-change estimates with a declared prior or heavy-tailed estimator

Shrink noisy log2 fold-change estimates with a declared prior or heavy-tailed estimator.

- **Routing name:** `shrink-noisy-log2-fold-change-estimates-with-a-declared-prior-or-heavy-tailed-estimator`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T072 — Compare unshrunk and shrunken effect rankings and flag sign reversals near zero

Compare unshrunk and shrunken effect rankings and flag sign reversals near zero.

- **Routing name:** `compare-unshrunk-and-shrunken-effect-rankings-and-flag-sign-reversals-near-zero`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T073 — Repeat the primary contrast after excluding each warning-level sample in turn

Repeat the primary contrast after excluding each warning-level sample in turn.

- **Routing name:** `repeat-the-primary-contrast-after-excluding-each-warning-level-sample-in-turn`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T074 — Perform leave-one-batch-out sensitivity analysis when multiple batches support the comparison

Perform leave-one-batch-out sensitivity analysis when multiple batches support the comparison.

- **Routing name:** `perform-leave-one-batch-out-sensitivity-analysis-when-multiple-batches-support-the-comparison`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T075 — Assess robustness to reasonable alternative low-count filtering thresholds

Assess robustness to reasonable alternative low-count filtering thresholds.

- **Routing name:** `assess-robustness-to-reasonable-alternative-low-count-filtering-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T076 — Compare results under a second justified normalization or modelling method on a bounded sensitivity set

Compare results under a second justified normalization or modelling method on a bounded sensitivity set.

- **Routing name:** `compare-results-under-a-second-justified-normalization-or-modelling-method-on-a-bounded-sensitivity-set`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T077 — Quantify concordance of effect direction, rank, and significance across sensitivity analyses

Quantify concordance of effect direction, rank, and significance across sensitivity analyses.

- **Routing name:** `quantify-concordance-of-effect-direction-rank-and-significance-across-sensitivity-analyses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T078 — Evaluate influence of high Cook-distance observations on top-ranked genes

Evaluate influence of high Cook-distance observations on top-ranked genes.

- **Routing name:** `evaluate-influence-of-high-cook-distance-observations-on-top-ranked-genes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T079 — Separate statistically stable findings from analysis-dependent findings using predefined criteria

Separate statistically stable findings from analysis-dependent findings using predefined criteria.

- **Routing name:** `separate-statistically-stable-findings-from-analysis-dependent-findings-using-predefined-criteria`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T080 — Produce a robustness table linking every promoted gene to all sensitivity outcomes

Produce a robustness table linking every promoted gene to all sensitivity outcomes.

- **Routing name:** `produce-a-robustness-table-linking-every-promoted-gene-to-all-sensitivity-outcomes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Biological interpretation and enrichment

### MYR-D011-T081 — Map tested gene identifiers to current symbols and stable accessions without silently dropping duplicates

Map tested gene identifiers to current symbols and stable accessions without silently dropping duplicates.

- **Routing name:** `map-tested-gene-identifiers-to-current-symbols-and-stable-accessions-without-silently-dropping-duplicates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T082 — Perform over-representation analysis using the actually tested gene universe as background

Perform over-representation analysis using the actually tested gene universe as background.

- **Routing name:** `perform-over-representation-analysis-using-the-actually-tested-gene-universe-as-background`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T083 — Run ranked gene-set enrichment on signed effect statistics with deterministic tie handling

Run ranked gene-set enrichment on signed effect statistics with deterministic tie handling.

- **Routing name:** `run-ranked-gene-set-enrichment-on-signed-effect-statistics-with-deterministic-tie-handling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T084 — Test pathway collections separately by database, version, organism, and evidence type

Test pathway collections separately by database, version, organism, and evidence type.

- **Routing name:** `test-pathway-collections-separately-by-database-version-organism-and-evidence-type`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T085 — Reduce redundant enriched terms using explicit semantic or gene-overlap thresholds

Reduce redundant enriched terms using explicit semantic or gene-overlap thresholds.

- **Routing name:** `reduce-redundant-enriched-terms-using-explicit-semantic-or-gene-overlap-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T086 — Identify coherent co-expression modules associated with the primary contrast

Identify coherent co-expression modules associated with the primary contrast.

- **Routing name:** `identify-coherent-co-expression-modules-associated-with-the-primary-contrast`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T087 — Assess whether enriched signals are driven by a few high-abundance or multifunctional genes

Assess whether enriched signals are driven by a few high-abundance or multifunctional genes.

- **Routing name:** `assess-whether-enriched-signals-are-driven-by-a-few-high-abundance-or-multifunctional-genes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T088 — Compare marker signatures against declared tissue, cell-type, or pathway expectations

Compare marker signatures against declared tissue, cell-type, or pathway expectations.

- **Routing name:** `compare-marker-signatures-against-declared-tissue-cell-type-or-pathway-expectations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T089 — Separate exploratory pathway findings from confirmatory gene-level endpoints in reporting

Separate exploratory pathway findings from confirmatory gene-level endpoints in reporting.

- **Routing name:** `separate-exploratory-pathway-findings-from-confirmatory-gene-level-endpoints-in-reporting`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T090 — Export gene-to-term membership and leading-edge contributions for every reported enrichment

Export gene-to-term membership and leading-edge contributions for every reported enrichment.

- **Routing name:** `export-gene-to-term-membership-and-leading-edge-contributions-for-every-reported-enrichment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Reporting, release, and review gates

### MYR-D011-T091 — Generate a machine-readable differential-expression table for every requested contrast

Generate a machine-readable differential-expression table for every requested contrast.

- **Routing name:** `generate-a-machine-readable-differential-expression-table-for-every-requested-contrast`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T092 — Produce a sample QC report with thresholds, failures, exclusions, and analyst decisions

Produce a sample QC report with thresholds, failures, exclusions, and analyst decisions.

- **Routing name:** `produce-a-sample-qc-report-with-thresholds-failures-exclusions-and-analyst-decisions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T093 — Export raw counts, normalized counts, transformed values, model coefficients, and contrast metadata separately

Export raw counts, normalized counts, transformed values, model coefficients, and contrast metadata separately.

- **Routing name:** `export-raw-counts-normalized-counts-transformed-values-model-coefficients-and-contrast-metadata-separately`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T094 — Record genome, annotation, gene-set, tool, container, parameter, and random-seed provenance

Record genome, annotation, gene-set, tool, container, parameter, and random-seed provenance.

- **Routing name:** `record-genome-annotation-gene-set-tool-container-parameter-and-random-seed-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T095 — Validate cross-file sample and gene identifier consistency across all release artifacts

Validate cross-file sample and gene identifier consistency across all release artifacts.

- **Routing name:** `validate-cross-file-sample-and-gene-identifier-consistency-across-all-release-artifacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T096 — Create reproducibility commands or workflow configuration sufficient to rerun the analysis

Create reproducibility commands or workflow configuration sufficient to rerun the analysis.

- **Routing name:** `create-reproducibility-commands-or-workflow-configuration-sufficient-to-rerun-the-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T097 — Archive logs, design matrices, session information, and intermediate QC summaries under retention rules

Archive logs, design matrices, session information, and intermediate QC summaries under retention rules.

- **Routing name:** `archive-logs-design-matrices-session-information-and-intermediate-qc-summaries-under-retention-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T098 — Flag conclusions that depend on small sample size, confounding, outliers, or weak effect robustness

Flag conclusions that depend on small sample size, confounding, outliers, or weak effect robustness.

- **Routing name:** `flag-conclusions-that-depend-on-small-sample-size-confounding-outliers-or-weak-effect-robustness`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T099 — Require qualified review before any clinical, diagnostic, or treatment interpretation

Require qualified review before any clinical, diagnostic, or treatment interpretation.

- **Routing name:** `require-qualified-review-before-any-clinical-diagnostic-or-treatment-interpretation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D011-T100 — Release the analysis only when mandatory QC, model, provenance, and review gates pass or a waiver is recorded

Release the analysis only when mandatory QC, model, provenance, and review gates pass or a waiver is recorded.

- **Routing name:** `release-the-analysis-only-when-mandatory-qc-model-provenance-and-review-gates-pass-or-a-waiver-is-recorded`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
