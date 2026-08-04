# D052 — Base-Editing System Design

Batch **006** · 10 workstreams · 100 tasks

## 01. Edit specification and editor-class eligibility

### MYR-D052-T001 — Normalize the desired genomic substitution, reference allele, alternate allele, strand, genome build, transcript consequence, and zygosity into one edit record

Normalize the desired genomic substitution, reference allele, alternate allele, strand, genome build, transcript consequence, and zygosity into one edit record.

- **Routing name:** `normalize-the-desired-genomic-substitution-reference-allele-alternate-allele-strand-genome-build-transcript-consequence-and-zygosity-into-one-edit-record`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T002 — Determine whether the requested change is directly addressable by cytosine, adenine, glycosylase, or other validated base-editor chemistry

Determine whether the requested change is directly addressable by cytosine, adenine, glycosylase, or other validated base-editor chemistry.

- **Routing name:** `determine-whether-the-requested-change-is-directly-addressable-by-cytosine-adenine-glycosylase-or-other-validated-base-editor-chemistry`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T003 — Distinguish correction of a pathogenic allele from introduction of a protective allele, splice modification, regulatory editing, or screening mutagenesis

Distinguish correction of a pathogenic allele from introduction of a protective allele, splice modification, regulatory editing, or screening mutagenesis.

- **Routing name:** `distinguish-correction-of-a-pathogenic-allele-from-introduction-of-a-protective-allele-splice-modification-regulatory-editing-or-screening-mutagenesis`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T004 — Define acceptable bystander substitutions, prohibited amino-acid changes, maximum indel burden, and minimum product purity before design

Define acceptable bystander substitutions, prohibited amino-acid changes, maximum indel burden, and minimum product purity before design.

- **Routing name:** `define-acceptable-bystander-substitutions-prohibited-amino-acid-changes-maximum-indel-burden-and-minimum-product-purity-before-design`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T005 — Identify clinically relevant transcripts, coding frames, splice elements, and overlapping annotations affected by every possible edited nucleotide

Identify clinically relevant transcripts, coding frames, splice elements, and overlapping annotations affected by every possible edited nucleotide.

- **Routing name:** `identify-clinically-relevant-transcripts-coding-frames-splice-elements-and-overlapping-annotations-affected-by-every-possible-edited-nucleotide`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T006 — Capture sample-specific and population variants that alter PAM availability, editing windows, bystanders, or allele selectivity

Capture sample-specific and population variants that alter PAM availability, editing windows, bystanders, or allele selectivity.

- **Routing name:** `capture-sample-specific-and-population-variants-that-alter-pam-availability-editing-windows-bystanders-or-allele-selectivity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T007 — Specify intended cell type, division state, tissue, delivery duration, editor format, and dose range because performance is context dependent

Specify intended cell type, division state, tissue, delivery duration, editor format, and dose range because performance is context dependent.

- **Routing name:** `specify-intended-cell-type-division-state-tissue-delivery-duration-editor-format-and-dose-range-because-performance-is-context-dependent`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T008 — Compare base editing with nuclease, prime editing, RNA editing, or nonediting alternatives without assuming base editing is preferred

Compare base editing with nuclease, prime editing, RNA editing, or nonediting alternatives without assuming base editing is preferred.

- **Routing name:** `compare-base-editing-with-nuclease-prime-editing-rna-editing-or-nonediting-alternatives-without-assuming-base-editing-is-preferred`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T009 — Create a versioned evidence manifest for editor variants, sequence models, off-target assays, reference resources, and cell-context data

Create a versioned evidence manifest for editor variants, sequence models, off-target assays, reference resources, and cell-context data.

- **Routing name:** `create-a-versioned-evidence-manifest-for-editor-variants-sequence-models-off-target-assays-reference-resources-and-cell-context-data`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T010 — Issue a no-call when the desired nucleotide conversion or permissible product spectrum cannot be achieved by supported editor classes

Issue a no-call when the desired nucleotide conversion or permissible product spectrum cannot be achieved by supported editor classes.

- **Routing name:** `issue-a-no-call-when-the-desired-nucleotide-conversion-or-permissible-product-spectrum-cannot-be-achieved-by-supported-editor-classes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. PAM, spacer, and editing-window enumeration

### MYR-D052-T011 — Enumerate all spacer orientations that place the target nucleotide inside the empirically supported activity window of each eligible editor

Enumerate all spacer orientations that place the target nucleotide inside the empirically supported activity window of each eligible editor.

- **Routing name:** `enumerate-all-spacer-orientations-that-place-the-target-nucleotide-inside-the-empirically-supported-activity-window-of-each-eligible-editor`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T012 — Map every editable nucleotide within each candidate window to genomic, transcript, codon, amino-acid, splice, and regulatory consequences

