# D021 — Protein Structure Prediction and Confidence Assessment

Batch **003** · 10 workstreams · 100 tasks

## 01. Sequence intake and modelling scope

### MYR-D021-T001 — Validate amino-acid sequence syntax, alphabet, length, chain breaks, and noncanonical residue declarations

Validate amino-acid sequence syntax, alphabet, length, chain breaks, and noncanonical residue declarations.

- **Routing name:** `validate-amino-acid-sequence-syntax-alphabet-length-chain-breaks-and-noncanonical-residue-declarations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T002 — Reconcile construct sequence with canonical isoforms, signal peptides, tags, mutations, and unresolved termini

Reconcile construct sequence with canonical isoforms, signal peptides, tags, mutations, and unresolved termini.

- **Routing name:** `reconcile-construct-sequence-with-canonical-isoforms-signal-peptides-tags-mutations-and-unresolved-termini`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T003 — Detect low-complexity segments, coiled coils, transmembrane spans, repeats, and intrinsically disordered regions before modelling

Detect low-complexity segments, coiled coils, transmembrane spans, repeats, and intrinsically disordered regions before modelling.

- **Routing name:** `detect-low-complexity-segments-coiled-coils-transmembrane-spans-repeats-and-intrinsically-disordered-regions-before-modelling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T004 — Define whether the target is a monomer, obligate oligomer, transient complex, membrane protein, or multidomain assembly

Define whether the target is a monomer, obligate oligomer, transient complex, membrane protein, or multidomain assembly.

- **Routing name:** `define-whether-the-target-is-a-monomer-obligate-oligomer-transient-complex-membrane-protein-or-multidomain-assembly`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T005 — Specify required biological state, species, compartment, cofactors, ligands, and post-translational modifications

Specify required biological state, species, compartment, cofactors, ligands, and post-translational modifications.

- **Routing name:** `specify-required-biological-state-species-compartment-cofactors-ligands-and-post-translational-modifications`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T006 — Partition very long or multidomain sequences only when domain boundaries have independent structural support

Partition very long or multidomain sequences only when domain boundaries have independent structural support.

- **Routing name:** `partition-very-long-or-multidomain-sequences-only-when-domain-boundaries-have-independent-structural-support`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T007 — Identify sequence regions lacking sufficient evolutionary or template information and mark them as high-risk modelling zones

Identify sequence regions lacking sufficient evolutionary or template information and mark them as high-risk modelling zones.

- **Routing name:** `identify-sequence-regions-lacking-sufficient-evolutionary-or-template-information-and-mark-them-as-high-risk-modelling-zones`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T008 — Freeze residue numbering, chain identifiers, construct boundaries, and reference sequence checksums in the run manifest

Freeze residue numbering, chain identifiers, construct boundaries, and reference sequence checksums in the run manifest.

- **Routing name:** `freeze-residue-numbering-chain-identifiers-construct-boundaries-and-reference-sequence-checksums-in-the-run-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T009 — Estimate compute, memory, database, and model-ensemble requirements from sequence length and assembly size

Estimate compute, memory, database, and model-ensemble requirements from sequence length and assembly size.

- **Routing name:** `estimate-compute-memory-database-and-model-ensemble-requirements-from-sequence-length-and-assembly-size`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T010 — Reject structure-prediction requests whose biological sequence identity or intended molecular state is unresolved

Reject structure-prediction requests whose biological sequence identity or intended molecular state is unresolved.

- **Routing name:** `reject-structure-prediction-requests-whose-biological-sequence-identity-or-intended-molecular-state-is-unresolved`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Evolutionary evidence and template search

### MYR-D021-T011 — Generate a reproducible multiple-sequence alignment with explicit database versions and search sensitivity

Generate a reproducible multiple-sequence alignment with explicit database versions and search sensitivity.

- **Routing name:** `generate-a-reproducible-multiple-sequence-alignment-with-explicit-database-versions-and-search-sensitivity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T012 — Quantify alignment depth, effective sequence count, taxonomic diversity, coverage, and gap distribution by residue

Quantify alignment depth, effective sequence count, taxonomic diversity, coverage, and gap distribution by residue.

- **Routing name:** `quantify-alignment-depth-effective-sequence-count-taxonomic-diversity-coverage-and-gap-distribution-by-residue`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T013 — Detect paralog mixing, fragment contamination, artificial fusions, and taxonomically implausible homologs in the alignment

