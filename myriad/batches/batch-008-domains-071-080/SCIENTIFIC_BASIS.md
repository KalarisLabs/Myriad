# Scientific Basis and Scope Controls — Batch 008

## Architecture boundary

Batch 008 is a computational and evidence-management taxonomy for bioprocess and analytical-development agents. It does not authorize autonomous equipment control, GMP batch release, modification of validated recipes, or claims of regulatory compliance. Every node requires qualified human review and local procedures before operational use.

## Primary guidance families

- **ICH Q5A(R2), Q5B, Q5C, Q5D, and Q5E:** viral safety, expression-construct characterization, stability, cell substrates, and comparability for biotechnology products.
- **ICH Q6B:** specifications, analytical procedures, and acceptance criteria for biotechnological and biological products.
- **ICH Q8(R2), Q9(R1), Q10, Q11, and Q12:** pharmaceutical development, quality risk management, pharmaceutical quality systems, drug-substance development, and lifecycle management.
- **ICH Q13:** continuous manufacturing of drug substances and drug products, including control strategy and state-of-control considerations.
- **ICH Q2(R2) and Q14:** analytical-procedure validation and lifecycle-oriented analytical development.
- **FDA Process Validation guidance:** lifecycle stages covering process design, process qualification, and continued process verification.
- **FDA PAT framework:** risk-based use of process measurements, multivariate tools, and process control to improve manufacturing understanding.

## Domain-specific scientific controls

### D071 — Production Cell-Line Development
Tasks separate host selection, expression construct, clone derivation, genetic stability, productivity, product quality, adventitious-agent risk, bank governance, scale translation, and release documentation. A high titer does not establish clonality, stability, product comparability, or suitability for GMP use.

### D072 — Upstream Bioprocess Development
Tasks preserve seed-train history, media and feed provenance, viable-cell and metabolite trajectories, oxygen and carbon-dioxide transfer, osmolality, shear, contamination controls, harvest criteria, and scale-dependent uncertainty. Single-factor optimization is not treated as a substitute for multivariate process understanding.

### D073 — Bioreactor Modelling and Process Control
Tasks distinguish mechanistic, empirical, hybrid, and data-driven models; require observability and identifiability checks; and separate advisory recommendations from changes to validated control systems. Digital twins must be calibrated, versioned, challenged under disturbances, and bounded by their applicability domain.

### D074 — Media and Feed Optimization
Tasks distinguish component identity from supplier and lot effects, account for interactions and degradation, constrain designs by solubility and osmolality, and require confirmation under process-relevant scale and feeding conditions. Model-selected formulations are hypotheses until experimentally confirmed.

### D075 — Downstream Purification Development
Tasks preserve mass balance, yield, impurity clearance, resin or membrane history, residence time, pressure, pool criteria, viral-safety evidence, and product-quality effects across unit operations. Clearance claims require appropriate studies and cannot be inferred from platform precedent alone.

### D076 — Process Analytical Technology and Digital Bioprocessing
Tasks require measurement fitness, reference-method traceability, calibration maintenance, data-integrity controls, model-drift detection, cybersecurity boundaries, and explicit fallback states. A soft sensor does not replace a release method unless the approved control strategy supports that use.

### D077 — Quality by Design and Design-Space Modelling
Tasks connect quality target product profiles, critical quality attributes, material attributes, process parameters, prior knowledge, designed experiments, risk assessments, models, and control strategies. A statistically significant model is not automatically a regulatory design space or evidence of process robustness.

### D078 — Continuous and Intensified Biomanufacturing
Tasks model residence-time distributions, material genealogy, startup and shutdown, disturbances, diversion, surge capacity, integrated control, microbial control, and lot definition. Continuous operation does not eliminate batch disposition, traceability, or state-of-control requirements.

### D079 — Formulation, Stability, and Cold-Chain Engineering
Tasks separate degradation mechanisms, physical instability, container-closure interactions, extractables and leachables, shipping stress, temperature excursions, in-use stability, and shelf-life modelling. Extrapolation beyond supported conditions must produce a no-call or qualified uncertainty statement.

### D080 — Analytical Development, Lot Release, and Comparability
Tasks align analytical target profiles with method capability, orthogonality, validation, reference standards, specifications, stability indication, lifecycle monitoring, and comparability questions. Analytical similarity supports but does not by itself prove clinical equivalence, manufacturing acceptability, or regulatory approval.

## Anti-hallucination and anti-rot controls

- Guidance status, edition, jurisdiction, and retrieval date must be captured at execution time.
- Model versions, calibration sets, instrument configurations, and data transformations must be provenance-linked.
- Unknown, conflicting, censored, or out-of-domain evidence must remain explicit rather than being silently imputed as favorable.
- Regulatory and batch-release conclusions require qualified review; the agent may prepare evidence packages but may not make the legal disposition.
- Stable task goals and evidence contracts are stored locally, while volatile limits, product recipes, equipment settings, and current guidance are resolved from controlled sources at runtime.

## Controlled source register

Source status must be rechecked at runtime; the entries below were verified on **2026-08-04** and are not a substitute for jurisdiction-specific requirements.

1. ICH quality guideline index — authoritative family index for Q1–Q14: https://admin.ich.org/page/quality-guidelines
2. FDA Q5A(R2), final — viral safety evaluation for biotechnology products derived from human or animal cell lines: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q5ar2-viral-safety-evaluation-biotechnology-products-derived-cell-lines-human-or-animal-origin
3. FDA Q5B, final — analysis of expression constructs in cells producing recombinant proteins: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q5b-quality-biotechnological-products-analysis-expression-construct-cells-used-production-r-dna
4. FDA Q5D, final — derivation and characterization of production cell substrates: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q5d-quality-biotechnologicalbiological-products-derivation-and-characterization-cell-substrates-used
5. FDA Q5E, final — comparability after biotechnology manufacturing-process changes: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q5e-comparability-biotechnologicalbiological-products-subject-changes-their-manufacturing-process
6. FDA Q6B, final — tests, analytical procedures, and acceptance criteria for biological products: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q6b-specifications-test-procedures-and-acceptance-criteria-biotechnologicalbiological-products
7. FDA Q11, final — development and manufacture of drug substances: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q11-development-and-manufacture-drug-substances
8. FDA Q13, final — continuous manufacturing of drug substances and drug products: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q13-continuous-manufacturing-drug-substances-and-drug-products
9. FDA Q2(R2), final — validation of analytical procedures: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q2r2-validation-analytical-procedures
10. FDA Q14, final — analytical procedure development: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q14-analytical-procedure-development
11. FDA process validation, final — lifecycle principles and practices: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/process-validation-general-principles-and-practices
12. FDA PAT framework, final — process measurements, multivariate tools, and manufacturing control: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/pat-framework-innovative-pharmaceutical-development-manufacturing-and-quality-assurance
13. FDA Q8/Q9/Q10 Questions and Answers R5, final as posted May 2026 — implementation clarifications: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q8-q9-and-q10-questions-and-answers-r5
14. FDA comparability protocols, final — prospective assessment of postapproval CMC changes: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/comparability-protocols-postapproval-changes-chemistry-manufacturing-and-controls-information-nda