Map every editable nucleotide within each candidate window to genomic, transcript, codon, amino-acid, splice, and regulatory consequences.

- **Routing name:** `map-every-editable-nucleotide-within-each-candidate-window-to-genomic-transcript-codon-amino-acid-splice-and-regulatory-consequences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T013 — Calculate nick position, deaminase window coordinates, PAM identity, and strand orientation using the exact editor architecture

Calculate nick position, deaminase window coordinates, PAM identity, and strand orientation using the exact editor architecture.

- **Routing name:** `calculate-nick-position-deaminase-window-coordinates-pam-identity-and-strand-orientation-using-the-exact-editor-architecture`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T014 — Identify candidates enabled by engineered PAM-relaxed nucleases while separating supported PAMs from speculative recognition claims

Identify candidates enabled by engineered PAM-relaxed nucleases while separating supported PAMs from speculative recognition claims.

- **Routing name:** `identify-candidates-enabled-by-engineered-pam-relaxed-nucleases-while-separating-supported-pams-from-speculative-recognition-claims`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T015 — Flag spacer sequences with homopolymers, repeats, extreme composition, self-complementarity, or expression-system incompatibilities

Flag spacer sequences with homopolymers, repeats, extreme composition, self-complementarity, or expression-system incompatibilities.

- **Routing name:** `flag-spacer-sequences-with-homopolymers-repeats-extreme-composition-self-complementarity-or-expression-system-incompatibilities`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T016 — Assess whether target-window placement remains valid across transcript isoforms, haplotypes, and local indel or structural variation

Assess whether target-window placement remains valid across transcript isoforms, haplotypes, and local indel or structural variation.

- **Routing name:** `assess-whether-target-window-placement-remains-valid-across-transcript-isoforms-haplotypes-and-local-indel-or-structural-variation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T017 — Generate alternative spacers that trade target-window position against bystander burden, predicted efficiency, and off-target risk

Generate alternative spacers that trade target-window position against bystander burden, predicted efficiency, and off-target risk.

- **Routing name:** `generate-alternative-spacers-that-trade-target-window-position-against-bystander-burden-predicted-efficiency-and-off-target-risk`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T018 — Prevent coordinate errors by independently reconstructing expected edited strands and reverse-complement representations

Prevent coordinate errors by independently reconstructing expected edited strands and reverse-complement representations.

- **Routing name:** `prevent-coordinate-errors-by-independently-reconstructing-expected-edited-strands-and-reverse-complement-representations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T019 — Create a candidate matrix linking editor, spacer, PAM, activity window, intended nucleotide, and all co-editable bases

Create a candidate matrix linking editor, spacer, PAM, activity window, intended nucleotide, and all co-editable bases.

- **Routing name:** `create-a-candidate-matrix-linking-editor-spacer-pam-activity-window-intended-nucleotide-and-all-co-editable-bases`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T020 — Reject candidates whose target base falls outside the editor-specific window or depends on undocumented window expansion

Reject candidates whose target base falls outside the editor-specific window or depends on undocumented window expansion.

- **Routing name:** `reject-candidates-whose-target-base-falls-outside-the-editor-specific-window-or-depends-on-undocumented-window-expansion`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Bystander editing and consequence resolution

### MYR-D052-T021 — Enumerate every chemically editable bystander base in the activity window for each candidate spacer and editor combination

Enumerate every chemically editable bystander base in the activity window for each candidate spacer and editor combination.

- **Routing name:** `enumerate-every-chemically-editable-bystander-base-in-the-activity-window-for-each-candidate-spacer-and-editor-combination`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T022 — Predict amino-acid, splice, untranslated-region, regulatory, and noncoding consequences for every individual and combined bystander outcome

Predict amino-acid, splice, untranslated-region, regulatory, and noncoding consequences for every individual and combined bystander outcome.

- **Routing name:** `predict-amino-acid-splice-untranslated-region-regulatory-and-noncoding-consequences-for-every-individual-and-combined-bystander-outcome`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T023 — Distinguish benign synonymous bystanders from changes that alter codon usage, splicing enhancers, RNA structure, or protein function

Distinguish benign synonymous bystanders from changes that alter codon usage, splicing enhancers, RNA structure, or protein function.

- **Routing name:** `distinguish-benign-synonymous-bystanders-from-changes-that-alter-codon-usage-splicing-enhancers-rna-structure-or-protein-function`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T024 — Calculate the combinatorial product space when multiple targetable bases can be edited independently within one window

Calculate the combinatorial product space when multiple targetable bases can be edited independently within one window.

- **Routing name:** `calculate-the-combinatorial-product-space-when-multiple-targetable-bases-can-be-edited-independently-within-one-window`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T025 — Identify editor variants with narrowed, shifted, or context-specific windows that could reduce unacceptable bystander products

Identify editor variants with narrowed, shifted, or context-specific windows that could reduce unacceptable bystander products.

- **Routing name:** `identify-editor-variants-with-narrowed-shifted-or-context-specific-windows-that-could-reduce-unacceptable-bystander-products`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T026 — Assess allele-selective designs where a variant creates or removes a bystander, PAM, or editor-context motif

Assess allele-selective designs where a variant creates or removes a bystander, PAM, or editor-context motif.

- **Routing name:** `assess-allele-selective-designs-where-a-variant-creates-or-removes-a-bystander-pam-or-editor-context-motif`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T027 — Flag apparently acceptable windows where rare population variants create new harmful bystander outcomes

Flag apparently acceptable windows where rare population variants create new harmful bystander outcomes.

- **Routing name:** `flag-apparently-acceptable-windows-where-rare-population-variants-create-new-harmful-bystander-outcomes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T028 — Prioritize candidates by probability of desired pure product rather than target-base conversion alone

