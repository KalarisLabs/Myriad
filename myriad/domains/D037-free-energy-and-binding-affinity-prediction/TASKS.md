# D037 — Free-Energy and Binding-Affinity Prediction

Batch **004** · 10 workstreams · 100 tasks

## 01. Scientific question and thermodynamic-state definition

### MYR-D037-T001 — Define whether the objective is relative binding, absolute binding, hydration, solvation, partition, or conformational free energy

Define whether the objective is relative binding, absolute binding, hydration, solvation, partition, or conformational free energy.

- **Routing name:** `define-whether-the-objective-is-relative-binding-absolute-binding-hydration-solvation-partition-or-conformational-free-energy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T002 — Specify temperature, pressure, pH assumptions, ionic strength, standard state, and restraint conventions

Specify temperature, pressure, pH assumptions, ionic strength, standard state, and restraint conventions.

- **Routing name:** `specify-temperature-pressure-ph-assumptions-ionic-strength-standard-state-and-restraint-conventions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T003 — Define receptor sequence, construct, protonation, cofactors, ligands, waters, ions, and biological state

Define receptor sequence, construct, protonation, cofactors, ligands, waters, ions, and biological state.

- **Routing name:** `define-receptor-sequence-construct-protonation-cofactors-ligands-waters-ions-and-biological-state`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T004 — Distinguish experimental affinity observables and assay conditions from the simulated thermodynamic quantity

Distinguish experimental affinity observables and assay conditions from the simulated thermodynamic quantity.

- **Routing name:** `distinguish-experimental-affinity-observables-and-assay-conditions-from-the-simulated-thermodynamic-quantity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T005 — Identify ligand states, stereoisomers, tautomers, protonation states, and binding modes requiring separate treatment

Identify ligand states, stereoisomers, tautomers, protonation states, and binding modes requiring separate treatment.

- **Routing name:** `identify-ligand-states-stereoisomers-tautomers-protonation-states-and-binding-modes-requiring-separate-treatment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T006 — Define the comparison graph and reference compounds before simulations begin

Define the comparison graph and reference compounds before simulations begin.

- **Routing name:** `define-the-comparison-graph-and-reference-compounds-before-simulations-begin`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T007 — Specify acceptance criteria for uncertainty, cycle closure, overlap, convergence, and experimental agreement

Specify acceptance criteria for uncertainty, cycle closure, overlap, convergence, and experimental agreement.

- **Routing name:** `specify-acceptance-criteria-for-uncertainty-cycle-closure-overlap-convergence-and-experimental-agreement`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T008 — Identify transformations involving net charge, ring changes, scaffold changes, or binding-mode changes as elevated risk

Identify transformations involving net charge, ring changes, scaffold changes, or binding-mode changes as elevated risk.

- **Routing name:** `identify-transformations-involving-net-charge-ring-changes-scaffold-changes-or-binding-mode-changes-as-elevated-risk`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T009 — Establish negative controls and known reference transformations for protocol qualification

Establish negative controls and known reference transformations for protocol qualification.

- **Routing name:** `establish-negative-controls-and-known-reference-transformations-for-protocol-qualification`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T010 — Freeze scientific scope, states, protocol family, and analysis plan in a campaign manifest

Freeze scientific scope, states, protocol family, and analysis plan in a campaign manifest.

- **Routing name:** `freeze-scientific-scope-states-protocol-family-and-analysis-plan-in-a-campaign-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Ligand mapping and alchemical-network design

### MYR-D037-T011 — Validate ligand connectivity, stereochemistry, charge, protonation, and tautomer assignments before atom mapping

Validate ligand connectivity, stereochemistry, charge, protonation, and tautomer assignments before atom mapping.

- **Routing name:** `validate-ligand-connectivity-stereochemistry-charge-protonation-and-tautomer-assignments-before-atom-mapping`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T012 — Generate atom mappings with element, bond, ring, chirality, and core-preservation constraints

Generate atom mappings with element, bond, ring, chirality, and core-preservation constraints.

- **Routing name:** `generate-atom-mappings-with-element-bond-ring-chirality-and-core-preservation-constraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T013 — Reject mappings that invert stable stereochemistry or mutate chemically non-equivalent ring systems without justification

