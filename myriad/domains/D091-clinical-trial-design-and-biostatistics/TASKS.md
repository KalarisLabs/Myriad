# D091 — Clinical Trial Design and Biostatistics

Batch **010** · 10 workstreams · 100 tasks

## 01. Clinical question, estimand, and decision framework

### MYR-D091-T001 — Define decision scope and no-call criteria for clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering the clinical objective, population, treatment conditions, endpoint variable, intercurrent-event strategies, summary measure, and decision rule. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T002 — Audit input provenance and analytical fitness for clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Inspect development strategy, disease context, treatment mechanism, standard of care, stakeholder needs, prior evidence, and regulatory objectives. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T003 — Normalize interoperable representations while preserving unresolved discrepancies for clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Reconcile estimand attributes, hypotheses, treatment contrasts, decision thresholds, intercurrent events, and causal assumptions into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T004 — Compute decision-relevant measures with prespecified methods for clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Estimate clinical relevance, alignment among objective and estimand, feasibility, interpretability, and consequence of false-positive and false-negative decisions using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T005 — Quantify uncertainty and applicability limits for clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from decision uncertainty from disease heterogeneity, treatment switching, rescue medication, discontinuation, death, and evolving standard of care. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T006 — Detect critical failure modes before interpreting clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Test explicitly for vague objectives, endpoint-estimand mismatch, incompatible intercurrent-event handling, post hoc population changes, and clinically meaningless contrasts. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T007 — Enforce risk controls and escalation gates for clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Apply prespecified estimands, stakeholder agreement, causal assumption review, clinical relevance, and explicit no-call conditions. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T008 — Benchmark alternative approaches against predefined criteria for clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Compare treatment-policy, hypothetical, composite, while-on-treatment, principal-stratum, and multiple-estimand strategies. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T009 — Assemble the auditable decision artifact for clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Generate an estimand and decision charter linking clinical question, data collection, analysis, sensitivity, and interpretation. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T010 — Issue a qualified no-call and escalation package for clinical question, estimand, and decision framework in Clinical Trial Design and Biostatistics

Return a qualified no-call when the clinical objective cannot be translated into a coherent and measurable target of estimation. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-clinical-question-estimand-and-decision-framework-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Endpoint strategy, measurement, and adjudication

### MYR-D091-T011 — Define decision scope and no-call criteria for endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering selection and validation of primary, secondary, exploratory, composite, surrogate, patient-reported, digital, and safety endpoints. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T012 — Audit input provenance and analytical fitness for endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Inspect disease natural history, measurement properties, meaningful-change thresholds, assessment schedule, adjudication rules, and prior trials. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T013 — Normalize interoperable representations while preserving unresolved discrepancies for endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Reconcile endpoint definitions, visit windows, component rules, censoring, adjudication status, estimand mapping, and hierarchy into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T014 — Compute decision-relevant measures with prespecified methods for endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Estimate reliability, validity, responsiveness, event rate, missingness, burden, clinical meaningfulness, and cross-site consistency using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T015 — Quantify uncertainty and applicability limits for endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from endpoint uncertainty from measurement error, informative assessment, competing events, learning effects, and device or rater drift. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T016 — Detect critical failure modes before interpreting endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Test explicitly for endpoint switching, unvalidated surrogates, composite domination by minor components, inconsistent adjudication, and outcome ascertainment bias. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T017 — Enforce risk controls and escalation gates for endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Apply blinded adjudication where relevant, validation evidence, standardized assessment, meaningful thresholds, and prespecified hierarchy. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T018 — Benchmark alternative approaches against predefined criteria for endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Compare continuous, binary, ordinal, recurrent-event, time-to-event, composite, win-ratio, digital, and patient-reported endpoints. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T019 — Assemble the auditable decision artifact for endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Generate an endpoint specification package with definitions, measurement evidence, adjudication, estimand linkage, and failure handling. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T020 — Issue a qualified no-call and escalation package for endpoint strategy, measurement, and adjudication in Clinical Trial Design and Biostatistics

