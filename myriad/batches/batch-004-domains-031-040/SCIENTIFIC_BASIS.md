# Scientific basis and scope controls — Batch 004

Batch 004 covers therapeutic-target discovery, target validation, chemical informatics, ligand-based and structure-based virtual screening, QSAR, molecular free-energy calculations, high-throughput and phenotypic screening, and fragment/covalent discovery. Every node separates measured evidence, curated evidence, statistical inference, model prediction, and medicinal-chemistry hypothesis.

## Method anchors

- Target-identification and validation nodes separate human genetics, multi-omics, perturbation, pharmacology, tissue context, safety, tractability, clinical precedent, and causal direction rather than collapsing them into a single opaque score.
- Chemical-library and ligand-based nodes preserve source, standardized, parent, salt, tautomer, stereoisomer, and physical-sample identities; they require declared fingerprints, metrics, applicability, and benchmark splits.
- Docking nodes preserve receptor and ligand states, search-space definitions, random seeds, pose families, retrospective redocking/enrichment controls, and the distinction between docking score and experimental affinity.
- QSAR nodes follow the core validation concepts of a defined endpoint, unambiguous algorithm, applicability domain, goodness of fit, robustness, predictivity, leakage-resistant partitioning, calibration, and uncertainty.
- Free-energy nodes require explicit thermodynamic states, atom mappings, force-field provenance, independent replicas, phase-space overlap, convergence, cycle closure, and matched experimental definitions.
- HTS nodes use assay-design-aware controls, plate-map reconciliation, raw-signal retention, spatial diagnostics, multiple quality statistics, reproducible hit rules, dose-response diagnostics, and counter-screen evidence.
- Phenotypic-screen nodes preserve raw images or signals, object/profile lineage, batch correction diagnostics, replicate similarity, reference-signature context, and orthogonal causal validation.
- Fragment and covalent nodes distinguish weak binding, crystallographic density, ligand efficiency, growth-vector hypotheses, intrinsic reactivity, covalent kinetics, target occupancy, and proteome-wide selectivity.

## Operational boundaries

All tasks are bounded to computational analysis, data validation, evidence synthesis, or reporting. They do not authorize autonomous compound synthesis, biological experimentation, clinical decisions, or hazardous biological design. Predicted targets, poses, affinities, mechanisms, fragment elaborations, and covalent designs remain hypotheses until independently tested and reviewed.

## Primary references used to shape the taxonomy

- Open Targets Platform documentation for target–disease evidence categories, association scoring, and target-prioritisation factors.
- ChEMBL and RDKit documentation for curated bioactivity data, chemical representation, sanitization, stereochemistry, fingerprints, descriptors, and substructure operations.
- OECD guidance on validation of quantitative structure–activity relationship models.
- AutoDock Vina and Meeko documentation for receptor/ligand preparation, search-space definition, exhaustive search, pose export, and score comparability limits.
- OpenFE documentation for relative and absolute free-energy campaign planning, atom mappings, ligand networks, protocols, and post-simulation network analysis.
- NIH/NCATS Assay Guidance Manual for high-throughput assay validation, plate statistics, image-based screening, and confirmatory analysis.
- CellProfiler and Cell Painting resources for reproducible image segmentation, feature extraction, morphological profiling, and mechanism-of-action inference.
- wwPDB ligand-validation principles and fragment/covalent drug-discovery literature for density-supported ligand placement, ligand efficiency, covalent kinetics, and selectivity evidence.
