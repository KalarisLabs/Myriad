# D053 — Prime-Editing System Design

Batch **006** · 10 workstreams · 100 tasks

## 01. Edit definition and prime-editing feasibility

### MYR-D053-T001 — Normalize the intended substitution, insertion, deletion, or composite edit against a declared genome build, transcript release, strand, and haplotype

Normalize the intended substitution, insertion, deletion, or composite edit against a declared genome build, transcript release, strand, and haplotype.

- **Routing name:** `normalize-the-intended-substitution-insertion-deletion-or-composite-edit-against-a-declared-genome-build-transcript-release-strand-and-haplotype`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T002 — Confirm that the requested change can be encoded within a supported prime-editing architecture without hidden coordinate or orientation ambiguity

Confirm that the requested change can be encoded within a supported prime-editing architecture without hidden coordinate or orientation ambiguity.

- **Routing name:** `confirm-that-the-requested-change-can-be-encoded-within-a-supported-prime-editing-architecture-without-hidden-coordinate-or-orientation-ambiguity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T003 — Define acceptable edited alleles, prohibited byproducts, minimum desired-product purity, and maximum indel burden before pegRNA design

Define acceptable edited alleles, prohibited byproducts, minimum desired-product purity, and maximum indel burden before pegRNA design.

- **Routing name:** `define-acceptable-edited-alleles-prohibited-byproducts-minimum-desired-product-purity-and-maximum-indel-burden-before-pegrna-design`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T004 — Identify all transcript, coding, splice, regulatory, and overlapping-gene consequences of the intended edit and nearby sequence changes

Identify all transcript, coding, splice, regulatory, and overlapping-gene consequences of the intended edit and nearby sequence changes.

- **Routing name:** `identify-all-transcript-coding-splice-regulatory-and-overlapping-gene-consequences-of-the-intended-edit-and-nearby-sequence-changes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T005 — Capture sample-specific variants that alter PAMs, protospacer binding, primer binding, reverse-transcription templates, or product interpretation

Capture sample-specific variants that alter PAMs, protospacer binding, primer binding, reverse-transcription templates, or product interpretation.

- **Routing name:** `capture-sample-specific-variants-that-alter-pams-protospacer-binding-primer-binding-reverse-transcription-templates-or-product-interpretation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T006 — Specify target cell type, division state, delivery format, exposure duration, and intended editor generation because performance is context dependent

Specify target cell type, division state, delivery format, exposure duration, and intended editor generation because performance is context dependent.

- **Routing name:** `specify-target-cell-type-division-state-delivery-format-exposure-duration-and-intended-editor-generation-because-performance-is-context-dependent`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T007 — Compare prime editing with base editing, nuclease-mediated repair, RNA editing, or nonediting alternatives using explicit suitability criteria

Compare prime editing with base editing, nuclease-mediated repair, RNA editing, or nonediting alternatives using explicit suitability criteria.

- **Routing name:** `compare-prime-editing-with-base-editing-nuclease-mediated-repair-rna-editing-or-nonediting-alternatives-using-explicit-suitability-criteria`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T008 — Define whether silent auxiliary changes are permissible for PAM disruption, mismatch repair evasion, or product enrichment

Define whether silent auxiliary changes are permissible for PAM disruption, mismatch repair evasion, or product enrichment.

- **Routing name:** `define-whether-silent-auxiliary-changes-are-permissible-for-pam-disruption-mismatch-repair-evasion-or-product-enrichment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T009 — Create a versioned source manifest for editor constructs, reference sequences, prediction models, assay evidence, and safety resources

Create a versioned source manifest for editor constructs, reference sequences, prediction models, assay evidence, and safety resources.

- **Routing name:** `create-a-versioned-source-manifest-for-editor-constructs-reference-sequences-prediction-models-assay-evidence-and-safety-resources`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T010 — Issue a no-call when the desired edit, target locus, or acceptable product spectrum cannot be represented unambiguously

Issue a no-call when the desired edit, target locus, or acceptable product spectrum cannot be represented unambiguously.

- **Routing name:** `issue-a-no-call-when-the-desired-edit-target-locus-or-acceptable-product-spectrum-cannot-be-represented-unambiguously`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. Protospacer and PAM candidate enumeration

### MYR-D053-T011 — Enumerate strand-resolved protospacers whose nick positions permit reverse-transcription templates to encode the complete desired edit

Enumerate strand-resolved protospacers whose nick positions permit reverse-transcription templates to encode the complete desired edit.

- **Routing name:** `enumerate-strand-resolved-protospacers-whose-nick-positions-permit-reverse-transcription-templates-to-encode-the-complete-desired-edit`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T012 — Map each candidate nick site to edit distance, PAM identity, strand orientation, sequence context, and expected flap geometry