Prioritize candidates by probability of desired pure product rather than target-base conversion alone.

- **Routing name:** `prioritize-candidates-by-probability-of-desired-pure-product-rather-than-target-base-conversion-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T029 — Define which bystander products require direct quantification even when prediction models assign low probability

Define which bystander products require direct quantification even when prediction models assign low probability.

- **Routing name:** `define-which-bystander-products-require-direct-quantification-even-when-prediction-models-assign-low-probability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T030 — Produce a bystander-risk table with product identities, functional consequences, predicted abundance, and acceptability status

Produce a bystander-risk table with product identities, functional consequences, predicted abundance, and acceptability status.

- **Routing name:** `produce-a-bystander-risk-table-with-product-identities-functional-consequences-predicted-abundance-and-acceptability-status`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Sequence-context and editor-variant matching

### MYR-D052-T031 — Match local nucleotide context to editor-specific motif preferences, disfavoured motifs, and validated sequence-dependence evidence

Match local nucleotide context to editor-specific motif preferences, disfavoured motifs, and validated sequence-dependence evidence.

- **Routing name:** `match-local-nucleotide-context-to-editor-specific-motif-preferences-disfavoured-motifs-and-validated-sequence-dependence-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T032 — Compare editor variants for target conversion, window width, processivity, product purity, and context-dependent activity

Compare editor variants for target conversion, window width, processivity, product purity, and context-dependent activity.

- **Routing name:** `compare-editor-variants-for-target-conversion-window-width-processivity-product-purity-and-context-dependent-activity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T033 — Distinguish DNA-strand preference, deaminase identity, linker architecture, nickase variant, and uracil-glycosylase modulation among editors

Distinguish DNA-strand preference, deaminase identity, linker architecture, nickase variant, and uracil-glycosylase modulation among editors.

- **Routing name:** `distinguish-dna-strand-preference-deaminase-identity-linker-architecture-nickase-variant-and-uracil-glycosylase-modulation-among-editors`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T034 — Apply activity models only when the editor architecture, guide format, assay system, and sequence class match the training domain

Apply activity models only when the editor architecture, guide format, assay system, and sequence class match the training domain.

- **Routing name:** `apply-activity-models-only-when-the-editor-architecture-guide-format-assay-system-and-sequence-class-match-the-training-domain`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T035 — Estimate uncertainty when model predictions extrapolate to rare motifs, noncanonical PAMs, primary cells, or in vivo delivery

Estimate uncertainty when model predictions extrapolate to rare motifs, noncanonical PAMs, primary cells, or in vivo delivery.

- **Routing name:** `estimate-uncertainty-when-model-predictions-extrapolate-to-rare-motifs-noncanonical-pams-primary-cells-or-in-vivo-delivery`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T036 — Identify cases where reduced-window editors improve purity but may lower target conversion below the minimum threshold

Identify cases where reduced-window editors improve purity but may lower target conversion below the minimum threshold.

- **Routing name:** `identify-cases-where-reduced-window-editors-improve-purity-but-may-lower-target-conversion-below-the-minimum-threshold`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T037 — Assess temperature, cell-cycle, chromatin, and DNA-repair context only when evidence supports transfer to the intended system

Assess temperature, cell-cycle, chromatin, and DNA-repair context only when evidence supports transfer to the intended system.

