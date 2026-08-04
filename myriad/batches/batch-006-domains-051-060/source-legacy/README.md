# MYRIAD Phase 2 — Batch 006

This batch maps domains **051–060** into exactly **100 atomic agent tasks per domain**, for **1,000 tasks total**.

## Included domains

1. **CRISPR Guide Design and Off-Target Assessment** — `051-crispr-guide-design-and-off-target-assessment/TASKS.md`
2. **Base-Editing System Design** — `052-base-editing-system-design/TASKS.md`
3. **Prime-Editing System Design** — `053-prime-editing-system-design/TASKS.md`
4. **Gene-Therapy Vector and Payload Engineering** — `054-gene-therapy-vector-and-payload-engineering/TASKS.md`
5. **Adeno-Associated Virus Capsid Informatics** — `055-adeno-associated-virus-capsid-informatics/TASKS.md`
6. **Messenger RNA Therapeutic Design** — `056-messenger-rna-therapeutic-design/TASKS.md`
7. **Small-Interfering RNA Therapeutic Design** — `057-small-interfering-rna-therapeutic-design/TASKS.md`
8. **Antisense Oligonucleotide Design** — `058-antisense-oligonucleotide-design/TASKS.md`
9. **RNA Editing and Programmable RNA Therapeutics** — `059-rna-editing-and-programmable-rna-therapeutics/TASKS.md`
10. **Nucleic-Acid Delivery-System Engineering** — `060-nucleic-acid-delivery-system-engineering/TASKS.md`

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
- Globally unique task IDs, kebab-case routing names, and titles within this batch and across Batches 001–005.
- Ten workstreams with ten tasks each per domain.
- Explicit computational/evidence-management boundary and completion evidence on every task.
- No placeholders, samples, generic task stubs, or titles shorter than eight words.
- Durable task logic is separated from volatile guideline, database, editor, vector, chemistry, and delivery-platform content.

## Agent-skill architecture improvements

- Routing names and titles state when a node is useful and what bounded decision artifact it must produce.
- Tasks specify goals, constraints, evidence, and stopping conditions without hard-coding brittle runtime paths or tool versions.
- Volatile scientific details are referenced through versioned source manifests so future Phase 3 skills can disclose them progressively.
- Every task requires machine-readable output, explicit status, provenance, versioning, and review flags.

## State checkpoint

Phase 2 taxonomies are complete for domains 001–060. The next unmapped domain is **061 — Monoclonal Antibody Discovery**. Domains 001–060 may enter Phase 3 in batches of exactly ten `SKILL.md` files.