Map each candidate nick site to edit distance, PAM identity, strand orientation, sequence context, and expected flap geometry.

- **Routing name:** `map-each-candidate-nick-site-to-edit-distance-pam-identity-strand-orientation-sequence-context-and-expected-flap-geometry`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T013 — Identify candidates enabled by canonical and engineered PAM variants while separating validated PAM support from speculative compatibility

Identify candidates enabled by canonical and engineered PAM variants while separating validated PAM support from speculative compatibility.

- **Routing name:** `identify-candidates-enabled-by-canonical-and-engineered-pam-variants-while-separating-validated-pam-support-from-speculative-compatibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T014 — Flag protospacers with repeats, homopolymers, extreme composition, self-complementarity, or expression-system liabilities

Flag protospacers with repeats, homopolymers, extreme composition, self-complementarity, or expression-system liabilities.

- **Routing name:** `flag-protospacers-with-repeats-homopolymers-extreme-composition-self-complementarity-or-expression-system-liabilities`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T015 — Assess guide-binding disruption caused by the intended edit, silent auxiliary changes, or linked haplotype variants

Assess guide-binding disruption caused by the intended edit, silent auxiliary changes, or linked haplotype variants.

- **Routing name:** `assess-guide-binding-disruption-caused-by-the-intended-edit-silent-auxiliary-changes-or-linked-haplotype-variants`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T016 — Calculate whether the edited product destroys the PAM or seed sequence and how that may influence re-editing or product enrichment

Calculate whether the edited product destroys the PAM or seed sequence and how that may influence re-editing or product enrichment.

- **Routing name:** `calculate-whether-the-edited-product-destroys-the-pam-or-seed-sequence-and-how-that-may-influence-re-editing-or-product-enrichment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T017 — Generate alternative protospacers that trade edit distance against on-target activity, template length, byproduct risk, and specificity

Generate alternative protospacers that trade edit distance against on-target activity, template length, byproduct risk, and specificity.

- **Routing name:** `generate-alternative-protospacers-that-trade-edit-distance-against-on-target-activity-template-length-byproduct-risk-and-specificity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T018 — Prevent strand errors by reconstructing expected nicked strand, primer-binding sequence, template sequence, and final edited duplex independently

Prevent strand errors by reconstructing expected nicked strand, primer-binding sequence, template sequence, and final edited duplex independently.

- **Routing name:** `prevent-strand-errors-by-reconstructing-expected-nicked-strand-primer-binding-sequence-template-sequence-and-final-edited-duplex-independently`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T019 — Create a candidate matrix linking nuclease variant, protospacer, PAM, nick coordinate, edit geometry, and editable haplotypes

Create a candidate matrix linking nuclease variant, protospacer, PAM, nick coordinate, edit geometry, and editable haplotypes.

- **Routing name:** `create-a-candidate-matrix-linking-nuclease-variant-protospacer-pam-nick-coordinate-edit-geometry-and-editable-haplotypes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T020 — Reject protospacers whose geometry cannot encode the requested edit within supported template or editor constraints

Reject protospacers whose geometry cannot encode the requested edit within supported template or editor constraints.

- **Routing name:** `reject-protospacers-whose-geometry-cannot-encode-the-requested-edit-within-supported-template-or-editor-constraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. Primer-binding-site design and initiation control

### MYR-D053-T021 — Enumerate primer-binding-site lengths for each protospacer using the exact nicked-strand sequence and orientation

Enumerate primer-binding-site lengths for each protospacer using the exact nicked-strand sequence and orientation.

- **Routing name:** `enumerate-primer-binding-site-lengths-for-each-protospacer-using-the-exact-nicked-strand-sequence-and-orientation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T022 — Estimate primer-binding stability from sequence composition, predicted melting behaviour, secondary structure, and intended cellular temperature

Estimate primer-binding stability from sequence composition, predicted melting behaviour, secondary structure, and intended cellular temperature.

- **Routing name:** `estimate-primer-binding-stability-from-sequence-composition-predicted-melting-behaviour-secondary-structure-and-intended-cellular-temperature`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T023 — Flag primer-binding sites disrupted by sample variants, common polymorphisms, repetitive sequence, or unstable terminal motifs

Flag primer-binding sites disrupted by sample variants, common polymorphisms, repetitive sequence, or unstable terminal motifs.

