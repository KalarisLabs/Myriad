# D034 — Ligand-Based Virtual Screening and Similarity Search

Batch **004** · 10 workstreams · 100 tasks

## 01. Query ligand and activity-set definition

### MYR-D034-T001 — Define the biological target, assay endpoint, activity direction, units, and acceptable evidence types for query ligands

Define the biological target, assay endpoint, activity direction, units, and acceptable evidence types for query ligands.

- **Routing name:** `define-the-biological-target-assay-endpoint-activity-direction-units-and-acceptable-evidence-types-for-query-ligands`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T002 — Reconcile query-ligand structures with source assay records and stable chemical identifiers

Reconcile query-ligand structures with source assay records and stable chemical identifiers.

- **Routing name:** `reconcile-query-ligand-structures-with-source-assay-records-and-stable-chemical-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T003 — Separate direct binders, functional modulators, phenotypic actives, inactive controls, and uncertain labels

Separate direct binders, functional modulators, phenotypic actives, inactive controls, and uncertain labels.

- **Routing name:** `separate-direct-binders-functional-modulators-phenotypic-actives-inactive-controls-and-uncertain-labels`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T004 — Normalize censored activity relations without converting bounds into exact measurements

Normalize censored activity relations without converting bounds into exact measurements.

- **Routing name:** `normalize-censored-activity-relations-without-converting-bounds-into-exact-measurements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T005 — Distinguish potency, efficacy, affinity, residence time, and selectivity endpoints before combining ligands

Distinguish potency, efficacy, affinity, residence time, and selectivity endpoints before combining ligands.

- **Routing name:** `distinguish-potency-efficacy-affinity-residence-time-and-selectivity-endpoints-before-combining-ligands`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T006 — Identify duplicate measurements and aggregate them using a prespecified assay-aware rule

Identify duplicate measurements and aggregate them using a prespecified assay-aware rule.

- **Routing name:** `identify-duplicate-measurements-and-aggregate-them-using-a-prespecified-assay-aware-rule`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T007 — Detect activity cliffs and contradictory labels among close analogues

Detect activity cliffs and contradictory labels among close analogues.

- **Routing name:** `detect-activity-cliffs-and-contradictory-labels-among-close-analogues`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T008 — Partition query ligands by binding mode, mechanism, target state, or chemotype when evidence supports separation

Partition query ligands by binding mode, mechanism, target state, or chemotype when evidence supports separation.

- **Routing name:** `partition-query-ligands-by-binding-mode-mechanism-target-state-or-chemotype-when-evidence-supports-separation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T009 — Define positive, negative, decoy, and external validation sets before method tuning

Define positive, negative, decoy, and external validation sets before method tuning.

- **Routing name:** `define-positive-negative-decoy-and-external-validation-sets-before-method-tuning`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T010 — Generate a query-set manifest with structures, labels, provenance, uncertainty, and inclusion rationale

Generate a query-set manifest with structures, labels, provenance, uncertainty, and inclusion rationale.

- **Routing name:** `generate-a-query-set-manifest-with-structures-labels-provenance-uncertainty-and-inclusion-rationale`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Screening-library representation preparation

### MYR-D034-T011 — Apply a frozen chemical-standardization pipeline consistently to query and screening libraries

Apply a frozen chemical-standardization pipeline consistently to query and screening libraries.

- **Routing name:** `apply-a-frozen-chemical-standardization-pipeline-consistently-to-query-and-screening-libraries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T012 — Preserve stereoisomers, tautomers, salts, and protonation states according to the declared search representation

Preserve stereoisomers, tautomers, salts, and protonation states according to the declared search representation.

- **Routing name:** `preserve-stereoisomers-tautomers-salts-and-protonation-states-according-to-the-declared-search-representation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T013 — Generate canonical parent structures while maintaining links to purchasable or physical sample forms

Generate canonical parent structures while maintaining links to purchasable or physical sample forms.

- **Routing name:** `generate-canonical-parent-structures-while-maintaining-links-to-purchasable-or-physical-sample-forms`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T014 — Enumerate pH-relevant states only when the selected similarity method requires state-specific representations

Enumerate pH-relevant states only when the selected similarity method requires state-specific representations.

- **Routing name:** `enumerate-ph-relevant-states-only-when-the-selected-similarity-method-requires-state-specific-representations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T015 — Remove invalid, duplicate, or unsupported structures with explicit exclusion reasons