Reject mappings that invert stable stereochemistry or mutate chemically non-equivalent ring systems without justification.

- **Routing name:** `reject-mappings-that-invert-stable-stereochemistry-or-mutate-chemically-non-equivalent-ring-systems-without-justification`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T014 — Score candidate edges for common core, charge change, topology complexity, and expected sampling difficulty

Score candidate edges for common core, charge change, topology complexity, and expected sampling difficulty.

- **Routing name:** `score-candidate-edges-for-common-core-charge-change-topology-complexity-and-expected-sampling-difficulty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T015 — Construct a connected ligand network with redundant cycles for internal consistency assessment

Construct a connected ligand network with redundant cycles for internal consistency assessment.

- **Routing name:** `construct-a-connected-ligand-network-with-redundant-cycles-for-internal-consistency-assessment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T016 — Avoid networks dependent on a single high-risk edge or poorly characterized reference ligand

Avoid networks dependent on a single high-risk edge or poorly characterized reference ligand.

- **Routing name:** `avoid-networks-dependent-on-a-single-high-risk-edge-or-poorly-characterized-reference-ligand`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T017 — Balance edge count, computational cost, chemical locality, and graph robustness

Balance edge count, computational cost, chemical locality, and graph robustness.

- **Routing name:** `balance-edge-count-computational-cost-chemical-locality-and-graph-robustness`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T018 — Plan separated-topology or alternative protocols for transformations unsuitable for a standard single-topology path

Plan separated-topology or alternative protocols for transformations unsuitable for a standard single-topology path.

- **Routing name:** `plan-separated-topology-or-alternative-protocols-for-transformations-unsuitable-for-a-standard-single-topology-path`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T019 — Visualize mappings and network topology for chemistry review before execution

Visualize mappings and network topology for chemistry review before execution.

- **Routing name:** `visualize-mappings-and-network-topology-for-chemistry-review-before-execution`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T020 — Export atom mappings, edge risk labels, network rationale, and stable identifiers

Export atom mappings, edge risk labels, network rationale, and stable identifiers.

- **Routing name:** `export-atom-mappings-edge-risk-labels-network-rationale-and-stable-identifiers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Force-field, charge, and parameter preparation

### MYR-D037-T021 — Assign protein, nucleic-acid, lipid, ion, water, cofactor, and ligand force fields with compatibility checks

Assign protein, nucleic-acid, lipid, ion, water, cofactor, and ligand force fields with compatibility checks.

- **Routing name:** `assign-protein-nucleic-acid-lipid-ion-water-cofactor-and-ligand-force-fields-with-compatibility-checks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T022 — Generate ligand partial charges using one declared method and preserved conformer inputs

Generate ligand partial charges using one declared method and preserved conformer inputs.

- **Routing name:** `generate-ligand-partial-charges-using-one-declared-method-and-preserved-conformer-inputs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T023 — Validate atom types, valence terms, improper torsions, ring parameters, and formal charge consistency

Validate atom types, valence terms, improper torsions, ring parameters, and formal charge consistency.

- **Routing name:** `validate-atom-types-valence-terms-improper-torsions-ring-parameters-and-formal-charge-consistency`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T024 — Identify unsupported cofactors, metals, covalent bonds, unusual elements, and post-translational modifications

Identify unsupported cofactors, metals, covalent bonds, unusual elements, and post-translational modifications.

- **Routing name:** `identify-unsupported-cofactors-metals-covalent-bonds-unusual-elements-and-post-translational-modifications`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T025 — Compare generated parameters against trusted analogues or quantum calculations for high-risk chemistries

Compare generated parameters against trusted analogues or quantum calculations for high-risk chemistries.

- **Routing name:** `compare-generated-parameters-against-trusted-analogues-or-quantum-calculations-for-high-risk-chemistries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T026 — Preserve parameter files and prevent mixing incompatible force-field families silently

Preserve parameter files and prevent mixing incompatible force-field families silently.

- **Routing name:** `preserve-parameter-files-and-prevent-mixing-incompatible-force-field-families-silently`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T027 — Check total system charge and ion composition after parameterization

Check total system charge and ion composition after parameterization.

- **Routing name:** `check-total-system-charge-and-ion-composition-after-parameterization`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T028 — Assess whether alternative protonation or tautomer states require separate free-energy branches