- **Routing name:** `flag-primer-binding-sites-disrupted-by-sample-variants-common-polymorphisms-repetitive-sequence-or-unstable-terminal-motifs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T024 — Compare primer-binding designs across validated length ranges rather than assuming one universal optimum

Compare primer-binding designs across validated length ranges rather than assuming one universal optimum.

- **Routing name:** `compare-primer-binding-designs-across-validated-length-ranges-rather-than-assuming-one-universal-optimum`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T025 — Assess whether excessive primer-binding complementarity could impair pegRNA folding, reverse-transcription initiation, or product release

Assess whether excessive primer-binding complementarity could impair pegRNA folding, reverse-transcription initiation, or product release.

- **Routing name:** `assess-whether-excessive-primer-binding-complementarity-could-impair-pegrna-folding-reverse-transcription-initiation-or-product-release`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T026 — Identify primer-binding sequences likely to pair with unintended genomic or pegRNA regions and create ambiguous initiation hypotheses

Identify primer-binding sequences likely to pair with unintended genomic or pegRNA regions and create ambiguous initiation hypotheses.

- **Routing name:** `identify-primer-binding-sequences-likely-to-pair-with-unintended-genomic-or-pegrna-regions-and-create-ambiguous-initiation-hypotheses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T027 — Preserve editor-, cell-, and locus-specific evidence when ranking primer-binding-site variants

Preserve editor-, cell-, and locus-specific evidence when ranking primer-binding-site variants.

- **Routing name:** `preserve-editor-cell-and-locus-specific-evidence-when-ranking-primer-binding-site-variants`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T028 — Generate a diversified primer-binding panel that samples distinct stability regimes when prediction uncertainty remains high

Generate a diversified primer-binding panel that samples distinct stability regimes when prediction uncertainty remains high.

- **Routing name:** `generate-a-diversified-primer-binding-panel-that-samples-distinct-stability-regimes-when-prediction-uncertainty-remains-high`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T029 — Record calculated and measured primer-binding features separately so empirical outcomes can recalibrate future designs

Record calculated and measured primer-binding features separately so empirical outcomes can recalibrate future designs.

- **Routing name:** `record-calculated-and-measured-primer-binding-features-separately-so-empirical-outcomes-can-recalibrate-future-designs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T030 — Produce a primer-binding shortlist with stability rationale, variant sensitivity, uncertainty, and paired template candidates

Produce a primer-binding shortlist with stability rationale, variant sensitivity, uncertainty, and paired template candidates.

- **Routing name:** `produce-a-primer-binding-shortlist-with-stability-rationale-variant-sensitivity-uncertainty-and-paired-template-candidates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. Reverse-transcription-template architecture

### MYR-D053-T031 — Enumerate reverse-transcription templates that fully encode the desired edit plus sufficient downstream homology for flap resolution

Enumerate reverse-transcription templates that fully encode the desired edit plus sufficient downstream homology for flap resolution.

- **Routing name:** `enumerate-reverse-transcription-templates-that-fully-encode-the-desired-edit-plus-sufficient-downstream-homology-for-flap-resolution`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T032 — Calculate edit position within the template, homology length, auxiliary substitutions, terminal sequence, and expected edited-strand product

Calculate edit position within the template, homology length, auxiliary substitutions, terminal sequence, and expected edited-strand product.

- **Routing name:** `calculate-edit-position-within-the-template-homology-length-auxiliary-substitutions-terminal-sequence-and-expected-edited-strand-product`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T033 — Compare template lengths across substitutions, insertions, deletions, and composite edits without transferring unsupported heuristics

Compare template lengths across substitutions, insertions, deletions, and composite edits without transferring unsupported heuristics.

- **Routing name:** `compare-template-lengths-across-substitutions-insertions-deletions-and-composite-edits-without-transferring-unsupported-heuristics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T034 — Flag templates containing repetitive motifs, long homopolymers, unstable termini, self-complementarity, or synthesis liabilities

Flag templates containing repetitive motifs, long homopolymers, unstable termini, self-complementarity, or synthesis liabilities.

- **Routing name:** `flag-templates-containing-repetitive-motifs-long-homopolymers-unstable-termini-self-complementarity-or-synthesis-liabilities`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T035 — Assess whether silent substitutions can disrupt PAMs, bias mismatch repair, prevent re-editing, or create unacceptable coding consequences

Assess whether silent substitutions can disrupt PAMs, bias mismatch repair, prevent re-editing, or create unacceptable coding consequences.

- **Routing name:** `assess-whether-silent-substitutions-can-disrupt-pams-bias-mismatch-repair-prevent-re-editing-or-create-unacceptable-coding-consequences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T036 — Identify templates whose encoded product creates cryptic splice sites, regulatory motifs, RNA structures, or unintended amino-acid changes

Identify templates whose encoded product creates cryptic splice sites, regulatory motifs, RNA structures, or unintended amino-acid changes.

