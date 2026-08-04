# D012 — Alternative Splicing and Isoform Analysis

Batch **002** · 10 workstreams · 100 tasks

## 01. Study design and isoform analysis contract

### MYR-D012-T001 — Validate sample, library, condition, replicate, and subject identifiers for the splicing study

Validate sample, library, condition, replicate, and subject identifiers for the splicing study.

- **Routing name:** `validate-sample-library-condition-replicate-and-subject-identifiers-for-the-splicing-study`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T002 — Record read length, layout, strandedness, RNA selection, and short-read or long-read sequencing chemistry

Record read length, layout, strandedness, RNA selection, and short-read or long-read sequencing chemistry.

- **Routing name:** `record-read-length-layout-strandedness-rna-selection-and-short-read-or-long-read-sequencing-chemistry`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T003 — Define whether inference targets splice events, exon usage, transcript usage, full-length isoforms, or gene-level expression

Define whether inference targets splice events, exon usage, transcript usage, full-length isoforms, or gene-level expression.

- **Routing name:** `define-whether-inference-targets-splice-events-exon-usage-transcript-usage-full-length-isoforms-or-gene-level-expression`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T004 — Verify that requested condition comparisons contain adequate biological replication for differential splicing

Verify that requested condition comparisons contain adequate biological replication for differential splicing.

- **Routing name:** `verify-that-requested-condition-comparisons-contain-adequate-biological-replication-for-differential-splicing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T005 — Detect confounding of condition with read length, library chemistry, sequencing run, or RNA quality

Detect confounding of condition with read length, library chemistry, sequencing run, or RNA quality.

- **Routing name:** `detect-confounding-of-condition-with-read-length-library-chemistry-sequencing-run-or-rna-quality`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T006 — Freeze the genome assembly, transcript annotation, splice-site convention, and chromosome naming scheme

Freeze the genome assembly, transcript annotation, splice-site convention, and chromosome naming scheme.

- **Routing name:** `freeze-the-genome-assembly-transcript-annotation-splice-site-convention-and-chromosome-naming-scheme`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T007 — Declare whether novel junctions and novel transcripts are permitted in the primary analysis

Declare whether novel junctions and novel transcripts are permitted in the primary analysis.

- **Routing name:** `declare-whether-novel-junctions-and-novel-transcripts-are-permitted-in-the-primary-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T008 — Define minimum junction support, minimum inclusion change, and false-discovery thresholds before testing

Define minimum junction support, minimum inclusion change, and false-discovery thresholds before testing.

- **Routing name:** `define-minimum-junction-support-minimum-inclusion-change-and-false-discovery-thresholds-before-testing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T009 — Specify handling of genes with overlapping annotations, paralogs, readthroughs, and antisense transcription

Specify handling of genes with overlapping annotations, paralogs, readthroughs, and antisense transcription.

- **Routing name:** `specify-handling-of-genes-with-overlapping-annotations-paralogs-readthroughs-and-antisense-transcription`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T010 — Freeze tool versions, parameters, random seeds, and all event-definition rules in the run manifest

Freeze tool versions, parameters, random seeds, and all event-definition rules in the run manifest.

- **Routing name:** `freeze-tool-versions-parameters-random-seeds-and-all-event-definition-rules-in-the-run-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. RNA-seq input and splice-signal quality control

### MYR-D012-T011 — Verify read-file integrity, pair synchronization, and read-length consistency required by the selected splicing method

Verify read-file integrity, pair synchronization, and read-length consistency required by the selected splicing method.

- **Routing name:** `verify-read-file-integrity-pair-synchronization-and-read-length-consistency-required-by-the-selected-splicing-method`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T012 — Infer strandedness and reject analyses configured with the opposite transcript orientation

Infer strandedness and reject analyses configured with the opposite transcript orientation.

- **Routing name:** `infer-strandedness-and-reject-analyses-configured-with-the-opposite-transcript-orientation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T013 — Quantify splice-aware mapping rate, junction-spanning reads, and canonical versus noncanonical junction fractions

Quantify splice-aware mapping rate, junction-spanning reads, and canonical versus noncanonical junction fractions.

- **Routing name:** `quantify-splice-aware-mapping-rate-junction-spanning-reads-and-canonical-versus-noncanonical-junction-fractions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T014 — Measure insert-size and mate-orientation distributions for paired-end short-read libraries

