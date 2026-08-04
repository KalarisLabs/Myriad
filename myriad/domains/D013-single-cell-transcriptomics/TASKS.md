# D013 — Single-Cell Transcriptomics

Batch **002** · 10 workstreams · 100 tasks

## 01. Experiment intake and assay configuration

### MYR-D013-T001 — Validate sample, donor, library, lane, capture, and multiplexing identifiers for the single-cell study

Validate sample, donor, library, lane, capture, and multiplexing identifiers for the single-cell study.

- **Routing name:** `validate-sample-donor-library-lane-capture-and-multiplexing-identifiers-for-the-single-cell-study`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T002 — Record platform, chemistry version, read structure, feature-barcode modalities, and expected cell recovery

Record platform, chemistry version, read structure, feature-barcode modalities, and expected cell recovery.

- **Routing name:** `record-platform-chemistry-version-read-structure-feature-barcode-modalities-and-expected-cell-recovery`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T003 — Reconcile donor, tissue, condition, time point, batch, and replicate metadata with the analysis design

Reconcile donor, tissue, condition, time point, batch, and replicate metadata with the analysis design.

- **Routing name:** `reconcile-donor-tissue-condition-time-point-batch-and-replicate-metadata-with-the-analysis-design`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T004 — Verify reference genome, transcript annotation, feature reference, and barcode whitelist compatibility

Verify reference genome, transcript annotation, feature reference, and barcode whitelist compatibility.

- **Routing name:** `verify-reference-genome-transcript-annotation-feature-reference-and-barcode-whitelist-compatibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T005 — Define whether nuclei, whole cells, fixed cells, or plate-based transcriptomes are being analysed

Define whether nuclei, whole cells, fixed cells, or plate-based transcriptomes are being analysed.

- **Routing name:** `define-whether-nuclei-whole-cells-fixed-cells-or-plate-based-transcriptomes-are-being-analysed`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T006 — Specify primary unit of inference for cell-level, sample-level, donor-level, and condition-level comparisons

Specify primary unit of inference for cell-level, sample-level, donor-level, and condition-level comparisons.

- **Routing name:** `specify-primary-unit-of-inference-for-cell-level-sample-level-donor-level-and-condition-level-comparisons`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T007 — Declare minimum donor replication and pseudobulk strategy for confirmatory differential expression

Declare minimum donor replication and pseudobulk strategy for confirmatory differential expression.

- **Routing name:** `declare-minimum-donor-replication-and-pseudobulk-strategy-for-confirmatory-differential-expression`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T008 — Define expected cell types, rare-population targets, and acceptable cell-recovery range before inspection

Define expected cell types, rare-population targets, and acceptable cell-recovery range before inspection.

- **Routing name:** `define-expected-cell-types-rare-population-targets-and-acceptable-cell-recovery-range-before-inspection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T009 — Freeze ambient-RNA, doublet, integration, clustering, and annotation policies in the run manifest

Freeze ambient-RNA, doublet, integration, clustering, and annotation policies in the run manifest.

- **Routing name:** `freeze-ambient-rna-doublet-integration-clustering-and-annotation-policies-in-the-run-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T010 — Estimate compute and storage needs from expected reads, barcodes, features, and modalities

Estimate compute and storage needs from expected reads, barcodes, features, and modalities.

- **Routing name:** `estimate-compute-and-storage-needs-from-expected-reads-barcodes-features-and-modalities`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Demultiplexing, alignment, and molecule counting

### MYR-D013-T011 — Verify raw read integrity and chemistry-specific read-length requirements

Verify raw read integrity and chemistry-specific read-length requirements.

- **Routing name:** `verify-raw-read-integrity-and-chemistry-specific-read-length-requirements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T012 — Demultiplex sequencing data while preserving sample-index and lane provenance

Demultiplex sequencing data while preserving sample-index and lane provenance.

- **Routing name:** `demultiplex-sequencing-data-while-preserving-sample-index-and-lane-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T013 — Extract cell barcodes and unique molecular identifiers at the declared read positions

Extract cell barcodes and unique molecular identifiers at the declared read positions.

- **Routing name:** `extract-cell-barcodes-and-unique-molecular-identifiers-at-the-declared-read-positions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T014 — Correct cell barcodes only against the chemistry-specific whitelist and permitted edit distance