Remove invalid, duplicate, or unsupported structures with explicit exclusion reasons.

- **Routing name:** `remove-invalid-duplicate-or-unsupported-structures-with-explicit-exclusion-reasons`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T016 — Calculate fingerprints, descriptors, conformers, or embeddings using identical software and parameters across all molecules

Calculate fingerprints, descriptors, conformers, or embeddings using identical software and parameters across all molecules.

- **Routing name:** `calculate-fingerprints-descriptors-conformers-or-embeddings-using-identical-software-and-parameters-across-all-molecules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T017 — Validate that feature generation is deterministic under fixed versions and seeds

Validate that feature generation is deterministic under fixed versions and seeds.

- **Routing name:** `validate-that-feature-generation-is-deterministic-under-fixed-versions-and-seeds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T018 — Detect unsupported elements, molecular sizes, or chemotypes outside the selected representation method

Detect unsupported elements, molecular sizes, or chemotypes outside the selected representation method.

- **Routing name:** `detect-unsupported-elements-molecular-sizes-or-chemotypes-outside-the-selected-representation-method`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T019 — Freeze library version, entity identifiers, standardization rules, and feature checksums

Freeze library version, entity identifiers, standardization rules, and feature checksums.

- **Routing name:** `freeze-library-version-entity-identifiers-standardization-rules-and-feature-checksums`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T020 — Produce a representation-QC report with failures, warnings, and state-enumeration counts

Produce a representation-QC report with failures, warnings, and state-enumeration counts.

- **Routing name:** `produce-a-representation-qc-report-with-failures-warnings-and-state-enumeration-counts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Fingerprint and descriptor model selection

### MYR-D034-T021 — Generate circular fingerprints with declared radius, bit length, feature settings, and count or bit semantics

Generate circular fingerprints with declared radius, bit length, feature settings, and count or bit semantics.

- **Routing name:** `generate-circular-fingerprints-with-declared-radius-bit-length-feature-settings-and-count-or-bit-semantics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T022 — Generate path-, substructure-, atom-pair-, or pharmacophore-based fingerprints for complementary similarity views

Generate path-, substructure-, atom-pair-, or pharmacophore-based fingerprints for complementary similarity views.

- **Routing name:** `generate-path-substructure-atom-pair-or-pharmacophore-based-fingerprints-for-complementary-similarity-views`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T023 — Calculate physicochemical descriptor vectors with missing-value and scaling rules

Calculate physicochemical descriptor vectors with missing-value and scaling rules.

- **Routing name:** `calculate-physicochemical-descriptor-vectors-with-missing-value-and-scaling-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T024 — Assess fingerprint collision, sparsity, density, and information content on the screening library

Assess fingerprint collision, sparsity, density, and information content on the screening library.

- **Routing name:** `assess-fingerprint-collision-sparsity-density-and-information-content-on-the-screening-library`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T025 — Compare fingerprint similarity distributions for known actives, inactives, and random library pairs

Compare fingerprint similarity distributions for known actives, inactives, and random library pairs.

- **Routing name:** `compare-fingerprint-similarity-distributions-for-known-actives-inactives-and-random-library-pairs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T026 — Select similarity metrics compatible with binary, count, continuous, or asymmetric feature representations

Select similarity metrics compatible with binary, count, continuous, or asymmetric feature representations.

- **Routing name:** `select-similarity-metrics-compatible-with-binary-count-continuous-or-asymmetric-feature-representations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T027 — Test whether fingerprint chirality, tautomer, or feature settings materially alter known-neighbour retrieval

Test whether fingerprint chirality, tautomer, or feature settings materially alter known-neighbour retrieval.

- **Routing name:** `test-whether-fingerprint-chirality-tautomer-or-feature-settings-materially-alter-known-neighbour-retrieval`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T028 — Avoid combining descriptor families whose scale or redundancy dominates the distance metric

Avoid combining descriptor families whose scale or redundancy dominates the distance metric.

- **Routing name:** `avoid-combining-descriptor-families-whose-scale-or-redundancy-dominates-the-distance-metric`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T029 — Document method-specific invariances and blind spots for each molecular representation

Document method-specific invariances and blind spots for each molecular representation.

- **Routing name:** `document-method-specific-invariances-and-blind-spots-for-each-molecular-representation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T030 — Lock the representation and similarity configuration before prospective screening