Measure insert-size and mate-orientation distributions for paired-end short-read libraries.

- **Routing name:** `measure-insert-size-and-mate-orientation-distributions-for-paired-end-short-read-libraries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T015 — Detect RNA degradation signatures using gene-body coverage and transcript-end bias

Detect RNA degradation signatures using gene-body coverage and transcript-end bias.

- **Routing name:** `detect-rna-degradation-signatures-using-gene-body-coverage-and-transcript-end-bias`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T016 — Quantify ribosomal, mitochondrial, intronic, intergenic, and unassigned read fractions

Quantify ribosomal, mitochondrial, intronic, intergenic, and unassigned read fractions.

- **Routing name:** `quantify-ribosomal-mitochondrial-intronic-intergenic-and-unassigned-read-fractions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T017 — Assess replicate concordance using junction counts, exon bins, and transcript abundance estimates

Assess replicate concordance using junction counts, exon bins, and transcript abundance estimates.

- **Routing name:** `assess-replicate-concordance-using-junction-counts-exon-bins-and-transcript-abundance-estimates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T018 — Detect samples with abnormal novel-junction burden or excessive multimapping at paralogous loci

Detect samples with abnormal novel-junction burden or excessive multimapping at paralogous loci.

- **Routing name:** `detect-samples-with-abnormal-novel-junction-burden-or-excessive-multimapping-at-paralogous-loci`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T019 — Estimate whether read depth supports the declared exon- or isoform-level resolution

Estimate whether read depth supports the declared exon- or isoform-level resolution.

- **Routing name:** `estimate-whether-read-depth-supports-the-declared-exon-or-isoform-level-resolution`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T020 — Issue sample-level pass, warning, or fail status before event discovery or differential testing

Issue sample-level pass, warning, or fail status before event discovery or differential testing.

- **Routing name:** `issue-sample-level-pass-warning-or-fail-status-before-event-discovery-or-differential-testing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Splice-aware alignment and junction catalogue construction

### MYR-D012-T021 — Build a splice-aware alignment index from the frozen genome and transcript annotation

Build a splice-aware alignment index from the frozen genome and transcript annotation.

- **Routing name:** `build-a-splice-aware-alignment-index-from-the-frozen-genome-and-transcript-annotation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T022 — Align short reads while retaining junction, multimapping, chimeric, and read-group evidence

Align short reads while retaining junction, multimapping, chimeric, and read-group evidence.

- **Routing name:** `align-short-reads-while-retaining-junction-multimapping-chimeric-and-read-group-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T023 — Extract observed splice junctions with strand, donor, acceptor, motif, and supporting-read counts

Extract observed splice junctions with strand, donor, acceptor, motif, and supporting-read counts.

- **Routing name:** `extract-observed-splice-junctions-with-strand-donor-acceptor-motif-and-supporting-read-counts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T024 — Collapse equivalent junction records and enforce coordinate and strand consistency

Collapse equivalent junction records and enforce coordinate and strand consistency.

- **Routing name:** `collapse-equivalent-junction-records-and-enforce-coordinate-and-strand-consistency`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T025 — Classify junctions as annotated, novel donor, novel acceptor, novel combination, or fully novel

Classify junctions as annotated, novel donor, novel acceptor, novel combination, or fully novel.

- **Routing name:** `classify-junctions-as-annotated-novel-donor-novel-acceptor-novel-combination-or-fully-novel`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T026 — Filter low-support junctions using replicate-aware thresholds rather than pooled counts alone

Filter low-support junctions using replicate-aware thresholds rather than pooled counts alone.

- **Routing name:** `filter-low-support-junctions-using-replicate-aware-thresholds-rather-than-pooled-counts-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T027 — Detect junctions supported only by mapping artefacts, repeats, or low-complexity sequence

Detect junctions supported only by mapping artefacts, repeats, or low-complexity sequence.