Return a qualified no-call when endpoint measurement or clinical meaning cannot support the intended decision. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-endpoint-strategy-measurement-and-adjudication-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Trial design, controls, randomization, and masking

### MYR-D091-T021 — Define decision scope and no-call criteria for trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering selection of an efficient and credible design, comparator, allocation, masking, stratification, and operational structure. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T022 — Audit input provenance and analytical fitness for trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Inspect clinical question, standard of care, ethics, recruitment, endpoint timing, treatment delivery, site capabilities, and prior data. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T023 — Normalize interoperable representations while preserving unresolved discrepancies for trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Reconcile design schema, arms, allocation ratios, randomization lists, strata, blocks, masking roles, emergency unblinding, and estimands into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T024 — Compute decision-relevant measures with prespecified methods for trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Estimate bias protection, power efficiency, balance, concealment, feasibility, ethical acceptability, and interpretability using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T025 — Quantify uncertainty and applicability limits for trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from design uncertainty from recruitment, treatment adherence, site heterogeneity, unblinding, contamination, and temporal changes. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T026 — Detect critical failure modes before interpreting trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Test explicitly for predictable randomization, inappropriate historical controls, unmasked outcome assessment, stratification overload, and allocation leakage. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T027 — Enforce risk controls and escalation gates for trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Apply concealed allocation, limited justified strata, masking procedures, independent randomization validation, and emergency-unblinding controls. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T028 — Benchmark alternative approaches against predefined criteria for trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Compare parallel, crossover, cluster, factorial, platform, basket, umbrella, pragmatic, and external-control designs. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T029 — Assemble the auditable decision artifact for trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Generate a trial-design blueprint with allocation, masking, bias controls, simulations, and operational assumptions. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T030 — Issue a qualified no-call and escalation package for trial design, controls, randomization, and masking in Clinical Trial Design and Biostatistics

Return a qualified no-call when no design can answer the clinical question ethically and with acceptable bias control. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-trial-design-controls-randomization-and-masking-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Sample size, power, precision, and operating characteristics

### MYR-D091-T031 — Define decision scope and no-call criteria for sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering justification of enrollment using effect, variance, event, dropout, multiplicity, design, and decision assumptions. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T032 — Audit input provenance and analytical fitness for sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Inspect historical data, clinically meaningful effect, nuisance parameters, accrual, follow-up, noncompliance, loss to follow-up, and simulation models. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T033 — Normalize interoperable representations while preserving unresolved discrepancies for sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Reconcile assumptions, formulas or simulation code, scenarios, power, precision, type-I error, expected sample size, and sensitivity tables into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T034 — Compute decision-relevant measures with prespecified methods for sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Estimate power, confidence-interval width, event count, operating characteristics, robustness, feasibility, and decision error using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T035 — Quantify uncertainty and applicability limits for sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from sample-size uncertainty from optimistic effects, uncertain event rates, variance drift, clustering, dropout, and delayed outcomes. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T036 — Detect critical failure modes before interpreting sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Test explicitly for effect-size cherry-picking, one-scenario calculations, ignored clustering, incorrect event assumptions, and unadjusted multiplicity. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T037 — Enforce risk controls and escalation gates for sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Apply clinically anchored effects, conservative sensitivity, reproducible code, parameter uncertainty, and independent statistical review. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T038 — Benchmark alternative approaches against predefined criteria for sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Compare analytic, simulation, Bayesian assurance, precision-based, event-driven, group-sequential, and adaptive calculations. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T039 — Assemble the auditable decision artifact for sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Generate a reproducible sample-size dossier with assumptions, scenario grid, operating characteristics, and feasibility implications. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T040 — Issue a qualified no-call and escalation package for sample size, power, precision, and operating characteristics in Clinical Trial Design and Biostatistics

Return a qualified no-call when reasonable assumptions yield inadequate operating characteristics or infeasible enrollment. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-sample-size-power-precision-and-operating-characteristics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Interim monitoring, adaptive design, and decision simulation

