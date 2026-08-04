# D022 — Cryogenic Electron Microscopy Data Processing

Batch **003** · 10 workstreams · 100 tasks

## 01. Acquisition intake and project configuration

### MYR-D022-T001 — Validate movie, micrograph, tilt-series, gain-reference, defect-map, and metadata file readability

Validate movie, micrograph, tilt-series, gain-reference, defect-map, and metadata file readability.

- **Routing name:** `validate-movie-micrograph-tilt-series-gain-reference-defect-map-and-metadata-file-readability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T002 — Reconcile microscope, detector, voltage, pixel size, magnification, exposure, frame rate, and energy-filter settings

Reconcile microscope, detector, voltage, pixel size, magnification, exposure, frame rate, and energy-filter settings.

- **Routing name:** `reconcile-microscope-detector-voltage-pixel-size-magnification-exposure-frame-rate-and-energy-filter-settings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T003 — Verify specimen identity, grid condition, imaging mode, symmetry expectation, and target molecular mass

Verify specimen identity, grid condition, imaging mode, symmetry expectation, and target molecular mass.

- **Routing name:** `verify-specimen-identity-grid-condition-imaging-mode-symmetry-expectation-and-target-molecular-mass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T004 — Normalize image orientation and handedness conventions without altering raw detector data

Normalize image orientation and handedness conventions without altering raw detector data.

- **Routing name:** `normalize-image-orientation-and-handedness-conventions-without-altering-raw-detector-data`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T005 — Detect missing, duplicated, truncated, or inconsistent acquisition files before processing

Detect missing, duplicated, truncated, or inconsistent acquisition files before processing.

- **Routing name:** `detect-missing-duplicated-truncated-or-inconsistent-acquisition-files-before-processing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T006 — Define whether the workflow is single-particle, helical, tomography, subtomogram averaging, or electron diffraction

Define whether the workflow is single-particle, helical, tomography, subtomogram averaging, or electron diffraction.

- **Routing name:** `define-whether-the-workflow-is-single-particle-helical-tomography-subtomogram-averaging-or-electron-diffraction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T007 — Freeze particle identifiers and source-micrograph lineage for every downstream extraction

Freeze particle identifiers and source-micrograph lineage for every downstream extraction.

- **Routing name:** `freeze-particle-identifiers-and-source-micrograph-lineage-for-every-downstream-extraction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T008 — Estimate storage and compute requirements from movie dimensions, frame counts, particle density, and target resolution

Estimate storage and compute requirements from movie dimensions, frame counts, particle density, and target resolution.

- **Routing name:** `estimate-storage-and-compute-requirements-from-movie-dimensions-frame-counts-particle-density-and-target-resolution`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T009 — Declare independent half-set policy before any three-dimensional refinement

Declare independent half-set policy before any three-dimensional refinement.

- **Routing name:** `declare-independent-half-set-policy-before-any-three-dimensional-refinement`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T010 — Reject projects lacking sufficient acquisition metadata to interpret physical pixel size or dose

Reject projects lacking sufficient acquisition metadata to interpret physical pixel size or dose.

- **Routing name:** `reject-projects-lacking-sufficient-acquisition-metadata-to-interpret-physical-pixel-size-or-dose`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Movie correction and exposure handling

### MYR-D022-T011 — Apply detector gain correction using the acquisition-matched gain reference

Apply detector gain correction using the acquisition-matched gain reference.

- **Routing name:** `apply-detector-gain-correction-using-the-acquisition-matched-gain-reference`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T012 — Remove hot pixels, dead pixels, and detector artifacts with logged masks

Remove hot pixels, dead pixels, and detector artifacts with logged masks.

- **Routing name:** `remove-hot-pixels-dead-pixels-and-detector-artifacts-with-logged-masks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T013 — Correct whole-frame and local beam-induced motion while retaining trajectory diagnostics

Correct whole-frame and local beam-induced motion while retaining trajectory diagnostics.

- **Routing name:** `correct-whole-frame-and-local-beam-induced-motion-while-retaining-trajectory-diagnostics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T014 — Calculate dose per frame and cumulative exposure from acquisition metadata

Calculate dose per frame and cumulative exposure from acquisition metadata.

- **Routing name:** `calculate-dose-per-frame-and-cumulative-exposure-from-acquisition-metadata`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T015 — Apply dose weighting only after verifying frame order and exposure units

Apply dose weighting only after verifying frame order and exposure units.

