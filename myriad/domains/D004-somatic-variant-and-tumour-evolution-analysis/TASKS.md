# D004 — Somatic Variant and Tumour Evolution Analysis

Batch **001** · 10 workstreams · 100 tasks

## 01. Case design and specimen manifest

### MYR-D004-T001 — Validate patient, tumour, normal, timepoint, lesion, replicate, and assay identifiers in the case manifest

Validate patient, tumour, normal, timepoint, lesion, replicate, and assay identifiers in the case manifest.

- **Routing name:** `validate-patient-tumour-normal-timepoint-lesion-replicate-and-assay-identifiers-in-the-case-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T002 — Confirm tumour-normal pairing and prohibit cross-patient normal assignment

Confirm tumour-normal pairing and prohibit cross-patient normal assignment.

- **Routing name:** `confirm-tumour-normal-pairing-and-prohibit-cross-patient-normal-assignment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T003 — Record specimen type, collection site, treatment state, preservation method, and estimated tumour content

Record specimen type, collection site, treatment state, preservation method, and estimated tumour content.

- **Routing name:** `record-specimen-type-collection-site-treatment-state-preservation-method-and-estimated-tumour-content`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T004 — Declare whether analysis is tumour-normal, tumour-only, multi-region, longitudinal, or single-cell

Declare whether analysis is tumour-normal, tumour-only, multi-region, longitudinal, or single-cell.

- **Routing name:** `declare-whether-analysis-is-tumour-normal-tumour-only-multi-region-longitudinal-or-single-cell`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T005 — Define reference build, callable intervals, panel design, and sequencing-assay limitations

Define reference build, callable intervals, panel design, and sequencing-assay limitations.

- **Routing name:** `define-reference-build-callable-intervals-panel-design-and-sequencing-assay-limitations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T006 — Verify consent, permitted use, and controlled-access requirements for somatic data

Verify consent, permitted use, and controlled-access requirements for somatic data.

- **Routing name:** `verify-consent-permitted-use-and-controlled-access-requirements-for-somatic-data`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T007 — Set minimum tumour and normal coverage, contamination, and purity thresholds

Set minimum tumour and normal coverage, contamination, and purity thresholds.

- **Routing name:** `set-minimum-tumour-and-normal-coverage-contamination-and-purity-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T008 — Declare expected germline resource, panel-of-normals, and population-frequency resource versions

Declare expected germline resource, panel-of-normals, and population-frequency resource versions.

- **Routing name:** `declare-expected-germline-resource-panel-of-normals-and-population-frequency-resource-versions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T009 — Define somatic SNV, indel, copy-number, structural, and mitochondrial analysis scope

Define somatic SNV, indel, copy-number, structural, and mitochondrial analysis scope.

- **Routing name:** `define-somatic-snv-indel-copy-number-structural-and-mitochondrial-analysis-scope`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T010 — Freeze caller, aligner, contamination, copy-number, phylogeny, container, and resource versions

Freeze caller, aligner, contamination, copy-number, phylogeny, container, and resource versions.

- **Routing name:** `freeze-caller-aligner-contamination-copy-number-phylogeny-container-and-resource-versions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Alignment and specimen identity QC

### MYR-D004-T011 — Validate tumour and normal FASTQ or alignment integrity and reference compatibility

Validate tumour and normal FASTQ or alignment integrity and reference compatibility.

- **Routing name:** `validate-tumour-and-normal-fastq-or-alignment-integrity-and-reference-compatibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T012 — Align or process tumour and normal reads using matched, assay-appropriate parameters

Align or process tumour and normal reads using matched, assay-appropriate parameters.

- **Routing name:** `align-or-process-tumour-and-normal-reads-using-matched-assay-appropriate-parameters`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T013 — Measure depth, mapping quality, duplication, insert size, clipping, and mismatch metrics

Measure depth, mapping quality, duplication, insert size, clipping, and mismatch metrics.

- **Routing name:** `measure-depth-mapping-quality-duplication-insert-size-clipping-and-mismatch-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T014 — Verify tumour-normal fingerprint concordance and detect sample swaps

