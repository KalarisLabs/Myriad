# MYRIAD Phase 2 — Batch 002

This batch maps domains **011–020** into exactly **100 atomic agent tasks per domain**, for **1,000 tasks total**.

## Included domains

1. **Bulk RNA Sequencing and Differential Expression** — `011-bulk-rna-sequencing-and-differential-expression/TASKS.md`
2. **Alternative Splicing and Isoform Analysis** — `012-alternative-splicing-and-isoform-analysis/TASKS.md`
3. **Single-Cell Transcriptomics** — `013-single-cell-transcriptomics/TASKS.md`
4. **Spatial Transcriptomics** — `014-spatial-transcriptomics/TASKS.md`
5. **Epigenomic Profiling** — `015-epigenomic-profiling/TASKS.md`
6. **Single-Cell and Spatial Epigenomics** — `016-single-cell-and-spatial-epigenomics/TASKS.md`
7. **Proteomics and Protein Quantification** — `017-proteomics-and-protein-quantification/TASKS.md`
8. **Post-Translational Modification Proteomics** — `018-post-translational-modification-proteomics/TASKS.md`
9. **Metabolomics and Lipidomics** — `019-metabolomics-and-lipidomics/TASKS.md`
10. **Multi-Omics Integration and Systems Biology** — `020-multi-omics-integration-and-systems-biology/TASKS.md`

## Machine-readable artifacts

- `all-tasks.jsonl` — one routing-ready task object per line.
- `BATCH_MANIFEST.json` — batch state, domain list, and continuation checkpoint.
- `VALIDATION_REPORT.json` — exact-count, naming, workstream, and uniqueness validation.
- Each domain directory contains `TASKS.md`, `tasks.json`, and `tasks.jsonl`.

## Validation invariants

- Exactly 10 domains.
- Exactly 100 tasks in every domain.
- Exactly 1,000 tasks globally.
- Globally unique task IDs, kebab-case routing names, and titles within this batch and across Batch 001.
- Ten workstreams with ten tasks each per domain.
- Computational/evidence-management boundary on every task.

## State checkpoint

Phase 2 taxonomies are complete for domains 001–020. The next unmapped domain is **021 — Protein Structure Prediction and Confidence Assessment**. Domains 001–020 may enter Phase 3 in batches of exactly ten `SKILL.md` files.