- **Routing name:** `apply-dose-weighting-only-after-verifying-frame-order-and-exposure-units`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T016 — Compare motion-correction parameter sets on a fixed representative subset

Compare motion-correction parameter sets on a fixed representative subset.

- **Routing name:** `compare-motion-correction-parameter-sets-on-a-fixed-representative-subset`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T017 — Flag movies with excessive drift, charging, stage jumps, or uncorrectable local motion

Flag movies with excessive drift, charging, stage jumps, or uncorrectable local motion.

- **Routing name:** `flag-movies-with-excessive-drift-charging-stage-jumps-or-uncorrectable-local-motion`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T018 — Preserve unweighted and dose-weighted summed micrographs separately

Preserve unweighted and dose-weighted summed micrographs separately.

- **Routing name:** `preserve-unweighted-and-dose-weighted-summed-micrographs-separately`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T019 — Validate output pixel size and dimensions after binning or Fourier cropping

Validate output pixel size and dimensions after binning or Fourier cropping.

- **Routing name:** `validate-output-pixel-size-and-dimensions-after-binning-or-fourier-cropping`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T020 — Export per-movie motion, dose, and rejection metrics

Export per-movie motion, dose, and rejection metrics.

- **Routing name:** `export-per-movie-motion-dose-and-rejection-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. CTF estimation and micrograph quality control

### MYR-D022-T021 — Estimate defocus, astigmatism, phase shift, and CTF fit for each accepted micrograph

Estimate defocus, astigmatism, phase shift, and CTF fit for each accepted micrograph.

- **Routing name:** `estimate-defocus-astigmatism-phase-shift-and-ctf-fit-for-each-accepted-micrograph`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T022 — Validate microscope voltage, spherical aberration, amplitude contrast, and pixel size supplied to CTF estimation

Validate microscope voltage, spherical aberration, amplitude contrast, and pixel size supplied to CTF estimation.

- **Routing name:** `validate-microscope-voltage-spherical-aberration-amplitude-contrast-and-pixel-size-supplied-to-ctf-estimation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T023 — Assess CTF fit range and information limit rather than ranking only by nominal defocus

Assess CTF fit range and information limit rather than ranking only by nominal defocus.

- **Routing name:** `assess-ctf-fit-range-and-information-limit-rather-than-ranking-only-by-nominal-defocus`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T024 — Detect crystalline ice, carbon edges, contamination, severe charging, and empty fields

Detect crystalline ice, carbon edges, contamination, severe charging, and empty fields.

- **Routing name:** `detect-crystalline-ice-carbon-edges-contamination-severe-charging-and-empty-fields`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T025 — Calculate ice-thickness and image-quality proxies when supported by the acquisition

Calculate ice-thickness and image-quality proxies when supported by the acquisition.

- **Routing name:** `calculate-ice-thickness-and-image-quality-proxies-when-supported-by-the-acquisition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T026 — Flag micrographs with implausible astigmatism, defocus, or phase-shift estimates

Flag micrographs with implausible astigmatism, defocus, or phase-shift estimates.

- **Routing name:** `flag-micrographs-with-implausible-astigmatism-defocus-or-phase-shift-estimates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T027 — Cluster micrographs by acquisition time and quality to detect session drift

Cluster micrographs by acquisition time and quality to detect session drift.

- **Routing name:** `cluster-micrographs-by-acquisition-time-and-quality-to-detect-session-drift`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T028 — Apply prespecified micrograph acceptance criteria without inspecting final reconstruction quality

Apply prespecified micrograph acceptance criteria without inspecting final reconstruction quality.

- **Routing name:** `apply-prespecified-micrograph-acceptance-criteria-without-inspecting-final-reconstruction-quality`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T029 — Preserve rejected micrographs and reason codes

Preserve rejected micrographs and reason codes.

