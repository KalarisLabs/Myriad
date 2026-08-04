# D033 — Chemical Library Curation and Standardization

Batch **004** · 10 workstreams · 100 tasks

## 01. File intake and record-level validation

### MYR-D033-T001 — Parse SDF, SMILES, MOL2, CSV, or vendor files with strict encoding and record-boundary validation

Parse SDF, SMILES, MOL2, CSV, or vendor files with strict encoding and record-boundary validation.

- **Routing name:** `parse-sdf-smiles-mol2-csv-or-vendor-files-with-strict-encoding-and-record-boundary-validation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T002 — Assign immutable source-record identifiers before any chemical transformation

Assign immutable source-record identifiers before any chemical transformation.

- **Routing name:** `assign-immutable-source-record-identifiers-before-any-chemical-transformation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T003 — Validate declared molecule counts against successfully parsed, rejected, and empty records

Validate declared molecule counts against successfully parsed, rejected, and empty records.

- **Routing name:** `validate-declared-molecule-counts-against-successfully-parsed-rejected-and-empty-records`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T004 — Preserve original structure strings, mol blocks, names, vendor identifiers, and source-file checksums

Preserve original structure strings, mol blocks, names, vendor identifiers, and source-file checksums.

- **Routing name:** `preserve-original-structure-strings-mol-blocks-names-vendor-identifiers-and-source-file-checksums`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T005 — Detect malformed atom, bond, charge, coordinate, and property blocks without silently repairing them

Detect malformed atom, bond, charge, coordinate, and property blocks without silently repairing them.

- **Routing name:** `detect-malformed-atom-bond-charge-coordinate-and-property-blocks-without-silently-repairing-them`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T006 — Reconcile duplicate property-field names and preserve source-specific metadata namespaces

Reconcile duplicate property-field names and preserve source-specific metadata namespaces.

- **Routing name:** `reconcile-duplicate-property-field-names-and-preserve-source-specific-metadata-namespaces`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T007 — Validate that each record contains at least one interpretable chemical component

Validate that each record contains at least one interpretable chemical component.

- **Routing name:** `validate-that-each-record-contains-at-least-one-interpretable-chemical-component`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T008 — Quarantine records with unsupported query atoms, polymers, Markush structures, or ambiguous attachment points

Quarantine records with unsupported query atoms, polymers, Markush structures, or ambiguous attachment points.

- **Routing name:** `quarantine-records-with-unsupported-query-atoms-polymers-markush-structures-or-ambiguous-attachment-points`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T009 — Classify records as discrete molecules, salts, solvates, mixtures, coordination complexes, or macromolecules

Classify records as discrete molecules, salts, solvates, mixtures, coordination complexes, or macromolecules.

- **Routing name:** `classify-records-as-discrete-molecules-salts-solvates-mixtures-coordination-complexes-or-macromolecules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T010 — Generate an intake report with accepted, warning, failed, and quarantined record counts and reasons

Generate an intake report with accepted, warning, failed, and quarantined record counts and reasons.

- **Routing name:** `generate-an-intake-report-with-accepted-warning-failed-and-quarantined-record-counts-and-reasons`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Chemical graph, valence, and stereochemistry checks

### MYR-D033-T011 — Validate atomic numbers, isotope labels, formal charges, radical states, and explicit valence assignments

Validate atomic numbers, isotope labels, formal charges, radical states, and explicit valence assignments.

- **Routing name:** `validate-atomic-numbers-isotope-labels-formal-charges-radical-states-and-explicit-valence-assignments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T012 — Detect impossible aromaticity, kekulization, valence, ring-closure, or bond-order representations

Detect impossible aromaticity, kekulization, valence, ring-closure, or bond-order representations.

- **Routing name:** `detect-impossible-aromaticity-kekulization-valence-ring-closure-or-bond-order-representations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T013 — Assign and validate tetrahedral, double-bond, axial, and other supported stereochemical descriptors

Assign and validate tetrahedral, double-bond, axial, and other supported stereochemical descriptors.

- **Routing name:** `assign-and-validate-tetrahedral-double-bond-axial-and-other-supported-stereochemical-descriptors`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T014 — Identify stereogenic elements with missing, contradictory, or non-isomeric source representation

Identify stereogenic elements with missing, contradictory, or non-isomeric source representation.

- **Routing name:** `identify-stereogenic-elements-with-missing-contradictory-or-non-isomeric-source-representation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T015 — Preserve specified stereochemistry through format conversion and canonicalization

