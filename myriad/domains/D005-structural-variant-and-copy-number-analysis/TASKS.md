# D005 — Structural Variant and Copy-Number Analysis

Batch **001** · 10 workstreams · 100 tasks

## 01. Analysis design and input qualification

### MYR-D005-T001 — Validate sample, library, pedigree, assay, and reference-build metadata for structural-variant analysis

Validate sample, library, pedigree, assay, and reference-build metadata for structural-variant analysis.

- **Routing name:** `validate-sample-library-pedigree-assay-and-reference-build-metadata-for-structural-variant-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T002 — Verify FASTQ, BAM, CRAM, VCF, BED, reference, and index integrity before processing

Verify FASTQ, BAM, CRAM, VCF, BED, reference, and index integrity before processing.

- **Routing name:** `verify-fastq-bam-cram-vcf-bed-reference-and-index-integrity-before-processing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T003 — Declare targeted, exome, short-read genome, long-read genome, optical-map, or hybrid analysis mode

Declare targeted, exome, short-read genome, long-read genome, optical-map, or hybrid analysis mode.

- **Routing name:** `declare-targeted-exome-short-read-genome-long-read-genome-optical-map-or-hybrid-analysis-mode`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T004 — Define minimum detectable event sizes and variant classes for the selected assay

Define minimum detectable event sizes and variant classes for the selected assay.

- **Routing name:** `define-minimum-detectable-event-sizes-and-variant-classes-for-the-selected-assay`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T005 — Record sample ploidy, sex-chromosome model, tumour status, and expected mosaicism

Record sample ploidy, sex-chromosome model, tumour status, and expected mosaicism.

- **Routing name:** `record-sample-ploidy-sex-chromosome-model-tumour-status-and-expected-mosaicism`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T006 — Define analysis regions, excluded gaps, low-mappability masks, and segmental-duplication masks

Define analysis regions, excluded gaps, low-mappability masks, and segmental-duplication masks.

- **Routing name:** `define-analysis-regions-excluded-gaps-low-mappability-masks-and-segmental-duplication-masks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T007 — Select compatible truth sets, population resources, and panel-of-normal resources

Select compatible truth sets, population resources, and panel-of-normal resources.

- **Routing name:** `select-compatible-truth-sets-population-resources-and-panel-of-normal-resources`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T008 — Set minimum split-read, paired-end, depth, assembly, or molecule support thresholds

Set minimum split-read, paired-end, depth, assembly, or molecule support thresholds.

- **Routing name:** `set-minimum-split-read-paired-end-depth-assembly-or-molecule-support-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T009 — Define cohort genotyping, family analysis, and release representation policies

Define cohort genotyping, family analysis, and release representation policies.

- **Routing name:** `define-cohort-genotyping-family-analysis-and-release-representation-policies`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T010 — Freeze aligner, caller, segmentation, genotyper, annotation, container, and reference versions

Freeze aligner, caller, segmentation, genotyper, annotation, container, and reference versions.

- **Routing name:** `freeze-aligner-caller-segmentation-genotyper-annotation-container-and-reference-versions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Alignment evidence and coverage modelling

### MYR-D005-T011 — Align reads with presets preserving split, supplementary, and discordant-pair evidence

Align reads with presets preserving split, supplementary, and discordant-pair evidence.

- **Routing name:** `align-reads-with-presets-preserving-split-supplementary-and-discordant-pair-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T012 — Validate supplementary alignment tags, mate information, CIGAR strings, and coordinate order

Validate supplementary alignment tags, mate information, CIGAR strings, and coordinate order.

- **Routing name:** `validate-supplementary-alignment-tags-mate-information-cigar-strings-and-coordinate-order`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T013 — Compute insert-size distributions and define discordant-pair orientation thresholds per library

Compute insert-size distributions and define discordant-pair orientation thresholds per library.

- **Routing name:** `compute-insert-size-distributions-and-define-discordant-pair-orientation-thresholds-per-library`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T014 — Quantify split-read, soft-clipped, unmapped-mate, and anomalous-depth evidence

Quantify split-read, soft-clipped, unmapped-mate, and anomalous-depth evidence.