Detect paralog mixing, fragment contamination, artificial fusions, and taxonomically implausible homologs in the alignment.

- **Routing name:** `detect-paralog-mixing-fragment-contamination-artificial-fusions-and-taxonomically-implausible-homologs-in-the-alignment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T014 — Construct paired alignments for complexes only when pairing evidence and organismal provenance are defensible

Construct paired alignments for complexes only when pairing evidence and organismal provenance are defensible.

- **Routing name:** `construct-paired-alignments-for-complexes-only-when-pairing-evidence-and-organismal-provenance-are-defensible`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T015 — Search experimental structure databases for homologous templates using sequence and profile methods

Search experimental structure databases for homologous templates using sequence and profile methods.

- **Routing name:** `search-experimental-structure-databases-for-homologous-templates-using-sequence-and-profile-methods`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T016 — Rank templates by identity, coverage, experimental method, resolution, biological assembly, ligand state, and mutation burden

Rank templates by identity, coverage, experimental method, resolution, biological assembly, ligand state, and mutation burden.

- **Routing name:** `rank-templates-by-identity-coverage-experimental-method-resolution-biological-assembly-ligand-state-and-mutation-burden`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T017 — Identify template conflicts that imply alternate conformations, domain orientations, or oligomeric states

Identify template conflicts that imply alternate conformations, domain orientations, or oligomeric states.

- **Routing name:** `identify-template-conflicts-that-imply-alternate-conformations-domain-orientations-or-oligomeric-states`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T018 — Declare template-date cutoffs and remove post-cutoff structures for prospective benchmark runs

Declare template-date cutoffs and remove post-cutoff structures for prospective benchmark runs.

- **Routing name:** `declare-template-date-cutoffs-and-remove-post-cutoff-structures-for-prospective-benchmark-runs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T019 — Build template-free and template-assisted model branches when template influence could materially change conclusions

Build template-free and template-assisted model branches when template influence could materially change conclusions.

- **Routing name:** `build-template-free-and-template-assisted-model-branches-when-template-influence-could-materially-change-conclusions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T020 — Archive alignment, template hits, exclusions, and pairing decisions as immutable modelling inputs

Archive alignment, template hits, exclusions, and pairing decisions as immutable modelling inputs.

- **Routing name:** `archive-alignment-template-hits-exclusions-and-pairing-decisions-as-immutable-modelling-inputs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Model generation and ensemble construction

### MYR-D021-T021 — Generate multiple independent structure predictions with recorded random seeds and model weights

Generate multiple independent structure predictions with recorded random seeds and model weights.

- **Routing name:** `generate-multiple-independent-structure-predictions-with-recorded-random-seeds-and-model-weights`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T022 — Preserve unrelaxed and relaxed coordinates separately for every generated model

Preserve unrelaxed and relaxed coordinates separately for every generated model.

- **Routing name:** `preserve-unrelaxed-and-relaxed-coordinates-separately-for-every-generated-model`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T023 — Run at least one structurally distinct prediction method when conclusions depend on uncertain regions

Run at least one structurally distinct prediction method when conclusions depend on uncertain regions.

- **Routing name:** `run-at-least-one-structurally-distinct-prediction-method-when-conclusions-depend-on-uncertain-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T024 — Generate alternative domain assemblies when interdomain confidence is weak despite high local confidence

Generate alternative domain assemblies when interdomain confidence is weak despite high local confidence.

- **Routing name:** `generate-alternative-domain-assemblies-when-interdomain-confidence-is-weak-despite-high-local-confidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T025 — Generate multimer predictions across plausible stoichiometries without assuming the largest score is biologically correct

Generate multimer predictions across plausible stoichiometries without assuming the largest score is biologically correct.

- **Routing name:** `generate-multimer-predictions-across-plausible-stoichiometries-without-assuming-the-largest-score-is-biologically-correct`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T026 — Generate membrane-aware models with declared topology and membrane orientation constraints when applicable

Generate membrane-aware models with declared topology and membrane orientation constraints when applicable.

- **Routing name:** `generate-membrane-aware-models-with-declared-topology-and-membrane-orientation-constraints-when-applicable`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T027 — Generate ligand-free protein models without fabricating bound ligand coordinates unsupported by the prediction method

