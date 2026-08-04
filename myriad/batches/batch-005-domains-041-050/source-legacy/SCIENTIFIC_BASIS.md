# Scientific Basis and Architecture Controls — Batch 005

## Scope

Batch 005 covers medicinal-chemistry optimization, ADME prediction, DMPK, PK–PD, QSP, nonclinical safety, biomarkers, molecular diagnostics, companion diagnostics, and pharmacogenomics. The task nodes are computational and evidence-management primitives. They do not replace qualified laboratory, medical, statistical, regulatory, or prescribing judgment.

## Agent-skill architecture improvement

The user-supplied PostHog essay, “What nobody tells you about writing agent skills” (Ian Vanagas, 3 August 2026), was used as an architecture heuristic rather than as a scientific source. Batch 005 applies its core lessons by:

- writing routing names and objectives around when a node should be invoked;
- giving each node a precise done condition, operational boundary, and required evidence;
- keeping the task node durable while routing volatile guidelines, labels, allele definitions, physiological libraries, and databases through versioned provenance;
- avoiding brittle file paths, line numbers, fixed tool lists, and runtime-specific assumptions;
- excluding broad work that does not have a repeatable input, bounded operation, or reviewable stopping condition.

## Authoritative scientific and regulatory anchors

The taxonomy was cross-checked against the following maintained primary sources, accessed 4 August 2026:

1. FDA, ICH M12 Drug Interaction Studies — harmonized design, conduct, and interpretation of enzyme- and transporter-mediated in vitro and clinical interaction studies.
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m12-drug-interaction-studies
2. FDA, Population Pharmacokinetics, February 2022 — study design, model evaluation, reporting, and regulatory use of population PK analyses.
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/population-pharmacokinetics
3. FDA, Physiologically Based Pharmacokinetic Analyses — Format and Content — submission structure, model qualification, and documentation expectations.
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/physiologically-based-pharmacokinetic-analyses-format-and-content-guidance-industry
4. FDA, Exposure–Response Relationships — Study Design, Data Analysis, and Regulatory Applications — use of exposure–response evidence in dose selection and regulatory decisions.
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/exposure-response-relationships-study-design-data-analysis-and-regulatory-applications
5. FDA, ICH M10 Bioanalytical Method Validation and Study Sample Analysis — validation and study-sample analysis for chromatographic and ligand-binding assays.
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/m10-bioanalytical-method-validation-and-study-sample-analysis
6. ICH Safety Guidelines — S1 carcinogenicity, S2 genotoxicity, S3 toxicokinetics, S5 reproductive toxicity, S7 safety pharmacology, S8 immunotoxicity, S9 oncology, S10 photosafety, S11 paediatric safety, S12 gene-therapy biodistribution, and S13 oligonucleotide safety.
   https://www.ich.org/page/safety-guidelines
7. FDA Biomarker Qualification Program and BEST resources — biomarker categories, context of use, qualification evidence, and submission resources.
   https://www.fda.gov/drugs/biomarker-qualification-program/general-biomarker-information
8. FDA, ICH Q2(R2) Validation of Analytical Procedures and Q14 Analytical Procedure Development — analytical performance, lifecycle, science-based development, and change management.
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q2r2-validation-analytical-procedures
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/q14-analytical-procedure-development
9. FDA, In Vitro Companion Diagnostic Devices and oncology class-labelling guidance — co-development, intended use, contemporaneous review, and supported labelling boundaries.
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/in-vitro-companion-diagnostic-devices
   https://www.fda.gov/regulatory-information/search-fda-guidance-documents/developing-and-labeling-in-vitro-companion-diagnostic-devices-specific-group-oncology-therapeutic
10. ICH E15 and E16 — definitions for genomic biomarkers and pharmacogenomics, and qualification submissions for biomarkers used in drug development.
    https://www.ich.org/page/efficacy-guidelines
11. FDA Table of Pharmacogenomic Biomarkers in Drug Labeling — current examples of biomarker information and actions represented in US labels.
    https://www.fda.gov/drugs/science-and-research-drugs/table-pharmacogenomic-biomarkers-drug-labeling
12. Clinical Pharmacogenetics Implementation Consortium (CPIC) guidelines — standardized genotype-to-phenotype and prescribing recommendations for use when genetic results are already available.
    https://cpicpgx.org/guidelines/

## Truth and scope controls

- Model predictions, structural alerts, database annotations, and literature-derived associations are not represented as experimental proof.
- A negative computational prediction is never treated as evidence that a compound, assay, or patient is safe.
- Regulatory guidance is jurisdiction-, date-, product-, and context-dependent; the taxonomy requires versioned sources and qualified review.
- Diagnostic and pharmacogenomic nodes generate decision support and evidence packages, not autonomous diagnoses, prescriptions, dose changes, or patient management.
- QSP, PBPK, PK–PD, and predictive-toxicology models require declared contexts of use, applicability boundaries, uncertainty analysis, and independent evaluation.