- **Routing name:** `preserve-rejected-micrographs-and-reason-codes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T030 — Export a micrograph-level QC table linked to source movies

Export a micrograph-level QC table linked to source movies.

- **Routing name:** `export-a-micrograph-level-qc-table-linked-to-source-movies`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Particle or object detection and extraction

### MYR-D022-T031 — Generate initial particle coordinates using reference-free or low-bias picking on a training subset

Generate initial particle coordinates using reference-free or low-bias picking on a training subset.

- **Routing name:** `generate-initial-particle-coordinates-using-reference-free-or-low-bias-picking-on-a-training-subset`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T032 — Validate particle-box size against particle diameter and expected high-resolution signal

Validate particle-box size against particle diameter and expected high-resolution signal.

- **Routing name:** `validate-particle-box-size-against-particle-diameter-and-expected-high-resolution-signal`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T033 — Detect duplicate, edge-truncated, overlapping, and contamination-associated picks

Detect duplicate, edge-truncated, overlapping, and contamination-associated picks.

- **Routing name:** `detect-duplicate-edge-truncated-overlapping-and-contamination-associated-picks`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T034 — Compare template-based and learned picking for selection bias and missed orientations

Compare template-based and learned picking for selection bias and missed orientations.

- **Routing name:** `compare-template-based-and-learned-picking-for-selection-bias-and-missed-orientations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T035 — Prevent use of high-resolution target projections that could imprint reference bias

Prevent use of high-resolution target projections that could imprint reference bias.

- **Routing name:** `prevent-use-of-high-resolution-target-projections-that-could-imprint-reference-bias`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T036 — Extract particles with exact source coordinates, pixel size, box size, and micrograph provenance

Extract particles with exact source coordinates, pixel size, box size, and micrograph provenance.

- **Routing name:** `extract-particles-with-exact-source-coordinates-pixel-size-box-size-and-micrograph-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T037 — Normalize particle images using a declared background annulus and masking policy

Normalize particle images using a declared background annulus and masking policy.

- **Routing name:** `normalize-particle-images-using-a-declared-background-annulus-and-masking-policy`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T038 — Assign particles to independent half-sets before three-dimensional refinement

Assign particles to independent half-sets before three-dimensional refinement.

- **Routing name:** `assign-particles-to-independent-half-sets-before-three-dimensional-refinement`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T039 — Quantify particle yield and density by micrograph to detect abnormal picking

Quantify particle yield and density by micrograph to detect abnormal picking.

- **Routing name:** `quantify-particle-yield-and-density-by-micrograph-to-detect-abnormal-picking`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T040 — Export accepted and rejected coordinate sets with picker confidence and reason codes

Export accepted and rejected coordinate sets with picker confidence and reason codes.

- **Routing name:** `export-accepted-and-rejected-coordinate-sets-with-picker-confidence-and-reason-codes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Two-dimensional classification and particle cleaning

### MYR-D022-T041 — Run reference-free two-dimensional classification on a declared particle subset or full stack

Run reference-free two-dimensional classification on a declared particle subset or full stack.

- **Routing name:** `run-reference-free-two-dimensional-classification-on-a-declared-particle-subset-or-full-stack`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T042 — Assess class occupancy, alignment stability, high-resolution detail, and contamination content

Assess class occupancy, alignment stability, high-resolution detail, and contamination content.

- **Routing name:** `assess-class-occupancy-alignment-stability-high-resolution-detail-and-contamination-content`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T043 — Reject classes dominated by ice, carbon, aggregation, empty boxes, or uninterpretable density

Reject classes dominated by ice, carbon, aggregation, empty boxes, or uninterpretable density.

- **Routing name:** `reject-classes-dominated-by-ice-carbon-aggregation-empty-boxes-or-uninterpretable-density`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T044 — Retain rare but coherent views unless excluded by prespecified criteria

Retain rare but coherent views unless excluded by prespecified criteria.

- **Routing name:** `retain-rare-but-coherent-views-unless-excluded-by-prespecified-criteria`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T045 — Detect duplicate views caused by overclassification or alignment collapse

Detect duplicate views caused by overclassification or alignment collapse.

- **Routing name:** `detect-duplicate-views-caused-by-overclassification-or-alignment-collapse`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T046 — Compare particle retention across classification seeds and class counts

Compare particle retention across classification seeds and class counts.

- **Routing name:** `compare-particle-retention-across-classification-seeds-and-class-counts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T047 — Prevent manual selection based solely on resemblance to an expected structure

Prevent manual selection based solely on resemblance to an expected structure.

- **Routing name:** `prevent-manual-selection-based-solely-on-resemblance-to-an-expected-structure`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T048 — Propagate class decisions back to particle and micrograph provenance

Propagate class decisions back to particle and micrograph provenance.

- **Routing name:** `propagate-class-decisions-back-to-particle-and-micrograph-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T049 — Quantify orientation diversity after each cleaning round

Quantify orientation diversity after each cleaning round.