Generate ligand-free protein models without fabricating bound ligand coordinates unsupported by the prediction method.

- **Routing name:** `generate-ligand-free-protein-models-without-fabricating-bound-ligand-coordinates-unsupported-by-the-prediction-method`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T028 — Sample alternate conformations for proteins known to undergo large state changes or hinge motions

Sample alternate conformations for proteins known to undergo large state changes or hinge motions.

- **Routing name:** `sample-alternate-conformations-for-proteins-known-to-undergo-large-state-changes-or-hinge-motions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T029 — Cluster predicted models by global fold, domain arrangement, interface geometry, and local backbone divergence

Cluster predicted models by global fold, domain arrangement, interface geometry, and local backbone divergence.

- **Routing name:** `cluster-predicted-models-by-global-fold-domain-arrangement-interface-geometry-and-local-backbone-divergence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T030 — Select representative ensemble members without collapsing materially distinct structural hypotheses

Select representative ensemble members without collapsing materially distinct structural hypotheses.

- **Routing name:** `select-representative-ensemble-members-without-collapsing-materially-distinct-structural-hypotheses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Local confidence and error interpretation

### MYR-D021-T031 — Extract per-residue local confidence values and map them to the exact released residue numbering

Extract per-residue local confidence values and map them to the exact released residue numbering.

- **Routing name:** `extract-per-residue-local-confidence-values-and-map-them-to-the-exact-released-residue-numbering`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T032 — Classify residues into high, medium, low, and very-low confidence bins using model-appropriate thresholds

Classify residues into high, medium, low, and very-low confidence bins using model-appropriate thresholds.

- **Routing name:** `classify-residues-into-high-medium-low-and-very-low-confidence-bins-using-model-appropriate-thresholds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T033 — Distinguish low confidence caused by intrinsic disorder from low confidence caused by inadequate information

Distinguish low confidence caused by intrinsic disorder from low confidence caused by inadequate information.

- **Routing name:** `distinguish-low-confidence-caused-by-intrinsic-disorder-from-low-confidence-caused-by-inadequate-information`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T034 — Calculate predicted aligned error matrices and identify rigid high-confidence blocks

Calculate predicted aligned error matrices and identify rigid high-confidence blocks.

- **Routing name:** `calculate-predicted-aligned-error-matrices-and-identify-rigid-high-confidence-blocks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T035 — Identify domain pairs whose relative placement is uncertain despite confident individual domains

Identify domain pairs whose relative placement is uncertain despite confident individual domains.

- **Routing name:** `identify-domain-pairs-whose-relative-placement-is-uncertain-despite-confident-individual-domains`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T036 — Flag loops, termini, insertions, and linkers whose coordinates should not guide atomic mechanistic claims

Flag loops, termini, insertions, and linkers whose coordinates should not guide atomic mechanistic claims.

- **Routing name:** `flag-loops-termini-insertions-and-linkers-whose-coordinates-should-not-guide-atomic-mechanistic-claims`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T037 — Compare local confidence across ensemble members and prediction methods

Compare local confidence across ensemble members and prediction methods.

- **Routing name:** `compare-local-confidence-across-ensemble-members-and-prediction-methods`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T038 — Quantify confidence around catalytic, binding, mutation, cleavage, and post-translational-modification sites

Quantify confidence around catalytic, binding, mutation, cleavage, and post-translational-modification sites.

- **Routing name:** `quantify-confidence-around-catalytic-binding-mutation-cleavage-and-post-translational-modification-sites`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T039 — Prevent interpretation of local confidence as an experimentally measured accuracy value

Prevent interpretation of local confidence as an experimentally measured accuracy value.

- **Routing name:** `prevent-interpretation-of-local-confidence-as-an-experimentally-measured-accuracy-value`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T040 — Export residue-level confidence and uncertainty annotations in machine-readable form

Export residue-level confidence and uncertainty annotations in machine-readable form.

- **Routing name:** `export-residue-level-confidence-and-uncertainty-annotations-in-machine-readable-form`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Complex and interface confidence

### MYR-D021-T041 — Calculate interface-specific confidence metrics for each predicted chain pair

Calculate interface-specific confidence metrics for each predicted chain pair.

- **Routing name:** `calculate-interface-specific-confidence-metrics-for-each-predicted-chain-pair`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T042 — Identify interfaces supported by strong interchain contact probability and low interchain predicted error

Identify interfaces supported by strong interchain contact probability and low interchain predicted error.

- **Routing name:** `identify-interfaces-supported-by-strong-interchain-contact-probability-and-low-interchain-predicted-error`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T043 — Detect chain placements driven by homomeric symmetry or repeated domains rather than specific pairing evidence

Detect chain placements driven by homomeric symmetry or repeated domains rather than specific pairing evidence.

- **Routing name:** `detect-chain-placements-driven-by-homomeric-symmetry-or-repeated-domains-rather-than-specific-pairing-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T044 — Compare alternative stoichiometries using interface confidence, buried area, clashes, and biological plausibility

