# Scientific Basis and Controlled Source Register — Batch 009

**Domains:** 081–090  
**Source-status verification date:** 2026-08-04

## Architecture boundary

Batch 009 decomposes microbial genomics, metagenomics, pathogen surveillance, microbiome therapeutics, phage informatics, synthetic biology, metabolic engineering, cell-free systems, precision breeding, and environmental biotechnology into bounded computational and evidence-management tasks. It does not provide organism-construction recipes, pathogen-enhancement instructions, clinical dosing, environmental-release authorization, or autonomous wet-lab execution.

Computational association, sequence similarity, predicted function, ecological correlation, circuit simulation, flux prediction, genomic selection, or contaminant-removal modelling remains a hypothesis or decision-support result until supported by fit-for-purpose experimental, field, clinical, manufacturing, and regulatory evidence.

## Domain-specific controls

### 081 — Microbial genomics and antimicrobial resistance

Tasks preserve isolate provenance, taxonomic confidence, assembly and contamination quality, determinant nomenclature and database version, genotype–phenotype discordance, mobile-element context, lineage structure, and assay limitations. Detection of a resistance-associated sequence does not by itself establish expression, phenotypic resistance, transmissibility, treatment failure, or public-health action.

### 082 — Metagenomics and microbiome analysis

Tasks distinguish compositional relative abundance from absolute burden, amplicon from shotgun inference, species from strain resolution, reads from metagenome-assembled genomes, gene presence from activity, association from causation, and discovery from external validation. Batch, extraction, contamination, host DNA, depth, reference bias, and multiple testing remain explicit.

### 083 — Pathogen genomic surveillance

Tasks require declared surveillance objectives, representative sampling, laboratory and pipeline QC, versioned lineage definitions, phylogenetic uncertainty, epidemiological corroboration, privacy controls, and proportionate communication. Genomic proximity alone does not establish direct transmission, source attribution, virulence, immune escape, or policy significance.

### 084 — Microbiome therapeutics

Tasks separate product identity, strain-level characterization, ecological function, potency, manufacturing consistency, colonization, target engagement, clinical outcome, safety, and durability. A taxonomic association or in vitro phenotype does not establish therapeutic benefit.

### 085 — Bacteriophage informatics

Tasks preserve host-range evidence, lifecycle classification, genomic-safety screening, receptor and resistance context, cocktail interactions, pharmacology, manufacturing characterization, and clinical/regulatory boundaries. Computational screening does not authorize phage administration or conclude absence of undesirable biological activity.

### 086–088 — Synthetic circuits, metabolic engineering, and cell-free biology

Tasks focus on requirements, model assumptions, observability, formal verification, burden, evolutionary stability, containment, reproducibility, resource competition, batch effects, and release criteria. They intentionally stop before generating harmful constructs, unreviewed sequences, organism-modification instructions, or autonomous laboratory control.

### 089 — Agricultural genomics and precision breeding

Tasks distinguish breeding values from causal biology, account for population structure and genotype-by-environment effects, preserve pedigree and diversity, evaluate uncertainty and fairness, and require field validation and locally authorized deployment. Genomic prediction does not prove agronomic performance or biosafety.

### 090 — Environmental biotechnology and bioremediation

Tasks connect the conceptual site model to contaminants, pathways, receptors, fate, ecological effects, monitoring, remedy performance, uncertainty, community concerns, and regulatory criteria. Modelled removal does not authorize environmental release or establish cleanup completion.

## Controlled primary-source register

Volatile nomenclature, databases, guidance, taxonomies, and regulatory status must be resolved at execution time. The following sources are anchors, not frozen substitutes for current local requirements:

1. **WHO, Principles for pathogen genomic data sharing via a global platform (2025).** Official WHO publication establishing principles for responsible, equitable pathogen genomic data sharing. https://www.who.int/publications/i/item/9789240114165
2. **FDA, Early Clinical Trials With Live Biotherapeutic Products: Chemistry, Manufacturing, and Control Information (final, June 2016).** Official CMC guidance for INDs involving live biotherapeutic products. https://www.fda.gov/regulatory-information/search-fda-guidance-documents/early-clinical-trials-live-biotherapeutic-products-chemistry-manufacturing-and-control-information
3. **FDA, Bacteriophage Therapy and Live Biotherapeutic Product resources.** Official entry point for current phage and LBP materials and regulatory contacts. https://www.fda.gov/vaccines-blood-biologics/cellular-gene-therapy-products/bacteriophage-therapy
4. **NCBI Taxonomy and sequence archives.** Versioned taxonomic and sequence resources; database release, accession, assembly, and retrieval date must be captured. https://www.ncbi.nlm.nih.gov/taxonomy
5. **FAO and CGIAR genomic breeding resources.** Execution must resolve species-, jurisdiction-, and programme-specific standards rather than assuming a universal deployment rule. https://www.fao.org
6. **US EPA bioremediation and contaminated-site resources.** Site decisions remain jurisdiction-specific and require current regulator-approved criteria. https://www.epa.gov/remedytech/bioremediation

## Anti-hallucination and anti-rot controls

- Preserve database release, reference accession, taxonomy version, model version, and retrieval date.
- Do not infer phenotype, function, transmission, pathogenicity, therapeutic benefit, ecological safety, or regulatory status from sequence similarity alone.
- Keep negative evidence distinct from evidence of absence and preserve assay detection limits.
- Separate in silico nomination from experimental confirmation, field performance, clinical evidence, and authorization.
- Return `no-call` when provenance, biosafety authority, intended use, comparator, denominator, or validation evidence is inadequate.
- Regenerate volatile reference sections from controlled sources rather than patching obsolete embedded facts.
