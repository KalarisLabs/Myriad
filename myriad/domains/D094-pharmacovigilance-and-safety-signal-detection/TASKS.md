# D094 — Pharmacovigilance and Safety-Signal Detection

Batch **010** · 10 workstreams · 100 tasks

## 01. Safety-source intake, triage, and reportability routing

### MYR-D094-T001 — Define decision scope and no-call criteria for safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering receipt and triage of spontaneous, solicited, clinical, literature, social, partner, product-quality, and digital safety information. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T002 — Audit input provenance and analytical fitness for safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Inspect source message, reporter, patient, product, event, dates, country, program context, attachments, and receipt timestamps. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T003 — Normalize interoperable representations while preserving unresolved discrepancies for safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Reconcile case identifiers, source type, minimum criteria, seriousness cues, special situations, follow-up needs, and regulatory clocks into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T004 — Compute decision-relevant measures with prespecified methods for safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Estimate valid-case detection, intake completeness, clock accuracy, duplicate risk, triage priority, and route to responsible organization using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T005 — Quantify uncertainty and applicability limits for safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from intake uncertainty from incomplete identities, translated content, indirect reports, social-media context, and multiple receipt channels. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T006 — Detect critical failure modes before interpreting safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Test explicitly for missed valid cases, incorrect day-zero assignment, lost attachments, duplicate creation, privacy overcollection, and misrouted responsibilities. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T007 — Enforce risk controls and escalation gates for safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Apply minimum-report criteria, source preservation, clock controls, privacy minimization, escalation for death or serious events, and human oversight. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T008 — Benchmark alternative approaches against predefined criteria for safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Compare manual, rules-based, NLP-assisted, partner-gateway, call-center, and literature-intake approaches with verified routing. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T009 — Assemble the auditable decision artifact for safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Generate a traceable intake record with source preservation, validity decision, regulatory clock, and follow-up plan. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T010 — Issue a qualified no-call and escalation package for safety-source intake, triage, and reportability routing in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when minimum criteria, receipt date, product involvement, or organizational responsibility cannot be determined. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-safety-source-intake-triage-and-reportability-routing-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Case data extraction, narrative, and structured coding

### MYR-D094-T011 — Define decision scope and no-call criteria for case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering conversion of safety reports into structured case data and a medically coherent chronology without adding unsupported facts. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T012 — Audit input provenance and analytical fitness for case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Inspect source documents, follow-up, medical history, concomitant products, laboratory data, timelines, translations, and dictionaries. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T013 — Normalize interoperable representations while preserving unresolved discrepancies for case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Reconcile patient and reporter data, products, events, tests, history, dates, seriousness, outcomes, MedDRA terms, and narrative chronology into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T014 — Compute decision-relevant measures with prespecified methods for case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Estimate field completeness, temporal consistency, coding accuracy, narrative fidelity, source traceability, and unresolved-question count using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T015 — Quantify uncertainty and applicability limits for case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from extraction uncertainty from ambiguous language, conflicting dates, poor scans, translation, abbreviations, and copied-forward records. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T016 — Detect critical failure modes before interpreting case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Test explicitly for hallucinated details, chronology inversion, coding from diagnosis assumptions, loss of negation, conflated patients, and source-text overwrite. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T017 — Enforce risk controls and escalation gates for case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Apply source-linked extraction, qualified coding review, uncertainty flags, verbatim retention, date logic, and no inference beyond evidence. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T018 — Benchmark alternative approaches against predefined criteria for case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Compare manual abstraction, structured forms, NLP-assisted extraction, terminology mapping, and hybrid medical review. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T019 — Assemble the auditable decision artifact for case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Generate a coded case record and narrative with field-level provenance, contradictions, and follow-up questions. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T020 — Issue a qualified no-call and escalation package for case data extraction, narrative, and structured coding in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when the report cannot be represented without inventing clinically material information. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-case-data-extraction-narrative-and-structured-coding-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Seriousness, expectedness, causality, and case assessment