Assess whether alternative protonation or tautomer states require separate free-energy branches.

- **Routing name:** `assess-whether-alternative-protonation-or-tautomer-states-require-separate-free-energy-branches`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T029 — Hash all parameter, charge, and topology artifacts with software and version provenance

Hash all parameter, charge, and topology artifacts with software and version provenance.

- **Routing name:** `hash-all-parameter-charge-and-topology-artifacts-with-software-and-version-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T030 — Block campaign execution when chemically significant parameters remain unvalidated

Block campaign execution when chemically significant parameters remain unvalidated.

- **Routing name:** `block-campaign-execution-when-chemically-significant-parameters-remain-unvalidated`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Complex and solvent system construction

### MYR-D037-T031 — Place each ligand state into a validated binding pose and preserve alternate credible pose branches

Place each ligand state into a validated binding pose and preserve alternate credible pose branches.

- **Routing name:** `place-each-ligand-state-into-a-validated-binding-pose-and-preserve-alternate-credible-pose-branches`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T032 — Build receptor–ligand complexes without introducing steric clashes or broken coordination geometry

Build receptor–ligand complexes without introducing steric clashes or broken coordination geometry.

- **Routing name:** `build-receptor-ligand-complexes-without-introducing-steric-clashes-or-broken-coordination-geometry`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T033 — Retain or remove crystallographic waters using declared structural and thermodynamic criteria

Retain or remove crystallographic waters using declared structural and thermodynamic criteria.

- **Routing name:** `retain-or-remove-crystallographic-waters-using-declared-structural-and-thermodynamic-criteria`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T034 — Solvate complex and solvent legs with matched water, box, salt, and ionic-strength conventions

Solvate complex and solvent legs with matched water, box, salt, and ionic-strength conventions.

- **Routing name:** `solvate-complex-and-solvent-legs-with-matched-water-box-salt-and-ionic-strength-conventions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T035 — Apply standard-state, orientational, positional, or conformational restraints with explicit definitions

Apply standard-state, orientational, positional, or conformational restraints with explicit definitions.

- **Routing name:** `apply-standard-state-orientational-positional-or-conformational-restraints-with-explicit-definitions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T036 — Create neutralizing or alchemical-ion strategies for charge-changing transformations

Create neutralizing or alchemical-ion strategies for charge-changing transformations.

- **Routing name:** `create-neutralizing-or-alchemical-ion-strategies-for-charge-changing-transformations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T037 — Validate periodic box dimensions, solute separation, atom counts, and net charges across end states

Validate periodic box dimensions, solute separation, atom counts, and net charges across end states.

- **Routing name:** `validate-periodic-box-dimensions-solute-separation-atom-counts-and-net-charges-across-end-states`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T038 — Minimize systems and inspect large forces, distorted geometry, and unstable cofactors

Minimize systems and inspect large forces, distorted geometry, and unstable cofactors.

- **Routing name:** `minimize-systems-and-inspect-large-forces-distorted-geometry-and-unstable-cofactors`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T039 — Generate end-state coordinate checks confirming mapped atoms and restraints correspond exactly

Generate end-state coordinate checks confirming mapped atoms and restraints correspond exactly.

- **Routing name:** `generate-end-state-coordinate-checks-confirming-mapped-atoms-and-restraints-correspond-exactly`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T040 — Produce a system-build report reconciling all components, transformations, restraints, and checksums

Produce a system-build report reconciling all components, transformations, restraints, and checksums.

- **Routing name:** `produce-a-system-build-report-reconciling-all-components-transformations-restraints-and-checksums`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Equilibration and sampling execution

### MYR-D037-T041 — Run staged minimization and equilibration with preserved checkpoints and restraint schedules

Run staged minimization and equilibration with preserved checkpoints and restraint schedules.

- **Routing name:** `run-staged-minimization-and-equilibration-with-preserved-checkpoints-and-restraint-schedules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T042 — Confirm stable temperature, pressure, density, energy, and binding-site geometry before production

Confirm stable temperature, pressure, density, energy, and binding-site geometry before production.

- **Routing name:** `confirm-stable-temperature-pressure-density-energy-and-binding-site-geometry-before-production`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T043 — Select lambda schedules or nonequilibrium switching protocols appropriate to transformation difficulty

Select lambda schedules or nonequilibrium switching protocols appropriate to transformation difficulty.

- **Routing name:** `select-lambda-schedules-or-nonequilibrium-switching-protocols-appropriate-to-transformation-difficulty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T044 — Run independent replicas with recorded seeds rather than one prolonged trajectory alone

