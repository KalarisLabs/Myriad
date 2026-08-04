# D003 — Germline Small-Variant Discovery

Batch **001** · 10 workstreams · 100 tasks

## 01. Study intake and sample identity

### MYR-D003-T001 — Validate sample manifests, pedigree files, assay metadata, and unique read-group identifiers

Validate sample manifests, pedigree files, assay metadata, and unique read-group identifiers.

- **Routing name:** `validate-sample-manifests-pedigree-files-assay-metadata-and-unique-read-group-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T002 — Verify FASTQ, BAM, CRAM, reference, interval, and known-sites checksums before processing

Verify FASTQ, BAM, CRAM, reference, interval, and known-sites checksums before processing.

- **Routing name:** `verify-fastq-bam-cram-reference-interval-and-known-sites-checksums-before-processing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T003 — Confirm reference build, decoy content, alternate contigs, and sequence-dictionary compatibility

Confirm reference build, decoy content, alternate contigs, and sequence-dictionary compatibility.

- **Routing name:** `confirm-reference-build-decoy-content-alternate-contigs-and-sequence-dictionary-compatibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T004 — Reconcile declared sex and pedigree relationships with available metadata before analysis

Reconcile declared sex and pedigree relationships with available metadata before analysis.

- **Routing name:** `reconcile-declared-sex-and-pedigree-relationships-with-available-metadata-before-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T005 — Define callable regions, excluded regions, and assay-specific coverage expectations

Define callable regions, excluded regions, and assay-specific coverage expectations.

- **Routing name:** `define-callable-regions-excluded-regions-and-assay-specific-coverage-expectations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T006 — Record sequencing platform, library preparation, capture kit, and read-layout metadata

Record sequencing platform, library preparation, capture kit, and read-layout metadata.

- **Routing name:** `record-sequencing-platform-library-preparation-capture-kit-and-read-layout-metadata`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T007 — Detect duplicate sample aliases and conflicting identifiers across laboratory and analysis systems

Detect duplicate sample aliases and conflicting identifiers across laboratory and analysis systems.

- **Routing name:** `detect-duplicate-sample-aliases-and-conflicting-identifiers-across-laboratory-and-analysis-systems`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T008 — Define cohort-level joint-genotyping groups and prohibited cross-study merges

Define cohort-level joint-genotyping groups and prohibited cross-study merges.

- **Routing name:** `define-cohort-level-joint-genotyping-groups-and-prohibited-cross-study-merges`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T009 — Set minimum sample, locus, genotype, and cohort quality thresholds in a frozen policy

Set minimum sample, locus, genotype, and cohort quality thresholds in a frozen policy.

- **Routing name:** `set-minimum-sample-locus-genotype-and-cohort-quality-thresholds-in-a-frozen-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T010 — Freeze caller, aligner, recalibration, annotation, container, and reference-resource versions

Freeze caller, aligner, recalibration, annotation, container, and reference-resource versions.

- **Routing name:** `freeze-caller-aligner-recalibration-annotation-container-and-reference-resource-versions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Raw-read preprocessing

### MYR-D003-T011 — Assess per-cycle base quality, nucleotide composition, adapter content, and read-length distributions

Assess per-cycle base quality, nucleotide composition, adapter content, and read-length distributions.

- **Routing name:** `assess-per-cycle-base-quality-nucleotide-composition-adapter-content-and-read-length-distributions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T012 — Detect malformed FASTQ records, duplicate read identifiers, and truncated paired-end files

Detect malformed FASTQ records, duplicate read identifiers, and truncated paired-end files.

- **Routing name:** `detect-malformed-fastq-records-duplicate-read-identifiers-and-truncated-paired-end-files`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T013 — Trim confirmed adapters only when they materially affect alignment or insert-size metrics

Trim confirmed adapters only when they materially affect alignment or insert-size metrics.

