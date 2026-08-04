# D015 — Epigenomic Profiling

Batch **002** · 10 workstreams · 100 tasks

## 01. Assay intake and epigenomic design

### MYR-D015-T001 — Validate sample, donor, tissue, condition, replicate, library, and sequencing-run identifiers

Validate sample, donor, tissue, condition, replicate, library, and sequencing-run identifiers.

- **Routing name:** `validate-sample-donor-tissue-condition-replicate-library-and-sequencing-run-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T002 — Record assay class, protocol version, antibody or enzyme, input control, spike-in, and library chemistry

Record assay class, protocol version, antibody or enzyme, input control, spike-in, and library chemistry.

- **Routing name:** `record-assay-class-protocol-version-antibody-or-enzyme-input-control-spike-in-and-library-chemistry`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T003 — Reconcile biological conditions, batches, extraction dates, operators, and sequencing runs with the design

Reconcile biological conditions, batches, extraction dates, operators, and sequencing runs with the design.

- **Routing name:** `reconcile-biological-conditions-batches-extraction-dates-operators-and-sequencing-runs-with-the-design`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T004 — Verify genome assembly, chromosome naming, blacklist, gene annotation, and mappability resource compatibility

Verify genome assembly, chromosome naming, blacklist, gene annotation, and mappability resource compatibility.

- **Routing name:** `verify-genome-assembly-chromosome-naming-blacklist-gene-annotation-and-mappability-resource-compatibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T005 — Define whether targets are narrow peaks, broad domains, accessibility regions, methylated cytosines, or nucleosome positions

Define whether targets are narrow peaks, broad domains, accessibility regions, methylated cytosines, or nucleosome positions.

- **Routing name:** `define-whether-targets-are-narrow-peaks-broad-domains-accessibility-regions-methylated-cytosines-or-nucleosome-positions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T006 — Confirm availability and pairing of input, IgG, mock, or untreated controls required by the assay

Confirm availability and pairing of input, IgG, mock, or untreated controls required by the assay.

- **Routing name:** `confirm-availability-and-pairing-of-input-igg-mock-or-untreated-controls-required-by-the-assay`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T007 — Declare primary contrasts, replicate rules, quality thresholds, and multiple-testing policy before analysis

Declare primary contrasts, replicate rules, quality thresholds, and multiple-testing policy before analysis.

- **Routing name:** `declare-primary-contrasts-replicate-rules-quality-thresholds-and-multiple-testing-policy-before-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T008 — Detect confounding of condition with antibody lot, protocol, batch, or sequencing platform

Detect confounding of condition with antibody lot, protocol, batch, or sequencing platform.

- **Routing name:** `detect-confounding-of-condition-with-antibody-lot-protocol-batch-or-sequencing-platform`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T009 — Freeze duplicate handling, peak calling, normalization, and consensus-region policies

Freeze duplicate handling, peak calling, normalization, and consensus-region policies.

- **Routing name:** `freeze-duplicate-handling-peak-calling-normalization-and-consensus-region-policies`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T010 — Freeze input checksums, container versions, parameters, and random seeds in the run manifest

Freeze input checksums, container versions, parameters, and random seeds in the run manifest.

- **Routing name:** `freeze-input-checksums-container-versions-parameters-and-random-seeds-in-the-run-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Raw-read and library quality control

### MYR-D015-T011 — Verify FASTQ integrity, pair synchronization, read length, and declared assay read structure

Verify FASTQ integrity, pair synchronization, read length, and declared assay read structure.

- **Routing name:** `verify-fastq-integrity-pair-synchronization-read-length-and-declared-assay-read-structure`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T012 — Summarize per-base quality, nucleotide composition, adapter contamination, and ambiguous-base rates

Summarize per-base quality, nucleotide composition, adapter contamination, and ambiguous-base rates.

- **Routing name:** `summarize-per-base-quality-nucleotide-composition-adapter-contamination-and-ambiguous-base-rates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T013 — Detect residual transposase, ligation, primer, and low-complexity sequence artefacts