Preserve specified stereochemistry through format conversion and canonicalization.

- **Routing name:** `preserve-specified-stereochemistry-through-format-conversion-and-canonicalization`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T016 — Detect stereochemical collapse caused by salt stripping, tautomerization, or coordinate regeneration

Detect stereochemical collapse caused by salt stripping, tautomerization, or coordinate regeneration.

- **Routing name:** `detect-stereochemical-collapse-caused-by-salt-stripping-tautomerization-or-coordinate-regeneration`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T017 — Validate wedge, hash, and three-dimensional chirality consistency when coordinates are present

Validate wedge, hash, and three-dimensional chirality consistency when coordinates are present.

- **Routing name:** `validate-wedge-hash-and-three-dimensional-chirality-consistency-when-coordinates-are-present`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T018 — Identify atropisomeric or conformationally stable stereochemistry not captured by the selected representation

Identify atropisomeric or conformationally stable stereochemistry not captured by the selected representation.

- **Routing name:** `identify-atropisomeric-or-conformationally-stable-stereochemistry-not-captured-by-the-selected-representation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T019 — Compare formal charge and valence states before and after sanitization and flag material changes

Compare formal charge and valence states before and after sanitization and flag material changes.

- **Routing name:** `compare-formal-charge-and-valence-states-before-and-after-sanitization-and-flag-material-changes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T020 — Quarantine structures whose valid chemical graph cannot be determined without expert intervention

Quarantine structures whose valid chemical graph cannot be determined without expert intervention.

- **Routing name:** `quarantine-structures-whose-valid-chemical-graph-cannot-be-determined-without-expert-intervention`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Salt, solvate, mixture, and parent handling

### MYR-D033-T021 — Separate disconnected components while retaining component stoichiometry and source ordering

Separate disconnected components while retaining component stoichiometry and source ordering.

- **Routing name:** `separate-disconnected-components-while-retaining-component-stoichiometry-and-source-ordering`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T022 — Classify counterions, solvates, co-crystal formers, adducts, and potentially active co-components

Classify counterions, solvates, co-crystal formers, adducts, and potentially active co-components.

- **Routing name:** `classify-counterions-solvates-co-crystal-formers-adducts-and-potentially-active-co-components`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T023 — Select a parent component using declared, deterministic rules rather than largest-fragment heuristics alone

Select a parent component using declared, deterministic rules rather than largest-fragment heuristics alone.

- **Routing name:** `select-a-parent-component-using-declared-deterministic-rules-rather-than-largest-fragment-heuristics-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T024 — Preserve salt-form and parent-structure identifiers as linked but distinct chemical entities

Preserve salt-form and parent-structure identifiers as linked but distinct chemical entities.

- **Routing name:** `preserve-salt-form-and-parent-structure-identifiers-as-linked-but-distinct-chemical-entities`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T025 — Prevent removal of covalently bound metals, prosthetic groups, or active co-components as presumed salts

Prevent removal of covalently bound metals, prosthetic groups, or active co-components as presumed salts.

- **Routing name:** `prevent-removal-of-covalently-bound-metals-prosthetic-groups-or-active-co-components-as-presumed-salts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T026 — Normalize common counterion representations without erasing charge balance provenance

Normalize common counterion representations without erasing charge balance provenance.

- **Routing name:** `normalize-common-counterion-representations-without-erasing-charge-balance-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T027 — Detect mixtures whose components cannot be assigned a single active parent

Detect mixtures whose components cannot be assigned a single active parent.

- **Routing name:** `detect-mixtures-whose-components-cannot-be-assigned-a-single-active-parent`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T028 — Reconcile hydrate and solvate annotations with molecular formula and source metadata

Reconcile hydrate and solvate annotations with molecular formula and source metadata.

- **Routing name:** `reconcile-hydrate-and-solvate-annotations-with-molecular-formula-and-source-metadata`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T029 — Calculate parent and as-supplied molecular properties separately when salt form affects interpretation

Calculate parent and as-supplied molecular properties separately when salt form affects interpretation.

- **Routing name:** `calculate-parent-and-as-supplied-molecular-properties-separately-when-salt-form-affects-interpretation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T030 — Generate a component-resolution table documenting retained, removed, and unresolved fragments