Verify tumour-normal fingerprint concordance and detect sample swaps.

- **Routing name:** `verify-tumour-normal-fingerprint-concordance-and-detect-sample-swaps`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T015 — Estimate cross-sample contamination independently in tumour and normal specimens

Estimate cross-sample contamination independently in tumour and normal specimens.

- **Routing name:** `estimate-cross-sample-contamination-independently-in-tumour-and-normal-specimens`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T016 — Infer sex-chromosome profiles and flag discordance between paired specimens

Infer sex-chromosome profiles and flag discordance between paired specimens.

- **Routing name:** `infer-sex-chromosome-profiles-and-flag-discordance-between-paired-specimens`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T017 — Detect index hopping or low-level mixture using informative germline alleles

Detect index hopping or low-level mixture using informative germline alleles.

- **Routing name:** `detect-index-hopping-or-low-level-mixture-using-informative-germline-alleles`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T018 — Quantify oxidative, deamination, fixation, and orientation-bias signatures

Quantify oxidative, deamination, fixation, and orientation-bias signatures.

- **Routing name:** `quantify-oxidative-deamination-fixation-and-orientation-bias-signatures`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T019 — Identify panel or exome intervals with systematic low coverage or paralogous mapping

Identify panel or exome intervals with systematic low coverage or paralogous mapping.

- **Routing name:** `identify-panel-or-exome-intervals-with-systematic-low-coverage-or-paralogous-mapping`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T020 — Freeze analysis-ready tumour and normal alignments with complete provenance

Freeze analysis-ready tumour and normal alignments with complete provenance.

- **Routing name:** `freeze-analysis-ready-tumour-and-normal-alignments-with-complete-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Purity, ploidy, and normal-comparator assessment

### MYR-D004-T021 — Estimate tumour purity from allele fractions and copy-number signals before variant filtering

Estimate tumour purity from allele fractions and copy-number signals before variant filtering.

- **Routing name:** `estimate-tumour-purity-from-allele-fractions-and-copy-number-signals-before-variant-filtering`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T022 — Estimate tumour ploidy and identify competing purity-ploidy solutions

Estimate tumour ploidy and identify competing purity-ploidy solutions.

- **Routing name:** `estimate-tumour-ploidy-and-identify-competing-purity-ploidy-solutions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T023 — Assess normal-sample contamination by tumour DNA or clonal haematopoiesis

Assess normal-sample contamination by tumour DNA or clonal haematopoiesis.

- **Routing name:** `assess-normal-sample-contamination-by-tumour-dna-or-clonal-haematopoiesis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T024 — Detect copy-neutral loss of heterozygosity affecting expected somatic allele fractions

Detect copy-neutral loss of heterozygosity affecting expected somatic allele fractions.

- **Routing name:** `detect-copy-neutral-loss-of-heterozygosity-affecting-expected-somatic-allele-fractions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T025 — Identify whole-genome duplication signatures and adjust clonality models accordingly

Identify whole-genome duplication signatures and adjust clonality models accordingly.

- **Routing name:** `identify-whole-genome-duplication-signatures-and-adjust-clonality-models-accordingly`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T026 — Evaluate whether tumour-only analysis has adequate population and artefact resources

Evaluate whether tumour-only analysis has adequate population and artefact resources.

- **Routing name:** `evaluate-whether-tumour-only-analysis-has-adequate-population-and-artefact-resources`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T027 — Construct or select an assay-matched panel of normals under leakage-prevention rules

Construct or select an assay-matched panel of normals under leakage-prevention rules.

