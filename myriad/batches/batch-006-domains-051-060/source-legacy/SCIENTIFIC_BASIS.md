# Scientific Basis and Operational Boundaries — Batch 006

## Architecture principles

Batch 006 keeps durable task logic separate from volatile editor, vector, chemistry, formulation, database, and regulatory content. Each node is narrowly routable, requires explicit completion evidence, and permits the executing agent to select compatible tools at runtime rather than embedding brittle filenames, line numbers, software versions, or fixed experimental thresholds.

The attached skill-authoring essay informed four architecture choices only: progressive disclosure, routing descriptions that explain when to invoke a node, explicit goals and constraints without brittle runtime micromanagement, and regeneration from versioned sources instead of accumulating ad hoc patches. It was not used as scientific evidence.

## Genome editing

The CRISPR, base-editing, and prime-editing domains separate target definition, sequence enumeration, product-spectrum analysis, off-target nomination, empirical assay evidence, delivery exposure, and clinical interpretation. Prediction scores are treated as hypotheses requiring calibration and orthogonal confirmation. Variant-aware and haplotype-aware analyses prevent reference-only designs from being represented as universally applicable.

The regulatory baseline is FDA's final January 2024 guidance, *Human Gene Therapy Products Incorporating Human Genome Editing*. Current implementations must additionally resolve the status and version of newer documents at runtime, including FDA's April 2026 draft guidance on NGS-based genome-editing safety assessment and June 2026 draft guidance on leveraging prior knowledge. Draft documents must remain explicitly labelled draft and non-binding.

Primary scientific anchors include GUIDE-seq and later genome-wide specificity methods; current evidence also shows that off-target profiles can vary by editor and cell context, supporting the taxonomy's insistence on empirical testing in the intended system. Base-editing nodes reflect the need to model target conversion, bystanders, indels, guide-dependent DNA effects, guide-independent deaminase activity, and RNA editing separately. Prime-editing nodes preserve the distinct contributions of protospacer, primer-binding site, reverse-transcription template, editor architecture, secondary nicking, and complete product spectrum.

## Gene therapy and AAV capsids

Vector and capsid nodes distinguish vector genomes, physical particles, genome-containing particles, cellular uptake, expression, potency, biodistribution, immunogenicity, and functional benefit. Capsid enrichment in pooled selections is not treated as equivalent to human target-cell transduction, and model-organism tropism is not silently generalized to humans.

AAV engineering nodes incorporate multi-trait selection, scaffold and library leakage controls, species and route dependence, immune escape trade-offs, and manufacturability. Machine-learning proposals remain inside their measured scaffold, assay, tissue, and species applicability domains unless prospectively validated.

## RNA and oligonucleotide therapeutics

mRNA, siRNA, antisense, and programmable-RNA nodes preserve modality-specific mechanisms, chemistry, target engagement, intracellular trafficking, pharmacodynamic persistence, sequence-dependent off-targets, innate immunity, and class effects. Plasma concentration, tissue concentration, active intracellular species, molecular effect, and functional outcome remain distinct evidence layers.

The oligonucleotide domains align with FDA's final June 2024 clinical-pharmacology guidance and treat FDA's November 2024 nonclinical-safety guidance as draft. They distinguish mechanism-related pharmacology from sequence-mediated off-targets, chemistry or class effects, conjugate or carrier effects, metabolites, and impurities. mRNA nodes separate coding design, UTRs, cap, polyadenylation, modified nucleosides, double-stranded RNA impurities, translation, protein quality, and formulation.

Programmable-RNA nodes separate endogenous ADAR recruitment, engineered RNA base editors, Cas13 cleavage or recruitment, splice redirection, translation control, localization, and sensing. Evidence from one effector family, ortholog, guide architecture, or cell system is not generalized automatically to another.

## Delivery systems

Delivery nodes decompose administration into carrier distribution, payload integrity, target-cell uptake, endosomal escape, cytosolic or nuclear access, target engagement, and biological response. Composition, process, analytical, biodistribution, safety, and PK-PD evidence are linked without claiming that one surrogate proves the full delivery mechanism.

Lipid-nanoparticle and alternative-carrier nodes preserve composition–process interactions, protein-corona effects, tissue and species dependence, repeat-dose immunity, biodegradation, and active intracellular payload. Model-guided material discovery requires leakage-resistant splits, calibrated uncertainty, prospective confirmation, and independent safety assessment.

## Safety boundary

The taxonomy supports computational design, evidence management, model evaluation, quality planning, and advisory reporting. It excludes autonomous wet-lab execution, clinical administration, human germline editing, pathogen enhancement, unreviewed patient-specific treatment decisions, and claims of regulatory compliance. High-consequence designs require qualified scientific, clinical, biosafety, ethics, quality, and regulatory review.

## Versioned primary-source register

Phase 3 implementations should resolve current versions and archive retrieval dates. Stable starting points include:

- FDA, *Human Gene Therapy Products Incorporating Human Genome Editing* (final, January 2024): https://www.fda.gov/regulatory-information/search-fda-guidance-documents/human-gene-therapy-products-incorporating-human-genome-editing
- FDA, *Safety Assessment of Genome Editing in Human Gene Therapy Products Using Next-Generation Sequencing* (draft, April 2026): https://www.fda.gov/regulatory-information/search-fda-guidance-documents/safety-assessment-genome-editing-human-gene-therapy-products-using-next-generation-sequencing
- FDA, *Leveraging Prior Knowledge in the Development of Human Gene Therapy Products Incorporating Genome Editing* (draft, June 2026): https://www.fda.gov/regulatory-information/search-fda-guidance-documents/leveraging-prior-knowledge-development-human-gene-therapy-products-incorporating-genome-editing
- FDA, *Clinical Pharmacology Considerations for the Development of Oligonucleotide Therapeutics* (final, June 2024): https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-pharmacology-considerations-development-oligonucleotide-therapeutics
- FDA, *Nonclinical Safety Assessment of Oligonucleotide-Based Therapeutics* (draft, November 2024): https://www.fda.gov/regulatory-information/search-fda-guidance-documents/nonclinical-safety-assessment-oligonucleotide-based-therapeutics
- Tsai et al., GUIDE-seq, *Nature Biotechnology* (2015): https://www.nature.com/articles/nbt.3117
- Shuto et al., prime-editor structural mechanism, *Nature* (2024): https://www.nature.com/articles/s41586-024-07497-8
- Zhao et al., precision-oriented evolved base editors, *Nature Communications* (2024): https://www.nature.com/articles/s41467-024-52483-3
- Chan et al., multi-trait AAV capsid engineering, *Nature Communications* (2024): https://www.nature.com/articles/s41467-024-50555-y
- Metkar et al., therapeutic mRNA design, *Nature Reviews Drug Discovery* (2024): https://www.nature.com/articles/s41573-023-00827-x
- Tang and Khvorova, RNAi drug design, *Nature Reviews Drug Discovery* (2024): https://www.nature.com/articles/s41573-024-00912-9
- Song et al., programmable RNA base editing, *Nature Chemical Biology* (2024): https://www.nature.com/articles/s41589-023-01531-y
- Hu et al., Cas13 guide-design principles, *Nature Structural & Molecular Biology* (2024): https://www.nature.com/articles/s41594-024-01336-0
- Cullis and Hope, lipid-nanoparticle evolution for nucleic-acid delivery, *Nature Reviews Drug Discovery* (2024): https://www.nature.com/articles/s41573-024-00977-6

These sources define evidence families, not universal fixed thresholds. Every executing agent must preserve source status, retrieval date, product context, assay context, and applicability limits.