- **Routing name:** `detect-junctions-supported-only-by-mapping-artefacts-repeats-or-low-complexity-sequence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T028 — Construct a reproducible union junction catalogue across all eligible samples

Construct a reproducible union junction catalogue across all eligible samples.

- **Routing name:** `construct-a-reproducible-union-junction-catalogue-across-all-eligible-samples`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T029 — Re-align or augment the index with validated novel junctions only under a predefined two-pass policy

Re-align or augment the index with validated novel junctions only under a predefined two-pass policy.

- **Routing name:** `re-align-or-augment-the-index-with-validated-novel-junctions-only-under-a-predefined-two-pass-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T030 — Export sample-by-junction count matrices with complete coordinate and annotation provenance

Export sample-by-junction count matrices with complete coordinate and annotation provenance.

- **Routing name:** `export-sample-by-junction-count-matrices-with-complete-coordinate-and-annotation-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Transcript assembly and isoform catalogue curation

### MYR-D012-T031 — Assemble sample-level transcripts from splice-aware alignments using strand-aware parameters

Assemble sample-level transcripts from splice-aware alignments using strand-aware parameters.

- **Routing name:** `assemble-sample-level-transcripts-from-splice-aware-alignments-using-strand-aware-parameters`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T032 — Merge sample transcript assemblies while preserving source-sample and support provenance

Merge sample transcript assemblies while preserving source-sample and support provenance.

- **Routing name:** `merge-sample-transcript-assemblies-while-preserving-source-sample-and-support-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T033 — Compare assembled transcripts with the frozen reference annotation using explicit structural classes

Compare assembled transcripts with the frozen reference annotation using explicit structural classes.

- **Routing name:** `compare-assembled-transcripts-with-the-frozen-reference-annotation-using-explicit-structural-classes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T034 — Remove transcripts lacking minimum exon, junction, coverage, or full-length support

Remove transcripts lacking minimum exon, junction, coverage, or full-length support.

- **Routing name:** `remove-transcripts-lacking-minimum-exon-junction-coverage-or-full-length-support`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T035 — Collapse redundant transcript models with identical intron chains and compatible transcript ends

Collapse redundant transcript models with identical intron chains and compatible transcript ends.

- **Routing name:** `collapse-redundant-transcript-models-with-identical-intron-chains-and-compatible-transcript-ends`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T036 — Separate retained introns from unspliced pre-mRNA or genomic contamination using coverage evidence

Separate retained introns from unspliced pre-mRNA or genomic contamination using coverage evidence.

- **Routing name:** `separate-retained-introns-from-unspliced-pre-mrna-or-genomic-contamination-using-coverage-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T037 — Identify novel cassette exons, alternative splice sites, alternative terminal exons, and mutually exclusive exons

Identify novel cassette exons, alternative splice sites, alternative terminal exons, and mutually exclusive exons.

- **Routing name:** `identify-novel-cassette-exons-alternative-splice-sites-alternative-terminal-exons-and-mutually-exclusive-exons`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T038 — Detect readthrough, antisense, and intergenic transcript models and assign conservative labels

Detect readthrough, antisense, and intergenic transcript models and assign conservative labels.

- **Routing name:** `detect-readthrough-antisense-and-intergenic-transcript-models-and-assign-conservative-labels`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T039 — Quantify reference transcript recovery and unsupported annotation complexity

Quantify reference transcript recovery and unsupported annotation complexity.

- **Routing name:** `quantify-reference-transcript-recovery-and-unsupported-annotation-complexity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T040 — Freeze a curated transcript catalogue for downstream quantification and event extraction

Freeze a curated transcript catalogue for downstream quantification and event extraction.

- **Routing name:** `freeze-a-curated-transcript-catalogue-for-downstream-quantification-and-event-extraction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Isoform abundance and usage quantification

### MYR-D012-T041 — Quantify transcript abundance against the frozen isoform catalogue with sequence- and positional-bias correction

Quantify transcript abundance against the frozen isoform catalogue with sequence- and positional-bias correction.