- **Routing name:** `assess-temperature-cell-cycle-chromatin-and-dna-repair-context-only-when-evidence-supports-transfer-to-the-intended-system`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T038 — Compare editor candidates across multiple models and preserve disagreement rather than selecting the highest uncalibrated score

Compare editor candidates across multiple models and preserve disagreement rather than selecting the highest uncalibrated score.

- **Routing name:** `compare-editor-candidates-across-multiple-models-and-preserve-disagreement-rather-than-selecting-the-highest-uncalibrated-score`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T039 — Generate a context-matched shortlist that balances target conversion, bystander purity, indels, and specificity

Generate a context-matched shortlist that balances target conversion, bystander purity, indels, and specificity.

- **Routing name:** `generate-a-context-matched-shortlist-that-balances-target-conversion-bystander-purity-indels-and-specificity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T040 — Lock the exact editor protein sequence and construct version before interpreting performance or safety evidence

Lock the exact editor protein sequence and construct version before interpreting performance or safety evidence.

- **Routing name:** `lock-the-exact-editor-protein-sequence-and-construct-version-before-interpreting-performance-or-safety-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Desired-product purity and indel-spectrum assessment

### MYR-D052-T041 — Predict target conversion, bystander combinations, unedited fraction, indels, and noncanonical substitutions as a complete product distribution

Predict target conversion, bystander combinations, unedited fraction, indels, and noncanonical substitutions as a complete product distribution.

- **Routing name:** `predict-target-conversion-bystander-combinations-unedited-fraction-indels-and-noncanonical-substitutions-as-a-complete-product-distribution`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T042 — Distinguish editing efficiency from desired-product purity and require both metrics in candidate comparison

Distinguish editing efficiency from desired-product purity and require both metrics in candidate comparison.

- **Routing name:** `distinguish-editing-efficiency-from-desired-product-purity-and-require-both-metrics-in-candidate-comparison`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T043 — Estimate how nicking strategy, DNA repair state, editor expression, and sequence context influence indel formation

Estimate how nicking strategy, DNA repair state, editor expression, and sequence context influence indel formation.

- **Routing name:** `estimate-how-nicking-strategy-dna-repair-state-editor-expression-and-sequence-context-influence-indel-formation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T044 — Flag candidates prone to target-base conversion accompanied by unacceptable frameshift, splice, or amino-acid byproducts

Flag candidates prone to target-base conversion accompanied by unacceptable frameshift, splice, or amino-acid byproducts.

- **Routing name:** `flag-candidates-prone-to-target-base-conversion-accompanied-by-unacceptable-frameshift-splice-or-amino-acid-byproducts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T045 — Assess whether product distributions differ materially between immortalized lines, primary cells, organoids, and intended tissue

Assess whether product distributions differ materially between immortalized lines, primary cells, organoids, and intended tissue.

- **Routing name:** `assess-whether-product-distributions-differ-materially-between-immortalized-lines-primary-cells-organoids-and-intended-tissue`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T046 — Reconcile short-read, long-read, and molecularly barcoded measurements when complex alleles or large events are plausible

Reconcile short-read, long-read, and molecularly barcoded measurements when complex alleles or large events are plausible.

- **Routing name:** `reconcile-short-read-long-read-and-molecularly-barcoded-measurements-when-complex-alleles-or-large-events-are-plausible`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T047 — Identify large deletions, rearrangements, or translocations that targeted amplicon summaries may not detect

Identify large deletions, rearrangements, or translocations that targeted amplicon summaries may not detect.

- **Routing name:** `identify-large-deletions-rearrangements-or-translocations-that-targeted-amplicon-summaries-may-not-detect`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T048 — Define minimum read depth and error correction needed to quantify rare but consequential edited products

Define minimum read depth and error correction needed to quantify rare but consequential edited products.

- **Routing name:** `define-minimum-read-depth-and-error-correction-needed-to-quantify-rare-but-consequential-edited-products`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T049 — Create candidate-specific acceptance limits for desired product, bystander products, indels, and unclassified outcomes

Create candidate-specific acceptance limits for desired product, bystander products, indels, and unclassified outcomes.

- **Routing name:** `create-candidate-specific-acceptance-limits-for-desired-product-bystander-products-indels-and-unclassified-outcomes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T050 — Generate a product-purity dossier that reports the full allele spectrum rather than only average target-base conversion

Generate a product-purity dossier that reports the full allele spectrum rather than only average target-base conversion.

- **Routing name:** `generate-a-product-purity-dossier-that-reports-the-full-allele-spectrum-rather-than-only-average-target-base-conversion`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. DNA off-target editing and deaminase-independent risk

### MYR-D052-T051 — Enumerate guide-dependent DNA off-target sites using nuclease-specific mismatch, bulge, PAM, and haplotype rules

Enumerate guide-dependent DNA off-target sites using nuclease-specific mismatch, bulge, PAM, and haplotype rules.

- **Routing name:** `enumerate-guide-dependent-dna-off-target-sites-using-nuclease-specific-mismatch-bulge-pam-and-haplotype-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T052 — Score candidate off-target loci while separating Cas-guided binding risk from deaminase-driven nucleotide-conversion risk

