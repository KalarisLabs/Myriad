---
name: normalize-qc-call-hts-hits
version: 1.0.0
description: >
  Activate when an agent must parse high-throughput screening plate-reader data,
  reconcile plate maps, detect row/column/edge artifacts, normalize inhibition or
  activation assays, calculate Z-prime or robust Z-prime, compute robust z-scores or
  B-scores, assess replicate concordance, control false discoveries, call primary hits,
  quarantine failed plates, or produce an auditable HTS campaign-level hit table.
parameters:
  type: object
  additionalProperties: false
  required:
    - reader_files
    - plate_map
    - assay_direction
    - plate_format
    - output_directory
    - control_labels
  properties:
    reader_files:
      type: array
      minItems: 1
      items:
        type: string
        pattern: '^.+\\.(csv|tsv|txt|xlsx)$'
    plate_map:
      type: string
      pattern: '^.+\\.(csv|tsv|xlsx)$'
    assay_direction:
      enum: [inhibition, activation]
    plate_format:
      enum: [96, 384, 1536]
    output_directory:
      type: string
      minLength: 1
    control_labels:
      type: object
      additionalProperties: false
      required: [positive, negative]
      properties:
        positive: {type: string, minLength: 1}
        negative: {type: string, minLength: 1}
        blank: {type: string, minLength: 1}
    signal_column:
      type: string
      minLength: 1
    plate_id_column:
      type: string
      default: plate_id
    well_column:
      type: string
      default: well
    sample_id_column:
      type: string
      default: sample_id
    normalization_method:
      enum: [auto, percent-activity, robust-z, b-score]
      default: auto
    hit_method:
      enum: [robust-z-threshold, ssmd, fdr-adjusted-model, fixed-percent-activity]
      default: robust-z-threshold
    hit_threshold:
      type: number
    fdr_alpha:
      type: number
      exclusiveMinimum: 0
      maximum: 0.25
      default: 0.05
    minimum_z_prime:
      type: number
      minimum: -10
      maximum: 1
      default: 0.5
    minimum_control_wells_per_class:
      type: integer
      minimum: 2
      default: 8
    maximum_missing_well_fraction:
      type: number
      minimum: 0
      maximum: 1
      default: 0.01
    edge_effect_threshold_mad:
      type: number
      exclusiveMinimum: 0
      default: 2.5
    replicate_correlation_minimum:
      type: number
      minimum: -1
      maximum: 1
      default: 0.7
outputs:
  type: object
  required: [status, plate_qc, hits, provenance]
  properties:
    status: {enum: [PASS, REVIEW, FAIL]}
    plate_qc: {type: array}
    hits: {type: array}
    provenance: {type: object}
runtime:
  operating_system: any
  required_python_packages:
    - pandas
    - numpy
    - scipy
    - statsmodels
    - openpyxl
  network_access: forbidden
  deterministic_environment: lockfile-or-container-digest-required
safety:
  execution_mode: data-analysis-only
  autonomous-compound-progression: prohibited
  human_review_required: true
---

# Mission

Transform heterogeneous HTS reader exports and plate maps into a canonical well-level dataset; identify plate artifacts; choose a normalization method by explicit diagnostics; quarantine failed plates; and call auditable hits using a declared statistical rule.

# Activation conditions

Use for plate-based primary or confirmatory screens with explicit positive and negative controls. Do not use when control identities are unknown, when wells contain pooled untraceable samples, or when the assay endpoint cannot be represented by a monotonic activation/inhibition direction.

# Preconditions and fail-closed checks

1. Compute SHA-256 for every source file and record parser/version details.
2. Require a unique `(plate_id, well)` in both reader data and plate map.
3. Normalize wells to zero-padded canonical form (`A01`, `A02`, ...), validating row and column bounds for the declared plate format.
4. Reject duplicated measurements unless a separate read/replicate identifier is present.
5. Require positive and negative control labels to exist on every plate unless the campaign design explicitly supplies shared controls; shared-control designs route to a separate validated method.
6. Require at least `minimum_control_wells_per_class` nonmissing wells for both positive and negative controls after exclusions.
7. Never infer control labels from extreme signal values.
8. Freeze package versions, random seeds, configuration, source hashes, and parser provenance in `run-manifest.json`.

# Deterministic procedure

## Step 1 — Parse and reconcile

Read supported files without automatic type coercion of IDs. For Excel, require a declared or unambiguous worksheet; otherwise stop `FAIL_AMBIGUOUS_WORKSHEET`.

Create a canonical table with:

- plate ID;
- canonical well;
- row index and column index;
- sample ID;
- sample/control class;
- replicate ID if available;
- raw signal;
- source file and source row;
- exclusion flag and reason.