Detect residual transposase, ligation, primer, and low-complexity sequence artefacts.

- **Routing name:** `detect-residual-transposase-ligation-primer-and-low-complexity-sequence-artefacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T014 — Estimate library complexity and duplicate saturation from deterministic subsampling

Estimate library complexity and duplicate saturation from deterministic subsampling.

- **Routing name:** `estimate-library-complexity-and-duplicate-saturation-from-deterministic-subsampling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T015 — Screen reads for microbial, vector, organellar, and cross-species contamination

Screen reads for microbial, vector, organellar, and cross-species contamination.

- **Routing name:** `screen-reads-for-microbial-vector-organellar-and-cross-species-contamination`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T016 — Compare quality profiles across antibody lots, protocol batches, lanes, and biological groups

Compare quality profiles across antibody lots, protocol batches, lanes, and biological groups.

- **Routing name:** `compare-quality-profiles-across-antibody-lots-protocol-batches-lanes-and-biological-groups`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T017 — Quantify spike-in reads separately from endogenous reads when spike-ins were used

Quantify spike-in reads separately from endogenous reads when spike-ins were used.

- **Routing name:** `quantify-spike-in-reads-separately-from-endogenous-reads-when-spike-ins-were-used`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T018 — Infer assay-specific fragment characteristics before and after trimming

Infer assay-specific fragment characteristics before and after trimming.

- **Routing name:** `infer-assay-specific-fragment-characteristics-before-and-after-trimming`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T019 — Quarantine malformed, truncated, orphaned, or non-IUPAC read records with reason codes

Quarantine malformed, truncated, orphaned, or non-IUPAC read records with reason codes.

- **Routing name:** `quarantine-malformed-truncated-orphaned-or-non-iupac-read-records-with-reason-codes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T020 — Issue library-level pass, warning, or fail status before alignment

Issue library-level pass, warning, or fail status before alignment.

- **Routing name:** `issue-library-level-pass-warning-or-fail-status-before-alignment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Alignment, filtering, and fragment processing

### MYR-D015-T021 — Build or verify the genome alignment index and chromosome dictionary from the frozen assembly

Build or verify the genome alignment index and chromosome dictionary from the frozen assembly.

- **Routing name:** `build-or-verify-the-genome-alignment-index-and-chromosome-dictionary-from-the-frozen-assembly`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T022 — Align reads with assay-appropriate local or end-to-end settings and complete read-group metadata

Align reads with assay-appropriate local or end-to-end settings and complete read-group metadata.

- **Routing name:** `align-reads-with-assay-appropriate-local-or-end-to-end-settings-and-complete-read-group-metadata`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T023 — Quantify unique, multimapped, unmapped, discordant, and chimeric alignment fractions

Quantify unique, multimapped, unmapped, discordant, and chimeric alignment fractions.

- **Routing name:** `quantify-unique-multimapped-unmapped-discordant-and-chimeric-alignment-fractions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T024 — Filter alignments by mapping quality using a prespecified threshold

Filter alignments by mapping quality using a prespecified threshold.

- **Routing name:** `filter-alignments-by-mapping-quality-using-a-prespecified-threshold`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T025 — Remove or separately quantify mitochondrial and organellar alignments according to assay policy

Remove or separately quantify mitochondrial and organellar alignments according to assay policy.

- **Routing name:** `remove-or-separately-quantify-mitochondrial-and-organellar-alignments-according-to-assay-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T026 — Remove blacklist-overlapping fragments only with the frozen blacklist version recorded

Remove blacklist-overlapping fragments only with the frozen blacklist version recorded.

- **Routing name:** `remove-blacklist-overlapping-fragments-only-with-the-frozen-blacklist-version-recorded`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T027 — Mark duplicates and apply assay-specific duplicate retention or removal rules

Mark duplicates and apply assay-specific duplicate retention or removal rules.

- **Routing name:** `mark-duplicates-and-apply-assay-specific-duplicate-retention-or-removal-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T028 — Correct paired-end fragment coordinates and validate insert-size distributions

Correct paired-end fragment coordinates and validate insert-size distributions.

- **Routing name:** `correct-paired-end-fragment-coordinates-and-validate-insert-size-distributions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T029 — Generate coordinate-sorted indexed alignments and fragment files with stable identifiers