Run independent replicas with recorded seeds rather than one prolonged trajectory alone.

- **Routing name:** `run-independent-replicas-with-recorded-seeds-rather-than-one-prolonged-trajectory-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T045 — Allocate sampling adaptively only using prespecified convergence and overlap diagnostics

Allocate sampling adaptively only using prespecified convergence and overlap diagnostics.

- **Routing name:** `allocate-sampling-adaptively-only-using-prespecified-convergence-and-overlap-diagnostics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T046 — Monitor ligand pose, key waters, protein conformation, rotamers, ions, and restraint coordinates during sampling

Monitor ligand pose, key waters, protein conformation, rotamers, ions, and restraint coordinates during sampling.

- **Routing name:** `monitor-ligand-pose-key-waters-protein-conformation-rotamers-ions-and-restraint-coordinates-during-sampling`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T047 — Detect ligand unbinding, pocket collapse, phase changes, vacuum bubbles, or unstable integration

Detect ligand unbinding, pocket collapse, phase changes, vacuum bubbles, or unstable integration.

- **Routing name:** `detect-ligand-unbinding-pocket-collapse-phase-changes-vacuum-bubbles-or-unstable-integration`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T048 — Preserve trajectory, energy, checkpoint, and log files for every leg, edge, lambda state, and replica

Preserve trajectory, energy, checkpoint, and log files for every leg, edge, lambda state, and replica.

- **Routing name:** `preserve-trajectory-energy-checkpoint-and-log-files-for-every-leg-edge-lambda-state-and-replica`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T049 — Reconcile planned and completed simulation time and identify truncated or restarted segments

Reconcile planned and completed simulation time and identify truncated or restarted segments.

- **Routing name:** `reconcile-planned-and-completed-simulation-time-and-identify-truncated-or-restarted-segments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T050 — Block analysis of simulations that fail physical-stability or checkpoint-continuity checks

Block analysis of simulations that fail physical-stability or checkpoint-continuity checks.

- **Routing name:** `block-analysis-of-simulations-that-fail-physical-stability-or-checkpoint-continuity-checks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Estimator, overlap, and convergence analysis

### MYR-D037-T051 — Estimate free-energy differences with an estimator appropriate to the sampled protocol

Estimate free-energy differences with an estimator appropriate to the sampled protocol.

- **Routing name:** `estimate-free-energy-differences-with-an-estimator-appropriate-to-the-sampled-protocol`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T052 — Calculate statistical uncertainty with correlation and effective-sample-size corrections

Calculate statistical uncertainty with correlation and effective-sample-size corrections.

- **Routing name:** `calculate-statistical-uncertainty-with-correlation-and-effective-sample-size-corrections`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T053 — Assess neighbouring-state phase-space overlap and identify disconnected or poorly overlapping states

Assess neighbouring-state phase-space overlap and identify disconnected or poorly overlapping states.

- **Routing name:** `assess-neighbouring-state-phase-space-overlap-and-identify-disconnected-or-poorly-overlapping-states`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T054 — Compare forward and reverse work distributions for nonequilibrium calculations

Compare forward and reverse work distributions for nonequilibrium calculations.

- **Routing name:** `compare-forward-and-reverse-work-distributions-for-nonequilibrium-calculations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T055 — Inspect free-energy estimates as a function of accumulated sampling time

Inspect free-energy estimates as a function of accumulated sampling time.

- **Routing name:** `inspect-free-energy-estimates-as-a-function-of-accumulated-sampling-time`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T056 — Compare independent replicas for agreement beyond nominal estimator uncertainty

Compare independent replicas for agreement beyond nominal estimator uncertainty.

- **Routing name:** `compare-independent-replicas-for-agreement-beyond-nominal-estimator-uncertainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T057 — Quantify equilibration discard, autocorrelation, and effective uncorrelated sample count

