# MYRIAD Phase 2 — Batch 009

This batch maps domains **081–090** into exactly **100 atomic agent tasks per domain**, for **1,000 tasks total**.

## Included domains

1. **Microbial Genomics and Antimicrobial Resistance Analysis** — `081-microbial-genomics-and-antimicrobial-resistance-analysis/TASKS.md`
2. **Metagenomics and Microbiome Analysis** — `082-metagenomics-and-microbiome-analysis/TASKS.md`
3. **Pathogen Genomic Surveillance** — `083-pathogen-genomic-surveillance/TASKS.md`
4. **Microbiome Therapeutic Development** — `084-microbiome-therapeutic-development/TASKS.md`
5. **Bacteriophage Discovery and Therapy Informatics** — `085-bacteriophage-discovery-and-therapy-informatics/TASKS.md`
6. **Synthetic Gene-Circuit Engineering** — `086-synthetic-gene-circuit-engineering/TASKS.md`
7. **Metabolic Pathway and Strain Engineering** — `087-metabolic-pathway-and-strain-engineering/TASKS.md`
8. **Cell-Free Synthetic Biology** — `088-cell-free-synthetic-biology/TASKS.md`
9. **Agricultural Genomics and Precision Breeding** — `089-agricultural-genomics-and-precision-breeding/TASKS.md`
10. **Environmental Biotechnology and Bioremediation** — `090-environmental-biotechnology-and-bioremediation/TASKS.md`

## Machine-readable artifacts

- `all-tasks.jsonl` — one routing-ready task object per line.
- `BATCH_MANIFEST.json` — batch state, domain list, and continuation checkpoint.
- `VALIDATION_REPORT.json` — exact-count, naming, workstream, specificity, and cross-batch uniqueness validation.
- `CHECKSUMS.json` — SHA-256 checksums for batch artifacts.
- Each domain directory contains `TASKS.md`, `tasks.json`, and `tasks.jsonl`.

## Validation invariants

- Exactly 10 domains, 100 tasks per domain, and 1,000 tasks globally.
- Exactly ten workstreams with ten tasks each per domain.
- Unique task IDs, routing names, and titles within Batch 009 and across all prior batches.
- At least ten words per routing title and at least thirty-five words per executable objective.
- Explicit execution boundaries and five completion-evidence requirements on every node.
- No placeholders, sample stubs, generic titles, silent imputation, or unsupported automatic decisions.

## Agent-skill architecture improvements

- Routing titles state the bounded operation and domain/workstream invocation context.
- Dense objectives carry the inputs, method intent, uncertainty, failure, controls, artifact, and no-call logic.
- Domain files and workstreams support progressive disclosure instead of loading all 1,000 nodes at once.
- Durable decision logic is separated from changing databases, models, standards, software, and guidance.
- Every task requires machine-readable status, provenance, versioning, errors, and qualified-review flags.
- Tasks are retained only when inputs, a repeatable operation, and a reviewable stopping condition are definable.

## State checkpoint

Phase 2 taxonomies are complete for domains 001–090. The next unmapped domain is **091 — Clinical Trial Design and Biostatistics**.