- **Routing name:** `identify-templates-whose-encoded-product-creates-cryptic-splice-sites-regulatory-motifs-rna-structures-or-unintended-amino-acid-changes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T037 — Estimate template secondary structure and interaction with scaffold or primer-binding regions without treating structure prediction as definitive

Estimate template secondary structure and interaction with scaffold or primer-binding regions without treating structure prediction as definitive.

- **Routing name:** `estimate-template-secondary-structure-and-interaction-with-scaffold-or-primer-binding-regions-without-treating-structure-prediction-as-definitive`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T038 — Generate template variants that separate homology-length effects from auxiliary-change effects in empirical testing

Generate template variants that separate homology-length effects from auxiliary-change effects in empirical testing.

- **Routing name:** `generate-template-variants-that-separate-homology-length-effects-from-auxiliary-change-effects-in-empirical-testing`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T039 — Reconstruct the complete edited genomic sequence for every template and verify reference-to-product alignment programmatically

Reconstruct the complete edited genomic sequence for every template and verify reference-to-product alignment programmatically.

- **Routing name:** `reconstruct-the-complete-edited-genomic-sequence-for-every-template-and-verify-reference-to-product-alignment-programmatically`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T040 — Produce a reverse-transcription-template ledger with sequence, encoded changes, homology, structural flags, and expected products

Produce a reverse-transcription-template ledger with sequence, encoded changes, homology, structural flags, and expected products.

- **Routing name:** `produce-a-reverse-transcription-template-ledger-with-sequence-encoded-changes-homology-structural-flags-and-expected-products`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. Editor architecture and secondary-nick strategy

### MYR-D053-T041 — Match pegRNA candidates to prime-editor generations, reverse transcriptase variants, Cas nickases, and expression formats supported by evidence

Match pegRNA candidates to prime-editor generations, reverse transcriptase variants, Cas nickases, and expression formats supported by evidence.

- **Routing name:** `match-pegrna-candidates-to-prime-editor-generations-reverse-transcriptase-variants-cas-nickases-and-expression-formats-supported-by-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T042 — Determine whether PE2, PE3, PE3b, paired, twin, or related architectures are appropriate for the edit and cell context

Determine whether PE2, PE3, PE3b, paired, twin, or related architectures are appropriate for the edit and cell context.

- **Routing name:** `determine-whether-pe2-pe3-pe3b-paired-twin-or-related-architectures-are-appropriate-for-the-edit-and-cell-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T043 — Enumerate secondary nicking guides with strand, distance, orientation, predicted activity, and allele-specific recognition annotations

Enumerate secondary nicking guides with strand, distance, orientation, predicted activity, and allele-specific recognition annotations.

- **Routing name:** `enumerate-secondary-nicking-guides-with-strand-distance-orientation-predicted-activity-and-allele-specific-recognition-annotations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T044 — Assess whether secondary nicking occurs preferentially on edited or unedited alleles and how that affects product purity

Assess whether secondary nicking occurs preferentially on edited or unedited alleles and how that affects product purity.

- **Routing name:** `assess-whether-secondary-nicking-occurs-preferentially-on-edited-or-unedited-alleles-and-how-that-affects-product-purity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T045 — Balance editing enhancement against indel, translocation, and undesired repair risk when ranking nicking strategies

Balance editing enhancement against indel, translocation, and undesired repair risk when ranking nicking strategies.

- **Routing name:** `balance-editing-enhancement-against-indel-translocation-and-undesired-repair-risk-when-ranking-nicking-strategies`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T046 — Flag secondary guides that introduce high-consequence off-targets or overlap dosage-sensitive regulatory sequence

Flag secondary guides that introduce high-consequence off-targets or overlap dosage-sensitive regulatory sequence.

- **Routing name:** `flag-secondary-guides-that-introduce-high-consequence-off-targets-or-overlap-dosage-sensitive-regulatory-sequence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T047 — Assess mismatch-repair modulation strategies only where the exact editor system, cell context, and safety implications are supported

Assess mismatch-repair modulation strategies only where the exact editor system, cell context, and safety implications are supported.

- **Routing name:** `assess-mismatch-repair-modulation-strategies-only-where-the-exact-editor-system-cell-context-and-safety-implications-are-supported`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T048 — Compare compact, split, dual-vector, or transient editor formats against packaging and exposure constraints

Compare compact, split, dual-vector, or transient editor formats against packaging and exposure constraints.

- **Routing name:** `compare-compact-split-dual-vector-or-transient-editor-formats-against-packaging-and-exposure-constraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T049 — Lock exact protein, linker, reverse-transcriptase, guide-scaffold, and nicking-guide versions before interpreting evidence

Lock exact protein, linker, reverse-transcriptase, guide-scaffold, and nicking-guide versions before interpreting evidence.

- **Routing name:** `lock-exact-protein-linker-reverse-transcriptase-guide-scaffold-and-nicking-guide-versions-before-interpreting-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T050 — Generate an architecture decision table connecting edit class, pegRNA, secondary nick, delivery format, expected benefit, and risk

