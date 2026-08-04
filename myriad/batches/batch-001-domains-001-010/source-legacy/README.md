# MYRIAD Phase 2 — Batch 001

This batch maps domains **001–010** into exactly **100 atomic agent tasks per domain**, for **1,000 tasks total**.

## Included domains

1. **De Novo Genome Assembly and Polishing** — `001-de-novo-genome-assembly-and-polishing/TASKS.md`
2. **Pangenome Construction and Graph Genomics** — `002-pangenome-construction-and-graph-genomics/TASKS.md`
3. **Germline Small-Variant Discovery** — `003-germline-small-variant-discovery/TASKS.md`
4. **Somatic Variant and Tumour Evolution Analysis** — `004-somatic-variant-and-tumour-evolution-analysis/TASKS.md`
5. **Structural Variant and Copy-Number Analysis** — `005-structural-variant-and-copy-number-analysis/TASKS.md`
6. **Repeat Expansion and Mobile-Element Genomics** — `006-repeat-expansion-and-mobile-element-genomics/TASKS.md`
7. **Genome Annotation and Functional Element Mapping** — `007-genome-annotation-and-functional-element-mapping/TASKS.md`
8. **Population Genomics and Genome-Wide Association Studies** — `008-population-genomics-and-genome-wide-association-studies/TASKS.md`
9. **Rare-Disease Genomic Diagnosis** — `009-rare-disease-genomic-diagnosis/TASKS.md`
10. **Clinical Variant Interpretation and Reporting** — `010-clinical-variant-interpretation-and-reporting/TASKS.md`

## Machine-readable artifacts

- `all-tasks.jsonl` — one routing-ready task object per line.
- `BATCH_MANIFEST.json` — batch state, domain list, and continuation checkpoint.
- `VALIDATION_REPORT.json` — exact-count and uniqueness validation.
- Each domain directory contains `TASKS.md`, `tasks.json`, and `tasks.jsonl`.

## Validation invariants

- Exactly 10 domains.
- Exactly 100 tasks in every domain.
- Exactly 1,000 tasks globally.
- Globally unique task IDs, kebab-case routing names, and titles.
- Ten workstreams with ten tasks each per domain.
- Computational/evidence-management boundary on every task.

## State checkpoint

Phase 2 task taxonomies are complete for domains 001–010. The next unmapped domain is **011 — Bulk RNA Sequencing and Differential Expression**. Any of domains 001–010 may now enter Phase 3 in batches of exactly ten `SKILL.md` files.