- **Routing name:** `quantify-orientation-diversity-after-each-cleaning-round`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T050 — Freeze the cleaned particle stack before ab initio reconstruction

Freeze the cleaned particle stack before ab initio reconstruction.

- **Routing name:** `freeze-the-cleaned-particle-stack-before-ab-initio-reconstruction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Initial models, heterogeneity, and symmetry

### MYR-D022-T051 — Generate multiple ab initio three-dimensional reconstructions from independently seeded subsets

Generate multiple ab initio three-dimensional reconstructions from independently seeded subsets.

- **Routing name:** `generate-multiple-ab-initio-three-dimensional-reconstructions-from-independently-seeded-subsets`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T052 — Assess whether initial models converge to consistent topology without imposed symmetry

Assess whether initial models converge to consistent topology without imposed symmetry.

- **Routing name:** `assess-whether-initial-models-converge-to-consistent-topology-without-imposed-symmetry`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T053 — Test plausible symmetry hypotheses against map features and refinement behaviour

Test plausible symmetry hypotheses against map features and refinement behaviour.

- **Routing name:** `test-plausible-symmetry-hypotheses-against-map-features-and-refinement-behaviour`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T054 — Identify junk, compositional, conformational, and orientation-related classes in heterogeneous refinement

Identify junk, compositional, conformational, and orientation-related classes in heterogeneous refinement.

- **Routing name:** `identify-junk-compositional-conformational-and-orientation-related-classes-in-heterogeneous-refinement`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T055 — Compare class solutions across random seeds and particle splits

Compare class solutions across random seeds and particle splits.

- **Routing name:** `compare-class-solutions-across-random-seeds-and-particle-splits`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T056 — Detect reference bias by reconstructing from deliberately distinct low-resolution starts

Detect reference bias by reconstructing from deliberately distinct low-resolution starts.

- **Routing name:** `detect-reference-bias-by-reconstructing-from-deliberately-distinct-low-resolution-starts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T057 — Estimate class occupancy uncertainty rather than treating assignments as exact

Estimate class occupancy uncertainty rather than treating assignments as exact.

- **Routing name:** `estimate-class-occupancy-uncertainty-rather-than-treating-assignments-as-exact`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T058 — Preserve unsymmetrized maps for validation of symmetry-supported features

Preserve unsymmetrized maps for validation of symmetry-supported features.

- **Routing name:** `preserve-unsymmetrized-maps-for-validation-of-symmetry-supported-features`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T059 — Select classes for refinement using prespecified structural and occupancy criteria

Select classes for refinement using prespecified structural and occupancy criteria.

- **Routing name:** `select-classes-for-refinement-using-prespecified-structural-and-occupancy-criteria`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T060 — Export all initial and heterogeneous maps with lineage to contributing particles

Export all initial and heterogeneous maps with lineage to contributing particles.

- **Routing name:** `export-all-initial-and-heterogeneous-maps-with-lineage-to-contributing-particles`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Three-dimensional refinement and optical corrections

### MYR-D022-T061 — Refine particle poses and shifts independently within frozen half-sets

Refine particle poses and shifts independently within frozen half-sets.

- **Routing name:** `refine-particle-poses-and-shifts-independently-within-frozen-half-sets`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T062 — Apply masks that exclude solvent without fitting high-resolution noise

Apply masks that exclude solvent without fitting high-resolution noise.

- **Routing name:** `apply-masks-that-exclude-solvent-without-fitting-high-resolution-noise`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T063 — Refine per-particle or grouped defocus only when supported by CTF information

Refine per-particle or grouped defocus only when supported by CTF information.

- **Routing name:** `refine-per-particle-or-grouped-defocus-only-when-supported-by-ctf-information`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T064 — Estimate and correct beam tilt, anisotropic magnification, trefoil, and higher-order aberrations when identifiable

Estimate and correct beam tilt, anisotropic magnification, trefoil, and higher-order aberrations when identifiable.

- **Routing name:** `estimate-and-correct-beam-tilt-anisotropic-magnification-trefoil-and-higher-order-aberrations-when-identifiable`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T065 — Correct particle motion or polishing parameters using cross-validation safeguards

Correct particle motion or polishing parameters using cross-validation safeguards.

- **Routing name:** `correct-particle-motion-or-polishing-parameters-using-cross-validation-safeguards`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T066 — Assess angular-distribution anisotropy and preferred orientation after refinement

Assess angular-distribution anisotropy and preferred orientation after refinement.

