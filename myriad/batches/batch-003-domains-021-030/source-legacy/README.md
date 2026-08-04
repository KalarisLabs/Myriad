# MYRIAD Phase 2 — Batch 003

This batch maps domains **021–030** into exactly **100 atomic agent tasks per domain**, for **1,000 tasks total**.

## Included domains

1. **Protein Structure Prediction and Confidence Assessment** — `021-protein-structure-prediction-and-confidence-assessment/TASKS.md`
2. **Cryogenic Electron Microscopy Data Processing** — `022-cryogenic-electron-microscopy-data-processing/TASKS.md`
3. **X-Ray Crystallography Informatics** — `023-x-ray-crystallography-informatics/TASKS.md`
4. **Biomolecular NMR Structure Analysis** — `024-biomolecular-nmr-structure-analysis/TASKS.md`
5. **Atomistic Molecular Dynamics Simulation** — `025-atomistic-molecular-dynamics-simulation/TASKS.md`
6. **Quantum Mechanics and QM/MM Modelling** — `026-quantum-mechanics-and-qm-mm-modelling/TASKS.md`
7. **Protein Stability and Folding Engineering** — `027-protein-stability-and-folding-engineering/TASKS.md`
8. **Protein–Protein Interaction Modelling** — `028-protein-protein-interaction-modelling/TASKS.md`
9. **De Novo Protein and Peptide Design** — `029-de-novo-protein-and-peptide-design/TASKS.md`
10. **Antibody Structure and Sequence Engineering** — `030-antibody-structure-and-sequence-engineering/TASKS.md`

## Machine-readable artifacts

- `all-tasks.jsonl` — one routing-ready task object per line.
- `BATCH_MANIFEST.json` — batch state, domain list, and continuation checkpoint.
- `VALIDATION_REPORT.json` — exact-count, naming, workstream, and uniqueness validation.
- `CHECKSUMS.json` — SHA-256 checksums for batch artifacts.
- Each domain directory contains `TASKS.md`, `tasks.json`, and `tasks.jsonl`.

## Validation invariants

- Exactly 10 domains.
- Exactly 100 tasks in every domain.
- Exactly 1,000 tasks globally.
- Globally unique task IDs, kebab-case routing names, and titles within this batch and across Batches 001–002.
- Ten workstreams with ten tasks each per domain.
- Computational/evidence-management and safety boundary on every task.

## State checkpoint

Phase 2 taxonomies are complete for domains 001–030. The next unmapped domain is **031 — Therapeutic Target Identification**. Domains 001–030 may enter Phase 3 in batches of exactly ten `SKILL.md` files.