### MYR-D094-T021 — Define decision scope and no-call criteria for seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering medical assessment of seriousness criteria, listedness or expectedness, outcome, causality evidence, and reporting implications. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T022 — Audit input provenance and analytical fitness for seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Inspect case chronology, product label or reference safety information, clinical course, dechallenge, rechallenge, alternatives, and reporter assessment. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T023 — Normalize interoperable representations while preserving unresolved discrepancies for seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Reconcile seriousness criteria, expectedness status, causality dimensions, outcome, case quality, reportability, and rationale into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T024 — Compute decision-relevant measures with prespecified methods for seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Estimate temporal plausibility, alternative causes, known association, dechallenge or rechallenge, biologic plausibility, and evidence completeness using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T025 — Quantify uncertainty and applicability limits for seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from assessment uncertainty from sparse clinical data, polypharmacy, comorbidity, evolving labels, and differing causality methods. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T026 — Detect critical failure modes before interpreting seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Test explicitly for seriousness inferred from symptom severity, stale reference safety information, deterministic causality scoring, and failure to preserve reporter opinion. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T027 — Enforce risk controls and escalation gates for seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Apply current reference documents, criterion-specific rationale, medical review, jurisdictional rules, and explicit unassessable categories. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T028 — Benchmark alternative approaches against predefined criteria for seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Compare structured causality, global introspection, case-series context, challenge-dechallenge, and Bayesian supportive approaches. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T029 — Assemble the auditable decision artifact for seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Generate a medical case assessment with seriousness, expectedness, causality rationale, reporting status, and uncertainty. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T030 — Issue a qualified no-call and escalation package for seriousness, expectedness, causality, and case assessment in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when clinically material facts or current reference information are insufficient for a qualified assessment. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-seriousness-expectedness-causality-and-case-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Duplicate detection, follow-up, and case-version reconciliation

### MYR-D094-T031 — Define decision scope and no-call criteria for duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering identification, merge, follow-up, and version control for potentially duplicate or evolving safety reports. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T032 — Audit input provenance and analytical fitness for duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Inspect patient and reporter descriptors, product, event, dates, geography, source, narrative similarity, attachments, and prior case versions. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T033 — Normalize interoperable representations while preserving unresolved discrepancies for duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Reconcile candidate duplicate pairs, match features, confidence, master case, merged fields, conflicts, follow-up status, and audit history into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T034 — Compute decision-relevant measures with prespecified methods for duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Estimate duplicate precision and recall, conflict resolution, follow-up yield, version completeness, and preservation of source provenance using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T035 — Quantify uncertainty and applicability limits for duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from matching uncertainty from privacy-masked identifiers, common events, translated narratives, delayed follow-up, and multiple reporters. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T036 — Detect critical failure modes before interpreting duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Test explicitly for incorrect merges, missed duplicates, deleted conflicting evidence, lost regulatory history, circular case linking, and follow-up to wrong reporter. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T037 — Enforce risk controls and escalation gates for duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Apply conservative merge thresholds, medical review, immutable source versions, field-level provenance, and reversible decisions. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T038 — Benchmark alternative approaches against predefined criteria for duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Compare deterministic, probabilistic, graph, text-similarity, temporal, and hybrid duplicate-detection strategies. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T039 — Assemble the auditable decision artifact for duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Generate a duplicate and follow-up reconciliation package with evidence, master-case logic, conflicts, and audit trail. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T040 — Issue a qualified no-call and escalation package for duplicate detection, follow-up, and case-version reconciliation in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when case identity cannot be resolved without unacceptable risk of merging distinct patients or fragmenting one case. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-duplicate-detection-follow-up-and-case-version-reconciliation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Aggregate case-series and descriptive safety analysis

### MYR-D094-T041 — Define decision scope and no-call criteria for aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering characterization of event patterns across products, doses, populations, time, seriousness, outcomes, and reporting sources. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T042 — Audit input provenance and analytical fitness for aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Inspect deduplicated cases, exposure estimates, product hierarchy, MedDRA coding, labels, dose, indication, time-to-onset, and follow-up quality. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T043 — Normalize interoperable representations while preserving unresolved discrepancies for aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Reconcile case-series tables, stratifications, onset distributions, outcomes, dechallenge, reporting rates, and case-quality categories into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T044 — Compute decision-relevant measures with prespecified methods for aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Estimate case counts, reporting rates where denominators support them, temporal patterns, seriousness, outcomes, dose relationships, and clustering using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T045 — Quantify uncertainty and applicability limits for aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from aggregate uncertainty from stimulated reporting, missing exposure, duplicate residuals, coding changes, and differential follow-up. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T046 — Detect critical failure modes before interpreting aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Test explicitly for spontaneous counts presented as incidence, inappropriate denominator mixing, coding-version drift, cherry-picked strata, and ignored case quality. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T047 — Enforce risk controls and escalation gates for aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Apply source-stratified interpretation, denominator qualification, versioned coding, case-quality weighting, and no causal conclusion from counts alone. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T048 — Benchmark alternative approaches against predefined criteria for aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Compare descriptive case series, observed-to-expected, temporal scan, cluster, product-event, and exposure-stratified analyses. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T049 — Assemble the auditable decision artifact for aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Generate an aggregate safety profile with source context, denominators, case quality, patterns, and limitations. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T050 — Issue a qualified no-call and escalation package for aggregate case-series and descriptive safety analysis in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when data source or denominator limitations prevent interpretable aggregate comparison. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-aggregate-case-series-and-descriptive-safety-analysis-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Disproportionality, data mining, and emerging-pattern detection