Lock the representation and similarity configuration before prospective screening.

- **Routing name:** `lock-the-representation-and-similarity-configuration-before-prospective-screening`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Two-dimensional similarity searching

### MYR-D034-T031 — Compute exact or approximate nearest neighbours for every query ligand with reproducible indexing parameters

Compute exact or approximate nearest neighbours for every query ligand with reproducible indexing parameters.

- **Routing name:** `compute-exact-or-approximate-nearest-neighbours-for-every-query-ligand-with-reproducible-indexing-parameters`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T032 — Perform substructure searches for required query motifs using atom-mapped SMARTS definitions

Perform substructure searches for required query motifs using atom-mapped SMARTS definitions.

- **Routing name:** `perform-substructure-searches-for-required-query-motifs-using-atom-mapped-smarts-definitions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T033 — Perform maximum-common-substructure comparisons with timeout, ring, bond, and stereochemistry constraints

Perform maximum-common-substructure comparisons with timeout, ring, bond, and stereochemistry constraints.

- **Routing name:** `perform-maximum-common-substructure-comparisons-with-timeout-ring-bond-and-stereochemistry-constraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T034 — Use asymmetric similarity when query containment is more relevant than global molecular resemblance

Use asymmetric similarity when query containment is more relevant than global molecular resemblance.

- **Routing name:** `use-asymmetric-similarity-when-query-containment-is-more-relevant-than-global-molecular-resemblance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T035 — Combine multi-query results using declared maximum, mean, rank-fusion, or evidence-weighted rules

Combine multi-query results using declared maximum, mean, rank-fusion, or evidence-weighted rules.

- **Routing name:** `combine-multi-query-results-using-declared-maximum-mean-rank-fusion-or-evidence-weighted-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T036 — Calibrate similarity thresholds against retrospective active and inactive retrieval rather than arbitrary cutoffs

Calibrate similarity thresholds against retrospective active and inactive retrieval rather than arbitrary cutoffs.

- **Routing name:** `calibrate-similarity-thresholds-against-retrospective-active-and-inactive-retrieval-rather-than-arbitrary-cutoffs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T037 — Identify candidate molecules retrieved only because of common or nonspecific fragments

Identify candidate molecules retrieved only because of common or nonspecific fragments.

- **Routing name:** `identify-candidate-molecules-retrieved-only-because-of-common-or-nonspecific-fragments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T038 — Preserve the exact query molecule, feature overlap, similarity score, and matched substructure for every hit

Preserve the exact query molecule, feature overlap, similarity score, and matched substructure for every hit.

- **Routing name:** `preserve-the-exact-query-molecule-feature-overlap-similarity-score-and-matched-substructure-for-every-hit`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T039 — Apply deterministic tie-breaking using similarity, query evidence, and stable molecule identifiers

Apply deterministic tie-breaking using similarity, query evidence, and stable molecule identifiers.

- **Routing name:** `apply-deterministic-tie-breaking-using-similarity-query-evidence-and-stable-molecule-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T040 — Export a neighbour table with rank, score, query source, overlap explanation, and representation provenance

Export a neighbour table with rank, score, query source, overlap explanation, and representation provenance.

- **Routing name:** `export-a-neighbour-table-with-rank-score-query-source-overlap-explanation-and-representation-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Pharmacophore and three-dimensional similarity

### MYR-D034-T041 — Derive ligand-based pharmacophore hypotheses from aligned active compounds with uncertainty annotations

Derive ligand-based pharmacophore hypotheses from aligned active compounds with uncertainty annotations.

- **Routing name:** `derive-ligand-based-pharmacophore-hypotheses-from-aligned-active-compounds-with-uncertainty-annotations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T042 — Separate mandatory, optional, excluded-volume, and tolerance-radius pharmacophore features

Separate mandatory, optional, excluded-volume, and tolerance-radius pharmacophore features.

- **Routing name:** `separate-mandatory-optional-excluded-volume-and-tolerance-radius-pharmacophore-features`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T043 — Generate conformer ensembles with declared protonation, stereochemistry, energy, and diversity settings

Generate conformer ensembles with declared protonation, stereochemistry, energy, and diversity settings.

- **Routing name:** `generate-conformer-ensembles-with-declared-protonation-stereochemistry-energy-and-diversity-settings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T044 — Validate conformer generation against known bioactive conformations when structures are available