Generate a component-resolution table documenting retained, removed, and unresolved fragments.

- **Routing name:** `generate-a-component-resolution-table-documenting-retained-removed-and-unresolved-fragments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Charge, protonation, tautomer, and aromatic normalization

### MYR-D033-T031 — Apply a versioned normalization rule set for common functional-group and charge representations

Apply a versioned normalization rule set for common functional-group and charge representations.

- **Routing name:** `apply-a-versioned-normalization-rule-set-for-common-functional-group-and-charge-representations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T032 — Canonicalize aromatic and kekule forms while preserving a reversible mapping to the source graph

Canonicalize aromatic and kekule forms while preserving a reversible mapping to the source graph.

- **Routing name:** `canonicalize-aromatic-and-kekule-forms-while-preserving-a-reversible-mapping-to-the-source-graph`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T033 — Normalize nitro, azide, sulfoxide, phosphate, boron, and other supported valence conventions consistently

Normalize nitro, azide, sulfoxide, phosphate, boron, and other supported valence conventions consistently.

- **Routing name:** `normalize-nitro-azide-sulfoxide-phosphate-boron-and-other-supported-valence-conventions-consistently`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T034 — Generate major protonation states only for workflows that explicitly require pH-dependent enumeration

Generate major protonation states only for workflows that explicitly require pH-dependent enumeration.

- **Routing name:** `generate-major-protonation-states-only-for-workflows-that-explicitly-require-ph-dependent-enumeration`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T035 — Generate tautomer ensembles using declared scoring, transformation, and maximum-enumeration rules

Generate tautomer ensembles using declared scoring, transformation, and maximum-enumeration rules.

- **Routing name:** `generate-tautomer-ensembles-using-declared-scoring-transformation-and-maximum-enumeration-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T036 — Distinguish deterministic representation normalization from uncertain pH-dependent physicochemical-state prediction

Distinguish deterministic representation normalization from uncertain pH-dependent physicochemical-state prediction.

- **Routing name:** `distinguish-deterministic-representation-normalization-from-uncertain-ph-dependent-physicochemical-state-prediction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T037 — Preserve source, standardized, parent, and enumerated forms as separate linked records

Preserve source, standardized, parent, and enumerated forms as separate linked records.

- **Routing name:** `preserve-source-standardized-parent-and-enumerated-forms-as-separate-linked-records`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T038 — Detect normalization rules that alter stereochemistry, isotope placement, or covalent connectivity unexpectedly

Detect normalization rules that alter stereochemistry, isotope placement, or covalent connectivity unexpectedly.

- **Routing name:** `detect-normalization-rules-that-alter-stereochemistry-isotope-placement-or-covalent-connectivity-unexpectedly`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T039 — Assign canonical SMILES, isomeric SMILES, InChI, and InChIKey with tool and version provenance

Assign canonical SMILES, isomeric SMILES, InChI, and InChIKey with tool and version provenance.

- **Routing name:** `assign-canonical-smiles-isomeric-smiles-inchi-and-inchikey-with-tool-and-version-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T040 — Produce a transformation log containing every graph change and its rule identifier

Produce a transformation log containing every graph change and its rule identifier.

- **Routing name:** `produce-a-transformation-log-containing-every-graph-change-and-its-rule-identifier`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Entity identity, deduplication, and hierarchy

### MYR-D033-T041 — Define identity layers for exact graph, stereoisomer, tautomer-insensitive parent, and connectivity-only matching

Define identity layers for exact graph, stereoisomer, tautomer-insensitive parent, and connectivity-only matching.

- **Routing name:** `define-identity-layers-for-exact-graph-stereoisomer-tautomer-insensitive-parent-and-connectivity-only-matching`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T042 — Cluster exact duplicates using standardized isomeric identity rather than names or vendor identifiers

Cluster exact duplicates using standardized isomeric identity rather than names or vendor identifiers.

- **Routing name:** `cluster-exact-duplicates-using-standardized-isomeric-identity-rather-than-names-or-vendor-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T043 — Detect conflicting structures sharing the same external identifier

Detect conflicting structures sharing the same external identifier.