- **Routing name:** `quantify-transcript-abundance-against-the-frozen-isoform-catalogue-with-sequence-and-positional-bias-correction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T042 — Retain inferential replicate or bootstrap uncertainty when supported by the quantification method

Retain inferential replicate or bootstrap uncertainty when supported by the quantification method.

- **Routing name:** `retain-inferential-replicate-or-bootstrap-uncertainty-when-supported-by-the-quantification-method`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T043 — Calculate transcript-per-million values for visualization while preserving count-scale estimates for inference

Calculate transcript-per-million values for visualization while preserving count-scale estimates for inference.

- **Routing name:** `calculate-transcript-per-million-values-for-visualization-while-preserving-count-scale-estimates-for-inference`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T044 — Aggregate transcript estimates to gene level without losing transcript-to-gene provenance

Aggregate transcript estimates to gene level without losing transcript-to-gene provenance.

- **Routing name:** `aggregate-transcript-estimates-to-gene-level-without-losing-transcript-to-gene-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T045 — Compute within-gene transcript usage proportions for every eligible sample

Compute within-gene transcript usage proportions for every eligible sample.

- **Routing name:** `compute-within-gene-transcript-usage-proportions-for-every-eligible-sample`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T046 — Filter transcripts with insufficient abundance or inferential precision using predefined rules

Filter transcripts with insufficient abundance or inferential precision using predefined rules.

- **Routing name:** `filter-transcripts-with-insufficient-abundance-or-inferential-precision-using-predefined-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T047 — Identify genes whose isoforms are not distinguishable given read length and shared exon structure

Identify genes whose isoforms are not distinguishable given read length and shared exon structure.

- **Routing name:** `identify-genes-whose-isoforms-are-not-distinguishable-given-read-length-and-shared-exon-structure`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T048 — Compare quantification stability across alternative transcript catalogues on a bounded subset

Compare quantification stability across alternative transcript catalogues on a bounded subset.

- **Routing name:** `compare-quantification-stability-across-alternative-transcript-catalogues-on-a-bounded-subset`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T049 — Detect abundance estimates dominated by multimapping or equivalence-class ambiguity

Detect abundance estimates dominated by multimapping or equivalence-class ambiguity.

- **Routing name:** `detect-abundance-estimates-dominated-by-multimapping-or-equivalence-class-ambiguity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T050 — Export sample-by-transcript abundance, count, uncertainty, and usage matrices

Export sample-by-transcript abundance, count, uncertainty, and usage matrices.

- **Routing name:** `export-sample-by-transcript-abundance-count-uncertainty-and-usage-matrices`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Splicing event definition and quantification

### MYR-D012-T051 — Enumerate skipped-exon events from the frozen junction and transcript catalogues

Enumerate skipped-exon events from the frozen junction and transcript catalogues.

- **Routing name:** `enumerate-skipped-exon-events-from-the-frozen-junction-and-transcript-catalogues`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T052 — Enumerate alternative 5-prime splice-site events with unambiguous donor grouping

Enumerate alternative 5-prime splice-site events with unambiguous donor grouping.

- **Routing name:** `enumerate-alternative-5-prime-splice-site-events-with-unambiguous-donor-grouping`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T053 — Enumerate alternative 3-prime splice-site events with unambiguous acceptor grouping

Enumerate alternative 3-prime splice-site events with unambiguous acceptor grouping.

- **Routing name:** `enumerate-alternative-3-prime-splice-site-events-with-unambiguous-acceptor-grouping`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T054 — Enumerate mutually exclusive exon events while preventing incompatible event duplication

Enumerate mutually exclusive exon events while preventing incompatible event duplication.

- **Routing name:** `enumerate-mutually-exclusive-exon-events-while-preventing-incompatible-event-duplication`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T055 — Enumerate retained-intron events with explicit intron and flanking-exon coordinates

Enumerate retained-intron events with explicit intron and flanking-exon coordinates.

- **Routing name:** `enumerate-retained-intron-events-with-explicit-intron-and-flanking-exon-coordinates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T056 — Enumerate alternative first-exon and alternative last-exon events separately from internal splicing

Enumerate alternative first-exon and alternative last-exon events separately from internal splicing.

- **Routing name:** `enumerate-alternative-first-exon-and-alternative-last-exon-events-separately-from-internal-splicing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T057 — Calculate inclusion and skipping counts for each event under a declared counting model

Calculate inclusion and skipping counts for each event under a declared counting model.

