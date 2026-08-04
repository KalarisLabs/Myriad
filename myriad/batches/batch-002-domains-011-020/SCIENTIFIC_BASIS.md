# Scientific Basis — MYRIAD Phase 2 Batch 002

This batch defines computational task nodes, not laboratory protocols or autonomous clinical decision systems. Thresholds and tools are intentionally represented as configurable, versioned inputs because suitable values depend on assay chemistry, organism, matrix, design, and validated local procedures.

## Domain foundations

- **Bulk RNA-seq:** count-based design, normalization, dispersion modelling, contrasts, effect sizes, and multiple-testing controls are aligned with Bioconductor DESeq2 guidance and community RNA-seq workflows.
- **Alternative splicing:** event-, exon-, junction-, transcript-, and long-read isoform tasks distinguish quantification resolution and preserve coverage/no-call gates consistent with rMATS and nf-core/rnasplice concepts.
- **Single-cell transcriptomics:** cell calling, ambient RNA, doublets, sample-aware QC, latent representation, clustering, annotation, pseudobulk inference, trajectories, and integration follow established Bioconductor single-cell analysis principles.
- **Spatial transcriptomics:** tasks preserve image-coordinate transforms, segmentation provenance, location-level QC, deconvolution uncertainty, specimen-level replication, and spatial-null assumptions; platform preprocessing concepts are aligned with current Space Ranger documentation.
- **Bulk epigenomics:** ATAC-seq and ChIP-seq tasks include assay-specific enrichment, library complexity, replicate concordance, blacklist, peak, consensus, and differential-region controls reflected in ENCODE data standards.
- **Single-cell epigenomics:** fragment QC, TSS enrichment, LSI, cluster-aware peaks, motif deviation, pseudobulk testing, and paired multiome integration reflect Signac and ArchR analysis frameworks.
- **Proteomics:** spectrum, peptide, protein-group, quantification, FDR, and interoperability tasks use HUPO Proteomics Standards Initiative concepts including mzML, mzIdentML, mzTab, mzQC, and controlled vocabularies.
- **PTM proteomics:** tasks distinguish peptidoform identification, site localization, site-level confidence, PTM-class evidence, protein normalization, and ProForma-compatible representation.
- **Metabolomics and lipidomics:** tasks separate feature detection from compound identification, preserve blank/QC/drift gates, distinguish structural confidence levels, and reflect Metabolomics Standards Initiative and Lipidomics Standards Initiative reporting concepts.
- **Multi-omics:** tasks require sample linkage, modality-specific QC, leakage-safe preprocessing, mapping provenance, external validation, ablation, uncertainty, and assumption-bounded causal interpretation; latent-factor nodes include MOFA-style multi-view modelling.

## Reference sources

1. Bioconductor DESeq2 vignette: https://bioconductor.org/packages/DESeq2/
2. nf-core/rnaseq: https://nf-co.re/rnaseq/
3. nf-core/rnasplice: https://nf-co.re/rnasplice/
4. Orchestrating Single-Cell Analysis with Bioconductor: https://bioconductor.org/books/
5. 10x Genomics Space Ranger: https://www.10xgenomics.com/support/software/space-ranger/latest
6. ENCODE data standards: https://www.encodeproject.org/data-standards/
7. Signac: https://stuartlab.org/signac/
8. ArchR: https://www.archrproject.com/
9. HUPO Proteomics Standards Initiative: https://hupo.org/Proteomics-Standards-Initiative-%28PSI%29
10. mzIdentML specification: https://hupo-psi.github.io/mzIdentML/
11. Lipidomics Standards Initiative: https://lipidomicstandards.org/
12. MOFA2 documentation: https://biofam.github.io/MOFA2/