Correct cell barcodes only against the chemistry-specific whitelist and permitted edit distance.

- **Routing name:** `correct-cell-barcodes-only-against-the-chemistry-specific-whitelist-and-permitted-edit-distance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T015 — Align or pseudoalign transcript reads to the frozen reference with modality-appropriate parameters

Align or pseudoalign transcript reads to the frozen reference with modality-appropriate parameters.

- **Routing name:** `align-or-pseudoalign-transcript-reads-to-the-frozen-reference-with-modality-appropriate-parameters`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T016 — Assign reads to genes using the declared intronic or exonic counting mode

Assign reads to genes using the declared intronic or exonic counting mode.

- **Routing name:** `assign-reads-to-genes-using-the-declared-intronic-or-exonic-counting-mode`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T017 — Collapse PCR duplicates by gene, corrected barcode, and UMI under an explicit UMI error model

Collapse PCR duplicates by gene, corrected barcode, and UMI under an explicit UMI error model.

- **Routing name:** `collapse-pcr-duplicates-by-gene-corrected-barcode-and-umi-under-an-explicit-umi-error-model`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T018 — Generate raw feature-by-barcode matrices including all observed barcodes before cell calling

Generate raw feature-by-barcode matrices including all observed barcodes before cell calling.

- **Routing name:** `generate-raw-feature-by-barcode-matrices-including-all-observed-barcodes-before-cell-calling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T019 — Quantify reads, mapped reads, valid barcodes, valid UMIs, saturation, and reads per cell

Quantify reads, mapped reads, valid barcodes, valid UMIs, saturation, and reads per cell.

- **Routing name:** `quantify-reads-mapped-reads-valid-barcodes-valid-umis-saturation-and-reads-per-cell`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T020 — Merge lanes or technical libraries only after verifying identical biological sample and chemistry metadata

Merge lanes or technical libraries only after verifying identical biological sample and chemistry metadata.

- **Routing name:** `merge-lanes-or-technical-libraries-only-after-verifying-identical-biological-sample-and-chemistry-metadata`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Cell calling, background correction, and cell quality control

### MYR-D013-T021 — Rank barcodes by total UMI count and identify the empirical cell-containing transition

Rank barcodes by total UMI count and identify the empirical cell-containing transition.

- **Routing name:** `rank-barcodes-by-total-umi-count-and-identify-the-empirical-cell-containing-transition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T022 — Call cell-containing barcodes with a method appropriate to expected recovery and ambient background

Call cell-containing barcodes with a method appropriate to expected recovery and ambient background.

- **Routing name:** `call-cell-containing-barcodes-with-a-method-appropriate-to-expected-recovery-and-ambient-background`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T023 — Estimate and correct ambient RNA contamination while retaining raw counts and contamination fractions

Estimate and correct ambient RNA contamination while retaining raw counts and contamination fractions.

- **Routing name:** `estimate-and-correct-ambient-rna-contamination-while-retaining-raw-counts-and-contamination-fractions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T024 — Calculate total counts, detected genes, mitochondrial fraction, ribosomal fraction, and complexity per cell

Calculate total counts, detected genes, mitochondrial fraction, ribosomal fraction, and complexity per cell.

- **Routing name:** `calculate-total-counts-detected-genes-mitochondrial-fraction-ribosomal-fraction-and-complexity-per-cell`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T025 — Fit sample-specific quality distributions rather than one global threshold across heterogeneous tissues

Fit sample-specific quality distributions rather than one global threshold across heterogeneous tissues.

- **Routing name:** `fit-sample-specific-quality-distributions-rather-than-one-global-threshold-across-heterogeneous-tissues`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T026 — Flag low-complexity, stressed, damaged, debris-associated, or background-dominated cells with reason codes

Flag low-complexity, stressed, damaged, debris-associated, or background-dominated cells with reason codes.