- **Routing name:** `assess-angular-distribution-anisotropy-and-preferred-orientation-after-refinement`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T067 — Compare symmetry-imposed and symmetry-free refinements for unsupported features

Compare symmetry-imposed and symmetry-free refinements for unsupported features.

- **Routing name:** `compare-symmetry-imposed-and-symmetry-free-refinements-for-unsupported-features`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T068 — Prevent particle reassignment between half-sets during refinement and polishing

Prevent particle reassignment between half-sets during refinement and polishing.

- **Routing name:** `prevent-particle-reassignment-between-half-sets-during-refinement-and-polishing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T069 — Checkpoint refinement state, optimizer parameters, and particle metadata

Checkpoint refinement state, optimizer parameters, and particle metadata.

- **Routing name:** `checkpoint-refinement-state-optimizer-parameters-and-particle-metadata`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T070 — Export final unfiltered half-maps, masks, postprocessed map, and refinement metadata

Export final unfiltered half-maps, masks, postprocessed map, and refinement metadata.

- **Routing name:** `export-final-unfiltered-half-maps-masks-postprocessed-map-and-refinement-metadata`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Resolution, map quality, and overfitting assessment

### MYR-D022-T071 — Calculate gold-standard Fourier shell correlation from independently refined half-maps

Calculate gold-standard Fourier shell correlation from independently refined half-maps.

- **Routing name:** `calculate-gold-standard-fourier-shell-correlation-from-independently-refined-half-maps`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T072 — Report resolution using declared FSC thresholds and mask-correction procedure

Report resolution using declared FSC thresholds and mask-correction procedure.

- **Routing name:** `report-resolution-using-declared-fsc-thresholds-and-mask-correction-procedure`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T073 — Calculate directional FSC or equivalent anisotropy metrics

Calculate directional FSC or equivalent anisotropy metrics.

- **Routing name:** `calculate-directional-fsc-or-equivalent-anisotropy-metrics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T074 — Estimate local resolution and map local-quality variation

Estimate local resolution and map local-quality variation.

- **Routing name:** `estimate-local-resolution-and-map-local-quality-variation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T075 — Inspect high-resolution noise substitution or phase-randomization controls for masking artifacts

Inspect high-resolution noise substitution or phase-randomization controls for masking artifacts.

- **Routing name:** `inspect-high-resolution-noise-substitution-or-phase-randomization-controls-for-masking-artifacts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T076 — Assess map sharpening across a bounded B-factor range without maximizing visual crispness alone

Assess map sharpening across a bounded B-factor range without maximizing visual crispness alone.

- **Routing name:** `assess-map-sharpening-across-a-bounded-b-factor-range-without-maximizing-visual-crispness-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T077 — Detect overfitting through half-map cross-validation and coordinate perturbation tests

Detect overfitting through half-map cross-validation and coordinate perturbation tests.

- **Routing name:** `detect-overfitting-through-half-map-cross-validation-and-coordinate-perturbation-tests`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T078 — Validate map handedness using interpretable secondary structure or external evidence

Validate map handedness using interpretable secondary structure or external evidence.

- **Routing name:** `validate-map-handedness-using-interpretable-secondary-structure-or-external-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T079 — Compare global nominal resolution with residue-level resolvability

Compare global nominal resolution with residue-level resolvability.

- **Routing name:** `compare-global-nominal-resolution-with-residue-level-resolvability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T080 — Export FSC curves, masks, local-resolution maps, and map-quality diagnostics

Export FSC curves, masks, local-resolution maps, and map-quality diagnostics.

- **Routing name:** `export-fsc-curves-masks-local-resolution-maps-and-map-quality-diagnostics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Atomic model building and map–model validation

### MYR-D022-T081 — Fit known or predicted components into density without altering map scale or handedness

Fit known or predicted components into density without altering map scale or handedness.

- **Routing name:** `fit-known-or-predicted-components-into-density-without-altering-map-scale-or-handedness`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T082 — Build atomic coordinates only where density supports residue-level interpretation

Build atomic coordinates only where density supports residue-level interpretation.