Score candidate off-target loci while separating Cas-guided binding risk from deaminase-driven nucleotide-conversion risk.

- **Routing name:** `score-candidate-off-target-loci-while-separating-cas-guided-binding-risk-from-deaminase-driven-nucleotide-conversion-risk`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T053 — Annotate every editable base within each off-target window rather than ranking sites by sequence similarity alone

Annotate every editable base within each off-target window rather than ranking sites by sequence similarity alone.

- **Routing name:** `annotate-every-editable-base-within-each-off-target-window-rather-than-ranking-sites-by-sequence-similarity-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T054 — Prioritize off-target sites by predicted editing, genomic consequence, chromatin accessibility, tissue exposure, and clonal-selection potential

Prioritize off-target sites by predicted editing, genomic consequence, chromatin accessibility, tissue exposure, and clonal-selection potential.

- **Routing name:** `prioritize-off-target-sites-by-predicted-editing-genomic-consequence-chromatin-accessibility-tissue-exposure-and-clonal-selection-potential`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T055 — Assess guide-independent DNA deamination evidence for the exact deaminase and editor architecture without generalizing across variants

Assess guide-independent DNA deamination evidence for the exact deaminase and editor architecture without generalizing across variants.

- **Routing name:** `assess-guide-independent-dna-deamination-evidence-for-the-exact-deaminase-and-editor-architecture-without-generalizing-across-variants`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T056 — Integrate cell-free and cellular off-target assays while preserving their distinct detection biases and exposure conditions

Integrate cell-free and cellular off-target assays while preserving their distinct detection biases and exposure conditions.

- **Routing name:** `integrate-cell-free-and-cellular-off-target-assays-while-preserving-their-distinct-detection-biases-and-exposure-conditions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T057 — Flag repetitive or homologous loci where off-target quantification may be obscured by mapping ambiguity

Flag repetitive or homologous loci where off-target quantification may be obscured by mapping ambiguity.

- **Routing name:** `flag-repetitive-or-homologous-loci-where-off-target-quantification-may-be-obscured-by-mapping-ambiguity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T058 — Estimate sample-specific off-target risk from variants that create new PAMs, protospacers, or editable sequence contexts

Estimate sample-specific off-target risk from variants that create new PAMs, protospacers, or editable sequence contexts.

- **Routing name:** `estimate-sample-specific-off-target-risk-from-variants-that-create-new-pams-protospacers-or-editable-sequence-contexts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T059 — Define empirical validation panels containing top sequence candidates, high-consequence loci, and assay-discovered sites

Define empirical validation panels containing top sequence candidates, high-consequence loci, and assay-discovered sites.

- **Routing name:** `define-empirical-validation-panels-containing-top-sequence-candidates-high-consequence-loci-and-assay-discovered-sites`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T060 — Produce a DNA specificity report with guide-dependent, guide-independent, structural-event, and detection-limit sections

Produce a DNA specificity report with guide-dependent, guide-independent, structural-event, and detection-limit sections.

- **Routing name:** `produce-a-dna-specificity-report-with-guide-dependent-guide-independent-structural-event-and-detection-limit-sections`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. RNA off-target editing and transcriptome context

### MYR-D052-T061 — Assess whether the selected deaminase architecture has documented guide-independent or guide-dependent RNA editing activity

Assess whether the selected deaminase architecture has documented guide-independent or guide-dependent RNA editing activity.

- **Routing name:** `assess-whether-the-selected-deaminase-architecture-has-documented-guide-independent-or-guide-dependent-rna-editing-activity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T062 — Identify transcriptome-wide sequence motifs and highly expressed transcripts that could be susceptible under intended editor exposure

Identify transcriptome-wide sequence motifs and highly expressed transcripts that could be susceptible under intended editor exposure.

- **Routing name:** `identify-transcriptome-wide-sequence-motifs-and-highly-expressed-transcripts-that-could-be-susceptible-under-intended-editor-exposure`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T063 — Distinguish transient RNA edits from permanent DNA edits while still evaluating functional and toxicological consequences

Distinguish transient RNA edits from permanent DNA edits while still evaluating functional and toxicological consequences.

- **Routing name:** `distinguish-transient-rna-edits-from-permanent-dna-edits-while-still-evaluating-functional-and-toxicological-consequences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T064 — Quantify RNA off-target editing with matched untreated, editor-only, guide-only, and technical controls when evidence is available