- **Routing name:** `quantify-split-read-soft-clipped-unmapped-mate-and-anomalous-depth-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T015 — Generate GC-corrected and mappability-aware depth bins at assay-appropriate resolution

Generate GC-corrected and mappability-aware depth bins at assay-appropriate resolution.

- **Routing name:** `generate-gc-corrected-and-mappability-aware-depth-bins-at-assay-appropriate-resolution`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T016 — Identify coverage waves, capture bias, and replication-timing artefacts

Identify coverage waves, capture bias, and replication-timing artefacts.

- **Routing name:** `identify-coverage-waves-capture-bias-and-replication-timing-artefacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T017 — Measure chromosome-specific baseline depth under sex and ploidy assumptions

Measure chromosome-specific baseline depth under sex and ploidy assumptions.

- **Routing name:** `measure-chromosome-specific-baseline-depth-under-sex-and-ploidy-assumptions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T018 — Detect sample contamination, swaps, and mixtures affecting allele-balance evidence

Detect sample contamination, swaps, and mixtures affecting allele-balance evidence.

- **Routing name:** `detect-sample-contamination-swaps-and-mixtures-affecting-allele-balance-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T019 — Estimate long-read length and mapping-quality sufficiency for breakpoint resolution

Estimate long-read length and mapping-quality sufficiency for breakpoint resolution.

- **Routing name:** `estimate-long-read-length-and-mapping-quality-sufficiency-for-breakpoint-resolution`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T020 — Freeze evidence tracks and QC metrics for caller-independent reuse

Freeze evidence tracks and QC metrics for caller-independent reuse.

- **Routing name:** `freeze-evidence-tracks-and-qc-metrics-for-caller-independent-reuse`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Structural-variant candidate discovery

### MYR-D005-T021 — Call deletion candidates from concordant split-read and paired-end evidence

Call deletion candidates from concordant split-read and paired-end evidence.

- **Routing name:** `call-deletion-candidates-from-concordant-split-read-and-paired-end-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T022 — Call tandem-duplication candidates from orientation-specific breakpoint evidence

Call tandem-duplication candidates from orientation-specific breakpoint evidence.

- **Routing name:** `call-tandem-duplication-candidates-from-orientation-specific-breakpoint-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T023 — Call inversion candidates while distinguishing inverted duplications and mapping artefacts

Call inversion candidates while distinguishing inverted duplications and mapping artefacts.

- **Routing name:** `call-inversion-candidates-while-distinguishing-inverted-duplications-and-mapping-artefacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T024 — Call interchromosomal and intrachromosomal translocation candidates

Call interchromosomal and intrachromosomal translocation candidates.

- **Routing name:** `call-interchromosomal-and-intrachromosomal-translocation-candidates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T025 — Call insertion candidates and retain inserted-sequence evidence when recoverable

Call insertion candidates and retain inserted-sequence evidence when recoverable.

- **Routing name:** `call-insertion-candidates-and-retain-inserted-sequence-evidence-when-recoverable`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T026 — Call mobile-element insertion candidates with family and orientation evidence

Call mobile-element insertion candidates with family and orientation evidence.

- **Routing name:** `call-mobile-element-insertion-candidates-with-family-and-orientation-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T027 — Assemble breakpoint-spanning reads locally for sequence-resolved candidate refinement

Assemble breakpoint-spanning reads locally for sequence-resolved candidate refinement.

- **Routing name:** `assemble-breakpoint-spanning-reads-locally-for-sequence-resolved-candidate-refinement`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T028 — Call long-read structural variants with technology-specific error modelling

Call long-read structural variants with technology-specific error modelling.

- **Routing name:** `call-long-read-structural-variants-with-technology-specific-error-modelling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T029 — Detect complex multi-breakpoint events without prematurely decomposing them

Detect complex multi-breakpoint events without prematurely decomposing them.

- **Routing name:** `detect-complex-multi-breakpoint-events-without-prematurely-decomposing-them`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T030 — Retain raw caller evidence and failure states for every candidate set

Retain raw caller evidence and failure states for every candidate set.

- **Routing name:** `retain-raw-caller-evidence-and-failure-states-for-every-candidate-set`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Copy-number segmentation and state inference

### MYR-D005-T031 — Normalize read depth against matched normals or an assay-compatible reference panel

Normalize read depth against matched normals or an assay-compatible reference panel.

- **Routing name:** `normalize-read-depth-against-matched-normals-or-an-assay-compatible-reference-panel`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T032 — Segment normalized depth into candidate copy-number regions

Segment normalized depth into candidate copy-number regions.