- **Routing name:** `calculate-inclusion-and-skipping-counts-for-each-event-under-a-declared-counting-model`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T058 — Estimate percent-spliced-in values with uncertainty and minimum-denominator checks

Estimate percent-spliced-in values with uncertainty and minimum-denominator checks.

- **Routing name:** `estimate-percent-spliced-in-values-with-uncertainty-and-minimum-denominator-checks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T059 — Collapse coordinate-equivalent events emitted by multiple transcripts into canonical event identifiers

Collapse coordinate-equivalent events emitted by multiple transcripts into canonical event identifiers.

- **Routing name:** `collapse-coordinate-equivalent-events-emitted-by-multiple-transcripts-into-canonical-event-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T060 — Export event definitions in a machine-readable schema with genome-build and annotation provenance

Export event definitions in a machine-readable schema with genome-build and annotation provenance.

- **Routing name:** `export-event-definitions-in-a-machine-readable-schema-with-genome-build-and-annotation-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Differential splicing and transcript-usage testing

### MYR-D012-T061 — Test differential cassette-exon inclusion between the primary conditions using biological replicates

Test differential cassette-exon inclusion between the primary conditions using biological replicates.

- **Routing name:** `test-differential-cassette-exon-inclusion-between-the-primary-conditions-using-biological-replicates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T062 — Test alternative donor and acceptor usage with event-appropriate count models

Test alternative donor and acceptor usage with event-appropriate count models.

- **Routing name:** `test-alternative-donor-and-acceptor-usage-with-event-appropriate-count-models`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T063 — Test mutually exclusive exon choice while enforcing the selected event model assumptions

Test mutually exclusive exon choice while enforcing the selected event model assumptions.

- **Routing name:** `test-mutually-exclusive-exon-choice-while-enforcing-the-selected-event-model-assumptions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T064 — Test differential intron retention after controlling for host-gene expression when required

Test differential intron retention after controlling for host-gene expression when required.

- **Routing name:** `test-differential-intron-retention-after-controlling-for-host-gene-expression-when-required`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T065 — Test differential transcript usage within genes using count-scale isoform estimates

Test differential transcript usage within genes using count-scale isoform estimates.

- **Routing name:** `test-differential-transcript-usage-within-genes-using-count-scale-isoform-estimates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T066 — Test multi-condition splicing effects with an omnibus model before pairwise follow-up

Test multi-condition splicing effects with an omnibus model before pairwise follow-up.

- **Routing name:** `test-multi-condition-splicing-effects-with-an-omnibus-model-before-pairwise-follow-up`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T067 — Test condition-by-time interactions for changing isoform usage trajectories

Test condition-by-time interactions for changing isoform usage trajectories.

- **Routing name:** `test-condition-by-time-interactions-for-changing-isoform-usage-trajectories`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T068 — Apply multiple-testing correction separately to declared event families or a unified prespecified universe

Apply multiple-testing correction separately to declared event families or a unified prespecified universe.

- **Routing name:** `apply-multiple-testing-correction-separately-to-declared-event-families-or-a-unified-prespecified-universe`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T069 — Classify events by adjusted significance and minimum absolute inclusion or usage change

Classify events by adjusted significance and minimum absolute inclusion or usage change.

- **Routing name:** `classify-events-by-adjusted-significance-and-minimum-absolute-inclusion-or-usage-change`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T070 — Return no-call status for low coverage, singular models, non-identifiable isoforms, or failed convergence

Return no-call status for low coverage, singular models, non-identifiable isoforms, or failed convergence.

- **Routing name:** `return-no-call-status-for-low-coverage-singular-models-non-identifiable-isoforms-or-failed-convergence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Long-read and complex transcript characterization

### MYR-D012-T071 — Validate full-length long-read molecule tags, primer evidence, and orientation before isoform calling

Validate full-length long-read molecule tags, primer evidence, and orientation before isoform calling.

- **Routing name:** `validate-full-length-long-read-molecule-tags-primer-evidence-and-orientation-before-isoform-calling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T072 — Cluster long reads into transcript models while retaining molecule- and sample-level support

Cluster long reads into transcript models while retaining molecule- and sample-level support.