### MYR-D091-T041 — Define decision scope and no-call criteria for interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering planning of interim efficacy, futility, safety, sample-size re-estimation, response adaptation, arm dropping, or platform decisions. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T042 — Audit input provenance and analytical fitness for interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Inspect trial design, information timing, endpoints, accrual, delay, decision boundaries, adaptation rules, simulations, and oversight roles. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T043 — Normalize interoperable representations while preserving unresolved discrepancies for interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Reconcile interim looks, information fractions, boundaries, adaptation algorithms, decision states, alpha spending, and reporting restrictions into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T044 — Compute decision-relevant measures with prespecified methods for interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Estimate type-I error, power, expected sample size, adaptation frequency, bias, confidence-interval coverage, and operational feasibility using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T045 — Quantify uncertainty and applicability limits for interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from adaptive uncertainty from outcome delay, enrollment trends, model misspecification, changing control performance, and operational leakage. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T046 — Detect critical failure modes before interpreting interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Test explicitly for unplanned peeking, unblinded sponsor influence, simulation under too few scenarios, adaptation-induced bias, and undocumented algorithm changes. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T047 — Enforce risk controls and escalation gates for interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Apply independent monitoring, locked rules, extensive simulation, firewalls, alpha control, and predefined exceptional circumstances. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T048 — Benchmark alternative approaches against predefined criteria for interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Compare group-sequential, seamless, adaptive enrichment, sample-size re-estimation, response-adaptive, Bayesian, and platform designs. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T049 — Assemble the auditable decision artifact for interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Generate an adaptive-design simulation report with decision rules, operating characteristics, governance, and implementation testing. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T050 — Issue a qualified no-call and escalation package for interim monitoring, adaptive design, and decision simulation in Clinical Trial Design and Biostatistics

Return a qualified no-call when adaptations cannot be implemented without unacceptable statistical or operational bias. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-interim-monitoring-adaptive-design-and-decision-simulation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Primary analysis, covariates, and model diagnostics

### MYR-D091-T051 — Define decision scope and no-call criteria for primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering specification of the primary estimator and statistical model aligned to the estimand and endpoint. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T052 — Audit input provenance and analytical fitness for primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Inspect analysis population, endpoint data, covariates, strata, clusters, repeated measures, censoring, intercurrent events, and assumptions. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T053 — Normalize interoperable representations while preserving unresolved discrepancies for primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Reconcile analysis datasets, model formula, contrasts, estimators, standard errors, confidence intervals, diagnostics, and convergence status into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T054 — Compute decision-relevant measures with prespecified methods for primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Estimate treatment effect, precision, model fit, calibration, residual behavior, proportionality or covariance assumptions, and robustness using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T055 — Quantify uncertainty and applicability limits for primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from analysis uncertainty from nonlinearity, informative censoring, sparse events, site effects, overdispersion, and model misspecification. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T056 — Detect critical failure modes before interpreting primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Test explicitly for post hoc covariate selection, separation, nonconvergence, incorrect variance, ignored clustering, and model-result cherry-picking. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T057 — Enforce risk controls and escalation gates for primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Apply prespecified models, blinded data review, robust variance where justified, convergence rules, diagnostics, and fallback hierarchy. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T058 — Benchmark alternative approaches against predefined criteria for primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Compare linear, generalized, mixed, survival, recurrent-event, ordinal, rank, semiparametric, and Bayesian estimators. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T059 — Assemble the auditable decision artifact for primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Generate a primary-analysis specification with executable code, diagnostics, fallback rules, and interpretation boundaries. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T060 — Issue a qualified no-call and escalation package for primary analysis, covariates, and model diagnostics in Clinical Trial Design and Biostatistics

Return a qualified no-call when model assumptions or data support are insufficient for a stable primary estimate. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-primary-analysis-covariates-and-model-diagnostics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Missing data, intercurrent events, and sensitivity analysis