- **Routing name:** `flag-low-complexity-stressed-damaged-debris-associated-or-background-dominated-cells-with-reason-codes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T027 — Calculate doublet scores using simulated or neighbourhood-based artificial doublets

Calculate doublet scores using simulated or neighbourhood-based artificial doublets.

- **Routing name:** `calculate-doublet-scores-using-simulated-or-neighbourhood-based-artificial-doublets`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T028 — Detect cross-genotype or heterotypic multiplets when genotype or lineage evidence is available

Detect cross-genotype or heterotypic multiplets when genotype or lineage evidence is available.

- **Routing name:** `detect-cross-genotype-or-heterotypic-multiplets-when-genotype-or-lineage-evidence-is-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T029 — Avoid automatic removal of plausible transitional states solely because they co-express lineage markers

Avoid automatic removal of plausible transitional states solely because they co-express lineage markers.

- **Routing name:** `avoid-automatic-removal-of-plausible-transitional-states-solely-because-they-co-express-lineage-markers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T030 — Export called, rejected, rescued, warning-level, and doublet cell manifests with all thresholds

Export called, rejected, rescued, warning-level, and doublet cell manifests with all thresholds.

- **Routing name:** `export-called-rejected-rescued-warning-level-and-doublet-cell-manifests-with-all-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Normalization, feature selection, and latent representation

### MYR-D013-T031 — Preserve raw integer counts in an immutable assay before transformation

Preserve raw integer counts in an immutable assay before transformation.

- **Routing name:** `preserve-raw-integer-counts-in-an-immutable-assay-before-transformation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T032 — Normalize library-size differences with a method compatible with sparse single-cell counts

Normalize library-size differences with a method compatible with sparse single-cell counts.

- **Routing name:** `normalize-library-size-differences-with-a-method-compatible-with-sparse-single-cell-counts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T033 — Apply log transformation or model-based variance stabilization only to the intended downstream assay

Apply log transformation or model-based variance stabilization only to the intended downstream assay.

- **Routing name:** `apply-log-transformation-or-model-based-variance-stabilization-only-to-the-intended-downstream-assay`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T034 — Select highly variable genes using sample- or batch-aware variance modelling

Select highly variable genes using sample- or batch-aware variance modelling.

- **Routing name:** `select-highly-variable-genes-using-sample-or-batch-aware-variance-modelling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T035 — Exclude mitochondrial, ribosomal, cell-cycle, or stress genes from feature selection only under a declared policy

Exclude mitochondrial, ribosomal, cell-cycle, or stress genes from feature selection only under a declared policy.

- **Routing name:** `exclude-mitochondrial-ribosomal-cell-cycle-or-stress-genes-from-feature-selection-only-under-a-declared-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T036 — Scale selected features while preventing numerical dominance by extreme outliers

Scale selected features while preventing numerical dominance by extreme outliers.

- **Routing name:** `scale-selected-features-while-preventing-numerical-dominance-by-extreme-outliers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T037 — Run principal-component analysis and quantify variance explained by each component

Run principal-component analysis and quantify variance explained by each component.

- **Routing name:** `run-principal-component-analysis-and-quantify-variance-explained-by-each-component`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T038 — Select retained dimensions using reproducible spectral, permutation, or elbow criteria

Select retained dimensions using reproducible spectral, permutation, or elbow criteria.

- **Routing name:** `select-retained-dimensions-using-reproducible-spectral-permutation-or-elbow-criteria`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T039 — Evaluate whether latent dimensions correlate primarily with technical covariates

Evaluate whether latent dimensions correlate primarily with technical covariates.

- **Routing name:** `evaluate-whether-latent-dimensions-correlate-primarily-with-technical-covariates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T040 — Store normalization factors, feature-selection statistics, loadings, and retained dimensions

Store normalization factors, feature-selection statistics, loadings, and retained dimensions.

- **Routing name:** `store-normalization-factors-feature-selection-statistics-loadings-and-retained-dimensions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Neighbour graphs, clustering, and cluster stability

### MYR-D013-T041 — Construct a k-nearest-neighbour graph from the frozen latent representation

Construct a k-nearest-neighbour graph from the frozen latent representation.

- **Routing name:** `construct-a-k-nearest-neighbour-graph-from-the-frozen-latent-representation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T042 — Build a shared-nearest-neighbour or weighted graph with recorded distance and neighbour parameters