- **Routing name:** `detect-conflicting-structures-sharing-the-same-external-identifier`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T044 — Detect identical standardized structures associated with incompatible names, formulas, or registry identifiers

Detect identical standardized structures associated with incompatible names, formulas, or registry identifiers.

- **Routing name:** `detect-identical-standardized-structures-associated-with-incompatible-names-formulas-or-registry-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T045 — Preserve separate records for distinct stereoisomers, isotopologues, charge states, or covalent forms when scientifically relevant

Preserve separate records for distinct stereoisomers, isotopologues, charge states, or covalent forms when scientifically relevant.

- **Routing name:** `preserve-separate-records-for-distinct-stereoisomers-isotopologues-charge-states-or-covalent-forms-when-scientifically-relevant`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T046 — Create parent–salt–tautomer–stereoisomer–lot entity relationships without merging independent source provenance

Create parent–salt–tautomer–stereoisomer–lot entity relationships without merging independent source provenance.

- **Routing name:** `create-parent-salt-tautomer-stereoisomer-lot-entity-relationships-without-merging-independent-source-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T047 — Reconcile duplicate bioactivity or inventory records only after chemical identity has been established

Reconcile duplicate bioactivity or inventory records only after chemical identity has been established.

- **Routing name:** `reconcile-duplicate-bioactivity-or-inventory-records-only-after-chemical-identity-has-been-established`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T048 — Assign stable internal entity identifiers independent of input order

Assign stable internal entity identifiers independent of input order.

- **Routing name:** `assign-stable-internal-entity-identifiers-independent-of-input-order`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T049 — Generate duplicate clusters with canonical representative selection and merge rationale

Generate duplicate clusters with canonical representative selection and merge rationale.

- **Routing name:** `generate-duplicate-clusters-with-canonical-representative-selection-and-merge-rationale`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T050 — Block irreversible deduplication when the chosen identity layer is not declared

Block irreversible deduplication when the chosen identity layer is not declared.

- **Routing name:** `block-irreversible-deduplication-when-the-chosen-identity-layer-is-not-declared`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Descriptor and physicochemical annotation

### MYR-D033-T051 — Calculate molecular formula, exact mass, average mass, heavy-atom count, and formal charge on standardized structures

Calculate molecular formula, exact mass, average mass, heavy-atom count, and formal charge on standardized structures.

- **Routing name:** `calculate-molecular-formula-exact-mass-average-mass-heavy-atom-count-and-formal-charge-on-standardized-structures`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T052 — Calculate hydrogen-bond donor, acceptor, rotatable-bond, ring, aromatic-ring, and stereocentre counts

Calculate hydrogen-bond donor, acceptor, rotatable-bond, ring, aromatic-ring, and stereocentre counts.

- **Routing name:** `calculate-hydrogen-bond-donor-acceptor-rotatable-bond-ring-aromatic-ring-and-stereocentre-counts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T053 — Calculate logP, topological polar surface area, and related descriptors with named algorithms and versions

Calculate logP, topological polar surface area, and related descriptors with named algorithms and versions.

- **Routing name:** `calculate-logp-topological-polar-surface-area-and-related-descriptors-with-named-algorithms-and-versions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T054 — Flag descriptor failures caused by unsupported elements, valence states, or molecular size

Flag descriptor failures caused by unsupported elements, valence states, or molecular size.

- **Routing name:** `flag-descriptor-failures-caused-by-unsupported-elements-valence-states-or-molecular-size`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T055 — Compute descriptors separately for parent, salt, and enumerated states where interpretation differs

Compute descriptors separately for parent, salt, and enumerated states where interpretation differs.

- **Routing name:** `compute-descriptors-separately-for-parent-salt-and-enumerated-states-where-interpretation-differs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T056 — Validate descriptor units, numerical ranges, missing values, and deterministic repeatability

Validate descriptor units, numerical ranges, missing values, and deterministic repeatability.

- **Routing name:** `validate-descriptor-units-numerical-ranges-missing-values-and-deterministic-repeatability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T057 — Compare recalculated properties with supplier metadata and flag material discrepancies

Compare recalculated properties with supplier metadata and flag material discrepancies.

- **Routing name:** `compare-recalculated-properties-with-supplier-metadata-and-flag-material-discrepancies`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T058 — Annotate elemental composition and identify organometallic, inorganic, isotope-labelled, or unusual-element subsets