Validate conformer generation against known bioactive conformations when structures are available.

- **Routing name:** `validate-conformer-generation-against-known-bioactive-conformations-when-structures-are-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T045 — Screen conformers against pharmacophore hypotheses while retaining conformer and feature mappings

Screen conformers against pharmacophore hypotheses while retaining conformer and feature mappings.

- **Routing name:** `screen-conformers-against-pharmacophore-hypotheses-while-retaining-conformer-and-feature-mappings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T046 — Calculate shape and electrostatic similarity with method-specific normalization

Calculate shape and electrostatic similarity with method-specific normalization.

- **Routing name:** `calculate-shape-and-electrostatic-similarity-with-method-specific-normalization`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T047 — Assess alignment ambiguity and retain materially distinct high-scoring overlays

Assess alignment ambiguity and retain materially distinct high-scoring overlays.

- **Routing name:** `assess-alignment-ambiguity-and-retain-materially-distinct-high-scoring-overlays`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T048 — Penalize candidates satisfying pharmacophores only through implausible high-energy conformations

Penalize candidates satisfying pharmacophores only through implausible high-energy conformations.

- **Routing name:** `penalize-candidates-satisfying-pharmacophores-only-through-implausible-high-energy-conformations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T049 — Compare pharmacophore or shape retrieval with two-dimensional similarity to identify complementary hits

Compare pharmacophore or shape retrieval with two-dimensional similarity to identify complementary hits.

- **Routing name:** `compare-pharmacophore-or-shape-retrieval-with-two-dimensional-similarity-to-identify-complementary-hits`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T050 — Export aligned poses, matched features, conformer energies, and uncertainty for every retained candidate

Export aligned poses, matched features, conformer energies, and uncertainty for every retained candidate.

- **Routing name:** `export-aligned-poses-matched-features-conformer-energies-and-uncertainty-for-every-retained-candidate`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Learned embeddings and ligand-based prediction

### MYR-D034-T051 — Generate molecular embeddings with frozen model weights, tokenizer, pooling, and preprocessing versions

Generate molecular embeddings with frozen model weights, tokenizer, pooling, and preprocessing versions.

- **Routing name:** `generate-molecular-embeddings-with-frozen-model-weights-tokenizer-pooling-and-preprocessing-versions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T052 — Check whether screening molecules fall outside the chemical domain represented during model training

Check whether screening molecules fall outside the chemical domain represented during model training.

- **Routing name:** `check-whether-screening-molecules-fall-outside-the-chemical-domain-represented-during-model-training`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T053 — Prevent target or assay labels from leaking into unsupervised or supervised embedding benchmarks

Prevent target or assay labels from leaking into unsupervised or supervised embedding benchmarks.

- **Routing name:** `prevent-target-or-assay-labels-from-leaking-into-unsupervised-or-supervised-embedding-benchmarks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T054 — Compare embedding-neighbour retrieval with conventional fingerprints on temporally separated data

Compare embedding-neighbour retrieval with conventional fingerprints on temporally separated data.

- **Routing name:** `compare-embedding-neighbour-retrieval-with-conventional-fingerprints-on-temporally-separated-data`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T055 — Fine-tune ligand-based classifiers only with scaffold-aware and assay-aware data splits

Fine-tune ligand-based classifiers only with scaffold-aware and assay-aware data splits.

- **Routing name:** `fine-tune-ligand-based-classifiers-only-with-scaffold-aware-and-assay-aware-data-splits`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T056 — Calibrate predicted active probabilities on validation data representative of the prospective library

Calibrate predicted active probabilities on validation data representative of the prospective library.

- **Routing name:** `calibrate-predicted-active-probabilities-on-validation-data-representative-of-the-prospective-library`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T057 — Quantify prediction uncertainty across model seeds, ensembles, or conformer representations

Quantify prediction uncertainty across model seeds, ensembles, or conformer representations.

- **Routing name:** `quantify-prediction-uncertainty-across-model-seeds-ensembles-or-conformer-representations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T058 — Detect candidates ranked highly because of model artefacts, salts, tokenization failures, or unusual elements

