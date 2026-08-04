# Scientific Basis and Controlled Source Register — Batch 010

**Domains:** 091–100  
**Source-status verification date:** 2026-08-04

## Architecture boundary

Batch 010 decomposes clinical trial design, clinical data standards, real-world evidence, pharmacovigilance, regulatory submissions, GxP computerized systems, laboratory informatics, FAIR data, biomedical knowledge graphs, and biotechnology AI governance into bounded advisory and evidence-management tasks. It does not autonomously enroll participants, make treatment or safety decisions, submit to regulators, release validated systems, disposition regulated records or batches, deploy models, or authorize biosafety or biosecurity actions.

## Domain-specific controls

### 091 — Clinical trial design and biostatistics

Tasks require alignment among clinical question, estimand, endpoint, design, randomization, sample size, intercurrent-event strategy, multiplicity, missing-data assumptions, sensitivity analysis, and reporting. Simulated operating characteristics support design decisions but do not guarantee trial success or regulatory acceptance.

### 092 — Clinical data management and standards

Tasks separate source capture, edit checks, coding, external transfers, SDTM tabulation, ADaM analysis data, Define-XML metadata, reviewer guides, traceability, lock, and archive. Versioned CDISC standards and controlled terminology must be resolved against the study's submission context; syntactic conformance alone does not establish semantic correctness.

### 093 — Real-world evidence and pharmacoepidemiology

Tasks specify target-trial logic, data fitness, cohort construction, exposure and outcome phenotypes, confounding control, longitudinal treatment, sensitivity analyses, transportability, and transparent reporting. Observational association is not silently upgraded to causal evidence.

### 094 — Pharmacovigilance and safety signals

Tasks preserve case-level uncertainty, duplicate detection, expectedness, seriousness, exposure denominators, stimulated reporting, indication and channeling effects, disproportionality limitations, clinical assessment, pharmacoepidemiologic confirmation, and risk-management effectiveness. A statistical signal is not equivalent to a verified causal risk.

### 095 — Regulatory intelligence and submissions

Tasks maintain jurisdiction, product class, pathway, current guidance status, CTD content ownership, evidence traceability, eCTD technical validity, response commitments, labeling provenance, and lifecycle change control. The agent prepares reviewable artifacts but does not claim legal sufficiency or transmit submissions.

### 096 — GxP compliance and computerized-system validation

Tasks apply intended-use and risk-based assurance, requirements traceability, supplier evidence, data integrity, testing, security, migration, release readiness, incident and CAPA handling, periodic review, and retirement. Passing scripted tests does not alone establish fitness for intended use or regulatory compliance.

### 097 — Laboratory informatics, LIMS, and ELN automation

Tasks preserve sample genealogy, instrument and method versions, raw-data links, calculations, results, inventory, workflow state, signatures, access, audit trails, interoperability, retention, and exception handling. Automation may route and validate records but may not silently alter approved data or laboratory decisions.

### 098 — FAIR biomedical data and ontology engineering

Tasks address persistent identifiers, metadata, ontologies, mappings, provenance, access, privacy, licensing, interoperable formats, APIs, quality, repository selection, and preservation. FAIRness is assessed dimensionally and does not imply that data are open, ethically reusable, high quality, or fit for every purpose.

### 099 — Biomedical knowledge graphs and evidence synthesis

Tasks separate source licensing, schema, entity resolution, extraction, evidence typing, confidence, contradiction, temporal validity, graph construction, reasoning, evaluation, and governance. Graph connectivity or model confidence does not establish biological causality or clinical truth.

### 100 — Biotech AI validation, governance, biosafety, and biosecurity

Tasks begin with intended use and risk classification, then cover dataset governance, model development, calibration, robustness, security, human factors, deployment monitoring, incident handling, biosafety and biosecurity misuse risk, auditability, and retirement. General model benchmarks cannot substitute for use-case-specific validation and accountable authorization.

## Controlled primary-source register

1. **ICH E6(R3) Good Clinical Practice — FDA final guidance, September 2025.** Risk-proportionate quality by design, participant protection, and reliable trial results. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e6r3-good-clinical-practice-gcp
2. **ICH E8(R1), General Considerations for Clinical Studies.** Official principles for study quality, design, and conduct. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/e8r1-general-considerations-clinical-studies
3. **ICH M14 — FDA final guidance, March 2026.** Principles for non-interventional studies using real-world data for medicine safety assessment. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m14-general-principles-planning-designing-analyzing-and-reporting-non-interventional-studies-utilize
4. **FDA Real-World Evidence resources and final guidances.** Current data-fitness, registry, claims/EHR, submission, and evidentiary expectations must be resolved at execution time. https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence
5. **CDISC standards library.** Resolve current versions of SDTM, ADaM, Define-XML, ODM, and controlled terminology for the specific submission and implementation context. https://www.cdisc.org/standards
6. **FDA eCTD submission standards.** FDA supports eCTD v4.0 for new applications and maintains versioned v3.2.2 and v4.0 technical resources; implementation package versions and dates must be checked at execution time. https://www.fda.gov/drugs/electronic-regulatory-submission-and-review/electronic-common-technical-document-ectd
7. **FAIR Guiding Principles (Wilkinson et al., 2016).** Foundational principles for findability, accessibility, interoperability, and reuse. https://doi.org/10.1038/sdata.2016.18
8. **NIST AI Risk Management Framework.** AI RMF 1.0 is a voluntary use-case-agnostic framework; NIST states it is being revised, and the Generative AI Profile is a companion resource. https://www.nist.gov/itl/ai-risk-management-framework
9. **NIST AI 600-1, Generative AI Profile (2024).** Cross-sector companion profile for generative-AI risk management. https://doi.org/10.6028/NIST.AI.600-1

## Anti-hallucination and anti-rot controls

- Capture jurisdiction, standard or guidance version, effective date, controlled terminology package, implementation guide, and retrieval date.
- Preserve the distinction among draft, final, supported, required, accepted, and deprecated status.
- Do not infer semantic correctness, causal validity, regulatory acceptability, clinical safety, or compliance from a passing schema or software validation alone.
- Keep model development, independent validation, deployment authorization, monitoring, and retirement as separate evidence states.
- Require human accountability for participant protection, safety escalation, submission decisions, GxP release, access control, and biosafety/biosecurity authorization.
- Regenerate volatile reference and implementation details from official sources instead of accumulating undocumented patches.