Generate an architecture decision table connecting edit class, pegRNA, secondary nick, delivery format, expected benefit, and risk.

- **Routing name:** `generate-an-architecture-decision-table-connecting-edit-class-pegrna-secondary-nick-delivery-format-expected-benefit-and-risk`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. pegRNA stability and engineered scaffold extensions

### MYR-D053-T051 — Predict pegRNA folding across spacer, scaffold, primer-binding site, template, and engineered stabilizing extension regions

Predict pegRNA folding across spacer, scaffold, primer-binding site, template, and engineered stabilizing extension regions.

- **Routing name:** `predict-pegrna-folding-across-spacer-scaffold-primer-binding-site-template-and-engineered-stabilizing-extension-regions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T052 — Identify interactions that could sequester the primer-binding site, disrupt scaffold recognition, or expose degradation-prone termini

Identify interactions that could sequester the primer-binding site, disrupt scaffold recognition, or expose degradation-prone termini.

- **Routing name:** `identify-interactions-that-could-sequester-the-primer-binding-site-disrupt-scaffold-recognition-or-expose-degradation-prone-termini`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T053 — Compare unmodified pegRNAs with validated structured or protective extensions using construct-specific evidence

Compare unmodified pegRNAs with validated structured or protective extensions using construct-specific evidence.

- **Routing name:** `compare-unmodified-pegrnas-with-validated-structured-or-protective-extensions-using-construct-specific-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T054 — Flag engineered extensions whose benefit was demonstrated only in incompatible editor, cell, or delivery contexts

Flag engineered extensions whose benefit was demonstrated only in incompatible editor, cell, or delivery contexts.

- **Routing name:** `flag-engineered-extensions-whose-benefit-was-demonstrated-only-in-incompatible-editor-cell-or-delivery-contexts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T055 — Assess sequence motifs associated with premature transcription termination, variable processing, or guide-expression instability

Assess sequence motifs associated with premature transcription termination, variable processing, or guide-expression instability.

- **Routing name:** `assess-sequence-motifs-associated-with-premature-transcription-termination-variable-processing-or-guide-expression-instability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T056 — Check compatibility of pegRNA designs with RNA polymerase promoter constraints and intended transcript initiation nucleotide

Check compatibility of pegRNA designs with RNA polymerase promoter constraints and intended transcript initiation nucleotide.

- **Routing name:** `check-compatibility-of-pegrna-designs-with-rna-polymerase-promoter-constraints-and-intended-transcript-initiation-nucleotide`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T057 — Estimate synthesis and cloning feasibility for long or structured pegRNAs without inferring biological performance from manufacturability

Estimate synthesis and cloning feasibility for long or structured pegRNAs without inferring biological performance from manufacturability.

- **Routing name:** `estimate-synthesis-and-cloning-feasibility-for-long-or-structured-pegrnas-without-inferring-biological-performance-from-manufacturability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T058 — Generate matched pegRNA variants that isolate the effect of primer-binding, template, scaffold, or stabilizing architecture

Generate matched pegRNA variants that isolate the effect of primer-binding, template, scaffold, or stabilizing architecture.

- **Routing name:** `generate-matched-pegrna-variants-that-isolate-the-effect-of-primer-binding-template-scaffold-or-stabilizing-architecture`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T059 — Record predicted structure ensembles and uncertainty instead of presenting a single minimum-energy fold as ground truth

Record predicted structure ensembles and uncertainty instead of presenting a single minimum-energy fold as ground truth.

- **Routing name:** `record-predicted-structure-ensembles-and-uncertainty-instead-of-presenting-a-single-minimum-energy-fold-as-ground-truth`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T060 — Produce a pegRNA-stability report with structural liabilities, extension rationale, expression constraints, and test priorities

Produce a pegRNA-stability report with structural liabilities, extension rationale, expression constraints, and test priorities.

- **Routing name:** `produce-a-pegrna-stability-report-with-structural-liabilities-extension-rationale-expression-constraints-and-test-priorities`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Product spectrum and repair-outcome modelling

### MYR-D053-T061 — Enumerate desired edits, partial template incorporations, scaffold-derived insertions, indels, unedited alleles, and unintended substitutions

Enumerate desired edits, partial template incorporations, scaffold-derived insertions, indels, unedited alleles, and unintended substitutions.

- **Routing name:** `enumerate-desired-edits-partial-template-incorporations-scaffold-derived-insertions-indels-unedited-alleles-and-unintended-substitutions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T062 — Distinguish total edit frequency from exact desired-product purity and require both in every candidate comparison

Distinguish total edit frequency from exact desired-product purity and require both in every candidate comparison.

