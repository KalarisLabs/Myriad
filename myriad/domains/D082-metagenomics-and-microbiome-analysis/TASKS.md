# D082 — Metagenomics and Microbiome Analysis

Batch **009** · 10 workstreams · 100 tasks

## 01. Study design, sampling frame, and metadata harmonization

### MYR-D082-T001 — Define decision scope and no-call criteria for study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering the biological question, target population, body site or environment, sampling frame, comparison groups, and analysis endpoint. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T002 — Audit input provenance and analytical fitness for study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Inspect protocols, collection devices, preservation, extraction batches, host covariates, medications, diet, geography, time points, and consent. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T003 — Normalize interoperable representations while preserving unresolved discrepancies for study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Reconcile sample identifiers, ontology terms, repeated-measure structure, batch labels, covariate coding, and missingness reasons into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T004 — Compute decision-relevant measures with prespecified methods for study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Estimate design balance, confounder coverage, longitudinal density, batch-treatment aliasing, and effective sample size using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T005 — Quantify uncertainty and applicability limits for study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from inferential uncertainty from unmeasured confounding, convenience sampling, compositional outcomes, and temporal variability. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T006 — Detect critical failure modes before interpreting study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Test explicitly for sample leakage, duplicated participants, impossible timelines, batch confounding, site mislabelling, and inappropriate independence assumptions. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T007 — Enforce risk controls and escalation gates for study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Apply minimum metadata, blocked or paired analysis requirements, exclusion rules, and no-call conditions for aliased designs. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T008 — Benchmark alternative approaches against predefined criteria for study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Compare cross-sectional, longitudinal, case-control, cohort, intervention, and nested sampling designs using prespecified estimands. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T009 — Assemble the auditable decision artifact for study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Generate a microbiome analysis design contract with cohort flow, covariate dictionary, contrasts, and bias register. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T010 — Issue a qualified no-call and escalation package for study design, sampling frame, and metadata harmonization in Metagenomics and Microbiome Analysis

Return a qualified no-call when the sampling frame, comparison definition, or critical confounders cannot support the intended claim. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-study-design-sampling-frame-and-metadata-harmonization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Raw-read QC, host filtering, and contaminant control

### MYR-D082-T011 — Define decision scope and no-call criteria for raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering read acceptance and decontamination for amplicon, shotgun, long-read, metatranscriptomic, or virome datasets. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T012 — Audit input provenance and analytical fitness for raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Inspect raw reads, run metadata, primers, adapters, host references, extraction blanks, library blanks, mock communities, and spike-ins. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T013 — Normalize interoperable representations while preserving unresolved discrepancies for raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Reconcile read quality, trimming coordinates, host-read disposition, control prevalence, contaminant probabilities, and retained-read provenance into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T014 — Compute decision-relevant measures with prespecified methods for raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Estimate yield, quality, primer retention, host fraction, complexity, control signal, index leakage, and taxonomic composition of removed reads using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T015 — Quantify uncertainty and applicability limits for raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from contamination uncertainty under low biomass, incomplete host references, reagent-lot effects, and multiplex crosstalk. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T016 — Detect critical failure modes before interpreting raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Test explicitly for overaggressive host removal, untrimmed primers, reagent contaminants, barcode bleed, duplicate libraries, and sequence truncation. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T017 — Enforce risk controls and escalation gates for raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Apply control-informed prevalence and frequency rules, minimum retained depth, host-privacy safeguards, and low-biomass no-call criteria. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T018 — Benchmark alternative approaches against predefined criteria for raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Compare quality trimming, error correction, host depletion, k-mer screening, and statistical decontamination strategies with sensitivity checks. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T019 — Assemble the auditable decision artifact for raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Generate a read-processing ledger linking every removed and retained read category to parameters and controls. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T020 — Issue a qualified no-call and escalation package for raw-read QC, host filtering, and contaminant control in Metagenomics and Microbiome Analysis