Quantify RNA off-target editing with matched untreated, editor-only, guide-only, and technical controls when evidence is available.

- **Routing name:** `quantify-rna-off-target-editing-with-matched-untreated-editor-only-guide-only-and-technical-controls-when-evidence-is-available`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T065 — Correct transcriptome-wide RNA editing analysis for mapping artefacts, germline variants, paralogs, and endogenous editing sites

Correct transcriptome-wide RNA editing analysis for mapping artefacts, germline variants, paralogs, and endogenous editing sites.

- **Routing name:** `correct-transcriptome-wide-rna-editing-analysis-for-mapping-artefacts-germline-variants-paralogs-and-endogenous-editing-sites`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T066 — Prioritize recurrent nonsynonymous, splice-altering, regulatory, or dosage-sensitive transcript edits for orthogonal confirmation

Prioritize recurrent nonsynonymous, splice-altering, regulatory, or dosage-sensitive transcript edits for orthogonal confirmation.

- **Routing name:** `prioritize-recurrent-nonsynonymous-splice-altering-regulatory-or-dosage-sensitive-transcript-edits-for-orthogonal-confirmation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T067 — Compare RNA-off-target profiles across editor variants designed to reduce promiscuous deaminase activity

Compare RNA-off-target profiles across editor variants designed to reduce promiscuous deaminase activity.

- **Routing name:** `compare-rna-off-target-profiles-across-editor-variants-designed-to-reduce-promiscuous-deaminase-activity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T068 — Assess whether short editor exposure sufficiently mitigates RNA editing without compromising desired DNA product purity

Assess whether short editor exposure sufficiently mitigates RNA editing without compromising desired DNA product purity.

- **Routing name:** `assess-whether-short-editor-exposure-sufficiently-mitigates-rna-editing-without-compromising-desired-dna-product-purity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T069 — Define assay detection limits and tissue-expression boundaries before declaring absence of consequential RNA off-target activity

Define assay detection limits and tissue-expression boundaries before declaring absence of consequential RNA off-target activity.

- **Routing name:** `define-assay-detection-limits-and-tissue-expression-boundaries-before-declaring-absence-of-consequential-rna-off-target-activity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T070 — Generate a transcriptome specificity ledger linking sites, frequencies, functional annotations, controls, and reversibility

Generate a transcriptome specificity ledger linking sites, frequencies, functional annotations, controls, and reversibility.

- **Routing name:** `generate-a-transcriptome-specificity-ledger-linking-sites-frequencies-functional-annotations-controls-and-reversibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Cell context, delivery, and exposure-aware performance

### MYR-D052-T071 — Assess target-locus accessibility, DNA-repair state, cell-cycle status, and target-cell abundance in the intended biological system

Assess target-locus accessibility, DNA-repair state, cell-cycle status, and target-cell abundance in the intended biological system.

- **Routing name:** `assess-target-locus-accessibility-dna-repair-state-cell-cycle-status-and-target-cell-abundance-in-the-intended-biological-system`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T072 — Compare editor delivery as ribonucleoprotein, mRNA, viral, plasmid, or split systems with respect to onset, duration, and specificity

Compare editor delivery as ribonucleoprotein, mRNA, viral, plasmid, or split systems with respect to onset, duration, and specificity.

- **Routing name:** `compare-editor-delivery-as-ribonucleoprotein-mrna-viral-plasmid-or-split-systems-with-respect-to-onset-duration-and-specificity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T073 — Estimate whether vector packaging constraints require compact editors, split architectures, dual vectors, or alternative delivery modalities

Estimate whether vector packaging constraints require compact editors, split architectures, dual vectors, or alternative delivery modalities.

- **Routing name:** `estimate-whether-vector-packaging-constraints-require-compact-editors-split-architectures-dual-vectors-or-alternative-delivery-modalities`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T074 — Account for editor expression kinetics when translating in vitro efficiency and off-target measurements to intended exposure

Account for editor expression kinetics when translating in vitro efficiency and off-target measurements to intended exposure.

- **Routing name:** `account-for-editor-expression-kinetics-when-translating-in-vitro-efficiency-and-off-target-measurements-to-intended-exposure`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T075 — Evaluate tissue distribution and non-target-cell editing risk from the selected delivery system independently of molecular specificity

Evaluate tissue distribution and non-target-cell editing risk from the selected delivery system independently of molecular specificity.