Compare alternative stoichiometries using interface confidence, buried area, clashes, and biological plausibility.

- **Routing name:** `compare-alternative-stoichiometries-using-interface-confidence-buried-area-clashes-and-biological-plausibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T045 — Flag interfaces dominated by low-complexity, disordered, or poorly aligned residues

Flag interfaces dominated by low-complexity, disordered, or poorly aligned residues.

- **Routing name:** `flag-interfaces-dominated-by-low-complexity-disordered-or-poorly-aligned-residues`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T046 — Assess whether predicted interfaces overlap known active sites, transmembrane surfaces, or inaccessible cellular compartments

Assess whether predicted interfaces overlap known active sites, transmembrane surfaces, or inaccessible cellular compartments.

- **Routing name:** `assess-whether-predicted-interfaces-overlap-known-active-sites-transmembrane-surfaces-or-inaccessible-cellular-compartments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T047 — Distinguish confident chain folds from uncertain relative chain orientation

Distinguish confident chain folds from uncertain relative chain orientation.

- **Routing name:** `distinguish-confident-chain-folds-from-uncertain-relative-chain-orientation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T048 — Compare predicted interfaces with cross-links, mutagenesis, coevolution, or known complex structures when available

Compare predicted interfaces with cross-links, mutagenesis, coevolution, or known complex structures when available.

- **Routing name:** `compare-predicted-interfaces-with-cross-links-mutagenesis-coevolution-or-known-complex-structures-when-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T049 — Reject interface claims that depend on a single low-confidence model or unsupported chain pairing

Reject interface claims that depend on a single low-confidence model or unsupported chain pairing.

- **Routing name:** `reject-interface-claims-that-depend-on-a-single-low-confidence-model-or-unsupported-chain-pairing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T050 — Export ranked interface hypotheses with explicit support, contradictions, and no-call states

Export ranked interface hypotheses with explicit support, contradictions, and no-call states.

- **Routing name:** `export-ranked-interface-hypotheses-with-explicit-support-contradictions-and-no-call-states`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Cofactors, ligands, metals, and modifications

### MYR-D021-T051 — Inventory required cofactors, metals, prosthetic groups, glycans, lipids, and covalent modifications from curated evidence

Inventory required cofactors, metals, prosthetic groups, glycans, lipids, and covalent modifications from curated evidence.

- **Routing name:** `inventory-required-cofactors-metals-prosthetic-groups-glycans-lipids-and-covalent-modifications-from-curated-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T052 — Map known ligand-contact residues onto predicted coordinates while retaining source provenance

Map known ligand-contact residues onto predicted coordinates while retaining source provenance.

- **Routing name:** `map-known-ligand-contact-residues-onto-predicted-coordinates-while-retaining-source-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T053 — Detect geometrically implausible catalytic or metal-binding residue arrangements

Detect geometrically implausible catalytic or metal-binding residue arrangements.

- **Routing name:** `detect-geometrically-implausible-catalytic-or-metal-binding-residue-arrangements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T054 — Compare predicted pocket geometry across ensemble members and alternate conformational states

Compare predicted pocket geometry across ensemble members and alternate conformational states.

- **Routing name:** `compare-predicted-pocket-geometry-across-ensemble-members-and-alternate-conformational-states`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T055 — Flag pockets formed primarily by low-confidence loops or uncertain domain orientations

Flag pockets formed primarily by low-confidence loops or uncertain domain orientations.