Generate coordinate-sorted indexed alignments and fragment files with stable identifiers.

- **Routing name:** `generate-coordinate-sorted-indexed-alignments-and-fragment-files-with-stable-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T030 — Validate post-filter yield, chromosome coverage, and cross-file read-count reconciliation

Validate post-filter yield, chromosome coverage, and cross-file read-count reconciliation.

- **Routing name:** `validate-post-filter-yield-chromosome-coverage-and-cross-file-read-count-reconciliation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Accessibility and chromatin-enrichment quality assessment

### MYR-D015-T031 — Calculate transcription-start-site enrichment and nucleosome-free versus nucleosomal fragment fractions for ATAC-seq

Calculate transcription-start-site enrichment and nucleosome-free versus nucleosomal fragment fractions for ATAC-seq.

- **Routing name:** `calculate-transcription-start-site-enrichment-and-nucleosome-free-versus-nucleosomal-fragment-fractions-for-atac-seq`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T032 — Assess periodic nucleosomal fragment-length structure and transposase insertion profiles in accessibility libraries

Assess periodic nucleosomal fragment-length structure and transposase insertion profiles in accessibility libraries.

- **Routing name:** `assess-periodic-nucleosomal-fragment-length-structure-and-transposase-insertion-profiles-in-accessibility-libraries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T033 — Measure library complexity and fraction of reads in peaks for accessibility assays

Measure library complexity and fraction of reads in peaks for accessibility assays.

- **Routing name:** `measure-library-complexity-and-fraction-of-reads-in-peaks-for-accessibility-assays`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T034 — Calculate cross-correlation or strand-shift metrics appropriate to ChIP-seq target class

Calculate cross-correlation or strand-shift metrics appropriate to ChIP-seq target class.

- **Routing name:** `calculate-cross-correlation-or-strand-shift-metrics-appropriate-to-chip-seq-target-class`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T035 — Measure immunoprecipitation enrichment relative to input, IgG, or mock controls

Measure immunoprecipitation enrichment relative to input, IgG, or mock controls.

- **Routing name:** `measure-immunoprecipitation-enrichment-relative-to-input-igg-or-mock-controls`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T036 — Quantify fraction of reads in peaks for transcription-factor, histone-mark, CUT&RUN, and CUT&Tag assays

Quantify fraction of reads in peaks for transcription-factor, histone-mark, CUT&RUN, and CUT&Tag assays.

- **Routing name:** `quantify-fraction-of-reads-in-peaks-for-transcription-factor-histone-mark-cut-and-run-and-cut-and-tag-assays`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T037 — Evaluate replicate concordance using common bins and provisional peaks

Evaluate replicate concordance using common bins and provisional peaks.

- **Routing name:** `evaluate-replicate-concordance-using-common-bins-and-provisional-peaks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T038 — Assess spike-in recovery and scaling stability when exogenous chromatin was used

Assess spike-in recovery and scaling stability when exogenous chromatin was used.

- **Routing name:** `assess-spike-in-recovery-and-scaling-stability-when-exogenous-chromatin-was-used`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T039 — Detect low complexity, excessive background, weak enrichment, absent nucleosomal structure, or control failures

Detect low complexity, excessive background, weak enrichment, absent nucleosomal structure, or control failures.

- **Routing name:** `detect-low-complexity-excessive-background-weak-enrichment-absent-nucleosomal-structure-or-control-failures`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T040 — Assign assay-specific quality tiers using declared multimetric thresholds

Assign assay-specific quality tiers using declared multimetric thresholds.

- **Routing name:** `assign-assay-specific-quality-tiers-using-declared-multimetric-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. DNA methylation data processing and quality control

### MYR-D015-T041 — Validate bisulfite, enzymatic-conversion, or array-platform metadata and expected strand conventions

Validate bisulfite, enzymatic-conversion, or array-platform metadata and expected strand conventions.

- **Routing name:** `validate-bisulfite-enzymatic-conversion-or-array-platform-metadata-and-expected-strand-conventions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T042 — Trim conversion-specific adapters and biased terminal positions under a frozen policy