Detect candidates ranked highly because of model artefacts, salts, tokenization failures, or unusual elements.

- **Routing name:** `detect-candidates-ranked-highly-because-of-model-artefacts-salts-tokenization-failures-or-unusual-elements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T059 — Use learned rankings as one evidence stream rather than replacing chemical similarity explanations

Use learned rankings as one evidence stream rather than replacing chemical similarity explanations.

- **Routing name:** `use-learned-rankings-as-one-evidence-stream-rather-than-replacing-chemical-similarity-explanations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T060 — Export model cards, training-set provenance, applicability status, and per-candidate uncertainty

Export model cards, training-set provenance, applicability status, and per-candidate uncertainty.

- **Routing name:** `export-model-cards-training-set-provenance-applicability-status-and-per-candidate-uncertainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Scaffold diversity, novelty, and analogue selection

### MYR-D034-T061 — Assign query and candidate scaffolds using a declared scaffold decomposition

Assign query and candidate scaffolds using a declared scaffold decomposition.

- **Routing name:** `assign-query-and-candidate-scaffolds-using-a-declared-scaffold-decomposition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T062 — Identify close analogues, matched molecular pairs, scaffold hops, and remote chemotype neighbours separately

Identify close analogues, matched molecular pairs, scaffold hops, and remote chemotype neighbours separately.

- **Routing name:** `identify-close-analogues-matched-molecular-pairs-scaffold-hops-and-remote-chemotype-neighbours-separately`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T063 — Calculate novelty relative to known actives, patents, internal compounds, and the query set

Calculate novelty relative to known actives, patents, internal compounds, and the query set.

- **Routing name:** `calculate-novelty-relative-to-known-actives-patents-internal-compounds-and-the-query-set`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T064 — Prevent trivial rediscovery of query duplicates, salts, stereochemical aliases, or near-identical registered compounds

Prevent trivial rediscovery of query duplicates, salts, stereochemical aliases, or near-identical registered compounds.

- **Routing name:** `prevent-trivial-rediscovery-of-query-duplicates-salts-stereochemical-aliases-or-near-identical-registered-compounds`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T065 — Cluster high-ranked candidates and cap per-cluster selection to preserve chemical diversity

Cluster high-ranked candidates and cap per-cluster selection to preserve chemical diversity.

- **Routing name:** `cluster-high-ranked-candidates-and-cap-per-cluster-selection-to-preserve-chemical-diversity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T066 — Select representatives balancing similarity, scaffold novelty, property constraints, and sample availability

Select representatives balancing similarity, scaffold novelty, property constraints, and sample availability.

- **Routing name:** `select-representatives-balancing-similarity-scaffold-novelty-property-constraints-and-sample-availability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T067 — Identify candidates that preserve key pharmacophore features while changing central scaffold topology

Identify candidates that preserve key pharmacophore features while changing central scaffold topology.

- **Routing name:** `identify-candidates-that-preserve-key-pharmacophore-features-while-changing-central-scaffold-topology`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T068 — Quantify whether novelty claims are robust across fingerprint and scaffold definitions

Quantify whether novelty claims are robust across fingerprint and scaffold definitions.

- **Routing name:** `quantify-whether-novelty-claims-are-robust-across-fingerprint-and-scaffold-definitions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T069 — Flag structurally novel candidates whose similarity evidence is weak or outside method applicability

Flag structurally novel candidates whose similarity evidence is weak or outside method applicability.

- **Routing name:** `flag-structurally-novel-candidates-whose-similarity-evidence-is-weak-or-outside-method-applicability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T070 — Produce a selection table separating analogue expansion, scaffold hopping, and exploratory chemical-space coverage

Produce a selection table separating analogue expansion, scaffold hopping, and exploratory chemical-space coverage.

- **Routing name:** `produce-a-selection-table-separating-analogue-expansion-scaffold-hopping-and-exploratory-chemical-space-coverage`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Bias, applicability, and confounder controls

### MYR-D034-T071 — Detect assay-series, publication, vendor, and chemical-series biases in the known-ligand set

Detect assay-series, publication, vendor, and chemical-series biases in the known-ligand set.

- **Routing name:** `detect-assay-series-publication-vendor-and-chemical-series-biases-in-the-known-ligand-set`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T072 — Assess whether high retrieval performance is driven by analogue leakage across train and test partitions