Quantify equilibration discard, autocorrelation, and effective uncorrelated sample count.

- **Routing name:** `quantify-equilibration-discard-autocorrelation-and-effective-uncorrelated-sample-count`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T058 — Detect hidden metastable states through ligand, protein, water, and torsional observables

Detect hidden metastable states through ligand, protein, water, and torsional observables.

- **Routing name:** `detect-hidden-metastable-states-through-ligand-protein-water-and-torsional-observables`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T059 — Assign converged, provisionally converged, unconverged, failed, or no-call status to each edge

Assign converged, provisionally converged, unconverged, failed, or no-call status to each edge.

- **Routing name:** `assign-converged-provisionally-converged-unconverged-failed-or-no-call-status-to-each-edge`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T060 — Export per-edge estimates, uncertainties, overlap diagnostics, sampling diagnostics, and failure reasons

Export per-edge estimates, uncertainties, overlap diagnostics, sampling diagnostics, and failure reasons.

- **Routing name:** `export-per-edge-estimates-uncertainties-overlap-diagnostics-sampling-diagnostics-and-failure-reasons`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Cycle closure and network inference

### MYR-D037-T061 — Calculate thermodynamic cycle-closure errors for all independent cycles in the ligand network

Calculate thermodynamic cycle-closure errors for all independent cycles in the ligand network.

- **Routing name:** `calculate-thermodynamic-cycle-closure-errors-for-all-independent-cycles-in-the-ligand-network`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T062 — Identify alchemical edges disproportionately responsible for inconsistent thermodynamic cycle closures

Identify alchemical edges disproportionately responsible for inconsistent thermodynamic cycle closures.

- **Routing name:** `identify-alchemical-edges-disproportionately-responsible-for-inconsistent-thermodynamic-cycle-closures`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T063 — Fit network-wide ligand free energies using uncertainty-aware maximum-likelihood or equivalent inference

Fit network-wide ligand free energies using uncertainty-aware maximum-likelihood or equivalent inference.

- **Routing name:** `fit-network-wide-ligand-free-energies-using-uncertainty-aware-maximum-likelihood-or-equivalent-inference`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T064 — Compare direct and indirect estimates for transformations supported by redundant paths

Compare direct and indirect estimates for transformations supported by redundant paths.

- **Routing name:** `compare-direct-and-indirect-estimates-for-transformations-supported-by-redundant-paths`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T065 — Propagate edge uncertainty and covariance into ligand-level estimates where supported

Propagate edge uncertainty and covariance into ligand-level estimates where supported.

- **Routing name:** `propagate-edge-uncertainty-and-covariance-into-ligand-level-estimates-where-supported`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T066 — Detect disconnected network components or weak bridges that destabilize reference-based estimates

Detect disconnected network components or weak bridges that destabilize reference-based estimates.

- **Routing name:** `detect-disconnected-network-components-or-weak-bridges-that-destabilize-reference-based-estimates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T067 — Assess rank sensitivity to removal of high-risk or inconsistent edges

Assess rank sensitivity to removal of high-risk or inconsistent edges.

- **Routing name:** `assess-rank-sensitivity-to-removal-of-high-risk-or-inconsistent-edges`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T068 — Replan targeted replicate or bridging calculations for unresolved network regions

Replan targeted replicate or bridging calculations for unresolved network regions.

- **Routing name:** `replan-targeted-replicate-or-bridging-calculations-for-unresolved-network-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T069 — Preserve raw edge estimates separately from network-adjusted values

Preserve raw edge estimates separately from network-adjusted values.

- **Routing name:** `preserve-raw-edge-estimates-separately-from-network-adjusted-values`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T070 — Generate a network-consistency report with cycles, residuals, leverage, and remediation status

Generate a network-consistency report with cycles, residuals, leverage, and remediation status.

- **Routing name:** `generate-a-network-consistency-report-with-cycles-residuals-leverage-and-remediation-status`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Experimental comparison and uncertainty calibration

### MYR-D037-T071 — Harmonize experimental affinity type, units, temperature, construct, protonation context, and assay conditions

Harmonize experimental affinity type, units, temperature, construct, protonation context, and assay conditions.