- **Routing name:** `construct-or-select-an-assay-matched-panel-of-normals-under-leakage-prevention-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T028 — Validate germline-resource allele representations against the analysis reference build

Validate germline-resource allele representations against the analysis reference build.

- **Routing name:** `validate-germline-resource-allele-representations-against-the-analysis-reference-build`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T029 — Calculate locus-specific expected allele-fraction ranges under purity and copy-number states

Calculate locus-specific expected allele-fraction ranges under purity and copy-number states.

- **Routing name:** `calculate-locus-specific-expected-allele-fraction-ranges-under-purity-and-copy-number-states`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T030 — Emit a specimen-model confidence report before somatic calling proceeds

Emit a specimen-model confidence report before somatic calling proceeds.

- **Routing name:** `emit-a-specimen-model-confidence-report-before-somatic-calling-proceeds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Somatic SNV and indel calling

### MYR-D004-T031 — Call somatic SNVs and indels for each tumour-normal pair using local haplotype assembly

Call somatic SNVs and indels for each tumour-normal pair using local haplotype assembly.

- **Routing name:** `call-somatic-snvs-and-indels-for-each-tumour-normal-pair-using-local-haplotype-assembly`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T032 — Call tumour-only somatic candidates only when the declared comparator resources are available

Call tumour-only somatic candidates only when the declared comparator resources are available.

- **Routing name:** `call-tumour-only-somatic-candidates-only-when-the-declared-comparator-resources-are-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T033 — Run multi-sample calling for related tumour specimens under a patient-specific joint model

Run multi-sample calling for related tumour specimens under a patient-specific joint model.

- **Routing name:** `run-multi-sample-calling-for-related-tumour-specimens-under-a-patient-specific-joint-model`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T034 — Capture read-orientation, strand, mapping, and assembly evidence for every candidate allele

Capture read-orientation, strand, mapping, and assembly evidence for every candidate allele.

- **Routing name:** `capture-read-orientation-strand-mapping-and-assembly-evidence-for-every-candidate-allele`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T035 — Handle mitochondrial somatic variants with circular-reference and heteroplasmy-aware settings

Handle mitochondrial somatic variants with circular-reference and heteroplasmy-aware settings.

- **Routing name:** `handle-mitochondrial-somatic-variants-with-circular-reference-and-heteroplasmy-aware-settings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T036 — Detect low-allele-fraction candidates under assay-specific depth and error constraints

Detect low-allele-fraction candidates under assay-specific depth and error constraints.

- **Routing name:** `detect-low-allele-fraction-candidates-under-assay-specific-depth-and-error-constraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T037 — Validate caller outputs, headers, sample labels, and reference alleles before filtering

Validate caller outputs, headers, sample labels, and reference alleles before filtering.

- **Routing name:** `validate-caller-outputs-headers-sample-labels-and-reference-alleles-before-filtering`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T038 — Merge interval-sharded calls while resolving duplicate boundary candidates deterministically

Merge interval-sharded calls while resolving duplicate boundary candidates deterministically.

- **Routing name:** `merge-interval-sharded-calls-while-resolving-duplicate-boundary-candidates-deterministically`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T039 — Retain caller evidence for rejected and accepted candidates

Retain caller evidence for rejected and accepted candidates.

- **Routing name:** `retain-caller-evidence-for-rejected-and-accepted-candidates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T040 — Freeze raw somatic candidate callsets per specimen and patient

Freeze raw somatic candidate callsets per specimen and patient.

- **Routing name:** `freeze-raw-somatic-candidate-callsets-per-specimen-and-patient`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Artefact and germline filtering

### MYR-D004-T041 — Filter candidates using tumour-normal evidence, panel-of-normals recurrence, and germline population frequency

Filter candidates using tumour-normal evidence, panel-of-normals recurrence, and germline population frequency.

- **Routing name:** `filter-candidates-using-tumour-normal-evidence-panel-of-normals-recurrence-and-germline-population-frequency`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T042 — Model read-orientation artefacts from context-specific error priors

Model read-orientation artefacts from context-specific error priors.

- **Routing name:** `model-read-orientation-artefacts-from-context-specific-error-priors`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T043 — Filter oxidative, deamination, fixation, polymerase-slippage, and end-repair artefacts