### MYR-D091-T061 — Define decision scope and no-call criteria for missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering handling of missing outcomes and post-randomization events consistent with the estimand and plausible missingness mechanisms. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T062 — Audit input provenance and analytical fitness for missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Inspect missingness patterns, reasons, timing, treatment changes, rescue, discontinuation, death, follow-up, and auxiliary variables. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T063 — Normalize interoperable representations while preserving unresolved discrepancies for missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Reconcile missingness categories, intercurrent-event states, imputation models, tipping parameters, censoring rules, and sensitivity scenarios into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T064 — Compute decision-relevant measures with prespecified methods for missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Estimate amount and pattern of missingness, robustness of treatment effect, tipping points, model dependence, and uncertainty inflation using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T065 — Quantify uncertainty and applicability limits for missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from sensitivity uncertainty from unverifiable missingness assumptions, sparse patterns, death truncation, and incompatible auxiliary data. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T066 — Detect critical failure modes before interpreting missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Test explicitly for complete-case default, last-observation carry-forward misuse, conflated intercurrent events, implausible imputation, and selective sensitivity reporting. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T067 — Enforce risk controls and escalation gates for missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Apply estimand-consistent handling, reason-specific analysis, multiple imputation diagnostics, controlled sensitivity ranges, and transparent no-call outcomes. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T068 — Benchmark alternative approaches against predefined criteria for missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Compare likelihood, multiple imputation, inverse probability, reference-based, pattern-mixture, joint, and tipping-point analyses. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T069 — Assemble the auditable decision artifact for missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Generate a missing-data and sensitivity package showing assumptions, diagnostics, tipping regions, and conclusion stability. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T070 — Issue a qualified no-call and escalation package for missing data, intercurrent events, and sensitivity analysis in Clinical Trial Design and Biostatistics

Return a qualified no-call when conclusions depend on unsupported assumptions within clinically plausible missing-data scenarios. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-missing-data-intercurrent-events-and-sensitivity-analysis-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Multiplicity, subgroup, and heterogeneity strategy

### MYR-D091-T071 — Define decision scope and no-call criteria for multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering control and interpretation of multiple endpoints, doses, populations, time points, interim looks, and subgroup effects. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T072 — Audit input provenance and analytical fitness for multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Inspect hypothesis hierarchy, endpoint correlations, dose-response, subgroup definitions, biomarkers, prior evidence, and decision priorities. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T073 — Normalize interoperable representations while preserving unresolved discrepancies for multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Reconcile hypothesis families, testing sequence, alpha allocation, adjusted intervals, interaction terms, subgroup estimates, and credibility criteria into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T074 — Compute decision-relevant measures with prespecified methods for multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Estimate familywise error, false discovery, power, interaction evidence, heterogeneity, consistency, and decision coherence using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T075 — Quantify uncertainty and applicability limits for multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from multiplicity uncertainty from data-driven hypotheses, sparse subgroups, correlated tests, and changing clinical priorities. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T076 — Detect critical failure modes before interpreting multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Test explicitly for unadjusted endpoint mining, within-subgroup significance comparisons, post hoc cutpoints, subgroup overclaim, and inconsistent estimands. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T077 — Enforce risk controls and escalation gates for multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Apply prespecified families, interaction tests, shrinkage, multiplicity adjustment, minimum information, and exploratory labels. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T078 — Benchmark alternative approaches against predefined criteria for multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Compare fixed-sequence, gatekeeping, graphical, closed-testing, hierarchical, Bayesian multilevel, and false-discovery strategies. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T079 — Assemble the auditable decision artifact for multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Generate a multiplicity and heterogeneity plan with hypothesis graph, adjusted inference, subgroup credibility, and reporting language. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T080 — Issue a qualified no-call and escalation package for multiplicity, subgroup, and heterogeneity strategy in Clinical Trial Design and Biostatistics

Return a qualified no-call when the hypothesis family or subgroup evidence cannot support confirmatory claims. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-multiplicity-subgroup-and-heterogeneity-strategy-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Quality-by-design, operational data, and trial conduct analytics