Return a qualified no-call when controls are missing, host privacy cannot be protected, or contamination overwhelms biological signal. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-raw-read-qc-host-filtering-and-contaminant-control-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Amplicon feature inference and taxonomic assignment

### MYR-D082-T021 — Define decision scope and no-call criteria for amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering denoising and taxonomic analysis of marker-gene sequencing without treating read counts as absolute abundance. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T022 — Audit input provenance and analytical fitness for amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Inspect demultiplexed reads, primer region, orientation, error model, chimera settings, taxonomic reference version, and mock controls. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T023 — Normalize interoperable representations while preserving unresolved discrepancies for amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Reconcile amplicon sequence variants, feature tables, representative sequences, taxonomic ranks, confidence scores, and phylogenetic placement into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T024 — Compute decision-relevant measures with prespecified methods for amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Estimate error-model fit, chimera burden, feature prevalence, taxonomic resolution, mock-community recovery, and unclassified fraction using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T025 — Quantify uncertainty and applicability limits for amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from assignment uncertainty from variable-region limits, reference gaps, copy-number variation, and closely related taxa. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T026 — Detect critical failure modes before interpreting amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Test explicitly for OTU inflation, residual primers, batch-specific error models, contaminant ASVs, impossible rank assignments, and compositional misinterpretation. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T027 — Enforce risk controls and escalation gates for amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Apply region-compatible reference training, confidence thresholds, prevalence filters, control checks, and rank-specific no-call rules. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T028 — Benchmark alternative approaches against predefined criteria for amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Compare ASV, exact-sequence, phylogenetic-placement, and curated-classifier approaches benchmarked on controls and held-out samples. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T029 — Assemble the auditable decision artifact for amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Generate an amplicon feature and taxonomy package with denoising diagnostics, reference provenance, and unresolved assignments. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T030 — Issue a qualified no-call and escalation package for amplicon feature inference and taxonomic assignment in Metagenomics and Microbiome Analysis

Return a qualified no-call when marker resolution or control performance cannot support species-level or quantitative conclusions. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-amplicon-feature-inference-and-taxonomic-assignment-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Shotgun taxonomic and strain-resolved profiling

### MYR-D082-T031 — Define decision scope and no-call criteria for shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering community composition estimation from shotgun or long-read data at species, subspecies, and strain resolution. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T032 — Audit input provenance and analytical fitness for shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Inspect filtered reads, marker and genome databases, pangenomes, mapping parameters, abundance models, and negative controls. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T033 — Normalize interoperable representations while preserving unresolved discrepancies for shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Reconcile taxon identifiers, relative abundance, coverage breadth, strain haplotypes, marker support, and unclassified read categories into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T034 — Compute decision-relevant measures with prespecified methods for shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Estimate species abundance, genome coverage, strain mixture, allelic diversity, detection limits, and agreement across profilers using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T035 — Quantify uncertainty and applicability limits for shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from taxonomic uncertainty from shared sequence, reference bias, novel taxa, horizontal transfer, and low-abundance sampling. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T036 — Detect critical failure modes before interpreting shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Test explicitly for false species calls from conserved genes, database contamination, reference duplication, compositional artifacts, and strain overresolution. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T037 — Enforce risk controls and escalation gates for shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Apply minimum unique-marker support, breadth thresholds, control-adjusted detection, and explicit unresolved-strain categories. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T038 — Benchmark alternative approaches against predefined criteria for shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Compare marker-based, whole-genome mapping, k-mer, assembly-assisted, and pangenome-aware profilers with consensus rules. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T039 — Assemble the auditable decision artifact for shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Generate a taxonomic and strain profile with detection limits, classifier concordance, and reference-space coverage. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T040 — Issue a qualified no-call and escalation package for shotgun taxonomic and strain-resolved profiling in Metagenomics and Microbiome Analysis

Return a qualified no-call when available reads or references cannot distinguish closely related taxa or stable strain haplotypes. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-shotgun-taxonomic-and-strain-resolved-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Metagenome assembly, binning, and genome reconstruction