Filter oxidative, deamination, fixation, polymerase-slippage, and end-repair artefacts.

- **Routing name:** `filter-oxidative-deamination-fixation-polymerase-slippage-and-end-repair-artefacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T044 — Flag candidates driven by low mapping quality, soft clipping, or paralogous alignments

Flag candidates driven by low mapping quality, soft clipping, or paralogous alignments.

- **Routing name:** `flag-candidates-driven-by-low-mapping-quality-soft-clipping-or-paralogous-alignments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T045 — Distinguish retained germline variants from somatic candidates using normal genotype likelihoods

Distinguish retained germline variants from somatic candidates using normal genotype likelihoods.

- **Routing name:** `distinguish-retained-germline-variants-from-somatic-candidates-using-normal-genotype-likelihoods`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T046 — Detect clonal-haematopoiesis variants in blood normals using gene, allele-fraction, and age-aware evidence

Detect clonal-haematopoiesis variants in blood normals using gene, allele-fraction, and age-aware evidence.

- **Routing name:** `detect-clonal-haematopoiesis-variants-in-blood-normals-using-gene-allele-fraction-and-age-aware-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T047 — Apply tumour-purity and local-copy-number-aware allele-fraction plausibility checks

Apply tumour-purity and local-copy-number-aware allele-fraction plausibility checks.

- **Routing name:** `apply-tumour-purity-and-local-copy-number-aware-allele-fraction-plausibility-checks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T048 — Filter sequencing-context artefacts in homopolymers, tandem repeats, and low-complexity regions

Filter sequencing-context artefacts in homopolymers, tandem repeats, and low-complexity regions.

- **Routing name:** `filter-sequencing-context-artefacts-in-homopolymers-tandem-repeats-and-low-complexity-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T049 — Require independent molecule or duplex support when the assay provides molecular barcodes

Require independent molecule or duplex support when the assay provides molecular barcodes.

- **Routing name:** `require-independent-molecule-or-duplex-support-when-the-assay-provides-molecular-barcodes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T050 — Emit explicit filter reasons without deleting rejected candidate records

Emit explicit filter reasons without deleting rejected candidate records.

- **Routing name:** `emit-explicit-filter-reasons-without-deleting-rejected-candidate-records`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Somatic copy-number and structural context

### MYR-D004-T051 — Estimate allele-specific copy number from tumour-normal depth and heterozygous germline sites

Estimate allele-specific copy number from tumour-normal depth and heterozygous germline sites.

- **Routing name:** `estimate-allele-specific-copy-number-from-tumour-normal-depth-and-heterozygous-germline-sites`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T052 — Segment copy-ratio and B-allele-frequency signals with assay-aware smoothing

Segment copy-ratio and B-allele-frequency signals with assay-aware smoothing.

- **Routing name:** `segment-copy-ratio-and-b-allele-frequency-signals-with-assay-aware-smoothing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T053 — Assign absolute major and minor copy-number states under purity-ploidy solutions

Assign absolute major and minor copy-number states under purity-ploidy solutions.

- **Routing name:** `assign-absolute-major-and-minor-copy-number-states-under-purity-ploidy-solutions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T054 — Detect focal amplifications, homozygous deletions, and arm-level alterations

Detect focal amplifications, homozygous deletions, and arm-level alterations.

- **Routing name:** `detect-focal-amplifications-homozygous-deletions-and-arm-level-alterations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T055 — Identify copy-neutral loss of heterozygosity and uniparental-disomy segments

Identify copy-neutral loss of heterozygosity and uniparental-disomy segments.

- **Routing name:** `identify-copy-neutral-loss-of-heterozygosity-and-uniparental-disomy-segments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T056 — Call structural variants and gene fusions from discordant, split, and assembly evidence

Call structural variants and gene fusions from discordant, split, and assembly evidence.