- **Routing name:** `build-atomic-coordinates-only-where-density-supports-residue-level-interpretation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T083 — Refine coordinates against one half-map and validate against the other when feasible

Refine coordinates against one half-map and validate against the other when feasible.

- **Routing name:** `refine-coordinates-against-one-half-map-and-validate-against-the-other-when-feasible`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T084 — Calculate map–model correlation globally, locally, and by component

Calculate map–model correlation globally, locally, and by component.

- **Routing name:** `calculate-map-model-correlation-globally-locally-and-by-component`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T085 — Evaluate atomic geometry, clashes, rotamers, backbone torsions, and covalent chemistry

Evaluate atomic geometry, clashes, rotamers, backbone torsions, and covalent chemistry.

- **Routing name:** `evaluate-atomic-geometry-clashes-rotamers-backbone-torsions-and-covalent-chemistry`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T086 — Calculate residue-level map resolvability metrics and identify unsupported coordinates

Calculate residue-level map resolvability metrics and identify unsupported coordinates.

- **Routing name:** `calculate-residue-level-map-resolvability-metrics-and-identify-unsupported-coordinates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T087 — Validate ligand, metal, glycan, lipid, and covalent-adduct placement against local density

Validate ligand, metal, glycan, lipid, and covalent-adduct placement against local density.

- **Routing name:** `validate-ligand-metal-glycan-lipid-and-covalent-adduct-placement-against-local-density`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T088 — Detect model overfitting caused by excessive refinement parameters or tight restraints

Detect model overfitting caused by excessive refinement parameters or tight restraints.

- **Routing name:** `detect-model-overfitting-caused-by-excessive-refinement-parameters-or-tight-restraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T089 — Compare alternative sequence registers in ambiguous density regions

Compare alternative sequence registers in ambiguous density regions.

- **Routing name:** `compare-alternative-sequence-registers-in-ambiguous-density-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T090 — Export model–map validation results with explicit unsupported and unmodelled regions

Export model–map validation results with explicit unsupported and unmodelled regions.

- **Routing name:** `export-model-map-validation-results-with-explicit-unsupported-and-unmodelled-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Deposition, provenance, and release gates

### MYR-D022-T091 — Prepare EMDB-compatible maps, half-maps, masks, FSC data, and experimental metadata

Prepare EMDB-compatible maps, half-maps, masks, FSC data, and experimental metadata.

- **Routing name:** `prepare-emdb-compatible-maps-half-maps-masks-fsc-data-and-experimental-metadata`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T092 — Prepare PDB-compatible coordinates and map–model metadata when an atomic model is released

Prepare PDB-compatible coordinates and map–model metadata when an atomic model is released.

- **Routing name:** `prepare-pdb-compatible-coordinates-and-map-model-metadata-when-an-atomic-model-is-released`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T093 — Run official archive validation services before deposition

Run official archive validation services before deposition.

- **Routing name:** `run-official-archive-validation-services-before-deposition`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T094 — Record software versions, command lines, random seeds, hardware, and metadata transformations

Record software versions, command lines, random seeds, hardware, and metadata transformations.

- **Routing name:** `record-software-versions-command-lines-random-seeds-hardware-and-metadata-transformations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T095 — Hash raw acquisitions, particle stacks, half-maps, masks, maps, and coordinate files

Hash raw acquisitions, particle stacks, half-maps, masks, maps, and coordinate files.

- **Routing name:** `hash-raw-acquisitions-particle-stacks-half-maps-masks-maps-and-coordinate-files`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T096 — Generate particle-flow counts from movies through final reconstruction

Generate particle-flow counts from movies through final reconstruction.

- **Routing name:** `generate-particle-flow-counts-from-movies-through-final-reconstruction`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T097 — Label sharpened, unsharpened, focused, composite, and locally filtered maps unambiguously

Label sharpened, unsharpened, focused, composite, and locally filtered maps unambiguously.

- **Routing name:** `label-sharpened-unsharpened-focused-composite-and-locally-filtered-maps-unambiguously`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T098 — Require expert review of symmetry, handedness, heterogeneity, and model interpretation

Require expert review of symmetry, handedness, heterogeneity, and model interpretation.

- **Routing name:** `require-expert-review-of-symmetry-handedness-heterogeneity-and-model-interpretation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T099 — Block atomic claims in density regions lacking reproducible half-map support

Block atomic claims in density regions lacking reproducible half-map support.

- **Routing name:** `block-atomic-claims-in-density-regions-lacking-reproducible-half-map-support`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D022-T100 — Release only when half-set independence, map quality, model validation, provenance, and deposition gates pass

Release only when half-set independence, map quality, model validation, provenance, and deposition gates pass.

- **Routing name:** `release-only-when-half-set-independence-map-quality-model-validation-provenance-and-deposition-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