- **Routing name:** `distinguish-total-edit-frequency-from-exact-desired-product-purity-and-require-both-in-every-candidate-comparison`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T063 — Model flap competition, mismatch repair, nick repair, re-editing, and sequence-context effects as hypotheses with explicit uncertainty

Model flap competition, mismatch repair, nick repair, re-editing, and sequence-context effects as hypotheses with explicit uncertainty.

- **Routing name:** `model-flap-competition-mismatch-repair-nick-repair-re-editing-and-sequence-context-effects-as-hypotheses-with-explicit-uncertainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T064 — Identify pegRNA designs likely to produce partial edits because the desired change lies near template boundaries or unstable homology

Identify pegRNA designs likely to produce partial edits because the desired change lies near template boundaries or unstable homology.

- **Routing name:** `identify-pegrna-designs-likely-to-produce-partial-edits-because-the-desired-change-lies-near-template-boundaries-or-unstable-homology`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T065 — Assess whether auxiliary changes create mixed products, haplotype ambiguity, or unintended protein and splice consequences

Assess whether auxiliary changes create mixed products, haplotype ambiguity, or unintended protein and splice consequences.

- **Routing name:** `assess-whether-auxiliary-changes-create-mixed-products-haplotype-ambiguity-or-unintended-protein-and-splice-consequences`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T066 — Define long-read or linked-read analysis when short amplicons cannot resolve complex products or large rearrangements

Define long-read or linked-read analysis when short amplicons cannot resolve complex products or large rearrangements.

- **Routing name:** `define-long-read-or-linked-read-analysis-when-short-amplicons-cannot-resolve-complex-products-or-large-rearrangements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T067 — Quantify low-frequency but high-consequence deletions, insertions, translocations, or chromosomal abnormalities with appropriate assays

Quantify low-frequency but high-consequence deletions, insertions, translocations, or chromosomal abnormalities with appropriate assays.

- **Routing name:** `quantify-low-frequency-but-high-consequence-deletions-insertions-translocations-or-chromosomal-abnormalities-with-appropriate-assays`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T068 — Reconcile product distributions across technical platforms, replicate experiments, cell types, and exposure conditions

Reconcile product distributions across technical platforms, replicate experiments, cell types, and exposure conditions.

- **Routing name:** `reconcile-product-distributions-across-technical-platforms-replicate-experiments-cell-types-and-exposure-conditions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T069 — Establish candidate-specific acceptance limits for exact product, partial products, indels, large events, and unclassified reads

Establish candidate-specific acceptance limits for exact product, partial products, indels, large events, and unclassified reads.

- **Routing name:** `establish-candidate-specific-acceptance-limits-for-exact-product-partial-products-indels-large-events-and-unclassified-reads`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T070 — Generate a complete product-spectrum dossier rather than reporting only the intended edit percentage

Generate a complete product-spectrum dossier rather than reporting only the intended edit percentage.

- **Routing name:** `generate-a-complete-product-spectrum-dossier-rather-than-reporting-only-the-intended-edit-percentage`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Off-target, structural, and genotoxicity assessment

### MYR-D053-T071 — Enumerate guide-dependent off-target sites for pegRNA and secondary nicking guides using nuclease-specific alignment rules

Enumerate guide-dependent off-target sites for pegRNA and secondary nicking guides using nuclease-specific alignment rules.

- **Routing name:** `enumerate-guide-dependent-off-target-sites-for-pegrna-and-secondary-nicking-guides-using-nuclease-specific-alignment-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T072 — Assess prime-editing activity at off-target sites by considering primer-binding and template compatibility in addition to Cas binding

Assess prime-editing activity at off-target sites by considering primer-binding and template compatibility in addition to Cas binding.

- **Routing name:** `assess-prime-editing-activity-at-off-target-sites-by-considering-primer-binding-and-template-compatibility-in-addition-to-cas-binding`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T073 — Identify potential template-derived sequence incorporation at off-target nicks, endogenous breaks, or unintended priming sites

Identify potential template-derived sequence incorporation at off-target nicks, endogenous breaks, or unintended priming sites.

- **Routing name:** `identify-potential-template-derived-sequence-incorporation-at-off-target-nicks-endogenous-breaks-or-unintended-priming-sites`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T074 — Prioritize off-target loci by editing plausibility, genomic consequence, tissue exposure, mappability, and clonal-selection potential

Prioritize off-target loci by editing plausibility, genomic consequence, tissue exposure, mappability, and clonal-selection potential.

- **Routing name:** `prioritize-off-target-loci-by-editing-plausibility-genomic-consequence-tissue-exposure-mappability-and-clonal-selection-potential`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T075 — Evaluate paired-nick and multiplex architectures for translocations, large deletions, inversions, and chromosomal rearrangements