- **Routing name:** `call-structural-variants-and-gene-fusions-from-discordant-split-and-assembly-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T057 — Reconcile structural breakpoints with copy-number segment boundaries

Reconcile structural breakpoints with copy-number segment boundaries.

- **Routing name:** `reconcile-structural-breakpoints-with-copy-number-segment-boundaries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T058 — Annotate complex rearrangement patterns including chromothripsis-like signatures cautiously

Annotate complex rearrangement patterns including chromothripsis-like signatures cautiously.

- **Routing name:** `annotate-complex-rearrangement-patterns-including-chromothripsis-like-signatures-cautiously`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T059 — Calculate mutation multiplicity for SNVs located in altered copy-number segments

Calculate mutation multiplicity for SNVs located in altered copy-number segments.

- **Routing name:** `calculate-mutation-multiplicity-for-snvs-located-in-altered-copy-number-segments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T060 — Freeze a unified somatic genome-state model for downstream clonality inference

Freeze a unified somatic genome-state model for downstream clonality inference.

- **Routing name:** `freeze-a-unified-somatic-genome-state-model-for-downstream-clonality-inference`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Clonality and cancer-cell-fraction inference

### MYR-D004-T061 — Estimate cancer-cell fraction for each somatic variant from allele fraction, purity, and copy number

Estimate cancer-cell fraction for each somatic variant from allele fraction, purity, and copy number.

- **Routing name:** `estimate-cancer-cell-fraction-for-each-somatic-variant-from-allele-fraction-purity-and-copy-number`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T062 — Propagate uncertainty from depth, purity, and copy-number state into clonality intervals

Propagate uncertainty from depth, purity, and copy-number state into clonality intervals.

- **Routing name:** `propagate-uncertainty-from-depth-purity-and-copy-number-state-into-clonality-intervals`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T063 — Cluster mutations by compatible cancer-cell-fraction distributions

Cluster mutations by compatible cancer-cell-fraction distributions.

- **Routing name:** `cluster-mutations-by-compatible-cancer-cell-fraction-distributions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T064 — Distinguish clonal, subclonal, and indeterminate alterations using predefined posterior thresholds

Distinguish clonal, subclonal, and indeterminate alterations using predefined posterior thresholds.

- **Routing name:** `distinguish-clonal-subclonal-and-indeterminate-alterations-using-predefined-posterior-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T065 — Identify mutations duplicated before or after copy-number gains using multiplicity estimates

Identify mutations duplicated before or after copy-number gains using multiplicity estimates.

- **Routing name:** `identify-mutations-duplicated-before-or-after-copy-number-gains-using-multiplicity-estimates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T066 — Test cluster stability across alternative purity-ploidy solutions

Test cluster stability across alternative purity-ploidy solutions.

- **Routing name:** `test-cluster-stability-across-alternative-purity-ploidy-solutions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T067 — Detect clusters supported only by low-coverage or artefact-prone variants

Detect clusters supported only by low-coverage or artefact-prone variants.

- **Routing name:** `detect-clusters-supported-only-by-low-coverage-or-artefact-prone-variants`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T068 — Compare clonality estimates across callers or inference models

Compare clonality estimates across callers or inference models.

- **Routing name:** `compare-clonality-estimates-across-callers-or-inference-models`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T069 — Assign driver candidates to clonal architecture without overstating timing certainty

Assign driver candidates to clonal architecture without overstating timing certainty.

- **Routing name:** `assign-driver-candidates-to-clonal-architecture-without-overstating-timing-certainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T070 — Emit patient-level mutation clusters with uncertainty and supporting evidence

Emit patient-level mutation clusters with uncertainty and supporting evidence.