- **Routing name:** `evaluate-tissue-distribution-and-non-target-cell-editing-risk-from-the-selected-delivery-system-independently-of-molecular-specificity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T076 — Flag immune recognition risks related to editor protein, vector, repeated dosing, or innate sensing without inferring clinical acceptability

Flag immune recognition risks related to editor protein, vector, repeated dosing, or innate sensing without inferring clinical acceptability.

- **Routing name:** `flag-immune-recognition-risks-related-to-editor-protein-vector-repeated-dosing-or-innate-sensing-without-inferring-clinical-acceptability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T077 — Assess whether target cells are dividing or quiescent and whether that changes expected editing, repair, persistence, or selection

Assess whether target cells are dividing or quiescent and whether that changes expected editing, repair, persistence, or selection.

- **Routing name:** `assess-whether-target-cells-are-dividing-or-quiescent-and-whether-that-changes-expected-editing-repair-persistence-or-selection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T078 — Compare ex vivo and in vivo workflows using distinct release, biodistribution, clonality, and follow-up requirements

Compare ex vivo and in vivo workflows using distinct release, biodistribution, clonality, and follow-up requirements.

- **Routing name:** `compare-ex-vivo-and-in-vivo-workflows-using-distinct-release-biodistribution-clonality-and-follow-up-requirements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T079 — Identify delivery conditions that could create sustained editor expression beyond the specificity evidence base

Identify delivery conditions that could create sustained editor expression beyond the specificity evidence base.

- **Routing name:** `identify-delivery-conditions-that-could-create-sustained-editor-expression-beyond-the-specificity-evidence-base`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T080 — Produce a context-transfer matrix showing which activity and safety claims are directly supported, extrapolated, or unknown

Produce a context-transfer matrix showing which activity and safety claims are directly supported, extrapolated, or unknown.

- **Routing name:** `produce-a-context-transfer-matrix-showing-which-activity-and-safety-claims-are-directly-supported-extrapolated-or-unknown`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Model calibration and experimental evidence integration

### MYR-D052-T081 — Assemble editor-specific training and validation evidence with sequence, cell type, delivery format, assay, and outcome definitions

Assemble editor-specific training and validation evidence with sequence, cell type, delivery format, assay, and outcome definitions.

- **Routing name:** `assemble-editor-specific-training-and-validation-evidence-with-sequence-cell-type-delivery-format-assay-and-outcome-definitions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T082 — Benchmark activity and product-purity models on held-out sequence contexts that resemble the intended design space

Benchmark activity and product-purity models on held-out sequence contexts that resemble the intended design space.

- **Routing name:** `benchmark-activity-and-product-purity-models-on-held-out-sequence-contexts-that-resemble-the-intended-design-space`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T083 — Prevent leakage across duplicated guides, shared loci, close sequence analogues, cell replicates, and publication-derived splits

Prevent leakage across duplicated guides, shared loci, close sequence analogues, cell replicates, and publication-derived splits.

- **Routing name:** `prevent-leakage-across-duplicated-guides-shared-loci-close-sequence-analogues-cell-replicates-and-publication-derived-splits`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T084 — Calibrate predicted probabilities for target conversion, pure product, bystanders, and indels rather than reporting raw scores alone

Calibrate predicted probabilities for target conversion, pure product, bystanders, and indels rather than reporting raw scores alone.

- **Routing name:** `calibrate-predicted-probabilities-for-target-conversion-pure-product-bystanders-and-indels-rather-than-reporting-raw-scores-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T085 — Compare model residuals across nucleotide context, window position, editor variant, chromatin state, and cell type

Compare model residuals across nucleotide context, window position, editor variant, chromatin state, and cell type.

- **Routing name:** `compare-model-residuals-across-nucleotide-context-window-position-editor-variant-chromatin-state-and-cell-type`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T086 — Use experimentally measured candidates to update rankings while preserving pre-specified acceptance criteria and auditability

Use experimentally measured candidates to update rankings while preserving pre-specified acceptance criteria and auditability.

- **Routing name:** `use-experimentally-measured-candidates-to-update-rankings-while-preserving-pre-specified-acceptance-criteria-and-auditability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T087 — Identify information-rich candidates that discriminate competing editor or window hypotheses when testing capacity is limited

Identify information-rich candidates that discriminate competing editor or window hypotheses when testing capacity is limited.

- **Routing name:** `identify-information-rich-candidates-that-discriminate-competing-editor-or-window-hypotheses-when-testing-capacity-is-limited`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T088 — Retain failed editor-guide combinations and unexpected products as negative evidence for future design cycles

Retain failed editor-guide combinations and unexpected products as negative evidence for future design cycles.

- **Routing name:** `retain-failed-editor-guide-combinations-and-unexpected-products-as-negative-evidence-for-future-design-cycles`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T089 — Define when model uncertainty or domain shift requires empirical screening rather than computational selection

Define when model uncertainty or domain shift requires empirical screening rather than computational selection.

- **Routing name:** `define-when-model-uncertainty-or-domain-shift-requires-empirical-screening-rather-than-computational-selection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T090 — Generate a model-evidence report with calibration, applicability domain, residual patterns, and unresolved uncertainties