Annotate elemental composition and identify organometallic, inorganic, isotope-labelled, or unusual-element subsets.

- **Routing name:** `annotate-elemental-composition-and-identify-organometallic-inorganic-isotope-labelled-or-unusual-element-subsets`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T059 — Create screening-relevant property bins without treating heuristic filters as universal drug-likeness rules

Create screening-relevant property bins without treating heuristic filters as universal drug-likeness rules.

- **Routing name:** `create-screening-relevant-property-bins-without-treating-heuristic-filters-as-universal-drug-likeness-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T060 — Export a descriptor dictionary defining structure basis, algorithm, version, unit, and missing-value semantics

Export a descriptor dictionary defining structure basis, algorithm, version, unit, and missing-value semantics.

- **Routing name:** `export-a-descriptor-dictionary-defining-structure-basis-algorithm-version-unit-and-missing-value-semantics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Interference, reactivity, and assay-liability flags

### MYR-D033-T061 — Apply versioned substructure alerts for frequent hitters while retaining matched atom mappings

Apply versioned substructure alerts for frequent hitters while retaining matched atom mappings.

- **Routing name:** `apply-versioned-substructure-alerts-for-frequent-hitters-while-retaining-matched-atom-mappings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T062 — Flag electrophiles, redox-active motifs, metal chelators, detergents, and reactive functionalities relevant to assay context

Flag electrophiles, redox-active motifs, metal chelators, detergents, and reactive functionalities relevant to assay context.

- **Routing name:** `flag-electrophiles-redox-active-motifs-metal-chelators-detergents-and-reactive-functionalities-relevant-to-assay-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T063 — Identify known or predicted colloidal aggregators using structural alerts and available experimental annotations

Identify known or predicted colloidal aggregators using structural alerts and available experimental annotations.

- **Routing name:** `identify-known-or-predicted-colloidal-aggregators-using-structural-alerts-and-available-experimental-annotations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T064 — Flag intrinsic fluorescence, absorbance, quenching, luminescence, or colour liabilities at assay wavelengths when data exist

Flag intrinsic fluorescence, absorbance, quenching, luminescence, or colour liabilities at assay wavelengths when data exist.

- **Routing name:** `flag-intrinsic-fluorescence-absorbance-quenching-luminescence-or-colour-liabilities-at-assay-wavelengths-when-data-exist`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T065 — Identify unstable, hydrolysable, oxidizable, photoreactive, or polymerization-prone motifs

Identify unstable, hydrolysable, oxidizable, photoreactive, or polymerization-prone motifs.

- **Routing name:** `identify-unstable-hydrolysable-oxidizable-photoreactive-or-polymerization-prone-motifs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T066 — Distinguish intentional covalent-warhead design from nonspecific reactive-compound assay liability

Distinguish intentional covalent-warhead design from nonspecific reactive-compound assay liability.

- **Routing name:** `distinguish-intentional-covalent-warhead-design-from-nonspecific-reactive-compound-assay-liability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T067 — Annotate nuisance flags as warnings rather than automatic exclusions unless assay-specific rules require removal

Annotate nuisance flags as warnings rather than automatic exclusions unless assay-specific rules require removal.

- **Routing name:** `annotate-nuisance-flags-as-warnings-rather-than-automatic-exclusions-unless-assay-specific-rules-require-removal`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T068 — Detect compounds with multiple orthogonal interference risks and elevate review priority

Detect compounds with multiple orthogonal interference risks and elevate review priority.

- **Routing name:** `detect-compounds-with-multiple-orthogonal-interference-risks-and-elevate-review-priority`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T069 — Reconcile alert results across rule-set versions and record changed classifications

Reconcile alert results across rule-set versions and record changed classifications.

- **Routing name:** `reconcile-alert-results-across-rule-set-versions-and-record-changed-classifications`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T070 — Generate an assay-liability table with alert pattern, matched atoms, context, severity, and disposition

Generate an assay-liability table with alert pattern, matched atoms, context, severity, and disposition.

- **Routing name:** `generate-an-assay-liability-table-with-alert-pattern-matched-atoms-context-severity-and-disposition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Diversity, scaffold, and chemical-space assessment

### MYR-D033-T071 — Generate declared fingerprints for every valid standardized parent structure