### MYR-D082-T041 — Define decision scope and no-call criteria for metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering recovery of metagenome-assembled genomes and extrachromosomal elements with quality appropriate to the intended ecological inference. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T042 — Audit input provenance and analytical fitness for metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Inspect quality-controlled reads, co-assembly groups, coverage profiles, long-read links, assembly graphs, and reference collections. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T043 — Normalize interoperable representations while preserving unresolved discrepancies for metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Reconcile contigs, bins, MAG identifiers, completeness, contamination, strain heterogeneity, taxonomy, and graph linkages into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T044 — Compute decision-relevant measures with prespecified methods for metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Estimate assembly recovery, bin completeness, contamination, redundancy, strain mixture, circularity, and read-support consistency using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T045 — Quantify uncertainty and applicability limits for metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from reconstruction uncertainty from uneven abundance, repeats, microdiversity, co-abundance assumptions, and incomplete marker sets. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T046 — Detect critical failure modes before interpreting metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Test explicitly for chimeric bins, strain collapse, duplicated markers, cross-sample contamination, host contigs, and false plasmid assignment. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T047 — Enforce risk controls and escalation gates for metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Apply quality categories, contamination limits, dereplication thresholds, graph inspection, and no-call rules for strain-resolved claims. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T048 — Benchmark alternative approaches against predefined criteria for metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Compare single-sample, co-assembly, differential-coverage, long-read, graph, and reference-assisted reconstruction strategies. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T049 — Assemble the auditable decision artifact for metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Generate a MAG and element catalog with quality metrics, dereplication clusters, read mappings, and unresolved contigs. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T050 — Issue a qualified no-call and escalation package for metagenome assembly, binning, and genome reconstruction in Metagenomics and Microbiome Analysis

Return a qualified no-call when bin quality or strain complexity cannot support genome-level metabolic or phylogenetic conclusions. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-metagenome-assembly-binning-and-genome-reconstruction-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Functional gene, pathway, and resistome profiling

### MYR-D082-T051 — Define decision scope and no-call criteria for functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering quantification of genes, pathways, metabolic modules, resistance functions, and virulence-associated functions in communities. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T052 — Audit input provenance and analytical fitness for functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Inspect reads or assemblies, gene catalogs, orthology databases, pathway definitions, AMR references, normalization choices, and mapping parameters. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T053 — Normalize interoperable representations while preserving unresolved discrepancies for functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Reconcile gene families, ortholog groups, pathway coverage, reaction modules, resistance classes, abundance units, and confidence tiers into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T054 — Compute decision-relevant measures with prespecified methods for functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Estimate gene abundance, pathway completeness, copy-number-adjusted signal, functional diversity, contribution by taxa, and unassigned fraction using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T055 — Quantify uncertainty and applicability limits for functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from functional uncertainty from homolog ambiguity, pathway redundancy, annotation transfer, gene length, and database incompleteness. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T056 — Detect critical failure modes before interpreting functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Test explicitly for double counting, partial-pathway overcalls, nonfunctional homologs, taxon-function misattribution, and unsupported resistance phenotype inference. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T057 — Enforce risk controls and escalation gates for functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Apply alignment-quality thresholds, pathway-completeness rules, multi-mapping treatment, and separation of gene presence from activity. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T058 — Benchmark alternative approaches against predefined criteria for functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Compare read-based, assembly-based, translated-search, profile-HMM, and pathway-reconstruction workflows with database sensitivity analysis. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T059 — Assemble the auditable decision artifact for functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Generate a functional profile linking abundance, coverage, taxonomic contributors, database versions, and ambiguity. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T060 — Issue a qualified no-call and escalation package for functional gene, pathway, and resistome profiling in Metagenomics and Microbiome Analysis

Return a qualified no-call when homology or pathway evidence cannot support a specific biochemical, resistance, or pathogenic phenotype claim. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-functional-gene-pathway-and-resistome-profiling-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Compositional statistics and differential abundance