Generate a model-evidence report with calibration, applicability domain, residual patterns, and unresolved uncertainties.

- **Routing name:** `generate-a-model-evidence-report-with-calibration-applicability-domain-residual-patterns-and-unresolved-uncertainties`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Decision governance, release, and lifecycle control

### MYR-D052-T091 — Rank candidates by desired-product probability, bystander acceptability, DNA specificity, RNA specificity, delivery fit, and evidence strength

Rank candidates by desired-product probability, bystander acceptability, DNA specificity, RNA specificity, delivery fit, and evidence strength.

- **Routing name:** `rank-candidates-by-desired-product-probability-bystander-acceptability-dna-specificity-rna-specificity-delivery-fit-and-evidence-strength`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T092 — Define advance, reserve, redesign, and reject states before reviewing the final candidate set

Define advance, reserve, redesign, and reject states before reviewing the final candidate set.

- **Routing name:** `define-advance-reserve-redesign-and-reject-states-before-reviewing-the-final-candidate-set`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T093 — Block release when editor identity, target haplotype, product spectrum, off-target search, or assay sensitivity remains unresolved

Block release when editor identity, target haplotype, product spectrum, off-target search, or assay sensitivity remains unresolved.

- **Routing name:** `block-release-when-editor-identity-target-haplotype-product-spectrum-off-target-search-or-assay-sensitivity-remains-unresolved`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T094 — Require independent base-editing safety review for designs affecting oncogenes, tumour suppressors, reproductive tissues, dosage-sensitive genes, or irreversible clinical outcomes

Require independent base-editing safety review for designs affecting oncogenes, tumour suppressors, reproductive tissues, dosage-sensitive genes, or irreversible clinical outcomes.

- **Routing name:** `require-independent-base-editing-safety-review-for-designs-affecting-oncogenes-tumour-suppressors-reproductive-tissues-dosage-sensitive-genes-or-irreversible-clinical-outcomes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T095 — Create machine-readable pass, warning, fail, and no-call states for every editor-guide candidate and critical evidence dimension

Create machine-readable pass, warning, fail, and no-call states for every editor-guide candidate and critical evidence dimension.

- **Routing name:** `create-machine-readable-pass-warning-fail-and-no-call-states-for-every-editor-guide-candidate-and-critical-evidence-dimension`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T096 — Record editor sequence, guide sequence, reference build, model versions, assay conditions, and reviewer decisions in the release manifest

Record editor sequence, guide sequence, reference build, model versions, assay conditions, and reviewer decisions in the release manifest.

- **Routing name:** `record-editor-sequence-guide-sequence-reference-build-model-versions-assay-conditions-and-reviewer-decisions-in-the-release-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T097 — Generate a concise design card linking intended conversion, window, bystanders, purity, specificity, delivery, and next validation step

Generate a concise design card linking intended conversion, window, bystanders, purity, specificity, delivery, and next validation step.

- **Routing name:** `generate-a-concise-design-card-linking-intended-conversion-window-bystanders-purity-specificity-delivery-and-next-validation-step`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T098 — Schedule reanalysis when editor variants, scoring models, population resources, regulatory guidance, or empirical evidence materially change

Schedule reanalysis when editor variants, scoring models, population resources, regulatory guidance, or empirical evidence materially change.

- **Routing name:** `schedule-reanalysis-when-editor-variants-scoring-models-population-resources-regulatory-guidance-or-empirical-evidence-materially-change`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T099 — Keep computational nomination distinct from wet-lab confirmation, product release, clinical dosing, and long-term safety conclusions

Keep computational nomination distinct from wet-lab confirmation, product release, clinical dosing, and long-term safety conclusions.

- **Routing name:** `keep-computational-nomination-distinct-from-wet-lab-confirmation-product-release-clinical-dosing-and-long-term-safety-conclusions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D052-T100 — Release the base-editing package only after sequence, product-purity, specificity, delivery, safety, and provenance gates pass

Release the base-editing package only after sequence, product-purity, specificity, delivery, safety, and provenance gates pass.

- **Routing name:** `release-the-base-editing-package-only-after-sequence-product-purity-specificity-delivery-safety-and-provenance-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