Trim conversion-specific adapters and biased terminal positions under a frozen policy.

- **Routing name:** `trim-conversion-specific-adapters-and-biased-terminal-positions-under-a-frozen-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T043 — Align converted reads with a methylation-aware aligner and report unique mapping

Align converted reads with a methylation-aware aligner and report unique mapping.

- **Routing name:** `align-converted-reads-with-a-methylation-aware-aligner-and-report-unique-mapping`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T044 — Estimate bisulfite or enzymatic conversion efficiency from spike-in or non-CpG cytosines

Estimate bisulfite or enzymatic conversion efficiency from spike-in or non-CpG cytosines.

- **Routing name:** `estimate-bisulfite-or-enzymatic-conversion-efficiency-from-spike-in-or-non-cpg-cytosines`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T045 — Deduplicate alignments with library-type-appropriate rules

Deduplicate alignments with library-type-appropriate rules.

- **Routing name:** `deduplicate-alignments-with-library-type-appropriate-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T046 — Call methylated and unmethylated counts separately for CpG and non-CpG contexts

Call methylated and unmethylated counts separately for CpG and non-CpG contexts.

- **Routing name:** `call-methylated-and-unmethylated-counts-separately-for-cpg-and-non-cpg-contexts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T047 — Filter cytosines with insufficient coverage or extreme strand disagreement

Filter cytosines with insufficient coverage or extreme strand disagreement.

- **Routing name:** `filter-cytosines-with-insufficient-coverage-or-extreme-strand-disagreement`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T048 — Calculate global CpG methylation and sample-level methylation distributions

Calculate global CpG methylation and sample-level methylation distributions.

- **Routing name:** `calculate-global-cpg-methylation-and-sample-level-methylation-distributions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T049 — For arrays, filter failed probes, cross-reactive probes, SNP-affected probes, and unsupported chromosomes

For arrays, filter failed probes, cross-reactive probes, SNP-affected probes, and unsupported chromosomes.

- **Routing name:** `for-arrays-filter-failed-probes-cross-reactive-probes-snp-affected-probes-and-unsupported-chromosomes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T050 — Issue methylation-sample pass, warning, or fail status using platform-specific metrics

Issue methylation-sample pass, warning, or fail status using platform-specific metrics.

- **Routing name:** `issue-methylation-sample-pass-warning-or-fail-status-using-platform-specific-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Peak, domain, and region definition

### MYR-D015-T051 — Call narrow accessibility or transcription-factor peaks against the declared control model

Call narrow accessibility or transcription-factor peaks against the declared control model.

- **Routing name:** `call-narrow-accessibility-or-transcription-factor-peaks-against-the-declared-control-model`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T052 — Call broad histone-mark domains with target-appropriate gap and enrichment settings

Call broad histone-mark domains with target-appropriate gap and enrichment settings.

- **Routing name:** `call-broad-histone-mark-domains-with-target-appropriate-gap-and-enrichment-settings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T053 — Call CUT&RUN or CUT&Tag peaks with low-background-compatible parameters

Call CUT&RUN or CUT&Tag peaks with low-background-compatible parameters.

- **Routing name:** `call-cut-and-run-or-cut-and-tag-peaks-with-low-background-compatible-parameters`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T054 — Generate replicate-specific peak sets without pooling away replicate information

Generate replicate-specific peak sets without pooling away replicate information.

- **Routing name:** `generate-replicate-specific-peak-sets-without-pooling-away-replicate-information`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T055 — Assess replicate concordance and irreproducibility using a declared framework

Assess replicate concordance and irreproducibility using a declared framework.

- **Routing name:** `assess-replicate-concordance-and-irreproducibility-using-a-declared-framework`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T056 — Construct consensus regions requiring a prespecified number of passing replicates

Construct consensus regions requiring a prespecified number of passing replicates.

- **Routing name:** `construct-consensus-regions-requiring-a-prespecified-number-of-passing-replicates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T057 — Merge nearby regions only under fixed distance and target-class rules