- **Routing name:** `cluster-long-reads-into-transcript-models-while-retaining-molecule-and-sample-level-support`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T073 — Correct splice junctions only within a bounded distance of high-confidence short-read or annotation evidence

Correct splice junctions only within a bounded distance of high-confidence short-read or annotation evidence.

- **Routing name:** `correct-splice-junctions-only-within-a-bounded-distance-of-high-confidence-short-read-or-annotation-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T074 — Classify full-splice matches, incomplete matches, novel-in-catalogue, and novel-not-in-catalogue isoforms

Classify full-splice matches, incomplete matches, novel-in-catalogue, and novel-not-in-catalogue isoforms.

- **Routing name:** `classify-full-splice-matches-incomplete-matches-novel-in-catalogue-and-novel-not-in-catalogue-isoforms`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T075 — Detect and flag reverse-transcriptase switching, internal priming, and template-switch artefacts

Detect and flag reverse-transcriptase switching, internal priming, and template-switch artefacts.

- **Routing name:** `detect-and-flag-reverse-transcriptase-switching-internal-priming-and-template-switch-artefacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T076 — Detect candidate fusion junctions using split reads, discordant pairs, and independent molecule support gates

Detect candidate fusion junctions using split reads, discordant pairs, and independent molecule support gates.

- **Routing name:** `detect-candidate-fusion-junctions-using-split-reads-discordant-pairs-and-independent-molecule-support-gates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T077 — Detect back-splice junctions consistent with circular RNA using strand-aware chimeric evidence

Detect back-splice junctions consistent with circular RNA using strand-aware chimeric evidence.

- **Routing name:** `detect-back-splice-junctions-consistent-with-circular-rna-using-strand-aware-chimeric-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T078 — Distinguish trans-splicing, readthrough, genomic rearrangement, and mapping-artefact explanations

Distinguish trans-splicing, readthrough, genomic rearrangement, and mapping-artefact explanations.

- **Routing name:** `distinguish-trans-splicing-readthrough-genomic-rearrangement-and-mapping-artefact-explanations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T079 — Cross-check full-length and complex transcripts against short-read abundance and genomic structural-variant evidence

Cross-check full-length and complex transcripts against short-read abundance and genomic structural-variant evidence.

- **Routing name:** `cross-check-full-length-and-complex-transcripts-against-short-read-abundance-and-genomic-structural-variant-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T080 — Export high-confidence isoforms, fusions, and circular transcripts with evidence tiers and support metrics

Export high-confidence isoforms, fusions, and circular transcripts with evidence tiers and support metrics.

- **Routing name:** `export-high-confidence-isoforms-fusions-and-circular-transcripts-with-evidence-tiers-and-support-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Validation, visualization, and robustness assessment

### MYR-D012-T081 — Generate sashimi-style junction visualizations using identical coverage scales across comparison groups

Generate sashimi-style junction visualizations using identical coverage scales across comparison groups.

- **Routing name:** `generate-sashimi-style-junction-visualizations-using-identical-coverage-scales-across-comparison-groups`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T082 — Visualize transcript structures with exon, junction, coding-sequence, and event annotations

Visualize transcript structures with exon, junction, coding-sequence, and event annotations.

- **Routing name:** `visualize-transcript-structures-with-exon-junction-coding-sequence-and-event-annotations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T083 — Inspect top events for unique mappability, repeat overlap, and local alignment ambiguity

Inspect top events for unique mappability, repeat overlap, and local alignment ambiguity.

- **Routing name:** `inspect-top-events-for-unique-mappability-repeat-overlap-and-local-alignment-ambiguity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T084 — Recalculate leading events after excluding each warning-level sample in turn

Recalculate leading events after excluding each warning-level sample in turn.

- **Routing name:** `recalculate-leading-events-after-excluding-each-warning-level-sample-in-turn`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T085 — Compare event calls across two justified splicing methods on a bounded validation set

Compare event calls across two justified splicing methods on a bounded validation set.

- **Routing name:** `compare-event-calls-across-two-justified-splicing-methods-on-a-bounded-validation-set`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T086 — Assess sensitivity to alternative minimum junction-count and inclusion-change thresholds

Assess sensitivity to alternative minimum junction-count and inclusion-change thresholds.

- **Routing name:** `assess-sensitivity-to-alternative-minimum-junction-count-and-inclusion-change-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T087 — Verify that differential splicing is not explained solely by host-gene expression change

