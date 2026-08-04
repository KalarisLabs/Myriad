# MYRIAD Phase 2 — Batch 004

This batch maps domains **031–040** into exactly **100 atomic agent tasks per domain**, for **1,000 tasks total**.

## Included domains

1. **Therapeutic Target Identification** — `031-therapeutic-target-identification/TASKS.md`
2. **Target Validation and Causal Evidence Assessment** — `032-target-validation-and-causal-evidence-assessment/TASKS.md`
3. **Chemical Library Curation and Standardization** — `033-chemical-library-curation-and-standardization/TASKS.md`
4. **Ligand-Based Virtual Screening and Similarity Search** — `034-ligand-based-virtual-screening-and-similarity-search/TASKS.md`
5. **Protein–Ligand Docking and Pose Evaluation** — `035-protein-ligand-docking-and-pose-evaluation/TASKS.md`
6. **Quantitative Structure–Activity Relationship Modelling** — `036-quantitative-structure-activity-relationship-modelling/TASKS.md`
7. **Free-Energy and Binding-Affinity Prediction** — `037-free-energy-and-binding-affinity-prediction/TASKS.md`
8. **High-Throughput Screening Informatics** — `038-high-throughput-screening-informatics/TASKS.md`
9. **Phenotypic Screening and Mechanism-of-Action Inference** — `039-phenotypic-screening-and-mechanism-of-action-inference/TASKS.md`
10. **Fragment-Based and Covalent Drug Discovery** — `040-fragment-based-and-covalent-drug-discovery/TASKS.md`

## Machine-readable artifacts

- `all-tasks.jsonl` — one routing-ready task object per line.
- `BATCH_MANIFEST.json` — batch state, domain list, and continuation checkpoint.
- `VALIDATION_REPORT.json` — exact-count, naming, workstream, atomicity, and uniqueness validation.
- `CHECKSUMS.json` — SHA-256 checksums for batch artifacts.
- Each domain directory contains `TASKS.md`, `tasks.json`, and `tasks.jsonl`.

## Validation invariants

- Exactly 10 domains.
- Exactly 100 tasks in every domain.
- Exactly 1,000 tasks globally.
- Globally unique task IDs, kebab-case routing names, and titles within this batch and across Batches 001–003.
- Ten workstreams with ten tasks each per domain.
- Explicit computational/evidence-management boundary and completion evidence on every task.
- Reject generic or non-atomic task titles through lexical and structural quality checks.

## State checkpoint

Phase 2 taxonomies are complete for domains 001–040. The next unmapped domain is **041 — Multi-Parameter Medicinal Chemistry Optimization**. Domains 001–040 may enter Phase 3 in batches of exactly ten `SKILL.md` files.