### MYR-D094-T051 — Define decision scope and no-call criteria for disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering screening of spontaneous reports and other safety data for product-event combinations requiring review. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T052 — Audit input provenance and analytical fitness for disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Inspect deduplicated coded cases, product and event hierarchies, background database, time, geography, age, sex, and reporting source. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T053 — Normalize interoperable representations while preserving unresolved discrepancies for disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Reconcile contingency counts, reporting odds, proportional reporting ratios, information components, shrinkage estimates, trends, and alerts into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T054 — Compute decision-relevant measures with prespecified methods for disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Estimate signal score, confidence interval, case count, temporal emergence, subgroup concentration, robustness, and masking or competition effects using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T055 — Quantify uncertainty and applicability limits for disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from screening uncertainty from reporting bias, channeling, notoriety, competition, coding changes, and database composition. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T056 — Detect critical failure modes before interpreting disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Test explicitly for threshold-only signal declaration, uncorrected repeated screening, masked signals, product hierarchy errors, and causality claims from disproportionality. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T057 — Enforce risk controls and escalation gates for disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Apply minimum case review, empirical shrinkage where appropriate, temporal and subgroup checks, hierarchy sensitivity, and human validation. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T058 — Benchmark alternative approaches against predefined criteria for disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Compare frequentist, Bayesian, empirical-Bayes, tree-based, temporal, network, and sequence-pattern screening methods. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T059 — Assemble the auditable decision artifact for disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Generate a prioritized screening output with statistics, case context, artifacts, and review recommendation. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T060 — Issue a qualified no-call and escalation package for disproportionality, data mining, and emerging-pattern detection in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when the alert is explained by data artifacts or lacks enough cases for meaningful medical review. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-disproportionality-data-mining-and-emerging-pattern-detection-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Signal validation, prioritization, and assessment

### MYR-D094-T061 — Define decision scope and no-call criteria for signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering transition of a potential signal through validation, prioritization, evidence assessment, and decision tracking. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T062 — Audit input provenance and analytical fitness for signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Inspect cases, epidemiology, clinical trials, nonclinical data, literature, mechanism, class effects, exposure, labels, and regulatory history. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T063 — Normalize interoperable representations while preserving unresolved discrepancies for signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Reconcile signal identifiers, validation status, evidence matrix, priority score, questions, actions, owners, and decision history into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T064 — Compute decision-relevant measures with prespecified methods for signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Estimate case strength, consistency, temporality, specificity, dose response, biologic plausibility, impact, preventability, and evidence gaps using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T065 — Quantify uncertainty and applicability limits for signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from signal uncertainty from sparse cases, confounding, class effects, evolving use, competing risks, and incomplete exposure. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T066 — Detect critical failure modes before interpreting signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Test explicitly for single-source decisions, popularity bias, duplicate evidence counting, mechanistic overreach, and undocumented signal closure. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T067 — Enforce risk controls and escalation gates for signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Apply multidisciplinary review, explicit criteria, source independence, benefit-risk relevance, tracked actions, and qualified governance. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T068 — Benchmark alternative approaches against predefined criteria for signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Compare case-series, literature, observed-to-expected, pharmacoepidemiologic, mechanistic, and class-wide assessment strategies. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T069 — Assemble the auditable decision artifact for signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Generate a signal assessment report with evidence, uncertainty, priority, recommended actions, and closure rationale. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T070 — Issue a qualified no-call and escalation package for signal validation, prioritization, and assessment in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when evidence remains too weak or contradictory to support a signal conclusion beyond continued monitoring. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-signal-validation-prioritization-and-assessment-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Pharmacoepidemiologic signal evaluation and quantification