### MYR-D091-T081 — Define decision scope and no-call criteria for quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering identification and monitoring of critical-to-quality factors affecting participant protection and trial result reliability. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T082 — Audit input provenance and analytical fitness for quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Inspect protocol, site capabilities, recruitment, deviations, monitoring, data timeliness, endpoint processes, safety reporting, and vendor data. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T083 — Normalize interoperable representations while preserving unresolved discrepancies for quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Reconcile critical factors, risk indicators, thresholds, site trends, deviation categories, root causes, and corrective actions into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T084 — Compute decision-relevant measures with prespecified methods for quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Estimate eligibility accuracy, consent, treatment fidelity, endpoint completeness, safety timeliness, data integrity, and site variability using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T085 — Quantify uncertainty and applicability limits for quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from operational uncertainty from delayed data, inconsistent site processes, risk-indicator multiplicity, and changing recruitment patterns. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T086 — Detect critical failure modes before interpreting quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Test explicitly for metric gaming, excessive low-value monitoring, unblinded operational decisions, threshold drift, and confounding site volume with quality. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T087 — Enforce risk controls and escalation gates for quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Apply risk-based monitoring, centralized analytics, documented thresholds, participant-protection priority, and independent escalation. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T088 — Benchmark alternative approaches against predefined criteria for quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Compare source review, centralized monitoring, statistical monitoring, targeted visits, quality tolerance limits, and process-improvement approaches. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T089 — Assemble the auditable decision artifact for quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Generate a trial quality dashboard with critical risks, evidence, actions, owners, and impact assessment. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T090 — Issue a qualified no-call and escalation package for quality-by-design, operational data, and trial conduct analytics in Clinical Trial Design and Biostatistics

Return a qualified no-call when critical participant-safety or reliability risks cannot be controlled within the approved trial design. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-quality-by-design-operational-data-and-trial-conduct-analytics-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Statistical reporting, reproducibility, and decision interpretation

### MYR-D091-T091 — Define decision scope and no-call criteria for statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Create a versioned decision charter covering production of transparent results, tables, figures, listings, analysis datasets, code, and conclusions aligned with the protocol. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T092 — Audit input provenance and analytical fitness for statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Inspect protocol, amendments, analysis plan, data cuts, analysis datasets, code, outputs, deviations, and clinical interpretation. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T093 — Normalize interoperable representations while preserving unresolved discrepancies for statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Reconcile results, effect sizes, confidence intervals, p-values, estimands, sensitivity outcomes, deviations, metadata, and version history into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T094 — Compute decision-relevant measures with prespecified methods for statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Estimate reproducibility, traceability, completeness, numerical consistency, conclusion stability, and alignment with prespecified analyses using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T095 — Quantify uncertainty and applicability limits for statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Characterize uncertainty arising from reporting uncertainty from late changes, database corrections, multiple data cuts, unresolved deviations, and model dependence. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T096 — Detect critical failure modes before interpreting statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Test explicitly for selective reporting, p-value emphasis without effect size, unexplained deviations, inconsistent populations, and irreproducible tables. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T097 — Enforce risk controls and escalation gates for statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Apply independent programming, validation, code review, output reconciliation, transparent deviations, and qualified clinical-statistical sign-off. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T098 — Benchmark alternative approaches against predefined criteria for statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Compare traditional, estimand-focused, Bayesian, adaptive, pragmatic, and participant-level reproducible reporting packages. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T099 — Assemble the auditable decision artifact for statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Generate a statistical evidence dossier with datasets, metadata, code, validated outputs, sensitivities, and interpretation limits. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D091-T100 — Issue a qualified no-call and escalation package for statistical reporting, reproducibility, and decision interpretation in Clinical Trial Design and Biostatistics

Return a qualified no-call when results cannot be reproduced or interpreted consistently with the approved design and estimand. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-statistical-reporting-reproducibility-and-decision-interpretation-in-clinical-trial-design-and-biostatistics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
