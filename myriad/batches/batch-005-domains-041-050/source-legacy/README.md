# MYRIAD Phase 2 — Batch 005

This batch maps domains **041–050** into exactly **100 atomic agent tasks per domain**, for **1,000 tasks total**.

## Included domains

1. **Multi-Parameter Medicinal Chemistry Optimization** — `041-multi-parameter-medicinal-chemistry-optimization/TASKS.md`
2. **Absorption, Distribution, Metabolism, and Excretion Prediction** — `042-absorption-distribution-metabolism-and-excretion-prediction/TASKS.md`
3. **Drug Metabolism and Pharmacokinetics Analysis** — `043-drug-metabolism-and-pharmacokinetics-analysis/TASKS.md`
4. **Pharmacokinetic–Pharmacodynamic Modelling** — `044-pharmacokinetic-pharmacodynamic-modelling/TASKS.md`
5. **Quantitative Systems Pharmacology** — `045-quantitative-systems-pharmacology/TASKS.md`
6. **Preclinical Safety and Predictive Toxicology** — `046-preclinical-safety-and-predictive-toxicology/TASKS.md`
7. **Biomarker Discovery and Qualification** — `047-biomarker-discovery-and-qualification/TASKS.md`
8. **Molecular Diagnostics and Assay Interpretation** — `048-molecular-diagnostics-and-assay-interpretation/TASKS.md`
9. **Companion Diagnostic Co-Development** — `049-companion-diagnostic-co-development/TASKS.md`
10. **Pharmacogenomics and Precision Dosing** — `050-pharmacogenomics-and-precision-dosing/TASKS.md`

## Machine-readable artifacts

- `all-tasks.jsonl` — one routing-ready task object per line.
- `BATCH_MANIFEST.json` — batch state, domain list, and continuation checkpoint.
- `VALIDATION_REPORT.json` — exact-count, naming, workstream, atomicity, specificity, and cross-batch uniqueness validation.
- `CHECKSUMS.json` — SHA-256 checksums for batch artifacts.
- Each domain directory contains `TASKS.md`, `tasks.json`, and `tasks.jsonl`.

## Validation invariants

- Exactly 10 domains.
- Exactly 100 tasks in every domain.
- Exactly 1,000 tasks globally.
- Globally unique task IDs, kebab-case routing names, and titles within this batch and across Batches 001–004.
- Ten workstreams with ten tasks each per domain.
- Explicit computational/evidence-management boundary and completion evidence on every task.
- No placeholders, samples, generic task stubs, or titles shorter than eight words.
- Durable task logic is separated from volatile guideline, label, database, and physiological content.

## State checkpoint

Phase 2 taxonomies are complete for domains 001–050. The next unmapped domain is **051 — CRISPR Guide Design and Off-Target Assessment**. Domains 001–050 may enter Phase 3 in batches of exactly ten `SKILL.md` files.
