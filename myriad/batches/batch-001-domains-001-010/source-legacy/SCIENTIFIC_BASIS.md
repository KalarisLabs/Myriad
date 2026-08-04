# Scientific and Standards Basis

This Phase 2 taxonomy is original work. It is organized to remain compatible with widely used primary standards and current authoritative workflow guidance while avoiding tool-specific lock-in at the taxonomy layer.

## Primary anchors

- Broad Institute GATK Best Practices for preprocessing, germline short-variant discovery, somatic short-variant discovery, and somatic copy-number analysis.
- ClinGen Variant Classification Guidance and the ClinGen variant-curation standard operating procedures for transparent evidence evaluation and ACMG/AMP criterion use.
- ACMG/AMP five-tier sequence-variant interpretation framework, with gene-specific specifications applied only when explicitly available.
- SAM/BAM/CRAM and VCF/BCF specifications maintained by the Global Alliance for Genomics and Health / samtools hts-specs community.
- NHGRI Human Genome Reference Program and Human Pangenome Reference Consortium concepts for diverse assemblies, graph references, coordinate systems, and bias evaluation.

## Design rules applied

1. Taxonomy nodes are atomic: each node performs one bounded operation and stops before downstream execution.
2. Every node requires machine-readable outputs, an explicit disposition, provenance, and review flags.
3. Reference build, transcript, resource, tool, model, and policy versions are treated as mandatory inputs or provenance.
4. Clinical nodes remain decision-support steps and require qualified human review before diagnostic release.
5. Low-confidence, technically unsupported, or model-inapplicable states fail closed or emit a no-call/review status.
6. Imported database assertions are not treated as independent primary evidence without source-level review.
7. Population, ancestry, sex chromosome, ploidy, assay, and genomic-context limitations are represented explicitly.

## Date boundary

Scientific-basis review completed for this batch on 2026-08-03. Phase 3 `SKILL.md` generation must pin the exact tool, resource, schema, and policy versions selected for each task at implementation time.