- **Routing name:** `trim-confirmed-adapters-only-when-they-materially-affect-alignment-or-insert-size-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T014 — Reject or quarantine samples with insufficient yield for declared assay requirements

Reject or quarantine samples with insufficient yield for declared assay requirements.

- **Routing name:** `reject-or-quarantine-samples-with-insufficient-yield-for-declared-assay-requirements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T015 — Estimate cross-sample contamination from k-mers or common polymorphic loci before alignment

Estimate cross-sample contamination from k-mers or common polymorphic loci before alignment.

- **Routing name:** `estimate-cross-sample-contamination-from-k-mers-or-common-polymorphic-loci-before-alignment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T016 — Partition reads by read group while preserving original lane and library provenance

Partition reads by read group while preserving original lane and library provenance.

- **Routing name:** `partition-reads-by-read-group-while-preserving-original-lane-and-library-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T017 — Validate paired-end synchronization and identify orphaned mates

Validate paired-end synchronization and identify orphaned mates.

- **Routing name:** `validate-paired-end-synchronization-and-identify-orphaned-mates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T018 — Quantify optical, patterned-flow-cell, and sequence duplicate indicators at the read level

Quantify optical, patterned-flow-cell, and sequence duplicate indicators at the read level.

- **Routing name:** `quantify-optical-patterned-flow-cell-and-sequence-duplicate-indicators-at-the-read-level`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T019 — Emit a pre-alignment sample disposition with pass, warning, fail, or waiver status

Emit a pre-alignment sample disposition with pass, warning, fail, or waiver status.

- **Routing name:** `emit-a-pre-alignment-sample-disposition-with-pass-warning-fail-or-waiver-status`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T020 — Create immutable normalized FASTQ manifests for downstream alignment

Create immutable normalized FASTQ manifests for downstream alignment.

- **Routing name:** `create-immutable-normalized-fastq-manifests-for-downstream-alignment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Alignment and post-alignment processing

### MYR-D003-T021 — Align reads to the declared reference with technology-appropriate deterministic parameters

Align reads to the declared reference with technology-appropriate deterministic parameters.

- **Routing name:** `align-reads-to-the-declared-reference-with-technology-appropriate-deterministic-parameters`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T022 — Sort alignments and validate coordinate order, mate consistency, CIGAR syntax, and reference tags

Sort alignments and validate coordinate order, mate consistency, CIGAR syntax, and reference tags.

- **Routing name:** `sort-alignments-and-validate-coordinate-order-mate-consistency-cigar-syntax-and-reference-tags`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T023 — Mark or model duplicate fragments while retaining library-specific duplicate metrics

Mark or model duplicate fragments while retaining library-specific duplicate metrics.

- **Routing name:** `mark-or-model-duplicate-fragments-while-retaining-library-specific-duplicate-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T024 — Recalculate base-quality scores only when the required training resources are compatible

Recalculate base-quality scores only when the required training resources are compatible.

- **Routing name:** `recalculate-base-quality-scores-only-when-the-required-training-resources-are-compatible`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T025 — Compute coverage, mapping quality, insert size, duplication, mismatch, and clipping metrics

Compute coverage, mapping quality, insert size, duplication, mismatch, and clipping metrics.

- **Routing name:** `compute-coverage-mapping-quality-insert-size-duplication-mismatch-and-clipping-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T026 — Detect contamination, sample swaps, and unexpected mixtures from common variant sites

Detect contamination, sample swaps, and unexpected mixtures from common variant sites.

- **Routing name:** `detect-contamination-sample-swaps-and-unexpected-mixtures-from-common-variant-sites`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T027 — Infer genetic sex from sex-chromosome coverage and heterozygosity with assay-aware thresholds

Infer genetic sex from sex-chromosome coverage and heterozygosity with assay-aware thresholds.