### MYR-D082-T061 — Define decision scope and no-call criteria for compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering testing of microbiome features against prespecified exposures or outcomes under compositional, sparse, and overdispersed data. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T062 — Audit input provenance and analytical fitness for compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Inspect feature tables, library sizes, covariates, repeated measures, batch variables, prevalence filters, and contrast definitions. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T063 — Normalize interoperable representations while preserving unresolved discrepancies for compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Reconcile analysis matrices, zeros, offsets, transformations, reference frames, effect sizes, confidence intervals, and adjusted p-values into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T064 — Compute decision-relevant measures with prespecified methods for compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Estimate differential abundance, prevalence shifts, log-ratio effects, uncertainty, false-discovery control, and method concordance using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T065 — Quantify uncertainty and applicability limits for compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from inferential uncertainty from zero generation, compositional closure, small samples, high dimensionality, and model misspecification. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T066 — Detect critical failure modes before interpreting compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Test explicitly for rarefaction misuse, unadjusted multiple testing, data leakage, pseudoreplication, unstable reference taxa, and direction reversals. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T067 — Enforce risk controls and escalation gates for compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Apply prespecified filtering, donor-aware models, multiplicity control, effect-size reporting, and sensitivity to normalization choices. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T068 — Benchmark alternative approaches against predefined criteria for compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Compare count, log-ratio, hurdle, rank-based, Bayesian, and permutation methods selected by design and validated through diagnostics. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T069 — Assemble the auditable decision artifact for compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Generate a differential-feature result set with model diagnostics, effect sizes, sensitivity analyses, and no-call labels. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T070 — Issue a qualified no-call and escalation package for compositional statistics and differential abundance in Metagenomics and Microbiome Analysis

Return a qualified no-call when design aliasing, sample size, or model diagnostics cannot support stable feature-level inference. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-compositional-statistics-and-differential-abundance-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Longitudinal ecology, interactions, and community dynamics

### MYR-D082-T071 — Define decision scope and no-call criteria for longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering analysis of temporal stability, succession, resilience, ecological states, and candidate interactions in repeated microbiome data. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T072 — Audit input provenance and analytical fitness for longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Inspect time-stamped profiles, interventions, exposure histories, irregular sampling, subject identifiers, and environmental covariates. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T073 — Normalize interoperable representations while preserving unresolved discrepancies for longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Reconcile trajectories, state assignments, transition matrices, temporal lags, volatility metrics, and interaction hypotheses into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T074 — Compute decision-relevant measures with prespecified methods for longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Estimate within-subject change, recovery time, state persistence, temporal association, ecological distance, and intervention response using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T075 — Quantify uncertainty and applicability limits for longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from dynamic uncertainty from sparse time points, asynchronous sampling, autocorrelation, regression to the mean, and unmeasured exposures. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T076 — Detect critical failure modes before interpreting longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Test explicitly for pseudotemporal claims, compositional correlation artifacts, reverse causation, synchronized batch effects, and overfit networks. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T077 — Enforce risk controls and escalation gates for longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Apply minimum temporal density, donor blocking, lag sensitivity, null-model comparison, and distinction between association and interaction. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T078 — Benchmark alternative approaches against predefined criteria for longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Compare mixed models, state-space models, dynamic time warping, ecological state models, and causal time-series approaches. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T079 — Assemble the auditable decision artifact for longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Generate a longitudinal ecology dossier with participant trajectories, state uncertainty, perturbation windows, and robustness checks. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T080 — Issue a qualified no-call and escalation package for longitudinal ecology, interactions, and community dynamics in Metagenomics and Microbiome Analysis

Return a qualified no-call when sampling density or intervention timing cannot distinguish biological dynamics from noise or confounding. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-longitudinal-ecology-interactions-and-community-dynamics-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Host integration, multi-omics, and mechanistic prioritization