- **Routing name:** `flag-pockets-formed-primarily-by-low-confidence-loops-or-uncertain-domain-orientations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T056 — Assess whether omitted cofactors could materially alter fold, oligomerization, or local geometry

Assess whether omitted cofactors could materially alter fold, oligomerization, or local geometry.

- **Routing name:** `assess-whether-omitted-cofactors-could-materially-alter-fold-oligomerization-or-local-geometry`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T057 — Preserve modified residue identity and numbering without silently converting it to an unmodified residue

Preserve modified residue identity and numbering without silently converting it to an unmodified residue.

- **Routing name:** `preserve-modified-residue-identity-and-numbering-without-silently-converting-it-to-an-unmodified-residue`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T058 — Identify steric conflicts introduced by modelled glycans, lipids, termini, or tags

Identify steric conflicts introduced by modelled glycans, lipids, termini, or tags.

- **Routing name:** `identify-steric-conflicts-introduced-by-modelled-glycans-lipids-termini-or-tags`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T059 — Avoid inferring ligand affinity or catalytic competence from predicted pocket presence alone

Avoid inferring ligand affinity or catalytic competence from predicted pocket presence alone.

- **Routing name:** `avoid-inferring-ligand-affinity-or-catalytic-competence-from-predicted-pocket-presence-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T060 — Produce a cofactor and ligand readiness report for downstream modelling

Produce a cofactor and ligand readiness report for downstream modelling.

- **Routing name:** `produce-a-cofactor-and-ligand-readiness-report-for-downstream-modelling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Geometry and physical plausibility validation

### MYR-D021-T061 — Check covalent geometry, chirality, peptide planarity, backbone torsions, side-chain rotamers, and atomic clashes

Check covalent geometry, chirality, peptide planarity, backbone torsions, side-chain rotamers, and atomic clashes.

- **Routing name:** `check-covalent-geometry-chirality-peptide-planarity-backbone-torsions-side-chain-rotamers-and-atomic-clashes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T062 — Identify chain breaks, missing atoms, duplicate atoms, zero occupancy, and invalid alternate-location records

Identify chain breaks, missing atoms, duplicate atoms, zero occupancy, and invalid alternate-location records.

- **Routing name:** `identify-chain-breaks-missing-atoms-duplicate-atoms-zero-occupancy-and-invalid-alternate-location-records`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T063 — Assess hydrophobic burial, exposed unsatisfied polar groups, and buried charge patterns as plausibility warnings

Assess hydrophobic burial, exposed unsatisfied polar groups, and buried charge patterns as plausibility warnings.

- **Routing name:** `assess-hydrophobic-burial-exposed-unsatisfied-polar-groups-and-buried-charge-patterns-as-plausibility-warnings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T064 — Validate disulfide connectivity against sequence separation, geometry, and cellular redox context

Validate disulfide connectivity against sequence separation, geometry, and cellular redox context.

- **Routing name:** `validate-disulfide-connectivity-against-sequence-separation-geometry-and-cellular-redox-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T065 — Check transmembrane helices for membrane-compatible orientation and polar-residue placement

Check transmembrane helices for membrane-compatible orientation and polar-residue placement.

- **Routing name:** `check-transmembrane-helices-for-membrane-compatible-orientation-and-polar-residue-placement`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T066 — Calculate residue-level packing and environment scores without treating them as experimental validation

Calculate residue-level packing and environment scores without treating them as experimental validation.

- **Routing name:** `calculate-residue-level-packing-and-environment-scores-without-treating-them-as-experimental-validation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T067 — Compare relaxed and unrelaxed models for topology changes or overoptimization artifacts

Compare relaxed and unrelaxed models for topology changes or overoptimization artifacts.

- **Routing name:** `compare-relaxed-and-unrelaxed-models-for-topology-changes-or-overoptimization-artifacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T068 — Detect knots, chain crossings, self-intersections, and impossible linker geometries

Detect knots, chain crossings, self-intersections, and impossible linker geometries.

- **Routing name:** `detect-knots-chain-crossings-self-intersections-and-impossible-linker-geometries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T069 — Return fail status for models with unresolved severe stereochemical or topological defects

Return fail status for models with unresolved severe stereochemical or topological defects.

- **Routing name:** `return-fail-status-for-models-with-unresolved-severe-stereochemical-or-topological-defects`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T070 — Archive all geometry diagnostics and corrected coordinate transformations

Archive all geometry diagnostics and corrected coordinate transformations.

- **Routing name:** `archive-all-geometry-diagnostics-and-corrected-coordinate-transformations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Comparative and experimental reconciliation