Build a shared-nearest-neighbour or weighted graph with recorded distance and neighbour parameters.

- **Routing name:** `build-a-shared-nearest-neighbour-or-weighted-graph-with-recorded-distance-and-neighbour-parameters`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T043 — Cluster cells across a bounded resolution grid without selecting resolution from marker desirability alone

Cluster cells across a bounded resolution grid without selecting resolution from marker desirability alone.

- **Routing name:** `cluster-cells-across-a-bounded-resolution-grid-without-selecting-resolution-from-marker-desirability-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T044 — Quantify cluster size, donor composition, sample composition, and technical-batch composition

Quantify cluster size, donor composition, sample composition, and technical-batch composition.

- **Routing name:** `quantify-cluster-size-donor-composition-sample-composition-and-technical-batch-composition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T045 — Detect clusters driven by mitochondrial, ribosomal, cell-cycle, or dissociation signatures

Detect clusters driven by mitochondrial, ribosomal, cell-cycle, or dissociation signatures.

- **Routing name:** `detect-clusters-driven-by-mitochondrial-ribosomal-cell-cycle-or-dissociation-signatures`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T046 — Assess cluster stability under cell subsampling and modest parameter perturbations

Assess cluster stability under cell subsampling and modest parameter perturbations.

- **Routing name:** `assess-cluster-stability-under-cell-subsampling-and-modest-parameter-perturbations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T047 — Identify overclustered groups lacking reproducible differential features

Identify overclustered groups lacking reproducible differential features.

- **Routing name:** `identify-overclustered-groups-lacking-reproducible-differential-features`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T048 — Identify underclustered groups with stable internal multimodality across donors

Identify underclustered groups with stable internal multimodality across donors.

- **Routing name:** `identify-underclustered-groups-with-stable-internal-multimodality-across-donors`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T049 — Select a primary clustering using prespecified stability and biological-separation criteria

Select a primary clustering using prespecified stability and biological-separation criteria.

- **Routing name:** `select-a-primary-clustering-using-prespecified-stability-and-biological-separation-criteria`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T050 — Preserve alternative clusterings and their mappings instead of overwriting exploratory results

Preserve alternative clusterings and their mappings instead of overwriting exploratory results.

- **Routing name:** `preserve-alternative-clusterings-and-their-mappings-instead-of-overwriting-exploratory-results`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Cell-type and cell-state annotation

### MYR-D013-T051 — Calculate cluster marker genes using donor-aware or sample-aware comparisons

Calculate cluster marker genes using donor-aware or sample-aware comparisons.

- **Routing name:** `calculate-cluster-marker-genes-using-donor-aware-or-sample-aware-comparisons`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T052 — Score curated cell-type marker sets with species, tissue, and ontology provenance

Score curated cell-type marker sets with species, tissue, and ontology provenance.

- **Routing name:** `score-curated-cell-type-marker-sets-with-species-tissue-and-ontology-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T053 — Map cells to a labelled reference only after checking feature and biological-domain compatibility

Map cells to a labelled reference only after checking feature and biological-domain compatibility.

- **Routing name:** `map-cells-to-a-labelled-reference-only-after-checking-feature-and-biological-domain-compatibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T054 — Compare reference-transfer labels with marker-based annotation and flag disagreements

Compare reference-transfer labels with marker-based annotation and flag disagreements.

- **Routing name:** `compare-reference-transfer-labels-with-marker-based-annotation-and-flag-disagreements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T055 — Distinguish canonical cell type from transient activation, stress, cycling, or interferon state

Distinguish canonical cell type from transient activation, stress, cycling, or interferon state.

- **Routing name:** `distinguish-canonical-cell-type-from-transient-activation-stress-cycling-or-interferon-state`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T056 — Assign hierarchical labels from broad compartment to subtype with confidence at each level

Assign hierarchical labels from broad compartment to subtype with confidence at each level.

