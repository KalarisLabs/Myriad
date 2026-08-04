# Scientific basis and scope controls — Batch 003

Batch 003 covers structural biology and protein engineering. Its nodes treat predicted structures, docking poses, simulations, and designed sequences as computational hypotheses rather than experimental proof.

## Method anchors

- Protein-structure confidence nodes distinguish residue-level confidence from interdomain or interface confidence and retain predicted aligned-error information.
- Cryo-EM nodes preserve independent half-sets, unfiltered half-maps, FSC evidence, local-resolution evidence, and map–model validation artifacts.
- Crystallography nodes preserve raw images, unmerged reflections, cross-validation flags, model–data fit, stereochemistry, and ligand evidence.
- NMR nodes maintain assignments, chemical shifts, restraints, ambiguity, ensemble validation, and dynamics-model uncertainty.
- Molecular dynamics and QM/MM nodes require explicit physical models, state definitions, convergence checks, independent sampling, and uncertainty.
- Protein-design and antibody-engineering nodes include structural recapitulation, developability, novelty, provenance, and biological-risk review.

## Operational boundaries

All tasks are bounded to computational analysis, data validation, evidence synthesis, or reporting. They do not authorize autonomous wet-lab execution, synthesis, clinical interpretation, or hazardous biological design. De novo design tasks explicitly quarantine toxin, virulence, immune-evasion, pathogen-enhancement, and other harmful-function similarities for qualified review.

## Primary references used to shape the taxonomy

- AlphaFold Protein Structure Database confidence documentation for pLDDT and predicted aligned error interpretation.
- EMDB and wwPDB validation resources for cryo-EM map, half-map, model–map, X-ray, and NMR validation.
- GROMACS documentation for system preparation, simulation management, checkpointing, periodic boundaries, and reproducibility.
- HADDOCK documentation for information-driven docking with experimental restraints.
- RFdiffusion and ProteinMPNN primary publications for generative backbone and inverse-folding design workflows.
- SAbDab and Thera-SAbDab resources for antibody sequence and structural context.