- **Routing name:** `segment-normalized-depth-into-candidate-copy-number-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T033 — Incorporate heterozygous-allele balance into allele-specific segmentation

Incorporate heterozygous-allele balance into allele-specific segmentation.

- **Routing name:** `incorporate-heterozygous-allele-balance-into-allele-specific-segmentation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T034 — Infer integer copy-number states under declared ploidy assumptions

Infer integer copy-number states under declared ploidy assumptions.

- **Routing name:** `infer-integer-copy-number-states-under-declared-ploidy-assumptions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T035 — Detect focal gains, focal losses, arm-level changes, and whole-chromosome aneuploidy

Detect focal gains, focal losses, arm-level changes, and whole-chromosome aneuploidy.

- **Routing name:** `detect-focal-gains-focal-losses-arm-level-changes-and-whole-chromosome-aneuploidy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T036 — Detect copy-neutral loss of heterozygosity from allele balance without depth change

Detect copy-neutral loss of heterozygosity from allele balance without depth change.

- **Routing name:** `detect-copy-neutral-loss-of-heterozygosity-from-allele-balance-without-depth-change`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T037 — Model mosaic copy-number fractions from attenuated depth and allele-balance shifts

Model mosaic copy-number fractions from attenuated depth and allele-balance shifts.

- **Routing name:** `model-mosaic-copy-number-fractions-from-attenuated-depth-and-allele-balance-shifts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T038 — Resolve sex-chromosome copy number under inferred genetic sex and pseudoautosomal boundaries

Resolve sex-chromosome copy number under inferred genetic sex and pseudoautosomal boundaries.

- **Routing name:** `resolve-sex-chromosome-copy-number-under-inferred-genetic-sex-and-pseudoautosomal-boundaries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T039 — Quantify segmentation uncertainty and alternative state assignments

Quantify segmentation uncertainty and alternative state assignments.

- **Routing name:** `quantify-segmentation-uncertainty-and-alternative-state-assignments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T040 — Freeze copy-number segments before integration with breakpoint calls

Freeze copy-number segments before integration with breakpoint calls.

- **Routing name:** `freeze-copy-number-segments-before-integration-with-breakpoint-calls`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Breakpoint refinement and sequence resolution

### MYR-D005-T041 — Cluster breakpoint evidence within technology-specific positional tolerances

Cluster breakpoint evidence within technology-specific positional tolerances.

- **Routing name:** `cluster-breakpoint-evidence-within-technology-specific-positional-tolerances`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T042 — Refine breakpoints using split-read alignments and local realignment

Refine breakpoints using split-read alignments and local realignment.

- **Routing name:** `refine-breakpoints-using-split-read-alignments-and-local-realignment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T043 — Reconstruct inserted sequence from soft-clipped, assembled, or long-read evidence

Reconstruct inserted sequence from soft-clipped, assembled, or long-read evidence.

- **Routing name:** `reconstruct-inserted-sequence-from-soft-clipped-assembled-or-long-read-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T044 — Classify breakpoint microhomology, blunt joins, and templated insertions

Classify breakpoint microhomology, blunt joins, and templated insertions.

- **Routing name:** `classify-breakpoint-microhomology-blunt-joins-and-templated-insertions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T045 — Normalize breakpoint orientation and confidence intervals into a canonical representation

Normalize breakpoint orientation and confidence intervals into a canonical representation.

- **Routing name:** `normalize-breakpoint-orientation-and-confidence-intervals-into-a-canonical-representation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T046 — Distinguish tandem duplication from interspersed duplication using flanking sequence context

Distinguish tandem duplication from interspersed duplication using flanking sequence context.

- **Routing name:** `distinguish-tandem-duplication-from-interspersed-duplication-using-flanking-sequence-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T047 — Resolve nested or overlapping events without double-counting supporting reads

Resolve nested or overlapping events without double-counting supporting reads.

- **Routing name:** `resolve-nested-or-overlapping-events-without-double-counting-supporting-reads`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T048 — Phase structural variants to nearby heterozygous markers when evidence permits

Phase structural variants to nearby heterozygous markers when evidence permits.

- **Routing name:** `phase-structural-variants-to-nearby-heterozygous-markers-when-evidence-permits`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T049 — Detect reference-assembly gaps or alternate-locus artefacts masquerading as breakpoints

Detect reference-assembly gaps or alternate-locus artefacts masquerading as breakpoints.