- **Routing name:** `emit-patient-level-mutation-clusters-with-uncertainty-and-supporting-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Spatial and longitudinal tumour evolution

### MYR-D004-T071 — Build a presence-absence and cancer-cell-fraction matrix across patient-matched specimens

Build a presence-absence and cancer-cell-fraction matrix across patient-matched specimens.

- **Routing name:** `build-a-presence-absence-and-cancer-cell-fraction-matrix-across-patient-matched-specimens`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T072 — Reconcile locus callability before treating absent variants as evolutionary losses

Reconcile locus callability before treating absent variants as evolutionary losses.

- **Routing name:** `reconcile-locus-callability-before-treating-absent-variants-as-evolutionary-losses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T073 — Infer candidate phylogenetic trees from shared and private mutation clusters

Infer candidate phylogenetic trees from shared and private mutation clusters.

- **Routing name:** `infer-candidate-phylogenetic-trees-from-shared-and-private-mutation-clusters`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T074 — Root tumour phylogenies using germline and normal-state assumptions

Root tumour phylogenies using germline and normal-state assumptions.

- **Routing name:** `root-tumour-phylogenies-using-germline-and-normal-state-assumptions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T075 — Identify trunk, branch, private, and convergent alterations across lesions or timepoints

Identify trunk, branch, private, and convergent alterations across lesions or timepoints.

- **Routing name:** `identify-trunk-branch-private-and-convergent-alterations-across-lesions-or-timepoints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T076 — Estimate treatment-associated clonal expansions and contractions with uncertainty

Estimate treatment-associated clonal expansions and contractions with uncertainty.

- **Routing name:** `estimate-treatment-associated-clonal-expansions-and-contractions-with-uncertainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T077 — Detect possible sample cross-contamination from implausible shared private mutations

Detect possible sample cross-contamination from implausible shared private mutations.

- **Routing name:** `detect-possible-sample-cross-contamination-from-implausible-shared-private-mutations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T078 — Compare alternative phylogenies and report unresolved branching relationships

Compare alternative phylogenies and report unresolved branching relationships.

- **Routing name:** `compare-alternative-phylogenies-and-report-unresolved-branching-relationships`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T079 — Map copy-number events and structural variants onto compatible evolutionary branches

Map copy-number events and structural variants onto compatible evolutionary branches.

- **Routing name:** `map-copy-number-events-and-structural-variants-onto-compatible-evolutionary-branches`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T080 — Generate a temporal or spatial evolution summary without inferring unsupported causality

Generate a temporal or spatial evolution summary without inferring unsupported causality.

- **Routing name:** `generate-a-temporal-or-spatial-evolution-summary-without-inferring-unsupported-causality`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Biological annotation and prioritization

### MYR-D004-T081 — Annotate somatic variants with transcript, protein, splice, regulatory, and hotspot consequences

Annotate somatic variants with transcript, protein, splice, regulatory, and hotspot consequences.

- **Routing name:** `annotate-somatic-variants-with-transcript-protein-splice-regulatory-and-hotspot-consequences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T082 — Attach cancer-gene, driver, pathway, and tumour-type evidence from versioned resources

Attach cancer-gene, driver, pathway, and tumour-type evidence from versioned resources.

- **Routing name:** `attach-cancer-gene-driver-pathway-and-tumour-type-evidence-from-versioned-resources`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T083 — Annotate population frequency to identify residual germline-like candidates

Annotate population frequency to identify residual germline-like candidates.

- **Routing name:** `annotate-population-frequency-to-identify-residual-germline-like-candidates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T084 — Flag variants in low-mappability, paralogous, or sequencing-artifact-prone regions

Flag variants in low-mappability, paralogous, or sequencing-artifact-prone regions.

- **Routing name:** `flag-variants-in-low-mappability-paralogous-or-sequencing-artifact-prone-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T085 — Prioritize alterations by evidence tier without converting research evidence into clinical recommendations

Prioritize alterations by evidence tier without converting research evidence into clinical recommendations.

- **Routing name:** `prioritize-alterations-by-evidence-tier-without-converting-research-evidence-into-clinical-recommendations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T086 — Identify biallelic inactivation patterns combining mutation, deletion, and loss of heterozygosity

Identify biallelic inactivation patterns combining mutation, deletion, and loss of heterozygosity.