Perform a full outer reconciliation between measurements and plate map. Classify every discrepancy as:

- `measurement_without_map`;
- `map_without_measurement`;
- `duplicate_measurement`;
- `duplicate_map_entry`;
- `invalid_well`;
- `missing_signal`.

If missing or unmatched wells exceed `maximum_missing_well_fraction` on a plate, fail that plate.

## Step 2 — Blank correction

When blank wells are declared and at least four valid blanks exist on the plate, calculate the blank median and subtract it from all wells. Store both raw and corrected values. If blank correction reverses more than 1% of values into an impossible domain for the assay's measurement technology, flag `BLANK_CORRECTION_DOMAIN_WARNING`; do not clip values silently.

When blanks are absent, retain raw signal as corrected signal and label `BLANK_NOT_AVAILABLE`.

## Step 3 — Control diagnostics

For positive and negative controls separately calculate:

- count;
- mean and standard deviation;
- median and median absolute deviation (MAD, scaled by 1.4826 for normal-consistent estimate);
- coefficient of variation when mean is nonzero;
- interquartile range;
- outlier count by `|x - median| / scaled_MAD > 4.5`.

Do not automatically delete control outliers. Produce two QC views:

1. all declared controls;
2. robust summary resistant to outliers.

A control well may be excluded only for a predeclared technical reason or a source-recorded failure. Statistical extremeness alone produces a warning, not deletion.

## Step 4 — Calculate assay separation

Calculate classical Z-prime:

```text
Z' = 1 - 3 * (sd_positive + sd_negative) / abs(mean_positive - mean_negative)
```

Calculate robust Z-prime using medians and scaled MAD in the same structure. If the positive and negative centers are equal, set both metrics to negative infinity and fail the plate.

Plate QC rule:

- `PASS_QC` when classical Z-prime and robust Z-prime are both at least `minimum_z_prime`;
- `REVIEW_QC` when robust Z-prime passes but classical Z-prime fails, or their absolute difference exceeds 0.2;
- `FAIL_QC` when robust Z-prime is below threshold, controls are mislabeled by assay direction, or required control counts are insufficient.

A `FAIL_QC` plate cannot yield promotable hits.

## Step 5 — Detect spatial artifacts

Using noncontrol, nonexcluded wells:

1. calculate row medians and column medians;
2. compare outer-edge wells with interior wells using median difference scaled by pooled MAD;
3. fit a two-way median-polish model when plate density and noncontrol coverage are sufficient;
4. inspect residual median by row and column;
5. flag entire rows/columns with residual shift exceeding `edge_effect_threshold_mad`.

Spatial diagnostics must be calculated before selecting normalization. Do not apply B-score when sample placement is strongly nonrandom and biological groups are confounded with rows or columns; mark `B_SCORE_CONFOUNDED`.

## Step 6 — Select normalization method

When the caller specifies a method, use it only if its preconditions pass.

For `auto`, choose in this order:

1. **B-score** when row/column artifacts are detected, noncontrol occupancy is sufficiently dense, and layout is not biologically confounded;
2. **percent-activity** when controls are robust and no material spatial effect is detected;
3. **robust-z** when control dynamic range is inadequate for stable percent scaling but the sample background is dense and expected hit rate is low;
4. otherwise stop `FAIL_NO_VALID_NORMALIZATION`.

### Percent activity

For inhibition assays, define 0% activity at the positive-control median and 100% activity at the negative-control median:

```text
percent_activity = 100 * (x - median_positive) / (median_negative - median_positive)
percent_inhibition = 100 - percent_activity
```

For activation assays, orient the formula so increasing biological response has increasing normalized activation. Preserve values outside 0–100; do not clip.

### Robust z-score

Calculate against the negative-control distribution when valid:

```text
robust_z = (x - median_negative) / (1.4826 * MAD_negative)
```

If negative-control MAD is zero, stop for that plate unless an approved pooled variance model is explicitly configured.

### B-score

Apply iterative median polish to the plate matrix and divide residuals by scaled MAD of noncontrol residuals. Controls and excluded wells must not distort sample residual scale. Record iteration limit, convergence tolerance, and final residual scale.

## Step 7 — Replicate handling

When sample replicates exist:

- retain well-level normalized values;
- calculate sample median, mean, standard deviation, and replicate count;
- calculate campaign-level Pearson and Spearman replicate correlations for matched samples;
- flag sample discordance when replicate signs conflict or robust spread exceeds a declared threshold;
- cap campaign status at `REVIEW` when replicate correlation is below `replicate_correlation_minimum`.

Never average across failed plates without retaining the plate QC state.

## Step 8 — Call hits