- **Routing name:** `harmonize-experimental-affinity-type-units-temperature-construct-protonation-context-and-assay-conditions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T072 — Propagate experimental replicate and assay uncertainty rather than treating measurements as exact

Propagate experimental replicate and assay uncertainty rather than treating measurements as exact.

- **Routing name:** `propagate-experimental-replicate-and-assay-uncertainty-rather-than-treating-measurements-as-exact`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T073 — Compare predicted and experimental relative differences on matched ligand and state definitions

Compare predicted and experimental relative differences on matched ligand and state definitions.

- **Routing name:** `compare-predicted-and-experimental-relative-differences-on-matched-ligand-and-state-definitions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T074 — Report mean error, absolute error, rank correlation, calibration, and confidence intervals

Report mean error, absolute error, rank correlation, calibration, and confidence intervals.

- **Routing name:** `report-mean-error-absolute-error-rank-correlation-calibration-and-confidence-intervals`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T075 — Assess whether observed discrepancies cluster by chemotype, charge change, pose, or receptor state

Assess whether observed discrepancies cluster by chemotype, charge change, pose, or receptor state.

- **Routing name:** `assess-whether-observed-discrepancies-cluster-by-chemotype-charge-change-pose-or-receptor-state`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T076 — Use prospective or temporally held-out compounds for protocol evaluation when available

Use prospective or temporally held-out compounds for protocol evaluation when available.

- **Routing name:** `use-prospective-or-temporally-held-out-compounds-for-protocol-evaluation-when-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T077 — Distinguish force-field bias, sampling failure, state mismatch, and experimental inconsistency

Distinguish force-field bias, sampling failure, state mismatch, and experimental inconsistency.

- **Routing name:** `distinguish-force-field-bias-sampling-failure-state-mismatch-and-experimental-inconsistency`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T078 — Calibrate nominal prediction uncertainty against held-out observed experimental residual distributions

Calibrate nominal prediction uncertainty against held-out observed experimental residual distributions.

- **Routing name:** `calibrate-nominal-prediction-uncertainty-against-held-out-observed-experimental-residual-distributions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T079 — Avoid refitting protocol parameters to the same benchmark used for final performance reporting

Avoid refitting protocol parameters to the same benchmark used for final performance reporting.

- **Routing name:** `avoid-refitting-protocol-parameters-to-the-same-benchmark-used-for-final-performance-reporting`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T080 — Produce an experiment-comparison table with matched definitions, uncertainty, residuals, and interpretation

Produce an experiment-comparison table with matched definitions, uncertainty, residuals, and interpretation.

- **Routing name:** `produce-an-experiment-comparison-table-with-matched-definitions-uncertainty-residuals-and-interpretation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Sensitivity analysis and failure remediation

### MYR-D037-T081 — Repeat high-impact edges with alternative seeds to test sampling sensitivity

Repeat high-impact edges with alternative seeds to test sampling sensitivity.

- **Routing name:** `repeat-high-impact-edges-with-alternative-seeds-to-test-sampling-sensitivity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T082 — Test alternate ligand protonation, tautomer, stereochemical, or pose states when chemically plausible

Test alternate ligand protonation, tautomer, stereochemical, or pose states when chemically plausible.

- **Routing name:** `test-alternate-ligand-protonation-tautomer-stereochemical-or-pose-states-when-chemically-plausible`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T083 — Test key receptor protonation, water, side-chain, or conformational hypotheses

Test key receptor protonation, water, side-chain, or conformational hypotheses.

- **Routing name:** `test-key-receptor-protonation-water-side-chain-or-conformational-hypotheses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T084 — Assess sensitivity to force field, charge method, lambda schedule, restraint, and box construction

Assess sensitivity to force field, charge method, lambda schedule, restraint, and box construction.

- **Routing name:** `assess-sensitivity-to-force-field-charge-method-lambda-schedule-restraint-and-box-construction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T085 — Redesign atom mappings that induce unnecessary ring, charge, or stereochemical complexity

Redesign atom mappings that induce unnecessary ring, charge, or stereochemical complexity.

- **Routing name:** `redesign-atom-mappings-that-induce-unnecessary-ring-charge-or-stereochemical-complexity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T086 — Add intermediate ligands or alternate network paths to replace unstable transformations

Add intermediate ligands or alternate network paths to replace unstable transformations.

- **Routing name:** `add-intermediate-ligands-or-alternate-network-paths-to-replace-unstable-transformations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T087 — Extend sampling only when diagnostics indicate additional sampling can resolve the failure