Assess whether high retrieval performance is driven by analogue leakage across train and test partitions.

- **Routing name:** `assess-whether-high-retrieval-performance-is-driven-by-analogue-leakage-across-train-and-test-partitions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T073 — Estimate applicability using nearest-neighbour distance, feature coverage, and representation validity

Estimate applicability using nearest-neighbour distance, feature coverage, and representation validity.

- **Routing name:** `estimate-applicability-using-nearest-neighbour-distance-feature-coverage-and-representation-validity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T074 — Identify frequent-hitter, aggregator, reactive, fluorescence, and other assay-liability motifs among top ranks

Identify frequent-hitter, aggregator, reactive, fluorescence, and other assay-liability motifs among top ranks.

- **Routing name:** `identify-frequent-hitter-aggregator-reactive-fluorescence-and-other-assay-liability-motifs-among-top-ranks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T075 — Compare candidate property distributions with known actives and the complete screening library

Compare candidate property distributions with known actives and the complete screening library.

- **Routing name:** `compare-candidate-property-distributions-with-known-actives-and-the-complete-screening-library`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T076 — Detect target-family promiscuous scaffolds that may inflate apparent ligand-based relevance

Detect target-family promiscuous scaffolds that may inflate apparent ligand-based relevance.

- **Routing name:** `detect-target-family-promiscuous-scaffolds-that-may-inflate-apparent-ligand-based-relevance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T077 — Stratify performance by scaffold, potency range, molecular size, charge, and stereochemical complexity

Stratify performance by scaffold, potency range, molecular size, charge, and stereochemical complexity.

- **Routing name:** `stratify-performance-by-scaffold-potency-range-molecular-size-charge-and-stereochemical-complexity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T078 — Run query-ablation analysis to identify single ligands dominating the final ranking

Run query-ablation analysis to identify single ligands dominating the final ranking.

- **Routing name:** `run-query-ablation-analysis-to-identify-single-ligands-dominating-the-final-ranking`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T079 — Report no-call status when query evidence is too sparse, heterogeneous, or chemically narrow for reliable screening

Report no-call status when query evidence is too sparse, heterogeneous, or chemically narrow for reliable screening.

- **Routing name:** `report-no-call-status-when-query-evidence-is-too-sparse-heterogeneous-or-chemically-narrow-for-reliable-screening`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T080 — Create a candidate-level applicability and liability report independent of the similarity score

Create a candidate-level applicability and liability report independent of the similarity score.

- **Routing name:** `create-a-candidate-level-applicability-and-liability-report-independent-of-the-similarity-score`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Retrospective benchmarking and ranking integration

### MYR-D034-T081 — Construct retrospective benchmarks with time-split or scaffold-split actives and property-matched decoys

Construct retrospective benchmarks with time-split or scaffold-split actives and property-matched decoys.

- **Routing name:** `construct-retrospective-benchmarks-with-time-split-or-scaffold-split-actives-and-property-matched-decoys`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T082 — Measure early enrichment, precision, recall, ranking quality, scaffold recovery, and confidence intervals

Measure early enrichment, precision, recall, ranking quality, scaffold recovery, and confidence intervals.

- **Routing name:** `measure-early-enrichment-precision-recall-ranking-quality-scaffold-recovery-and-confidence-intervals`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T083 — Compare similarity methods using identical query, library, standardization, and benchmark definitions

Compare similarity methods using identical query, library, standardization, and benchmark definitions.

- **Routing name:** `compare-similarity-methods-using-identical-query-library-standardization-and-benchmark-definitions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T084 — Tune thresholds and fusion weights only within training or validation partitions

Tune thresholds and fusion weights only within training or validation partitions.

- **Routing name:** `tune-thresholds-and-fusion-weights-only-within-training-or-validation-partitions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T085 — Evaluate whether consensus methods improve prospective-relevant metrics rather than average rank alone

Evaluate whether consensus methods improve prospective-relevant metrics rather than average rank alone.

- **Routing name:** `evaluate-whether-consensus-methods-improve-prospective-relevant-metrics-rather-than-average-rank-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T086 — Estimate uncertainty through bootstrap resampling of queries, actives, and screening candidates