### MYR-D094-T071 — Define decision scope and no-call criteria for pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering design of observational studies to confirm, refute, or quantify a safety signal in fit-for-purpose data. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T072 — Audit input provenance and analytical fitness for pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Inspect signal question, target population, exposure, outcome phenotype, confounders, data sources, latency, and background rates. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T073 — Normalize interoperable representations while preserving unresolved discrepancies for pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Reconcile protocol, cohort logic, case definitions, causal diagram, analysis plan, sensitivity analyses, and reporting outputs into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T074 — Compute decision-relevant measures with prespecified methods for pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Estimate relative and absolute risk, excess cases, timing, dose response, subgroup effects, robustness, and transportability using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T075 — Quantify uncertainty and applicability limits for pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from study uncertainty from confounding by indication, outcome misclassification, protopathic bias, surveillance bias, and rare events. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T076 — Detect critical failure modes before interpreting pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Test explicitly for poor comparators, immortal time, inadequate latency, unvalidated outcome, inappropriate adjustment, and overreliance on one database. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T077 — Enforce risk controls and escalation gates for pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Apply active comparators, target-trial alignment, validation, bias analysis, multiple data sources where needed, and protocol transparency. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T078 — Benchmark alternative approaches against predefined criteria for pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Compare cohort, case-control, self-controlled, case-crossover, observed-to-expected, registry, and distributed-database studies. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T079 — Assemble the auditable decision artifact for pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Generate a signal-quantification dossier with protocol, data fitness, results, sensitivity, and residual bias. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T080 — Issue a qualified no-call and escalation package for pharmacoepidemiologic signal evaluation and quantification in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when available data cannot identify or measure the safety risk with acceptable bias. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-pharmacoepidemiologic-signal-evaluation-and-quantification-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Risk management, minimization, and effectiveness evaluation

### MYR-D094-T081 — Define decision scope and no-call criteria for risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering selection, implementation, and evaluation of labeling, communication, monitoring, access, education, or restricted-use measures. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T082 — Audit input provenance and analytical fitness for risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Inspect signal assessment, benefit-risk profile, affected population, prescribing workflow, healthcare system, proposed measures, and outcome data. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T083 — Normalize interoperable representations while preserving unresolved discrepancies for risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Reconcile risk statements, target users, intervention components, implementation metrics, process outcomes, health outcomes, and review intervals into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T084 — Compute decision-relevant measures with prespecified methods for risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Estimate reach, knowledge, behavior, monitoring adherence, contraindicated use, event incidence, burden, equity, and unintended consequences using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T085 — Quantify uncertainty and applicability limits for risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from effectiveness uncertainty from secular trends, co-interventions, low event rates, poor exposure measurement, and implementation heterogeneity. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T086 — Detect critical failure modes before interpreting risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Test explicitly for process-only success claims, inaccessible materials, unintended treatment denial, risk displacement, unmeasured burden, and no baseline comparator. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T087 — Enforce risk controls and escalation gates for risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Apply clear objectives, theory of change, process and outcome measures, equity review, periodic reassessment, and modification triggers. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T088 — Benchmark alternative approaches against predefined criteria for risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Compare labeling, targeted communication, educational, laboratory monitoring, pregnancy prevention, registry, and controlled-access measures. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T089 — Assemble the auditable decision artifact for risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Generate a risk-minimization plan and effectiveness report with objectives, metrics, outcomes, burden, and adaptation decisions. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T090 — Issue a qualified no-call and escalation package for risk management, minimization, and effectiveness evaluation in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when the measure cannot be implemented, evaluated, or justified relative to its burden and benefit. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-risk-management-minimization-and-effectiveness-evaluation-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Periodic reporting, governance, automation validation, and inspection readiness

### MYR-D094-T091 — Define decision scope and no-call criteria for periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Create a versioned decision charter covering production of periodic safety reports, benefit-risk evaluations, signal logs, compliance metrics, and auditable automated workflows. Identify the accountable owner, intended users, permitted downstream actions, evidence thresholds, stopping conditions, and evidence that must be present before the task may return a decision rather than a no-call.