Verify that differential splicing is not explained solely by host-gene expression change.

- **Routing name:** `verify-that-differential-splicing-is-not-explained-solely-by-host-gene-expression-change`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T088 — Check concordance between junction counts, exon-bin counts, transcript usage, and long-read evidence

Check concordance between junction counts, exon-bin counts, transcript usage, and long-read evidence.

- **Routing name:** `check-concordance-between-junction-counts-exon-bin-counts-transcript-usage-and-long-read-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T089 — Classify findings as robust, method-dependent, coverage-limited, or structurally ambiguous

Classify findings as robust, method-dependent, coverage-limited, or structurally ambiguous.

- **Routing name:** `classify-findings-as-robust-method-dependent-coverage-limited-or-structurally-ambiguous`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T090 — Create a review packet containing plots, counts, coordinates, models, and all exclusion flags

Create a review packet containing plots, counts, coordinates, models, and all exclusion flags.

- **Routing name:** `create-a-review-packet-containing-plots-counts-coordinates-models-and-all-exclusion-flags`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Release, provenance, and review gates

### MYR-D012-T091 — Generate machine-readable tables for junctions, transcripts, events, differential tests, and complex transcripts

Generate machine-readable tables for junctions, transcripts, events, differential tests, and complex transcripts.

- **Routing name:** `generate-machine-readable-tables-for-junctions-transcripts-events-differential-tests-and-complex-transcripts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T092 — Export the curated transcript annotation and sequence files with stable versioned identifiers

Export the curated transcript annotation and sequence files with stable versioned identifiers.

- **Routing name:** `export-the-curated-transcript-annotation-and-sequence-files-with-stable-versioned-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T093 — Record genome, annotation, aligner, assembler, quantifier, event caller, model, and parameter provenance

Record genome, annotation, aligner, assembler, quantifier, event caller, model, and parameter provenance.

- **Routing name:** `record-genome-annotation-aligner-assembler-quantifier-event-caller-model-and-parameter-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T094 — Validate coordinate, strand, gene, transcript, and event identifiers across every release artifact

Validate coordinate, strand, gene, transcript, and event identifiers across every release artifact.

- **Routing name:** `validate-coordinate-strand-gene-transcript-and-event-identifiers-across-every-release-artifact`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T095 — Archive aligner logs, junction catalogues, transcript comparisons, and statistical diagnostics

Archive aligner logs, junction catalogues, transcript comparisons, and statistical diagnostics.

- **Routing name:** `archive-aligner-logs-junction-catalogues-transcript-comparisons-and-statistical-diagnostics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T096 — Create reproducibility commands or workflow configurations for the complete splicing analysis

Create reproducibility commands or workflow configurations for the complete splicing analysis.

- **Routing name:** `create-reproducibility-commands-or-workflow-configurations-for-the-complete-splicing-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T097 — Flag events unsupported by independent replicates, orthogonal evidence, or adequate read resolution

Flag events unsupported by independent replicates, orthogonal evidence, or adequate read resolution.

- **Routing name:** `flag-events-unsupported-by-independent-replicates-orthogonal-evidence-or-adequate-read-resolution`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T098 — Prevent automatic clinical interpretation of predicted isoforms, fusions, or splicing consequences

Prevent automatic clinical interpretation of predicted isoforms, fusions, or splicing consequences.

- **Routing name:** `prevent-automatic-clinical-interpretation-of-predicted-isoforms-fusions-or-splicing-consequences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T099 — Require qualified review for novel coding, disease-associated, or therapeutic splicing claims

Require qualified review for novel coding, disease-associated, or therapeutic splicing claims.

- **Routing name:** `require-qualified-review-for-novel-coding-disease-associated-or-therapeutic-splicing-claims`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D012-T100 — Release results only when input, alignment, event, statistical, provenance, and review gates pass

Release results only when input, alignment, event, statistical, provenance, and review gates pass.

- **Routing name:** `release-results-only-when-input-alignment-event-statistical-provenance-and-review-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