- **Routing name:** `assign-hierarchical-labels-from-broad-compartment-to-subtype-with-confidence-at-each-level`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T057 — Prevent assignment of rare labels when supporting markers are absent or ambiently expressed

Prevent assignment of rare labels when supporting markers are absent or ambiently expressed.

- **Routing name:** `prevent-assignment-of-rare-labels-when-supporting-markers-are-absent-or-ambiently-expressed`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T058 — Label unresolved groups as unknown or mixed rather than forcing a nearest known category

Label unresolved groups as unknown or mixed rather than forcing a nearest known category.

- **Routing name:** `label-unresolved-groups-as-unknown-or-mixed-rather-than-forcing-a-nearest-known-category`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T059 — Map final labels to stable cell ontology identifiers when a valid term exists

Map final labels to stable cell ontology identifiers when a valid term exists.

- **Routing name:** `map-final-labels-to-stable-cell-ontology-identifiers-when-a-valid-term-exists`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T060 — Export per-cell labels, cluster labels, confidence values, evidence, and reviewer overrides

Export per-cell labels, cluster labels, confidence values, evidence, and reviewer overrides.

- **Routing name:** `export-per-cell-labels-cluster-labels-confidence-values-evidence-and-reviewer-overrides`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Differential expression and population composition

### MYR-D013-T061 — Aggregate counts to donor-by-cell-type pseudobulk profiles for confirmatory condition testing

Aggregate counts to donor-by-cell-type pseudobulk profiles for confirmatory condition testing.

- **Routing name:** `aggregate-counts-to-donor-by-cell-type-pseudobulk-profiles-for-confirmatory-condition-testing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T062 — Require minimum cells and donors per cell type before constructing a pseudobulk contrast

Require minimum cells and donors per cell type before constructing a pseudobulk contrast.

- **Routing name:** `require-minimum-cells-and-donors-per-cell-type-before-constructing-a-pseudobulk-contrast`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T063 — Test cell-type-specific differential expression with donor and batch terms in the model

Test cell-type-specific differential expression with donor and batch terms in the model.

- **Routing name:** `test-cell-type-specific-differential-expression-with-donor-and-batch-terms-in-the-model`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T064 — Test within-donor paired contrasts when samples are matched across conditions

Test within-donor paired contrasts when samples are matched across conditions.

- **Routing name:** `test-within-donor-paired-contrasts-when-samples-are-matched-across-conditions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T065 — Estimate condition-associated changes in cell-type abundance using sample-level proportions

Estimate condition-associated changes in cell-type abundance using sample-level proportions.

- **Routing name:** `estimate-condition-associated-changes-in-cell-type-abundance-using-sample-level-proportions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T066 — Model compositional changes with methods that respect the simplex constraint

Model compositional changes with methods that respect the simplex constraint.

- **Routing name:** `model-compositional-changes-with-methods-that-respect-the-simplex-constraint`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T067 — Separate within-cell-state expression change from changes in cell-state frequency

Separate within-cell-state expression change from changes in cell-state frequency.

- **Routing name:** `separate-within-cell-state-expression-change-from-changes-in-cell-state-frequency`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T068 — Control false discovery across the prespecified cell-type and gene testing universe

Control false discovery across the prespecified cell-type and gene testing universe.

- **Routing name:** `control-false-discovery-across-the-prespecified-cell-type-and-gene-testing-universe`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T069 — Perform leave-one-donor-out sensitivity analysis for leading cell-type-specific findings

Perform leave-one-donor-out sensitivity analysis for leading cell-type-specific findings.

- **Routing name:** `perform-leave-one-donor-out-sensitivity-analysis-for-leading-cell-type-specific-findings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T070 — Return no-call status for comparisons lacking independent biological replication

Return no-call status for comparisons lacking independent biological replication.

- **Routing name:** `return-no-call-status-for-comparisons-lacking-independent-biological-replication`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Trajectories, dynamics, and cell-cell communication

### MYR-D013-T071 — Select biologically justified start and terminal states before supervised trajectory orientation

Select biologically justified start and terminal states before supervised trajectory orientation.