### MYR-D021-T071 — Align predictions to homologous experimental structures using domain-aware rather than only global superposition

Align predictions to homologous experimental structures using domain-aware rather than only global superposition.

- **Routing name:** `align-predictions-to-homologous-experimental-structures-using-domain-aware-rather-than-only-global-superposition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T072 — Calculate global and local structural similarity while reporting aligned coverage

Calculate global and local structural similarity while reporting aligned coverage.

- **Routing name:** `calculate-global-and-local-structural-similarity-while-reporting-aligned-coverage`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T073 — Compare predicted oligomers with curated biological assemblies rather than crystallographic contacts alone

Compare predicted oligomers with curated biological assemblies rather than crystallographic contacts alone.

- **Routing name:** `compare-predicted-oligomers-with-curated-biological-assemblies-rather-than-crystallographic-contacts-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T074 — Map experimental cross-links, hydrogen-deuterium exchange, FRET, mutagenesis, SAXS, and EM restraints to the model

Map experimental cross-links, hydrogen-deuterium exchange, FRET, mutagenesis, SAXS, and EM restraints to the model.

- **Routing name:** `map-experimental-cross-links-hydrogen-deuterium-exchange-fret-mutagenesis-saxs-and-em-restraints-to-the-model`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T075 — Identify experimental observations incompatible with the top-ranked predicted structure

Identify experimental observations incompatible with the top-ranked predicted structure.

- **Routing name:** `identify-experimental-observations-incompatible-with-the-top-ranked-predicted-structure`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T076 — Detect conformational-state mismatch between the prediction and the experimental reference

Detect conformational-state mismatch between the prediction and the experimental reference.

- **Routing name:** `detect-conformational-state-mismatch-between-the-prediction-and-the-experimental-reference`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T077 — Compare disease or engineered variants without attributing causal effects solely to model differences

Compare disease or engineered variants without attributing causal effects solely to model differences.

- **Routing name:** `compare-disease-or-engineered-variants-without-attributing-causal-effects-solely-to-model-differences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T078 — Quantify whether conclusions are stable across reasonable model and alignment choices

Quantify whether conclusions are stable across reasonable model and alignment choices.

- **Routing name:** `quantify-whether-conclusions-are-stable-across-reasonable-model-and-alignment-choices`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T079 — Downgrade claims when experimental evidence supports only fold-level rather than atomic accuracy

Downgrade claims when experimental evidence supports only fold-level rather than atomic accuracy.

- **Routing name:** `downgrade-claims-when-experimental-evidence-supports-only-fold-level-rather-than-atomic-accuracy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T080 — Generate a reconciled evidence table separating prediction, experiment, inference, and contradiction

Generate a reconciled evidence table separating prediction, experiment, inference, and contradiction.

- **Routing name:** `generate-a-reconciled-evidence-table-separating-prediction-experiment-inference-and-contradiction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Benchmarking and model selection

### MYR-D021-T081 — Define blinded benchmark targets, release-date cutoffs, and leakage controls before model comparison

Define blinded benchmark targets, release-date cutoffs, and leakage controls before model comparison.

- **Routing name:** `define-blinded-benchmark-targets-release-date-cutoffs-and-leakage-controls-before-model-comparison`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T082 — Score models with local, global, interface, and topology metrics appropriate to the target class

Score models with local, global, interface, and topology metrics appropriate to the target class.

- **Routing name:** `score-models-with-local-global-interface-and-topology-metrics-appropriate-to-the-target-class`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T083 — Stratify benchmark performance by sequence length, fold class, disorder, membrane status, and oligomeric state

Stratify benchmark performance by sequence length, fold class, disorder, membrane status, and oligomeric state.

- **Routing name:** `stratify-benchmark-performance-by-sequence-length-fold-class-disorder-membrane-status-and-oligomeric-state`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T084 — Compare confidence calibration by relating predicted confidence to observed structural error

Compare confidence calibration by relating predicted confidence to observed structural error.

- **Routing name:** `compare-confidence-calibration-by-relating-predicted-confidence-to-observed-structural-error`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T085 — Measure failure rates and no-call rates rather than reporting only successful predictions

Measure failure rates and no-call rates rather than reporting only successful predictions.

- **Routing name:** `measure-failure-rates-and-no-call-rates-rather-than-reporting-only-successful-predictions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T086 — Evaluate model ranking independently from model generation quality