- **Routing name:** `infer-genetic-sex-from-sex-chromosome-coverage-and-heterozygosity-with-assay-aware-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T028 — Verify fingerprint concordance across lanes, libraries, and technical replicates

Verify fingerprint concordance across lanes, libraries, and technical replicates.

- **Routing name:** `verify-fingerprint-concordance-across-lanes-libraries-and-technical-replicates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T029 — Identify regions with anomalous depth caused by capture failure, paralogy, or reference gaps

Identify regions with anomalous depth caused by capture failure, paralogy, or reference gaps.

- **Routing name:** `identify-regions-with-anomalous-depth-caused-by-capture-failure-paralogy-or-reference-gaps`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T030 — Freeze analysis-ready BAM or CRAM files with indexes, checksums, and validation reports

Freeze analysis-ready BAM or CRAM files with indexes, checksums, and validation reports.

- **Routing name:** `freeze-analysis-ready-bam-or-cram-files-with-indexes-checksums-and-validation-reports`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Per-sample variant calling

### MYR-D003-T031 — Run haplotype-aware per-sample variant calling in reference-confidence mode

Run haplotype-aware per-sample variant calling in reference-confidence mode.

- **Routing name:** `run-haplotype-aware-per-sample-variant-calling-in-reference-confidence-mode`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T032 — Restrict calling to declared intervals while retaining padding sufficient for local assembly

Restrict calling to declared intervals while retaining padding sufficient for local assembly.

- **Routing name:** `restrict-calling-to-declared-intervals-while-retaining-padding-sufficient-for-local-assembly`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T033 — Handle haploid, diploid, mitochondrial, and sex-chromosome ploidy according to sample context

Handle haploid, diploid, mitochondrial, and sex-chromosome ploidy according to sample context.

- **Routing name:** `handle-haploid-diploid-mitochondrial-and-sex-chromosome-ploidy-according-to-sample-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T034 — Capture active-region, assembly, and likelihood warnings from caller logs

Capture active-region, assembly, and likelihood warnings from caller logs.

- **Routing name:** `capture-active-region-assembly-and-likelihood-warnings-from-caller-logs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T035 — Validate reference-confidence blocks, variant records, and genotype-likelihood fields

Validate reference-confidence blocks, variant records, and genotype-likelihood fields.

- **Routing name:** `validate-reference-confidence-blocks-variant-records-and-genotype-likelihood-fields`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T036 — Detect samples with abnormal variant count, transition-transversion ratio, or heterozygosity

Detect samples with abnormal variant count, transition-transversion ratio, or heterozygosity.

- **Routing name:** `detect-samples-with-abnormal-variant-count-transition-transversion-ratio-or-heterozygosity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T037 — Measure per-sample callability by depth, mapping quality, and genotype-quality thresholds

Measure per-sample callability by depth, mapping quality, and genotype-quality thresholds.

- **Routing name:** `measure-per-sample-callability-by-depth-mapping-quality-and-genotype-quality-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T038 — Quarantine gVCFs with truncated blocks, incompatible headers, or unsorted records

Quarantine gVCFs with truncated blocks, incompatible headers, or unsorted records.

- **Routing name:** `quarantine-gvcfs-with-truncated-blocks-incompatible-headers-or-unsorted-records`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T039 — Combine only compatible per-sample gVCFs using deterministic interval sharding

Combine only compatible per-sample gVCFs using deterministic interval sharding.

- **Routing name:** `combine-only-compatible-per-sample-gvcfs-using-deterministic-interval-sharding`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T040 — Record sample-level calling provenance and resource consumption

Record sample-level calling provenance and resource consumption.

- **Routing name:** `record-sample-level-calling-provenance-and-resource-consumption`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Joint genotyping and cohort consolidation

### MYR-D003-T041 — Joint-genotype cohort gVCFs with a fixed sample set and reference build

Joint-genotype cohort gVCFs with a fixed sample set and reference build.