Merge nearby regions only under fixed distance and target-class rules.

- **Routing name:** `merge-nearby-regions-only-under-fixed-distance-and-target-class-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T058 — Remove blacklist and noncanonical regions while preserving an exclusion ledger

Remove blacklist and noncanonical regions while preserving an exclusion ledger.

- **Routing name:** `remove-blacklist-and-noncanonical-regions-while-preserving-an-exclusion-ledger`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T059 — Quantify sample-by-region fragment counts from the frozen consensus set

Quantify sample-by-region fragment counts from the frozen consensus set.

- **Routing name:** `quantify-sample-by-region-fragment-counts-from-the-frozen-consensus-set`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T060 — Annotate regions with nearest genes, promoters, enhancers, chromatin states, and genomic context

Annotate regions with nearest genes, promoters, enhancers, chromatin states, and genomic context.

- **Routing name:** `annotate-regions-with-nearest-genes-promoters-enhancers-chromatin-states-and-genomic-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Differential chromatin and methylation analysis

### MYR-D015-T061 — Normalize region counts with a method compatible with composition and depth differences

Normalize region counts with a method compatible with composition and depth differences.

- **Routing name:** `normalize-region-counts-with-a-method-compatible-with-composition-and-depth-differences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T062 — Test differential accessibility between conditions using biological replicates

Test differential accessibility between conditions using biological replicates.

- **Routing name:** `test-differential-accessibility-between-conditions-using-biological-replicates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T063 — Test differential transcription-factor or histone-mark occupancy with matched controls

Test differential transcription-factor or histone-mark occupancy with matched controls.

- **Routing name:** `test-differential-transcription-factor-or-histone-mark-occupancy-with-matched-controls`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T064 — Test condition-by-time or condition-by-genotype interactions in region counts

Test condition-by-time or condition-by-genotype interactions in region counts.

- **Routing name:** `test-condition-by-time-or-condition-by-genotype-interactions-in-region-counts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T065 — Identify differentially methylated cytosines using coverage-aware statistical models

Identify differentially methylated cytosines using coverage-aware statistical models.

- **Routing name:** `identify-differentially-methylated-cytosines-using-coverage-aware-statistical-models`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T066 — Aggregate cytosine evidence into differentially methylated regions with prespecified rules

Aggregate cytosine evidence into differentially methylated regions with prespecified rules.

- **Routing name:** `aggregate-cytosine-evidence-into-differentially-methylated-regions-with-prespecified-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T067 — Control false discovery over the declared region or cytosine testing universe

Control false discovery over the declared region or cytosine testing universe.

- **Routing name:** `control-false-discovery-over-the-declared-region-or-cytosine-testing-universe`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T068 — Require minimum absolute accessibility, occupancy, or methylation change for promotion

Require minimum absolute accessibility, occupancy, or methylation change for promotion.

- **Routing name:** `require-minimum-absolute-accessibility-occupancy-or-methylation-change-for-promotion`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T069 — Perform leave-one-replicate-out sensitivity analysis for leading differential regions

Perform leave-one-replicate-out sensitivity analysis for leading differential regions.

- **Routing name:** `perform-leave-one-replicate-out-sensitivity-analysis-for-leading-differential-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T070 — Return no-call status for under-replicated, confounded, or failed-quality comparisons

Return no-call status for under-replicated, confounded, or failed-quality comparisons.

- **Routing name:** `return-no-call-status-for-under-replicated-confounded-or-failed-quality-comparisons`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Regulatory interpretation and motif analysis

### MYR-D015-T071 — Test sequence motifs for enrichment using matched genomic background regions

Test sequence motifs for enrichment using matched genomic background regions.

- **Routing name:** `test-sequence-motifs-for-enrichment-using-matched-genomic-background-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T072 — Scan regions for motif instances with frozen motif database and score thresholds

Scan regions for motif instances with frozen motif database and score thresholds.