- **Routing name:** `select-biologically-justified-start-and-terminal-states-before-supervised-trajectory-orientation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T072 — Infer lineage topology from eligible cells using a declared graph or curve model

Infer lineage topology from eligible cells using a declared graph or curve model.

- **Routing name:** `infer-lineage-topology-from-eligible-cells-using-a-declared-graph-or-curve-model`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T073 — Calculate pseudotime while preserving branch-specific uncertainty

Calculate pseudotime while preserving branch-specific uncertainty.

- **Routing name:** `calculate-pseudotime-while-preserving-branch-specific-uncertainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T074 — Test genes for smooth expression change along pseudotime with multiple-testing control

Test genes for smooth expression change along pseudotime with multiple-testing control.

- **Routing name:** `test-genes-for-smooth-expression-change-along-pseudotime-with-multiple-testing-control`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T075 — Compare trajectory occupancy across conditions at the donor level

Compare trajectory occupancy across conditions at the donor level.

- **Routing name:** `compare-trajectory-occupancy-across-conditions-at-the-donor-level`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T076 — Estimate RNA velocity only when spliced and unspliced counting assumptions are met

Estimate RNA velocity only when spliced and unspliced counting assumptions are met.

- **Routing name:** `estimate-rna-velocity-only-when-spliced-and-unspliced-counting-assumptions-are-met`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T077 — Assess velocity coherence, latent-time stability, and sensitivity to kinetic-model choice

Assess velocity coherence, latent-time stability, and sensitivity to kinetic-model choice.

- **Routing name:** `assess-velocity-coherence-latent-time-stability-and-sensitivity-to-kinetic-model-choice`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T078 — Infer candidate ligand-receptor interactions using expressed partners and cell-type abundance constraints

Infer candidate ligand-receptor interactions using expressed partners and cell-type abundance constraints.

- **Routing name:** `infer-candidate-ligand-receptor-interactions-using-expressed-partners-and-cell-type-abundance-constraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T079 — Filter communication predictions lacking sufficient donor-level expression or receptor specificity

Filter communication predictions lacking sufficient donor-level expression or receptor specificity.

- **Routing name:** `filter-communication-predictions-lacking-sufficient-donor-level-expression-or-receptor-specificity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T080 — Report trajectories and communication links as model-based hypotheses rather than direct mechanistic proof

Report trajectories and communication links as model-based hypotheses rather than direct mechanistic proof.

- **Routing name:** `report-trajectories-and-communication-links-as-model-based-hypotheses-rather-than-direct-mechanistic-proof`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Batch integration and multimodal reconciliation

### MYR-D013-T081 — Quantify batch, donor, chemistry, and condition effects before any integration

Quantify batch, donor, chemistry, and condition effects before any integration.

- **Routing name:** `quantify-batch-donor-chemistry-and-condition-effects-before-any-integration`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T082 — Select integration covariates that do not erase the biological comparison of interest

Select integration covariates that do not erase the biological comparison of interest.

- **Routing name:** `select-integration-covariates-that-do-not-erase-the-biological-comparison-of-interest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T083 — Integrate batches in a latent space while retaining the unintegrated expression matrix

Integrate batches in a latent space while retaining the unintegrated expression matrix.

- **Routing name:** `integrate-batches-in-a-latent-space-while-retaining-the-unintegrated-expression-matrix`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T084 — Evaluate mixing of shared cell types separately from preservation of condition-specific states

Evaluate mixing of shared cell types separately from preservation of condition-specific states.

- **Routing name:** `evaluate-mixing-of-shared-cell-types-separately-from-preservation-of-condition-specific-states`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T085 — Detect overcorrection by loss of known biological differences or forced mixing of distinct lineages

Detect overcorrection by loss of known biological differences or forced mixing of distinct lineages.

- **Routing name:** `detect-overcorrection-by-loss-of-known-biological-differences-or-forced-mixing-of-distinct-lineages`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T086 — Detect undercorrection by residual batch-segregated neighbours within shared cell types

Detect undercorrection by residual batch-segregated neighbours within shared cell types.

- **Routing name:** `detect-undercorrection-by-residual-batch-segregated-neighbours-within-shared-cell-types`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T087 — Tune integration strength on a bounded grid using predefined biological and technical metrics

Tune integration strength on a bounded grid using predefined biological and technical metrics.

- **Routing name:** `tune-integration-strength-on-a-bounded-grid-using-predefined-biological-and-technical-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T088 — Map query datasets to a reference without altering reference labels or embeddings