### MYR-D082-T081 — Define decision scope and no-call criteria for host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering integration of microbiome features with host genomics, transcriptomics, proteomics, metabolomics, immune phenotypes, or clinical outcomes. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T082 — Audit input provenance and analytical fitness for host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Inspect matched multi-omic matrices, sample maps, assay QC, covariates, temporal alignment, prior pathways, and missing-modality patterns. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T083 — Normalize interoperable representations while preserving unresolved discrepancies for host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Reconcile cross-modal identifiers, harmonized scales, latent factors, networks, mediation variables, and provenance-linked feature mappings into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T084 — Compute decision-relevant measures with prespecified methods for host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Estimate shared variation, cross-modal associations, pathway coherence, mediation evidence, predictive gain, and donor-level reproducibility using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T085 — Quantify uncertainty and applicability limits for host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from integration uncertainty from unmatched samples, batch structure, high dimensionality, missing modalities, and causal ambiguity. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T086 — Detect critical failure modes before interpreting host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Test explicitly for sample-map errors, leakage across training folds, dominant assay batches, spurious correlation, and overinterpreted latent factors. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T087 — Enforce risk controls and escalation gates for host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Apply donor-wise validation, modality-specific QC, permutation baselines, causal-language restrictions, and preregistered integration targets. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T088 — Benchmark alternative approaches against predefined criteria for host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Compare multiblock, factor, network, kernel, mediation, and mechanistic-model approaches with held-out validation. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T089 — Assemble the auditable decision artifact for host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Generate a multi-omic evidence graph linking microbiome features to host measurements with uncertainty and alternative explanations. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T090 — Issue a qualified no-call and escalation package for host integration, multi-omics, and mechanistic prioritization in Metagenomics and Microbiome Analysis

Return a qualified no-call when sample alignment, validation, or temporal ordering cannot support mechanistic or predictive interpretation. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-host-integration-multi-omics-and-mechanistic-prioritization-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Biomarker validation, reproducibility, and responsible release

### MYR-D082-T091 — Define decision scope and no-call criteria for biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Create a versioned decision charter covering translation of microbiome signatures into reproducible classifiers, stratification hypotheses, or public datasets. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T092 — Audit input provenance and analytical fitness for biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Inspect discovery cohorts, external cohorts, locked pipelines, batch metadata, clinical endpoints, consent, and repository requirements. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T093 — Normalize interoperable representations while preserving unresolved discrepancies for biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Reconcile feature signatures, model objects, calibration outputs, performance metrics, decision thresholds, metadata packages, and access controls into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T094 — Compute decision-relevant measures with prespecified methods for biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Estimate external discrimination, calibration, decision utility, transportability, batch robustness, and reproducibility from raw data using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T095 — Quantify uncertainty and applicability limits for biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Characterize uncertainty arising from generalization uncertainty from geography, diet, platform, extraction, host population, prevalence, and temporal drift. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T096 — Detect critical failure modes before interpreting biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Test explicitly for cross-validation leakage, cohort memorization, unstable taxa, spectrum bias, privacy leakage, and irreproducible preprocessing. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T097 — Enforce risk controls and escalation gates for biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Apply external validation, locked thresholds, participant-level splits, model cards, controlled access, and no clinical-use claims without qualification. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T098 — Benchmark alternative approaches against predefined criteria for biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Compare taxonomic, functional, pathway, and multimodal signatures evaluated across independent sites and processing pipelines. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T099 — Assemble the auditable decision artifact for biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Generate a reproducible microbiome biomarker package with code, containers, data dictionary, calibration, and limitations. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D082-T100 — Issue a qualified no-call and escalation package for biomarker validation, reproducibility, and responsible release in Metagenomics and Microbiome Analysis

Return a qualified no-call when external validation, consent, privacy, or analytical reproducibility is insufficient for release or translational claims. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-biomarker-validation-reproducibility-and-responsible-release-in-metagenomics-and-microbiome-analysis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