Evaluate paired-nick and multiplex architectures for translocations, large deletions, inversions, and chromosomal rearrangements.

- **Routing name:** `evaluate-paired-nick-and-multiplex-architectures-for-translocations-large-deletions-inversions-and-chromosomal-rearrangements`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T076 — Integrate unbiased and targeted specificity assays while preserving their distinct detection limits and biological contexts

Integrate unbiased and targeted specificity assays while preserving their distinct detection limits and biological contexts.

- **Routing name:** `integrate-unbiased-and-targeted-specificity-assays-while-preserving-their-distinct-detection-limits-and-biological-contexts`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T077 — Assess sample-specific variants that create new protospacer, PAM, primer-binding, or template-compatible off-target configurations

Assess sample-specific variants that create new protospacer, PAM, primer-binding, or template-compatible off-target configurations.

- **Routing name:** `assess-sample-specific-variants-that-create-new-protospacer-pam-primer-binding-or-template-compatible-off-target-configurations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T078 — Flag genomic regions where repeats, homologous loci, or structural variation prevent confident off-target quantification

Flag genomic regions where repeats, homologous loci, or structural variation prevent confident off-target quantification.

- **Routing name:** `flag-genomic-regions-where-repeats-homologous-loci-or-structural-variation-prevent-confident-off-target-quantification`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T079 — Define a validation panel containing sequence-ranked sites, high-consequence sites, assay-discovered sites, and structural-event partners

Define a validation panel containing sequence-ranked sites, high-consequence sites, assay-discovered sites, and structural-event partners.

- **Routing name:** `define-a-validation-panel-containing-sequence-ranked-sites-high-consequence-sites-assay-discovered-sites-and-structural-event-partners`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T080 — Produce a specificity dossier covering pegRNA, nicking guide, template incorporation, structural events, and residual uncertainty

Produce a specificity dossier covering pegRNA, nicking guide, template incorporation, structural events, and residual uncertainty.

- **Routing name:** `produce-a-specificity-dossier-covering-pegrna-nicking-guide-template-incorporation-structural-events-and-residual-uncertainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Prediction calibration and empirical design-of-experiments

### MYR-D053-T081 — Assemble pegRNA outcome data with exact editor, cell type, delivery, sequence, assay, and product definitions

Assemble pegRNA outcome data with exact editor, cell type, delivery, sequence, assay, and product definitions.

- **Routing name:** `assemble-pegrna-outcome-data-with-exact-editor-cell-type-delivery-sequence-assay-and-product-definitions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T082 — Benchmark efficiency and purity models on held-out loci and edit classes resembling the intended design space

Benchmark efficiency and purity models on held-out loci and edit classes resembling the intended design space.

- **Routing name:** `benchmark-efficiency-and-purity-models-on-held-out-loci-and-edit-classes-resembling-the-intended-design-space`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T083 — Prevent leakage across shared protospacers, related templates, duplicate measurements, cell replicates, and publication-derived splits

Prevent leakage across shared protospacers, related templates, duplicate measurements, cell replicates, and publication-derived splits.

- **Routing name:** `prevent-leakage-across-shared-protospacers-related-templates-duplicate-measurements-cell-replicates-and-publication-derived-splits`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T084 — Calibrate predicted exact-edit probability, total editing, indels, and product purity rather than relying on unscaled scores

Calibrate predicted exact-edit probability, total editing, indels, and product purity rather than relying on unscaled scores.

- **Routing name:** `calibrate-predicted-exact-edit-probability-total-editing-indels-and-product-purity-rather-than-relying-on-unscaled-scores`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T085 — Compare residuals across edit distance, primer-binding stability, template length, edit class, sequence motif, and cell context

Compare residuals across edit distance, primer-binding stability, template length, edit class, sequence motif, and cell context.

- **Routing name:** `compare-residuals-across-edit-distance-primer-binding-stability-template-length-edit-class-sequence-motif-and-cell-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T086 — Select diversified pegRNA panels that maximize information about uncertain design dimensions under fixed experimental capacity

Select diversified pegRNA panels that maximize information about uncertain design dimensions under fixed experimental capacity.

- **Routing name:** `select-diversified-pegrna-panels-that-maximize-information-about-uncertain-design-dimensions-under-fixed-experimental-capacity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T087 — Use empirical results to update rankings without changing pre-specified success criteria after seeing outcomes

Use empirical results to update rankings without changing pre-specified success criteria after seeing outcomes.

- **Routing name:** `use-empirical-results-to-update-rankings-without-changing-pre-specified-success-criteria-after-seeing-outcomes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T088 — Preserve failed pegRNAs, partial-edit patterns, and model disagreements as reusable negative evidence

Preserve failed pegRNAs, partial-edit patterns, and model disagreements as reusable negative evidence.