- **Routing name:** `detect-reference-assembly-gaps-or-alternate-locus-artefacts-masquerading-as-breakpoints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T050 — Assign sequence-resolved, interval-resolved, or unresolved status to every event

Assign sequence-resolved, interval-resolved, or unresolved status to every event.

- **Routing name:** `assign-sequence-resolved-interval-resolved-or-unresolved-status-to-every-event`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Multi-caller integration and genotyping

### MYR-D005-T051 — Normalize caller-specific structural-variant records into a shared event schema

Normalize caller-specific structural-variant records into a shared event schema.

- **Routing name:** `normalize-caller-specific-structural-variant-records-into-a-shared-event-schema`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T052 — Cluster equivalent events using breakpoint, size, orientation, and sequence similarity

Cluster equivalent events using breakpoint, size, orientation, and sequence similarity.

- **Routing name:** `cluster-equivalent-events-using-breakpoint-size-orientation-and-sequence-similarity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T053 — Prevent merging distinct adjacent events in repetitive or rearranged regions

Prevent merging distinct adjacent events in repetitive or rearranged regions.

- **Routing name:** `prevent-merging-distinct-adjacent-events-in-repetitive-or-rearranged-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T054 — Select a representative consensus breakpoint while preserving all source calls

Select a representative consensus breakpoint while preserving all source calls.

- **Routing name:** `select-a-representative-consensus-breakpoint-while-preserving-all-source-calls`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T055 — Genotype consensus structural variants across all cohort samples

Genotype consensus structural variants across all cohort samples.

- **Routing name:** `genotype-consensus-structural-variants-across-all-cohort-samples`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T056 — Calculate genotype likelihoods from depth, split-read, paired-end, and long-read evidence

Calculate genotype likelihoods from depth, split-read, paired-end, and long-read evidence.

- **Routing name:** `calculate-genotype-likelihoods-from-depth-split-read-paired-end-and-long-read-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T057 — Assign no-call genotypes when local evidence or mappability is insufficient

Assign no-call genotypes when local evidence or mappability is insufficient.

- **Routing name:** `assign-no-call-genotypes-when-local-evidence-or-mappability-is-insufficient`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T058 — Reconcile copy-number genotypes with structural breakpoint genotypes

Reconcile copy-number genotypes with structural breakpoint genotypes.

- **Routing name:** `reconcile-copy-number-genotypes-with-structural-breakpoint-genotypes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T059 — Detect Mendelian inconsistencies and possible de novo structural variants in families

Detect Mendelian inconsistencies and possible de novo structural variants in families.

- **Routing name:** `detect-mendelian-inconsistencies-and-possible-de-novo-structural-variants-in-families`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T060 — Emit a provenance graph linking consensus events to every supporting caller record

Emit a provenance graph linking consensus events to every supporting caller record.

- **Routing name:** `emit-a-provenance-graph-linking-consensus-events-to-every-supporting-caller-record`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Quality filtering and artefact control

### MYR-D005-T061 — Filter events below class-specific support thresholds while retaining rejected records

Filter events below class-specific support thresholds while retaining rejected records.

- **Routing name:** `filter-events-below-class-specific-support-thresholds-while-retaining-rejected-records`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T062 — Flag breakpoints in low-mappability, satellite, centromeric, telomeric, or assembly-gap regions

Flag breakpoints in low-mappability, satellite, centromeric, telomeric, or assembly-gap regions.

- **Routing name:** `flag-breakpoints-in-low-mappability-satellite-centromeric-telomeric-or-assembly-gap-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T063 — Detect recurrent technical artefacts using control cohorts or panels of normals

Detect recurrent technical artefacts using control cohorts or panels of normals.

- **Routing name:** `detect-recurrent-technical-artefacts-using-control-cohorts-or-panels-of-normals`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T064 — Filter depth-only events driven by GC waves, capture boundaries, or batch effects

Filter depth-only events driven by GC waves, capture boundaries, or batch effects.

- **Routing name:** `filter-depth-only-events-driven-by-gc-waves-capture-boundaries-or-batch-effects`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T065 — Flag events with contradictory breakpoint orientation or impossible molecule geometry

Flag events with contradictory breakpoint orientation or impossible molecule geometry.

- **Routing name:** `flag-events-with-contradictory-breakpoint-orientation-or-impossible-molecule-geometry`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T066 — Detect paralogous-sequence and segmental-duplication mapping artefacts

Detect paralogous-sequence and segmental-duplication mapping artefacts.