Estimate uncertainty through bootstrap resampling of queries, actives, and screening candidates.

- **Routing name:** `estimate-uncertainty-through-bootstrap-resampling-of-queries-actives-and-screening-candidates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T087 — Inspect false positives and false negatives for representation, assay, and mechanism explanations

Inspect false positives and false negatives for representation, assay, and mechanism explanations.

- **Routing name:** `inspect-false-positives-and-false-negatives-for-representation-assay-and-mechanism-explanations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T088 — Select the production ranking method using prespecified benchmark criteria and complexity penalties

Select the production ranking method using prespecified benchmark criteria and complexity penalties.

- **Routing name:** `select-the-production-ranking-method-using-prespecified-benchmark-criteria-and-complexity-penalties`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T089 — Preserve alternate rankings when no method consistently dominates across target-relevant metrics

Preserve alternate rankings when no method consistently dominates across target-relevant metrics.

- **Routing name:** `preserve-alternate-rankings-when-no-method-consistently-dominates-across-target-relevant-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T090 — Generate a benchmark report with datasets, splits, metrics, uncertainty, failure modes, and selected configuration

Generate a benchmark report with datasets, splits, metrics, uncertainty, failure modes, and selected configuration.

- **Routing name:** `generate-a-benchmark-report-with-datasets-splits-metrics-uncertainty-failure-modes-and-selected-configuration`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Prospective release and experimental handoff

### MYR-D034-T091 — Generate a final candidate rank integrating similarity, pharmacophore, shape, learned, liability, and diversity evidence

Generate a final candidate rank integrating similarity, pharmacophore, shape, learned, liability, and diversity evidence.

- **Routing name:** `generate-a-final-candidate-rank-integrating-similarity-pharmacophore-shape-learned-liability-and-diversity-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T092 — Preserve component scores and prevent missing evidence from being interpreted as a favourable score

Preserve component scores and prevent missing evidence from being interpreted as a favourable score.

- **Routing name:** `preserve-component-scores-and-prevent-missing-evidence-from-being-interpreted-as-a-favourable-score`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T093 — Attach purchasability, sample identity, purity, concentration, and inventory status when available

Attach purchasability, sample identity, purity, concentration, and inventory status when available.

- **Routing name:** `attach-purchasability-sample-identity-purity-concentration-and-inventory-status-when-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T094 — Create machine-readable advance, reserve, deprioritize, and no-call categories with rationale

Create machine-readable advance, reserve, deprioritize, and no-call categories with rationale.

- **Routing name:** `create-machine-readable-advance-reserve-deprioritize-and-no-call-categories-with-rationale`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T095 — Hash query sets, screening library, features, models, parameters, and released rankings

Hash query sets, screening library, features, models, parameters, and released rankings.

- **Routing name:** `hash-query-sets-screening-library-features-models-parameters-and-released-rankings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T096 — Provide exact substructure, feature, overlay, or neighbour explanations supporting every advanced candidate

Provide exact substructure, feature, overlay, or neighbour explanations supporting every advanced candidate.

- **Routing name:** `provide-exact-substructure-feature-overlay-or-neighbour-explanations-supporting-every-advanced-candidate`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T097 — Require chemistry and assay review of novelty, liabilities, identity, and prospective test feasibility

Require chemistry and assay review of novelty, liabilities, identity, and prospective test feasibility.

- **Routing name:** `require-chemistry-and-assay-review-of-novelty-liabilities-identity-and-prospective-test-feasibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T098 — Block potency or binding claims for untested candidates regardless of virtual-screen rank

Block potency or binding claims for untested candidates regardless of virtual-screen rank.

- **Routing name:** `block-potency-or-binding-claims-for-untested-candidates-regardless-of-virtual-screen-rank`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T099 — Archive rejected candidates and filtering reasons for future model evaluation

Archive rejected candidates and filtering reasons for future model evaluation.

- **Routing name:** `archive-rejected-candidates-and-filtering-reasons-for-future-model-evaluation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D034-T100 — Release the ligand-based virtual-screen package only when benchmark, applicability, provenance, and review gates pass

Release the ligand-based virtual-screen package only when benchmark, applicability, provenance, and review gates pass.

- **Routing name:** `release-the-ligand-based-virtual-screen-package-only-when-benchmark-applicability-provenance-and-review-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