- **Routing name:** `preserve-failed-pegrnas-partial-edit-patterns-and-model-disagreements-as-reusable-negative-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T089 — Define when domain shift or uncertainty requires direct screening rather than model-based nomination

Define when domain shift or uncertainty requires direct screening rather than model-based nomination.

- **Routing name:** `define-when-domain-shift-or-uncertainty-requires-direct-screening-rather-than-model-based-nomination`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T090 — Generate a design-of-experiments matrix linking candidate variants, isolated hypotheses, controls, readouts, and stopping rules

Generate a design-of-experiments matrix linking candidate variants, isolated hypotheses, controls, readouts, and stopping rules.

- **Routing name:** `generate-a-design-of-experiments-matrix-linking-candidate-variants-isolated-hypotheses-controls-readouts-and-stopping-rules`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Decision governance, release, and lifecycle monitoring

### MYR-D053-T091 — Rank complete prime-editing systems by exact-product probability, byproduct burden, specificity, delivery compatibility, and evidence strength

Rank complete prime-editing systems by exact-product probability, byproduct burden, specificity, delivery compatibility, and evidence strength.

- **Routing name:** `rank-complete-prime-editing-systems-by-exact-product-probability-byproduct-burden-specificity-delivery-compatibility-and-evidence-strength`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T092 — Define advance, reserve, redesign, and reject criteria before reviewing the final system rankings

Define advance, reserve, redesign, and reject criteria before reviewing the final system rankings.

- **Routing name:** `define-advance-reserve-redesign-and-reject-criteria-before-reviewing-the-final-system-rankings`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T093 — Block release when reference sequence, pegRNA orientation, editor version, product spectrum, or assay sensitivity remains unresolved

Block release when reference sequence, pegRNA orientation, editor version, product spectrum, or assay sensitivity remains unresolved.

- **Routing name:** `block-release-when-reference-sequence-pegrna-orientation-editor-version-product-spectrum-or-assay-sensitivity-remains-unresolved`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T094 — Require independent prime-editing safety review for designs affecting oncogenes, tumour suppressors, reproductive tissues, dosage-sensitive genes, or irreversible clinical outcomes

Require independent prime-editing safety review for designs affecting oncogenes, tumour suppressors, reproductive tissues, dosage-sensitive genes, or irreversible clinical outcomes.

- **Routing name:** `require-independent-prime-editing-safety-review-for-designs-affecting-oncogenes-tumour-suppressors-reproductive-tissues-dosage-sensitive-genes-or-irreversible-clinical-outcomes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T095 — Create machine-readable pass, warning, fail, and no-call states for every system and critical evidence dimension

Create machine-readable pass, warning, fail, and no-call states for every system and critical evidence dimension.

- **Routing name:** `create-machine-readable-pass-warning-fail-and-no-call-states-for-every-system-and-critical-evidence-dimension`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T096 — Record editor sequence, pegRNA, nicking guide, reference build, models, assays, and reviewer decisions in the release manifest

Record editor sequence, pegRNA, nicking guide, reference build, models, assays, and reviewer decisions in the release manifest.

- **Routing name:** `record-editor-sequence-pegrna-nicking-guide-reference-build-models-assays-and-reviewer-decisions-in-the-release-manifest`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T097 — Generate a concise system card linking intended edit, pegRNA architecture, predicted outcomes, specificity, delivery, and next experiment

Generate a concise system card linking intended edit, pegRNA architecture, predicted outcomes, specificity, delivery, and next experiment.

- **Routing name:** `generate-a-concise-system-card-linking-intended-edit-pegrna-architecture-predicted-outcomes-specificity-delivery-and-next-experiment`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T098 — Schedule reanalysis when editor architectures, prediction models, reference resources, assay methods, or regulatory expectations materially change

Schedule reanalysis when editor architectures, prediction models, reference resources, assay methods, or regulatory expectations materially change.

- **Routing name:** `schedule-reanalysis-when-editor-architectures-prediction-models-reference-resources-assay-methods-or-regulatory-expectations-materially-change`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T099 — Keep computational nomination distinct from wet-lab confirmation, product release, clinical administration, and long-term safety conclusions

Keep computational nomination distinct from wet-lab confirmation, product release, clinical administration, and long-term safety conclusions.

- **Routing name:** `keep-computational-nomination-distinct-from-wet-lab-confirmation-product-release-clinical-administration-and-long-term-safety-conclusions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D053-T100 — Release the prime-editing package only after sequence, architecture, product, specificity, delivery, safety, and provenance gates pass

Release the prime-editing package only after sequence, architecture, product, specificity, delivery, safety, and provenance gates pass.

- **Routing name:** `release-the-prime-editing-package-only-after-sequence-architecture-product-specificity-delivery-safety-and-provenance-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