Map query datasets to a reference without altering reference labels or embeddings.

- **Routing name:** `map-query-datasets-to-a-reference-without-altering-reference-labels-or-embeddings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T089 — Reconcile paired RNA and protein feature-barcode modalities with modality-specific QC

Reconcile paired RNA and protein feature-barcode modalities with modality-specific QC.

- **Routing name:** `reconcile-paired-rna-and-protein-feature-barcode-modalities-with-modality-specific-qc`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T090 — Freeze the accepted integrated representation and document excluded integration candidates

Freeze the accepted integrated representation and document excluded integration candidates.

- **Routing name:** `freeze-the-accepted-integrated-representation-and-document-excluded-integration-candidates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Release, reproducibility, and review gates

### MYR-D013-T091 — Export raw counts, corrected counts, normalized assays, embeddings, graphs, clusters, and annotations separately

Export raw counts, corrected counts, normalized assays, embeddings, graphs, clusters, and annotations separately.

- **Routing name:** `export-raw-counts-corrected-counts-normalized-assays-embeddings-graphs-clusters-and-annotations-separately`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T092 — Generate machine-readable per-cell and per-sample QC tables with all thresholds and statuses

Generate machine-readable per-cell and per-sample QC tables with all thresholds and statuses.

- **Routing name:** `generate-machine-readable-per-cell-and-per-sample-qc-tables-with-all-thresholds-and-statuses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T093 — Record genome, annotation, chemistry, pipeline, package, model, parameter, and random-seed provenance

Record genome, annotation, chemistry, pipeline, package, model, parameter, and random-seed provenance.

- **Routing name:** `record-genome-annotation-chemistry-pipeline-package-model-parameter-and-random-seed-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T094 — Validate cell barcode uniqueness and metadata alignment across every released matrix and table

Validate cell barcode uniqueness and metadata alignment across every released matrix and table.

- **Routing name:** `validate-cell-barcode-uniqueness-and-metadata-alignment-across-every-released-matrix-and-table`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T095 — Archive ambient correction, doublet detection, integration, clustering, and annotation diagnostics

Archive ambient correction, doublet detection, integration, clustering, and annotation diagnostics.

- **Routing name:** `archive-ambient-correction-doublet-detection-integration-clustering-and-annotation-diagnostics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T096 — Create single-cell reproducibility commands or workflow configurations for primary and sensitivity analyses

Create single-cell reproducibility commands or workflow configurations for primary and sensitivity analyses.

- **Routing name:** `create-single-cell-reproducibility-commands-or-workflow-configurations-for-primary-and-sensitivity-analyses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T097 — Flag conclusions supported by cells but not by independent donors or samples

Flag conclusions supported by cells but not by independent donors or samples.

- **Routing name:** `flag-conclusions-supported-by-cells-but-not-by-independent-donors-or-samples`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T098 — Prevent automatic diagnostic or treatment claims from exploratory cell-state associations

Prevent automatic diagnostic or treatment claims from exploratory cell-state associations.

- **Routing name:** `prevent-automatic-diagnostic-or-treatment-claims-from-exploratory-cell-state-associations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T099 — Require qualified review of rare-cell, trajectory, communication, and disease-associated interpretations

Require qualified review of rare-cell, trajectory, communication, and disease-associated interpretations.

- **Routing name:** `require-qualified-review-of-rare-cell-trajectory-communication-and-disease-associated-interpretations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D013-T100 — Release the dataset only when cell calling, QC, statistical, provenance, and review gates pass

Release the dataset only when cell calling, QC, statistical, provenance, and review gates pass.

- **Routing name:** `release-the-dataset-only-when-cell-calling-qc-statistical-provenance-and-review-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