- **Routing name:** `scan-regions-for-motif-instances-with-frozen-motif-database-and-score-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T073 — Calculate transcription-factor footprint profiles only when depth and assay assumptions are satisfied

Calculate transcription-factor footprint profiles only when depth and assay assumptions are satisfied.

- **Routing name:** `calculate-transcription-factor-footprint-profiles-only-when-depth-and-assay-assumptions-are-satisfied`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T074 — Link distal regions to candidate genes using proximity, correlation, or validated contact evidence

Link distal regions to candidate genes using proximity, correlation, or validated contact evidence.

- **Routing name:** `link-distal-regions-to-candidate-genes-using-proximity-correlation-or-validated-contact-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T075 — Overlay regions with known enhancers, promoters, chromatin states, and disease-associated variants

Overlay regions with known enhancers, promoters, chromatin states, and disease-associated variants.

- **Routing name:** `overlay-regions-with-known-enhancers-promoters-chromatin-states-and-disease-associated-variants`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T076 — Identify region modules with coordinated accessibility, occupancy, or methylation changes

Identify region modules with coordinated accessibility, occupancy, or methylation changes.

- **Routing name:** `identify-region-modules-with-coordinated-accessibility-occupancy-or-methylation-changes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T077 — Test gene-set enrichment using genes linked under a declared region-to-gene policy

Test gene-set enrichment using genes linked under a declared region-to-gene policy.

- **Routing name:** `test-gene-set-enrichment-using-genes-linked-under-a-declared-region-to-gene-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T078 — Compare epigenomic changes with matched gene-expression changes when available

Compare epigenomic changes with matched gene-expression changes when available.

- **Routing name:** `compare-epigenomic-changes-with-matched-gene-expression-changes-when-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T079 — Distinguish motif presence, footprinting, and direct binding evidence in all interpretations

Distinguish motif presence, footprinting, and direct binding evidence in all interpretations.

- **Routing name:** `distinguish-motif-presence-footprinting-and-direct-binding-evidence-in-all-interpretations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T080 — Export region-to-gene, region-to-motif, and region-to-annotation evidence tables

Export region-to-gene, region-to-motif, and region-to-annotation evidence tables.

- **Routing name:** `export-region-to-gene-region-to-motif-and-region-to-annotation-evidence-tables`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Cross-assay integration and robustness

### MYR-D015-T081 — Compare accessibility peaks with transcription-factor and histone-mark occupancy

Compare accessibility peaks with transcription-factor and histone-mark occupancy.

- **Routing name:** `compare-accessibility-peaks-with-transcription-factor-and-histone-mark-occupancy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T082 — Overlay DNA methylation changes with promoter and enhancer accessibility changes

Overlay DNA methylation changes with promoter and enhancer accessibility changes.

- **Routing name:** `overlay-dna-methylation-changes-with-promoter-and-enhancer-accessibility-changes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T083 — Reconcile ATAC-seq, ChIP-seq, CUT&RUN, and CUT&Tag coordinates on one genome build

Reconcile ATAC-seq, ChIP-seq, CUT&RUN, and CUT&Tag coordinates on one genome build.

- **Routing name:** `reconcile-atac-seq-chip-seq-cut-and-run-and-cut-and-tag-coordinates-on-one-genome-build`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T084 — Assess sensitivity of consensus regions to peak caller and parameter choices

Assess sensitivity of consensus regions to peak caller and parameter choices.

- **Routing name:** `assess-sensitivity-of-consensus-regions-to-peak-caller-and-parameter-choices`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T085 — Assess sensitivity of differential results to normalization and region-definition choices

Assess sensitivity of differential results to normalization and region-definition choices.

- **Routing name:** `assess-sensitivity-of-differential-results-to-normalization-and-region-definition-choices`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T086 — Quantify concordance across biological replicates and independent assay modalities

Quantify concordance across biological replicates and independent assay modalities.

- **Routing name:** `quantify-concordance-across-biological-replicates-and-independent-assay-modalities`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T087 — Detect apparent changes driven by altered cell-type composition in bulk tissue