- **Routing name:** `identify-biallelic-inactivation-patterns-combining-mutation-deletion-and-loss-of-heterozygosity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T087 — Detect mutually exclusive or co-occurring pathway alterations within the patient case

Detect mutually exclusive or co-occurring pathway alterations within the patient case.

- **Routing name:** `detect-mutually-exclusive-or-co-occurring-pathway-alterations-within-the-patient-case`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T088 — Annotate mutational signatures only when mutation counts and assay scope are adequate

Annotate mutational signatures only when mutation counts and assay scope are adequate.

- **Routing name:** `annotate-mutational-signatures-only-when-mutation-counts-and-assay-scope-are-adequate`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T089 — Link variants to supported targeted-therapy or resistance evidence with jurisdiction and disease context

Link variants to supported targeted-therapy or resistance evidence with jurisdiction and disease context.

- **Routing name:** `link-variants-to-supported-targeted-therapy-or-resistance-evidence-with-jurisdiction-and-disease-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T090 — Produce a ranked alteration table with evidence provenance and uncertainty flags

Produce a ranked alteration table with evidence provenance and uncertainty flags.

- **Routing name:** `produce-a-ranked-alteration-table-with-evidence-provenance-and-uncertainty-flags`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Reporting, release, and governance

### MYR-D004-T091 — Generate filtered and unfiltered somatic VCF or BCF files with tumour-normal labels intact

Generate filtered and unfiltered somatic VCF or BCF files with tumour-normal labels intact.

- **Routing name:** `generate-filtered-and-unfiltered-somatic-vcf-or-bcf-files-with-tumour-normal-labels-intact`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T092 — Create specimen-level and patient-level mutation, copy-number, and clonality tables

Create specimen-level and patient-level mutation, copy-number, and clonality tables.

- **Routing name:** `create-specimen-level-and-patient-level-mutation-copy-number-and-clonality-tables`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T093 — Report callability, purity, ploidy, contamination, artefact, and coverage limitations

Report callability, purity, ploidy, contamination, artefact, and coverage limitations.

- **Routing name:** `report-callability-purity-ploidy-contamination-artefact-and-coverage-limitations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T094 — Record every tool, reference, resource, parameter, and model version

Record every tool, reference, resource, parameter, and model version.

- **Routing name:** `record-every-tool-reference-resource-parameter-and-model-version`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T095 — Validate cross-file patient, specimen, coordinate, and variant identifiers

Validate cross-file patient, specimen, coordinate, and variant identifiers.

- **Routing name:** `validate-cross-file-patient-specimen-coordinate-and-variant-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T096 — Archive raw candidates, filter evidence, copy-number models, and phylogeny inputs

Archive raw candidates, filter evidence, copy-number models, and phylogeny inputs.

- **Routing name:** `archive-raw-candidates-filter-evidence-copy-number-models-and-phylogeny-inputs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T097 — Generate reproducibility manifests for each specimen and patient-level integration step

Generate reproducibility manifests for each specimen and patient-level integration step.

- **Routing name:** `generate-reproducibility-manifests-for-each-specimen-and-patient-level-integration-step`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T098 — Issue human-review flags for low purity, missing normal, discordant models, or unstable phylogeny

Issue human-review flags for low purity, missing normal, discordant models, or unstable phylogeny.

- **Routing name:** `issue-human-review-flags-for-low-purity-missing-normal-discordant-models-or-unstable-phylogeny`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T099 — Separate research prioritization from any clinical interpretation or treatment recommendation

Separate research prioritization from any clinical interpretation or treatment recommendation.

- **Routing name:** `separate-research-prioritization-from-any-clinical-interpretation-or-treatment-recommendation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D004-T100 — Release the analysis only when identity, artefact, genome-state, and reproducibility gates pass

Release the analysis only when identity, artefact, genome-state, and reproducibility gates pass.

- **Routing name:** `release-the-analysis-only-when-identity-artefact-genome-state-and-reproducibility-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