- **Routing name:** `joint-genotype-cohort-gvcfs-with-a-fixed-sample-set-and-reference-build`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T042 — Consolidate interval-sharded genotype outputs while checking boundary consistency

Consolidate interval-sharded genotype outputs while checking boundary consistency.

- **Routing name:** `consolidate-interval-sharded-genotype-outputs-while-checking-boundary-consistency`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T043 — Retain invariant reference-confidence information required for cohort callability analysis

Retain invariant reference-confidence information required for cohort callability analysis.

- **Routing name:** `retain-invariant-reference-confidence-information-required-for-cohort-callability-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T044 — Detect multiallelic sites and preserve allele-specific annotation fields

Detect multiallelic sites and preserve allele-specific annotation fields.

- **Routing name:** `detect-multiallelic-sites-and-preserve-allele-specific-annotation-fields`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T045 — Reconcile duplicate samples or monozygotic pairs before cohort statistics are calculated

Reconcile duplicate samples or monozygotic pairs before cohort statistics are calculated.

- **Routing name:** `reconcile-duplicate-samples-or-monozygotic-pairs-before-cohort-statistics-are-calculated`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T046 — Measure cohort missingness, allele counts, genotype counts, and Hardy-Weinberg statistics

Measure cohort missingness, allele counts, genotype counts, and Hardy-Weinberg statistics.

- **Routing name:** `measure-cohort-missingness-allele-counts-genotype-counts-and-hardy-weinberg-statistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T047 — Identify batch-specific allele-frequency and missingness anomalies

Identify batch-specific allele-frequency and missingness anomalies.

- **Routing name:** `identify-batch-specific-allele-frequency-and-missingness-anomalies`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T048 — Detect genotype discordance among technical replicates and known pedigree pairs

Detect genotype discordance among technical replicates and known pedigree pairs.

- **Routing name:** `detect-genotype-discordance-among-technical-replicates-and-known-pedigree-pairs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T049 — Quarantine loci with malformed alleles, invalid genotypes, or inconsistent ploidy

Quarantine loci with malformed alleles, invalid genotypes, or inconsistent ploidy.

- **Routing name:** `quarantine-loci-with-malformed-alleles-invalid-genotypes-or-inconsistent-ploidy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T050 — Freeze the raw joint callset with a complete sample-order manifest

Freeze the raw joint callset with a complete sample-order manifest.

- **Routing name:** `freeze-the-raw-joint-callset-with-a-complete-sample-order-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Variant normalization and representation

### MYR-D003-T051 — Split or retain multiallelic records according to the declared downstream representation policy

Split or retain multiallelic records according to the declared downstream representation policy.

- **Routing name:** `split-or-retain-multiallelic-records-according-to-the-declared-downstream-representation-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T052 — Left-align and parsimoniously trim SNV and indel alleles against the exact reference build

Left-align and parsimoniously trim SNV and indel alleles against the exact reference build.

- **Routing name:** `left-align-and-parsimoniously-trim-snv-and-indel-alleles-against-the-exact-reference-build`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T053 — Decompose complex substitutions only when phase and biological equivalence are preserved

Decompose complex substitutions only when phase and biological equivalence are preserved.

- **Routing name:** `decompose-complex-substitutions-only-when-phase-and-biological-equivalence-are-preserved`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T054 — Normalize symbolic, spanning-deletion, and star alleles without losing genotype meaning

Normalize symbolic, spanning-deletion, and star alleles without losing genotype meaning.

- **Routing name:** `normalize-symbolic-spanning-deletion-and-star-alleles-without-losing-genotype-meaning`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T055 — Assign stable internal identifiers from reference build, contig, position, reference, and alternate allele

Assign stable internal identifiers from reference build, contig, position, reference, and alternate allele.

- **Routing name:** `assign-stable-internal-identifiers-from-reference-build-contig-position-reference-and-alternate-allele`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T056 — Validate reference alleles against the reference FASTA and quarantine mismatches

