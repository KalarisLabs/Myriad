# MYRIAD Phase 2 — Batch 007

This batch maps domains **061–070** into exactly **100 atomic agent tasks per domain**, for **1,000 tasks total**.

## Included domains

1. **Monoclonal Antibody Discovery** — `061-monoclonal-antibody-discovery/TASKS.md`
2. **Bispecific and Multispecific Antibody Engineering** — `062-bispecific-and-multispecific-antibody-engineering/TASKS.md`
3. **Antibody–Drug Conjugate Design** — `063-antibodydrug-conjugate-design/TASKS.md`
4. **Therapeutic Protein and Enzyme Engineering** — `064-therapeutic-protein-and-enzyme-engineering/TASKS.md`
5. **Targeted Protein Degradation** — `065-targeted-protein-degradation/TASKS.md`
6. **Vaccine Antigen and Immunogen Design** — `066-vaccine-antigen-and-immunogen-design/TASKS.md`
7. **Immunoinformatics and Epitope Prediction** — `067-immunoinformatics-and-epitope-prediction/TASKS.md`
8. **Biologic Immunogenicity Risk Assessment** — `068-biologic-immunogenicity-risk-assessment/TASKS.md`
9. **Engineered Immune-Cell Therapy** — `069-engineered-immune-cell-therapy/TASKS.md`
10. **Organoid, Organ-on-Chip, and Advanced Disease Models** — `070-organoid-organ-on-chip-and-advanced-disease-models/TASKS.md`

## Machine-readable artifacts

- `all-tasks.jsonl` — one routing-ready task object per line.
- `BATCH_MANIFEST.json` — batch state, domain list, and continuation checkpoint.
- `VALIDATION_REPORT.json` — exact-count, naming, workstream, specificity, and cross-batch uniqueness validation.
- `CHECKSUMS.json` — SHA-256 checksums for batch artifacts.
- Each domain directory contains `TASKS.md`, `tasks.json`, and `tasks.jsonl`.

## Validation invariants

- Exactly 10 domains, 100 tasks per domain, and 1,000 tasks globally.
- Exactly ten workstreams with ten tasks each per domain.
- Unique task IDs, routing names, and titles within Batch 007 and across Batches 001–006.
- Explicit execution boundaries and five completion-evidence requirements on every node.
- No placeholders, sample stubs, generic titles, or titles shorter than eight words.
- Computational nomination, experimental evidence, clinical decisions, and regulatory conclusions remain separated.

## Agent-skill architecture improvements

- Routing names state the bounded operation and invocation context.
- Domain files and workstreams support progressive disclosure instead of loading all 1,000 nodes at once.
- Durable task logic is separated from changing assays, databases, model versions, standards, and guidance.
- Every task requires machine-readable status, provenance, versioning, errors, and review flags.
- Tasks are retained only when inputs, a repeatable operation, and a reviewable stopping condition are definable.

## State checkpoint

Phase 2 taxonomies are complete for domains 001–070. The next unmapped domain is **071 — Production Cell-Line Development**. Domains 001–070 may enter Phase 3 in batches of exactly ten `SKILL.md` files.