Detect apparent changes driven by altered cell-type composition in bulk tissue.

- **Routing name:** `detect-apparent-changes-driven-by-altered-cell-type-composition-in-bulk-tissue`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T088 — Validate leading regions using orthogonal assays or public reference epigenomes when appropriate

Validate leading regions using orthogonal assays or public reference epigenomes when appropriate.

- **Routing name:** `validate-leading-regions-using-orthogonal-assays-or-public-reference-epigenomes-when-appropriate`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T089 — Classify findings as robust, assay-specific, composition-sensitive, or unresolved

Classify findings as robust, assay-specific, composition-sensitive, or unresolved.

- **Routing name:** `classify-findings-as-robust-assay-specific-composition-sensitive-or-unresolved`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T090 — Create a review packet with coverage tracks, region counts, models, and annotation evidence

Create a review packet with coverage tracks, region counts, models, and annotation evidence.

- **Routing name:** `create-a-review-packet-with-coverage-tracks-region-counts-models-and-annotation-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Release, provenance, and review gates

### MYR-D015-T091 — Export filtered alignments, fragments, coverage tracks, peaks, consensus regions, counts, and differential tables

Export filtered alignments, fragments, coverage tracks, peaks, consensus regions, counts, and differential tables.

- **Routing name:** `export-filtered-alignments-fragments-coverage-tracks-peaks-consensus-regions-counts-and-differential-tables`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T092 — Generate machine-readable assay-specific QC tables with thresholds and statuses

Generate machine-readable assay-specific QC tables with thresholds and statuses.

- **Routing name:** `generate-machine-readable-assay-specific-qc-tables-with-thresholds-and-statuses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T093 — Record genome, blacklist, annotation, antibody, control, pipeline, parameter, and seed provenance

Record genome, blacklist, annotation, antibody, control, pipeline, parameter, and seed provenance.

- **Routing name:** `record-genome-blacklist-annotation-antibody-control-pipeline-parameter-and-seed-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T094 — Validate chromosome, coordinate, sample, and region identifiers across every release artifact

Validate chromosome, coordinate, sample, and region identifiers across every release artifact.

- **Routing name:** `validate-chromosome-coordinate-sample-and-region-identifiers-across-every-release-artifact`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T095 — Archive peak-calling logs, replicate diagnostics, conversion metrics, and statistical model outputs

Archive peak-calling logs, replicate diagnostics, conversion metrics, and statistical model outputs.

- **Routing name:** `archive-peak-calling-logs-replicate-diagnostics-conversion-metrics-and-statistical-model-outputs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T096 — Create bulk-epigenomics reproducibility commands or workflow configurations for primary and sensitivity analyses

Create bulk-epigenomics reproducibility commands or workflow configurations for primary and sensitivity analyses.

- **Routing name:** `create-bulk-epigenomics-reproducibility-commands-or-workflow-configurations-for-primary-and-sensitivity-analyses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T097 — Flag regions supported by one replicate, one antibody lot, or one analysis method

Flag regions supported by one replicate, one antibody lot, or one analysis method.

- **Routing name:** `flag-regions-supported-by-one-replicate-one-antibody-lot-or-one-analysis-method`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T098 — Prevent automatic claims of causal regulation from accessibility, motif, or correlation evidence alone

Prevent automatic claims of causal regulation from accessibility, motif, or correlation evidence alone.

- **Routing name:** `prevent-automatic-claims-of-causal-regulation-from-accessibility-motif-or-correlation-evidence-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T099 — Require qualified review for clinical, diagnostic, or therapeutic interpretation

Require qualified review for clinical, diagnostic, or therapeutic interpretation.

- **Routing name:** `require-qualified-review-for-clinical-diagnostic-or-therapeutic-interpretation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D015-T100 — Release the analysis only when assay-specific QC, statistical, provenance, and review gates pass

Release the analysis only when assay-specific QC, statistical, provenance, and review gates pass.

- **Routing name:** `release-the-analysis-only-when-assay-specific-qc-statistical-provenance-and-review-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