- **Routing name:** `detect-paralogous-sequence-and-segmental-duplication-mapping-artefacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T067 — Evaluate allele-balance consistency for heterozygous deletions and duplications

Evaluate allele-balance consistency for heterozygous deletions and duplications.

- **Routing name:** `evaluate-allele-balance-consistency-for-heterozygous-deletions-and-duplications`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T068 — Apply size- and assay-specific minimum quality thresholds

Apply size- and assay-specific minimum quality thresholds.

- **Routing name:** `apply-size-and-assay-specific-minimum-quality-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T069 — Calibrate mosaic event thresholds from empirical background distributions

Calibrate mosaic event thresholds from empirical background distributions.

- **Routing name:** `calibrate-mosaic-event-thresholds-from-empirical-background-distributions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T070 — Generate explicit filter-reason and evidence-summary fields for each event

Generate explicit filter-reason and evidence-summary fields for each event.

- **Routing name:** `generate-explicit-filter-reason-and-evidence-summary-fields-for-each-event`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Functional and clinical annotation

### MYR-D005-T071 — Annotate genes, transcripts, exons, regulatory elements, and conserved regions affected by each event

Annotate genes, transcripts, exons, regulatory elements, and conserved regions affected by each event.

- **Routing name:** `annotate-genes-transcripts-exons-regulatory-elements-and-conserved-regions-affected-by-each-event`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T072 — Determine predicted loss-of-function, duplication, fusion, position-effect, or dosage consequences

Determine predicted loss-of-function, duplication, fusion, position-effect, or dosage consequences.

- **Routing name:** `determine-predicted-loss-of-function-duplication-fusion-position-effect-or-dosage-consequences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T073 — Annotate breakpoint disruption and gene-fusion orientation with transcript compatibility checks

Annotate breakpoint disruption and gene-fusion orientation with transcript compatibility checks.

- **Routing name:** `annotate-breakpoint-disruption-and-gene-fusion-orientation-with-transcript-compatibility-checks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T074 — Attach population structural-variant frequencies from reference-build-matched resources

Attach population structural-variant frequencies from reference-build-matched resources.

- **Routing name:** `attach-population-structural-variant-frequencies-from-reference-build-matched-resources`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T075 — Annotate dosage-sensitive genes and curated haploinsufficiency or triplosensitivity evidence

Annotate dosage-sensitive genes and curated haploinsufficiency or triplosensitivity evidence.

- **Routing name:** `annotate-dosage-sensitive-genes-and-curated-haploinsufficiency-or-triplosensitivity-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T076 — Flag events overlapping known benign polymorphic regions or recurrent technical regions

Flag events overlapping known benign polymorphic regions or recurrent technical regions.

- **Routing name:** `flag-events-overlapping-known-benign-polymorphic-regions-or-recurrent-technical-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T077 — Annotate inheritance, segregation, de novo status, and mosaic fraction in family datasets

Annotate inheritance, segregation, de novo status, and mosaic fraction in family datasets.

- **Routing name:** `annotate-inheritance-segregation-de-novo-status-and-mosaic-fraction-in-family-datasets`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T078 — Calculate affected coding bases and transcript fractions for partial-gene events

Calculate affected coding bases and transcript fractions for partial-gene events.

- **Routing name:** `calculate-affected-coding-bases-and-transcript-fractions-for-partial-gene-events`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T079 — Annotate complex events without reducing them to unsupported simple interpretations

Annotate complex events without reducing them to unsupported simple interpretations.

- **Routing name:** `annotate-complex-events-without-reducing-them-to-unsupported-simple-interpretations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T080 — Emit an evidence table keyed by stable structural-variant identifiers

Emit an evidence table keyed by stable structural-variant identifiers.