### Robust-z threshold

Default thresholds when `hit_threshold` is absent:

- inhibition: robust z `<= -3` when larger raw values mean more activity, after orientation to a common effect direction;
- activation: oriented robust z `>= 3`.

The implementation must first create `oriented_effect`, where larger always means stronger desired effect, then apply a single `>= threshold` rule. Save the orientation transform.

### Fixed percent activity

Require explicit `hit_threshold`. For inhibition, hits are percent inhibition at or above the threshold; for activation, normalized activation at or above threshold.

### SSMD

Use only with sufficient replicates to estimate sample and negative-control variance. Report effect estimate and uncertainty. Do not use a single-well SSMD formula while implying replicate-specific variance.

### FDR-adjusted model

Fit the declared statistical model, test in the desired direction, and adjust p-values with Benjamini–Hochberg at `fdr_alpha`. A compound is promotable only when it passes both adjusted significance and a predeclared minimum effect-size rule. If no effect-size rule is supplied, status is `REVIEW` and results are candidates, not confirmed hits.

## Step 9 — Gate and classify results

Each result receives:

- `PROMOTABLE_HIT`: passes hit rule, originates only from passing plates, and meets replicate rule;
- `REVIEW_HIT`: passes effect threshold but plate or replicate state is review;
- `QUARANTINED_HIT`: numerical hit on a failed plate;
- `NON_HIT`;
- `UNASSESSABLE`.

Quarantined hits must never appear in the promotable hit export.

## Step 10 — Campaign-level prioritization

Sort promotable hits by:

1. replicate-consistent desired effect;
2. stronger median oriented effect;
3. lower adjusted p-value where applicable;
4. lower replicate dispersion;
5. lexical sample ID.

Do not claim biological mechanism, selectivity, potency, or developability from primary-screen data alone.

# Quality gates

A plate fails when any is true:

- missing/unmapped wells exceed threshold;
- insufficient positive or negative controls;
- robust Z-prime below `minimum_z_prime`;
- control direction contradicts declared assay direction;
- normalization denominator or robust scale is zero;
- spatial correction is required but confounded and no valid alternative exists;
- source parsing is ambiguous or irreconcilable.

A campaign fails when all plates fail or no valid normalization exists. It is `REVIEW` when any hit-relevant plate is review, replicate concordance is inadequate, or method assumptions are materially violated.

# Output contract

Create:

```text
output_directory/
  run-manifest.json
  reconciliation-report.tsv
  canonical-wells.parquet
  plate-qc.tsv
  spatial-diagnostics.tsv
  normalized-wells.parquet
  sample-summary.tsv
  promotable-hits.tsv
  review-and-quarantined-hits.tsv
  decision.json
  logs/
```

`decision.json` must record method selection, formulas, thresholds, control summaries, plate dispositions, multiplicity correction, replicate logic, and every exclusion reason.

# Error handling

- Preserve original values; transformations create new columns.
- Never convert parse failures to zero or empty strings.
- Never remove outliers without an explicit recorded technical exclusion.
- One identical retry is allowed for transient file access failure.
- Parser ambiguity, zero denominators, and missing controls fail closed.

# Validation tests

1. Canonical well conversion correctly handles all wells for 96-, 384-, and 1536-well layouts.
2. Duplicate `(plate_id, well)` fails reconciliation.
3. Synthetic edge effect triggers spatial warning and B-score eligibility.
4. Layout-confounded rows prohibit automatic B-score.
5. A failed plate produces no promotable hits even when a well crosses the numerical threshold.
6. Classical and robust Z-prime calculations match hand-computed fixtures.
7. Benjamini–Hochberg adjusted p-values match a fixed reference vector.
8. Results are invariant to input row order.

# Safety and scope

This skill supports screening-data analysis only. Hit status is a statistical prioritization outcome, not evidence of therapeutic efficacy, safety, mechanism, or clinical utility. Compound progression requires orthogonal assays, counter-screens, medicinal chemistry review, and qualified human authorization.

# Scientific basis

- Zhang J.H., Chung T.D.Y., Oldenburg K.R. A simple statistical parameter for use in evaluation and validation of high throughput screening assays. *Journal of Biomolecular Screening* 4, 67–73 (1999). DOI: 10.1177/108705719900400206.
- Brideau C. et al. Improved statistical methods for hit selection in high-throughput screening. *Journal of Biomolecular Screening* 8, 634–647 (2003). DOI: 10.1177/1087057103258285.
- Zhang X.D. et al. Issues of Z-factor and an approach to avoid them for quality control in high-throughput screening studies. *Bioinformatics* 36, 5299–5303 (2020). DOI: 10.1093/bioinformatics/btaa978.