Generate declared fingerprints for every valid standardized parent structure.

- **Routing name:** `generate-declared-fingerprints-for-every-valid-standardized-parent-structure`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T072 — Calculate pairwise or approximate-neighbour similarity with metric and threshold provenance

Calculate pairwise or approximate-neighbour similarity with metric and threshold provenance.

- **Routing name:** `calculate-pairwise-or-approximate-neighbour-similarity-with-metric-and-threshold-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T073 — Assign Bemis–Murcko or alternative scaffolds using a declared scaffold definition

Assign Bemis–Murcko or alternative scaffolds using a declared scaffold definition.

- **Routing name:** `assign-bemis-murcko-or-alternative-scaffolds-using-a-declared-scaffold-definition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T074 — Cluster the library by fingerprint similarity with deterministic tie-breaking

Cluster the library by fingerprint similarity with deterministic tie-breaking.

- **Routing name:** `cluster-the-library-by-fingerprint-similarity-with-deterministic-tie-breaking`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T075 — Quantify scaffold frequency, singleton rate, nearest-neighbour similarity, and redundancy

Quantify scaffold frequency, singleton rate, nearest-neighbour similarity, and redundancy.

- **Routing name:** `quantify-scaffold-frequency-singleton-rate-nearest-neighbour-similarity-and-redundancy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T076 — Compare chemical-space coverage against a reference collection using matched descriptors and representations

Compare chemical-space coverage against a reference collection using matched descriptors and representations.

- **Routing name:** `compare-chemical-space-coverage-against-a-reference-collection-using-matched-descriptors-and-representations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T077 — Identify overrepresented series that could dominate screening statistics or model training

Identify overrepresented series that could dominate screening statistics or model training.

- **Routing name:** `identify-overrepresented-series-that-could-dominate-screening-statistics-or-model-training`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T078 — Select diversity subsets under explicit size, property, scaffold, and availability constraints

Select diversity subsets under explicit size, property, scaffold, and availability constraints.

- **Routing name:** `select-diversity-subsets-under-explicit-size-property-scaffold-and-availability-constraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T079 — Assess whether removed or quarantined records disproportionately affect specific chemical classes

Assess whether removed or quarantined records disproportionately affect specific chemical classes.

- **Routing name:** `assess-whether-removed-or-quarantined-records-disproportionately-affect-specific-chemical-classes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T080 — Produce a chemical-space report with coverage, gaps, redundancy, and selection rationale

Produce a chemical-space report with coverage, gaps, redundancy, and selection rationale.

- **Routing name:** `produce-a-chemical-space-report-with-coverage-gaps-redundancy-and-selection-rationale`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Inventory, provenance, and sample linkage

### MYR-D033-T081 — Link chemical entities to supplier, batch, lot, container, concentration, solvent, plate, and well identifiers

Link chemical entities to supplier, batch, lot, container, concentration, solvent, plate, and well identifiers.

- **Routing name:** `link-chemical-entities-to-supplier-batch-lot-container-concentration-solvent-plate-and-well-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T082 — Validate concentration units, stock dilution factors, and solvent fractions for screening-ready records

Validate concentration units, stock dilution factors, and solvent fractions for screening-ready records.

- **Routing name:** `validate-concentration-units-stock-dilution-factors-and-solvent-fractions-for-screening-ready-records`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T083 — Detect conflicting structures or concentrations assigned to the same sample or barcode

Detect conflicting structures or concentrations assigned to the same sample or barcode.

- **Routing name:** `detect-conflicting-structures-or-concentrations-assigned-to-the-same-sample-or-barcode`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T084 — Distinguish registered chemical identity from the physically supplied sample form

Distinguish registered chemical identity from the physically supplied sample form.

- **Routing name:** `distinguish-registered-chemical-identity-from-the-physically-supplied-sample-form`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T085 — Reconcile analytical purity, identity confirmation, and date-of-analysis metadata when available

Reconcile analytical purity, identity confirmation, and date-of-analysis metadata when available.

- **Routing name:** `reconcile-analytical-purity-identity-confirmation-and-date-of-analysis-metadata-when-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T086 — Flag expired, depleted, insoluble, precipitated, or freeze–thaw-compromised samples from inventory metadata