Validate reference alleles against the reference FASTA and quarantine mismatches.

- **Routing name:** `validate-reference-alleles-against-the-reference-fasta-and-quarantine-mismatches`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T057 — Recalculate allele-specific annotations after decomposition or splitting

Recalculate allele-specific annotations after decomposition or splitting.

- **Routing name:** `recalculate-allele-specific-annotations-after-decomposition-or-splitting`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T058 — Remove exact duplicate records while preserving provenance from all source shards

Remove exact duplicate records while preserving provenance from all source shards.

- **Routing name:** `remove-exact-duplicate-records-while-preserving-provenance-from-all-source-shards`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T059 — Sort records by declared contig order and validate tabix-compatible coordinate ordering

Sort records by declared contig order and validate tabix-compatible coordinate ordering.

- **Routing name:** `sort-records-by-declared-contig-order-and-validate-tabix-compatible-coordinate-ordering`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T060 — Emit a normalization audit mapping raw records to released records

Emit a normalization audit mapping raw records to released records.

- **Routing name:** `emit-a-normalization-audit-mapping-raw-records-to-released-records`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Variant quality modelling and filtering

### MYR-D003-T061 — Select hard filtering or statistical recalibration based on cohort size and truth-resource suitability

Select hard filtering or statistical recalibration based on cohort size and truth-resource suitability.

- **Routing name:** `select-hard-filtering-or-statistical-recalibration-based-on-cohort-size-and-truth-resource-suitability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T062 — Train separate quality models for SNVs and indels using compatible labelled resources

Train separate quality models for SNVs and indels using compatible labelled resources.

- **Routing name:** `train-separate-quality-models-for-snvs-and-indels-using-compatible-labelled-resources`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T063 — Evaluate model separation, sensitivity tranches, and annotation distributions before application

Evaluate model separation, sensitivity tranches, and annotation distributions before application.

- **Routing name:** `evaluate-model-separation-sensitivity-tranches-and-annotation-distributions-before-application`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T064 — Apply allele-specific quality filters to multiallelic records when supported

Apply allele-specific quality filters to multiallelic records when supported.

- **Routing name:** `apply-allele-specific-quality-filters-to-multiallelic-records-when-supported`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T065 — Define assay-specific hard filters for depth, strand bias, mapping quality, and read-position bias

Define assay-specific hard filters for depth, strand bias, mapping quality, and read-position bias.

- **Routing name:** `define-assay-specific-hard-filters-for-depth-strand-bias-mapping-quality-and-read-position-bias`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T066 — Flag low-complexity, segmental-duplication, and low-mappability loci using declared masks

Flag low-complexity, segmental-duplication, and low-mappability loci using declared masks.

- **Routing name:** `flag-low-complexity-segmental-duplication-and-low-mappability-loci-using-declared-masks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T067 — Detect excess heterozygosity and site-level contamination signatures

Detect excess heterozygosity and site-level contamination signatures.

- **Routing name:** `detect-excess-heterozygosity-and-site-level-contamination-signatures`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T068 — Apply genotype-level filters independently from site-level filters

Apply genotype-level filters independently from site-level filters.

- **Routing name:** `apply-genotype-level-filters-independently-from-site-level-filters`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T069 — Calibrate no-call rules for low-depth or low-genotype-quality genotypes

Calibrate no-call rules for low-depth or low-genotype-quality genotypes.

- **Routing name:** `calibrate-no-call-rules-for-low-depth-or-low-genotype-quality-genotypes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T070 — Generate filter-reason counts and preserve failed variants in an auditable callset

Generate filter-reason counts and preserve failed variants in an auditable callset.

- **Routing name:** `generate-filter-reason-counts-and-preserve-failed-variants-in-an-auditable-callset`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Functional and population annotation

### MYR-D003-T071 — Annotate allele frequencies from versioned ancestry-aware population resources

Annotate allele frequencies from versioned ancestry-aware population resources.

- **Routing name:** `annotate-allele-frequencies-from-versioned-ancestry-aware-population-resources`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T072 — Annotate transcript consequences using a declared transcript set and canonical-selection policy

Annotate transcript consequences using a declared transcript set and canonical-selection policy.

- **Routing name:** `annotate-transcript-consequences-using-a-declared-transcript-set-and-canonical-selection-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T073 — Annotate coding impact, splice-region context, regulatory overlap, and conservation scores