Evaluate model ranking independently from model generation quality.

- **Routing name:** `evaluate-model-ranking-independently-from-model-generation-quality`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T087 — Test sensitivity to alignment depth, template inclusion, recycle count, and random seed

Test sensitivity to alignment depth, template inclusion, recycle count, and random seed.

- **Routing name:** `test-sensitivity-to-alignment-depth-template-inclusion-recycle-count-and-random-seed`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T088 — Prevent use of homologous benchmark structures that entered training or template databases after the declared cutoff

Prevent use of homologous benchmark structures that entered training or template databases after the declared cutoff.

- **Routing name:** `prevent-use-of-homologous-benchmark-structures-that-entered-training-or-template-databases-after-the-declared-cutoff`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T089 — Select a primary model only when ranking criteria are prespecified and materially consistent

Select a primary model only when ranking criteria are prespecified and materially consistent.

- **Routing name:** `select-a-primary-model-only-when-ranking-criteria-are-prespecified-and-materially-consistent`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T090 — Retain alternative models when no single structure dominates across validated criteria

Retain alternative models when no single structure dominates across validated criteria.

- **Routing name:** `retain-alternative-models-when-no-single-structure-dominates-across-validated-criteria`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Release, provenance, and review gates

### MYR-D021-T091 — Export coordinates, confidence arrays, predicted-error matrices, alignments, templates, and run metadata together

Export coordinates, confidence arrays, predicted-error matrices, alignments, templates, and run metadata together.

- **Routing name:** `export-coordinates-confidence-arrays-predicted-error-matrices-alignments-templates-and-run-metadata-together`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T092 — Record model code, weights, database versions, hardware, precision mode, parameters, and random seeds

Record model code, weights, database versions, hardware, precision mode, parameters, and random seeds.

- **Routing name:** `record-model-code-weights-database-versions-hardware-precision-mode-parameters-and-random-seeds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T093 — Generate residue and interface annotations using stable chain and residue identifiers

Generate residue and interface annotations using stable chain and residue identifiers.

- **Routing name:** `generate-residue-and-interface-annotations-using-stable-chain-and-residue-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T094 — Create machine-readable pass, warning, fail, and no-call summaries for every model

Create machine-readable pass, warning, fail, and no-call summaries for every model.

- **Routing name:** `create-machine-readable-pass-warning-fail-and-no-call-summaries-for-every-model`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T095 — Hash all input sequences, reference databases, alignments, templates, and released coordinate files

Hash all input sequences, reference databases, alignments, templates, and released coordinate files.

- **Routing name:** `hash-all-input-sequences-reference-databases-alignments-templates-and-released-coordinate-files`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T096 — Label predicted structures clearly so they cannot be mistaken for experimentally determined models

Label predicted structures clearly so they cannot be mistaken for experimentally determined models.

- **Routing name:** `label-predicted-structures-clearly-so-they-cannot-be-mistaken-for-experimentally-determined-models`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T097 — Require expert review before using uncertain coordinates for mutagenesis, docking, or mechanism claims

Require expert review before using uncertain coordinates for mutagenesis, docking, or mechanism claims.

- **Routing name:** `require-expert-review-before-using-uncertain-coordinates-for-mutagenesis-docking-or-mechanism-claims`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T098 — Block direct clinical interpretation from structure prediction without independent variant-evidence assessment

Block direct clinical interpretation from structure prediction without independent variant-evidence assessment.

- **Routing name:** `block-direct-clinical-interpretation-from-structure-prediction-without-independent-variant-evidence-assessment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T099 — Archive discarded models and exclusion reasons to preserve model-selection traceability

Archive discarded models and exclusion reasons to preserve model-selection traceability.

- **Routing name:** `archive-discarded-models-and-exclusion-reasons-to-preserve-model-selection-traceability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D021-T100 — Release a structure ensemble only when sequence, confidence, geometry, provenance, and review gates pass

Release a structure ensemble only when sequence, confidence, geometry, provenance, and review gates pass.

- **Routing name:** `release-a-structure-ensemble-only-when-sequence-confidence-geometry-provenance-and-review-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