- **Routing name:** `define-decision-scope-and-no-call-criteria-for-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T092 — Audit input provenance and analytical fitness for periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Inspect case database, exposure, signals, studies, literature, regulatory actions, labels, commitments, automation models, and procedural requirements. Verify source provenance, identifiers, temporal ordering, units, completeness, permissions, chain of custody where applicable, and compatibility with the intended analysis; preserve missing, conflicting, censored, or inaccessible inputs as explicit structured defects.

- **Routing name:** `audit-input-provenance-and-analytical-fitness-for-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T093 — Normalize interoperable representations while preserving unresolved discrepancies for periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Reconcile report sections, interval and cumulative analyses, signal status, benefit-risk conclusions, compliance metrics, model versions, and audit records into versioned machine-readable structures. Record every mapping, normalization, deduplication, ontology or schema version, coordinate or unit conversion, and unresolved discordance without silently converting uncertainty into a favorable value.

- **Routing name:** `normalize-interoperable-representations-while-preserving-unresolved-discrepancies-for-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T094 — Compute decision-relevant measures with prespecified methods for periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Estimate report completeness, data reconciliation, submission timeliness, signal traceability, model accuracy, deviation closure, and reproducibility using methods selected before outcome inspection. Emit intermediate quantities, parameters, thresholds, calibration references, denominator definitions, and sensitivity outputs required to reproduce and independently review the result.

- **Routing name:** `compute-decision-relevant-measures-with-prespecified-methods-for-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T095 — Quantify uncertainty and applicability limits for periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Characterize uncertainty arising from governance uncertainty from database locks, source updates, coding versions, global reporting differences, and automation drift. Separate measurement, sampling, model, transportability, and decision uncertainty where relevant; propagate uncertainty into confidence intervals, sensitivity analyses, applicability statements, and no-call logic rather than reporting unsupported precision.

- **Routing name:** `quantify-uncertainty-and-applicability-limits-for-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T096 — Detect critical failure modes before interpreting periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Test explicitly for inconsistent cutoffs, missing local cases, copied conclusions, unvalidated automation, opaque model decisions, and unresolved compliance deviations. Use independent consistency checks, negative or positive controls, diagnostic plots or machine-readable diagnostics, and predeclared failure thresholds; block downstream interpretation whenever a failure invalidates the intended inference.

- **Routing name:** `detect-critical-failure-modes-before-interpreting-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T097 — Enforce risk controls and escalation gates for periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Apply qualified medical sign-off, source reconciliation, version control, automation monitoring, audit trails, and jurisdiction-specific requirements. Encode pass, warning, fail, and no-call gates; name the accountable reviewer and required escalation path; prevent the agent from executing laboratory, clinical, environmental, manufacturing, regulatory, or security actions beyond its authorized advisory boundary.

- **Routing name:** `enforce-risk-controls-and-escalation-gates-for-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T098 — Benchmark alternative approaches against predefined criteria for periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Compare manual, workflow-assisted, NLP-supported, rule-based, aggregate-reporting, and global-local reconciliation models. Use predefined scientific validity, predictive performance, robustness, resource, equity, safety, maintainability, and operational criteria as applicable; document trade-offs and avoid selecting an approach solely because it yields the most favorable observed result.

- **Routing name:** `benchmark-alternative-approaches-against-predefined-criteria-for-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T099 — Assemble the auditable decision artifact for periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Generate an inspection-ready pharmacovigilance dossier with case lineage, signals, reports, controls, deviations, and model validation. Include machine-readable status, provenance, assumptions, methods, versions, validation evidence, uncertainty, limitations, unresolved conflicts, decision rationale, and links to all supporting inputs so another qualified reviewer can reconstruct the conclusion.

- **Routing name:** `assemble-the-auditable-decision-artifact-for-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D094-T100 — Issue a qualified no-call and escalation package for periodic reporting, governance, automation validation, and inspection readiness in Pharmacovigilance and Safety-Signal Detection

Return a qualified no-call when safety records, decisions, automation behavior, or reporting compliance cannot be reconstructed. State exactly which evidence is absent or invalid, which downstream conclusions are prohibited, what additional data or qualified review could resolve the blocker, and whether any immediate safety, quality, privacy, regulatory, or biosecurity escalation is required.

- **Routing name:** `issue-a-qualified-no-call-and-escalation-package-for-periodic-reporting-governance-automation-validation-and-inspection-readiness-in-pharmacovigilance-and-safety-signal-detection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