Annotate coding impact, splice-region context, regulatory overlap, and conservation scores.

- **Routing name:** `annotate-coding-impact-splice-region-context-regulatory-overlap-and-conservation-scores`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T074 — Attach clinical database assertions without treating imported classifications as independent evidence

Attach clinical database assertions without treating imported classifications as independent evidence.

- **Routing name:** `attach-clinical-database-assertions-without-treating-imported-classifications-as-independent-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T075 — Annotate gene constraint, dosage sensitivity, disease validity, and inheritance information

Annotate gene constraint, dosage sensitivity, disease validity, and inheritance information.

- **Routing name:** `annotate-gene-constraint-dosage-sensitivity-disease-validity-and-inheritance-information`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T076 — Flag variants in pseudogenes, paralogous regions, segmental duplications, and homologous loci

Flag variants in pseudogenes, paralogous regions, segmental duplications, and homologous loci.

- **Routing name:** `flag-variants-in-pseudogenes-paralogous-regions-segmental-duplications-and-homologous-loci`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T077 — Annotate assay callability and local sequencing-context limitations per variant

Annotate assay callability and local sequencing-context limitations per variant.

- **Routing name:** `annotate-assay-callability-and-local-sequencing-context-limitations-per-variant`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T078 — Record annotation-source versions, access dates, and transcript identifiers

Record annotation-source versions, access dates, and transcript identifiers.

- **Routing name:** `record-annotation-source-versions-access-dates-and-transcript-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T079 — Detect conflicting annotations caused by reference-build or transcript-version mismatches

Detect conflicting annotations caused by reference-build or transcript-version mismatches.

- **Routing name:** `detect-conflicting-annotations-caused-by-reference-build-or-transcript-version-mismatches`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T080 — Emit a normalized machine-readable annotation table keyed by stable variant identifiers

Emit a normalized machine-readable annotation table keyed by stable variant identifiers.

- **Routing name:** `emit-a-normalized-machine-readable-annotation-table-keyed-by-stable-variant-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Sample, pedigree, and cohort quality control

### MYR-D003-T081 — Calculate sample missingness, heterozygosity, singleton count, and transition-transversion ratio

Calculate sample missingness, heterozygosity, singleton count, and transition-transversion ratio.

- **Routing name:** `calculate-sample-missingness-heterozygosity-singleton-count-and-transition-transversion-ratio`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T082 — Estimate pairwise relatedness and compare inferred relationships with the pedigree

Estimate pairwise relatedness and compare inferred relationships with the pedigree.

- **Routing name:** `estimate-pairwise-relatedness-and-compare-inferred-relationships-with-the-pedigree`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T083 — Detect sample swaps using fingerprint concordance and pedigree incompatibilities

Detect sample swaps using fingerprint concordance and pedigree incompatibilities.

- **Routing name:** `detect-sample-swaps-using-fingerprint-concordance-and-pedigree-incompatibilities`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T084 — Identify population-structure outliers relative to the intended analysis cohort

Identify population-structure outliers relative to the intended analysis cohort.

- **Routing name:** `identify-population-structure-outliers-relative-to-the-intended-analysis-cohort`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T085 — Measure Mendelian-error rates by family and genomic region

Measure Mendelian-error rates by family and genomic region.

- **Routing name:** `measure-mendelian-error-rates-by-family-and-genomic-region`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T086 — Assess allele balance distributions for heterozygous SNVs and indels

Assess allele balance distributions for heterozygous SNVs and indels.

- **Routing name:** `assess-allele-balance-distributions-for-heterozygous-snvs-and-indels`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T087 — Detect contamination or mosaicism signatures from allele-balance and genotype-likelihood patterns

Detect contamination or mosaicism signatures from allele-balance and genotype-likelihood patterns.

- **Routing name:** `detect-contamination-or-mosaicism-signatures-from-allele-balance-and-genotype-likelihood-patterns`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T088 — Quantify batch effects by sequencing run, capture kit, laboratory, and analysis date

Quantify batch effects by sequencing run, capture kit, laboratory, and analysis date.

- **Routing name:** `quantify-batch-effects-by-sequencing-run-capture-kit-laboratory-and-analysis-date`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T089 — Define sample and locus exclusions before downstream association or diagnostic analysis

Define sample and locus exclusions before downstream association or diagnostic analysis.

- **Routing name:** `define-sample-and-locus-exclusions-before-downstream-association-or-diagnostic-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T090 — Generate a cohort QC report with reversible exclusion lists and waiver records