Extend sampling only when diagnostics indicate additional sampling can resolve the failure.

- **Routing name:** `extend-sampling-only-when-diagnostics-indicate-additional-sampling-can-resolve-the-failure`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T088 — Avoid pooling incompatible state branches merely to reduce uncertainty

Avoid pooling incompatible state branches merely to reduce uncertainty.

- **Routing name:** `avoid-pooling-incompatible-state-branches-merely-to-reduce-uncertainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T089 — Document every rerun, protocol deviation, exclusion, and superseded estimate

Document every rerun, protocol deviation, exclusion, and superseded estimate.

- **Routing name:** `document-every-rerun-protocol-deviation-exclusion-and-superseded-estimate`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T090 — Generate a remediation decision table distinguishing fixable technical failures from model-form limitations

Generate a remediation decision table distinguishing fixable technical failures from model-form limitations.

- **Routing name:** `generate-a-remediation-decision-table-distinguishing-fixable-technical-failures-from-model-form-limitations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Campaign release and governance

### MYR-D037-T091 — Package chemical states, receptor states, mappings, networks, parameters, coordinates, trajectories, logs, and analyses

Package chemical states, receptor states, mappings, networks, parameters, coordinates, trajectories, logs, and analyses.

- **Routing name:** `package-chemical-states-receptor-states-mappings-networks-parameters-coordinates-trajectories-logs-and-analyses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T092 — Record software versions, protocol settings, hardware, precision, random seeds, and execution environment

Record software versions, protocol settings, hardware, precision, random seeds, and execution environment.

- **Routing name:** `record-software-versions-protocol-settings-hardware-precision-random-seeds-and-execution-environment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T093 — Hash every input, topology, parameter, run plan, simulation output, and released result

Hash every input, topology, parameter, run plan, simulation output, and released result.

- **Routing name:** `hash-every-input-topology-parameter-run-plan-simulation-output-and-released-result`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T094 — Create stable identifiers linking molecule, state, edge, leg, lambda state, replica, and analysis version

Create stable identifiers linking molecule, state, edge, leg, lambda state, replica, and analysis version.

- **Routing name:** `create-stable-identifiers-linking-molecule-state-edge-leg-lambda-state-replica-and-analysis-version`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T095 — Generate machine-readable pass, warning, fail, and no-call statuses at simulation, edge, and ligand levels

Generate machine-readable pass, warning, fail, and no-call statuses at simulation, edge, and ligand levels.

- **Routing name:** `generate-machine-readable-pass-warning-fail-and-no-call-statuses-at-simulation-edge-and-ligand-levels`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T096 — Require chemistry, structural, simulation, and assay review for decision-critical campaigns

Require chemistry, structural, simulation, and assay review for decision-critical campaigns.

- **Routing name:** `require-chemistry-structural-simulation-and-assay-review-for-decision-critical-campaigns`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T097 — Prevent interpretation of unconverged or state-ambiguous estimates as precise affinity predictions

Prevent interpretation of unconverged or state-ambiguous estimates as precise affinity predictions.

- **Routing name:** `prevent-interpretation-of-unconverged-or-state-ambiguous-estimates-as-precise-affinity-predictions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T098 — Archive raw and superseded results to support prospective validation and audit

Archive raw and superseded results to support prospective validation and audit.

- **Routing name:** `archive-raw-and-superseded-results-to-support-prospective-validation-and-audit`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T099 — Publish intended use, validated chemical domain, known failure modes, and uncertainty limitations

Publish intended use, validated chemical domain, known failure modes, and uncertainty limitations.

- **Routing name:** `publish-intended-use-validated-chemical-domain-known-failure-modes-and-uncertainty-limitations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D037-T100 — Release the free-energy campaign only when chemical integrity, convergence, network consistency, provenance, and review gates pass

Release the free-energy campaign only when chemical integrity, convergence, network consistency, provenance, and review gates pass.

- **Routing name:** `release-the-free-energy-campaign-only-when-chemical-integrity-convergence-network-consistency-provenance-and-review-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