Flag expired, depleted, insoluble, precipitated, or freeze–thaw-compromised samples from inventory metadata.

- **Routing name:** `flag-expired-depleted-insoluble-precipitated-or-freeze-thaw-compromised-samples-from-inventory-metadata`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T087 — Preserve chain of custody across repackaging, cherry-picking, pooling, and plate replication

Preserve chain of custody across repackaging, cherry-picking, pooling, and plate replication.

- **Routing name:** `preserve-chain-of-custody-across-repackaging-cherry-picking-pooling-and-plate-replication`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T088 — Identify samples lacking sufficient identity or inventory evidence for screening use

Identify samples lacking sufficient identity or inventory evidence for screening use.

- **Routing name:** `identify-samples-lacking-sufficient-identity-or-inventory-evidence-for-screening-use`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T089 — Generate machine-readable chemical-entity-to-sample and physical-sample-to-assay-plate mappings with stable identifiers and provenance

Generate machine-readable chemical-entity-to-sample and physical-sample-to-assay-plate mappings with stable identifiers and provenance.

- **Routing name:** `generate-machine-readable-chemical-entity-to-sample-and-physical-sample-to-assay-plate-mappings-with-stable-identifiers-and-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T090 — Hash source files, transformed structures, inventory tables, and released library snapshots

Hash source files, transformed structures, inventory tables, and released library snapshots.

- **Routing name:** `hash-source-files-transformed-structures-inventory-tables-and-released-library-snapshots`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Release quality control and versioning

### MYR-D033-T091 — Compare source and released record counts across every transformation stage

Compare source and released record counts across every transformation stage.

- **Routing name:** `compare-source-and-released-record-counts-across-every-transformation-stage`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T092 — Validate uniqueness, identifier stability, referential integrity, and parent–child chemical relationships

Validate uniqueness, identifier stability, referential integrity, and parent–child chemical relationships.

- **Routing name:** `validate-uniqueness-identifier-stability-referential-integrity-and-parent-child-chemical-relationships`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T093 — Rerun sanitization and descriptor calculations to confirm deterministic release reproducibility

Rerun sanitization and descriptor calculations to confirm deterministic release reproducibility.

- **Routing name:** `rerun-sanitization-and-descriptor-calculations-to-confirm-deterministic-release-reproducibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T094 — Check that every excluded or quarantined record has a specific machine-readable reason

Check that every excluded or quarantined record has a specific machine-readable reason.

- **Routing name:** `check-that-every-excluded-or-quarantined-record-has-a-specific-machine-readable-reason`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T095 — Generate before-and-after structure depictions for records with material transformations

Generate before-and-after structure depictions for records with material transformations.

- **Routing name:** `generate-before-and-after-structure-depictions-for-records-with-material-transformations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T096 — Require chemistry review for unresolved stereochemistry, mixtures, metals, reactive motifs, and identifier conflicts

Require chemistry review for unresolved stereochemistry, mixtures, metals, reactive motifs, and identifier conflicts.

- **Routing name:** `require-chemistry-review-for-unresolved-stereochemistry-mixtures-metals-reactive-motifs-and-identifier-conflicts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T097 — Create pass, warning, fail, and quarantine statuses for every source record and chemical entity

Create pass, warning, fail, and quarantine statuses for every source record and chemical entity.

- **Routing name:** `create-pass-warning-fail-and-quarantine-statuses-for-every-source-record-and-chemical-entity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T098 — Publish structure-standardization rules, software versions, parameters, and known limitations with the release

Publish structure-standardization rules, software versions, parameters, and known limitations with the release.

- **Routing name:** `publish-structure-standardization-rules-software-versions-parameters-and-known-limitations-with-the-release`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T099 — Archive prior library versions and generate entity-level additions, removals, merges, and structure-change diffs

Archive prior library versions and generate entity-level additions, removals, merges, and structure-change diffs.

- **Routing name:** `archive-prior-library-versions-and-generate-entity-level-additions-removals-merges-and-structure-change-diffs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D033-T100 — Release the curated library only when count reconciliation, provenance, chemical integrity, and review gates pass

Release the curated library only when count reconciliation, provenance, chemical integrity, and review gates pass.

- **Routing name:** `release-the-curated-library-only-when-count-reconciliation-provenance-chemical-integrity-and-review-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