Generate a cohort QC report with reversible exclusion lists and waiver records.

- **Routing name:** `generate-a-cohort-qc-report-with-reversible-exclusion-lists-and-waiver-records`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Release and reproducibility

### MYR-D003-T091 — Create filtered and unfiltered VCF or BCF releases with consistent headers and sample order

Create filtered and unfiltered VCF or BCF releases with consistent headers and sample order.

- **Routing name:** `create-filtered-and-unfiltered-vcf-or-bcf-releases-with-consistent-headers-and-sample-order`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T092 — Generate per-sample callable-region masks and cohort callability summaries

Generate per-sample callable-region masks and cohort callability summaries.

- **Routing name:** `generate-per-sample-callable-region-masks-and-cohort-callability-summaries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T093 — Publish site, genotype, sample, and annotation QC metrics in machine-readable tables

Publish site, genotype, sample, and annotation QC metrics in machine-readable tables.

- **Routing name:** `publish-site-genotype-sample-and-annotation-qc-metrics-in-machine-readable-tables`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T094 — Record every software, reference, resource, parameter, and container version

Record every software, reference, resource, parameter, and container version.

- **Routing name:** `record-every-software-reference-resource-parameter-and-container-version`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T095 — Validate VCF specification compliance, indexing, and random access across release files

Validate VCF specification compliance, indexing, and random access across release files.

- **Routing name:** `validate-vcf-specification-compliance-indexing-and-random-access-across-release-files`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T096 — Verify checksums and sample identifiers across callsets, metrics, and manifests

Verify checksums and sample identifiers across callsets, metrics, and manifests.

- **Routing name:** `verify-checksums-and-sample-identifiers-across-callsets-metrics-and-manifests`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T097 — Archive raw joint genotypes, normalized callsets, failed variants, and filter evidence

Archive raw joint genotypes, normalized callsets, failed variants, and filter evidence.

- **Routing name:** `archive-raw-joint-genotypes-normalized-callsets-failed-variants-and-filter-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T098 — Generate workflow replay commands and interval-shard manifests

Generate workflow replay commands and interval-shard manifests.

- **Routing name:** `generate-workflow-replay-commands-and-interval-shard-manifests`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T099 — Issue human-review flags for pedigree conflicts, contamination, sex discordance, or unusual ploidy

Issue human-review flags for pedigree conflicts, contamination, sex discordance, or unusual ploidy.

- **Routing name:** `issue-human-review-flags-for-pedigree-conflicts-contamination-sex-discordance-or-unusual-ploidy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D003-T100 — Release the germline callset only when identity, callability, representation, and quality gates pass

Release the germline callset only when identity, callability, representation, and quality gates pass.

- **Routing name:** `release-the-germline-callset-only-when-identity-callability-representation-and-quality-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