- **Routing name:** `emit-an-evidence-table-keyed-by-stable-structural-variant-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Cohort and comparative analysis

### MYR-D005-T081 — Calculate structural-variant allele frequencies with genotype missingness accounted for

Calculate structural-variant allele frequencies with genotype missingness accounted for.

- **Routing name:** `calculate-structural-variant-allele-frequencies-with-genotype-missingness-accounted-for`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T082 — Detect batch-associated event frequency differences across platforms or laboratories

Detect batch-associated event frequency differences across platforms or laboratories.

- **Routing name:** `detect-batch-associated-event-frequency-differences-across-platforms-or-laboratories`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T083 — Cluster recurrent breakpoints and copy-number regions across the cohort

Cluster recurrent breakpoints and copy-number regions across the cohort.

- **Routing name:** `cluster-recurrent-breakpoints-and-copy-number-regions-across-the-cohort`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T084 — Test enrichment of events in cases versus controls using appropriate burden models

Test enrichment of events in cases versus controls using appropriate burden models.

- **Routing name:** `test-enrichment-of-events-in-cases-versus-controls-using-appropriate-burden-models`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T085 — Compare event spectra by ancestry, sex, phenotype, tissue, or disease subgroup

Compare event spectra by ancestry, sex, phenotype, tissue, or disease subgroup.

- **Routing name:** `compare-event-spectra-by-ancestry-sex-phenotype-tissue-or-disease-subgroup`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T086 — Identify rare private and recurrent de novo structural variants

Identify rare private and recurrent de novo structural variants.

- **Routing name:** `identify-rare-private-and-recurrent-de-novo-structural-variants`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T087 — Measure caller sensitivity and precision against truth sets stratified by event class and region

Measure caller sensitivity and precision against truth sets stratified by event class and region.

- **Routing name:** `measure-caller-sensitivity-and-precision-against-truth-sets-stratified-by-event-class-and-region`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T088 — Quantify genotype concordance among technical replicates and orthogonal assays

Quantify genotype concordance among technical replicates and orthogonal assays.

- **Routing name:** `quantify-genotype-concordance-among-technical-replicates-and-orthogonal-assays`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T089 — Generate size, chromosome, class, and genomic-context distribution summaries

Generate size, chromosome, class, and genomic-context distribution summaries.

- **Routing name:** `generate-size-chromosome-class-and-genomic-context-distribution-summaries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T090 — Produce reversible cohort exclusion lists for low-quality samples and loci

Produce reversible cohort exclusion lists for low-quality samples and loci.

- **Routing name:** `produce-reversible-cohort-exclusion-lists-for-low-quality-samples-and-loci`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Release and reproducibility

### MYR-D005-T091 — Create normalized structural-variant VCF or BCF and copy-number segment releases

Create normalized structural-variant VCF or BCF and copy-number segment releases.

- **Routing name:** `create-normalized-structural-variant-vcf-or-bcf-and-copy-number-segment-releases`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T092 — Generate BEDPE, breakpoint-sequence, genotype, and evidence-summary artifacts

Generate BEDPE, breakpoint-sequence, genotype, and evidence-summary artifacts.

- **Routing name:** `generate-bedpe-breakpoint-sequence-genotype-and-evidence-summary-artifacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T093 — Validate record syntax, coordinate conventions, orientation fields, and reference alleles

Validate record syntax, coordinate conventions, orientation fields, and reference alleles.

- **Routing name:** `validate-record-syntax-coordinate-conventions-orientation-fields-and-reference-alleles`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T094 — Verify sample identifiers and event identifiers across all release files

Verify sample identifiers and event identifiers across all release files.

- **Routing name:** `verify-sample-identifiers-and-event-identifiers-across-all-release-files`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T095 — Record tool, reference, resource, parameter, and container versions

Record tool, reference, resource, parameter, and container versions.

- **Routing name:** `record-tool-reference-resource-parameter-and-container-versions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T096 — Archive raw calls, consensus clusters, rejected events, and copy-number models

Archive raw calls, consensus clusters, rejected events, and copy-number models.

- **Routing name:** `archive-raw-calls-consensus-clusters-rejected-events-and-copy-number-models`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T097 — Generate replay manifests for discovery, integration, genotyping, and annotation steps

Generate replay manifests for discovery, integration, genotyping, and annotation steps.

- **Routing name:** `generate-replay-manifests-for-discovery-integration-genotyping-and-annotation-steps`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T098 — Issue human-review flags for complex, mosaic, low-mappability, or clinically consequential events

Issue human-review flags for complex, mosaic, low-mappability, or clinically consequential events.

- **Routing name:** `issue-human-review-flags-for-complex-mosaic-low-mappability-or-clinically-consequential-events`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T099 — Separate computational consequence annotation from clinical classification

Separate computational consequence annotation from clinical classification.

- **Routing name:** `separate-computational-consequence-annotation-from-clinical-classification`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D005-T100 — Release the callset only when evidence, representation, genotype, and integrity gates pass

Release the callset only when evidence, representation, genotype, and integrity gates pass.

- **Routing name:** `release-the-callset-only-when-evidence-representation-genotype-and-integrity-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
