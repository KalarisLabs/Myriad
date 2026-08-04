# D067 — Immunoinformatics and Epitope Prediction

Batch **007** · 10 workstreams · 100 tasks

## 01. Question definition and reference control

### MYR-D067-T001 — Define whether the task concerns antigen processing, MHC presentation, T-cell recognition, antibody binding, population coverage, or immune safety

Define whether the task concerns antigen processing, MHC presentation, T-cell recognition, antibody binding, population coverage, or immune safety.

- **Routing name:** `define-whether-the-task-concerns-antigen-processing-mhc-presentation-t-cell-recognition-antibody-binding-population-coverage-or-immune-safety`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T002 — Normalize antigen sequence, isoform, strain, mutation set, processing state, and coordinate system into one versioned reference

Normalize antigen sequence, isoform, strain, mutation set, processing state, and coordinate system into one versioned reference.

- **Routing name:** `normalize-antigen-sequence-isoform-strain-mutation-set-processing-state-and-coordinate-system-into-one-versioned-reference`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T003 — Validate HLA nomenclature, resolution, expression status, and allele availability against current authoritative references

Validate HLA nomenclature, resolution, expression status, and allele availability against current authoritative references.

- **Routing name:** `validate-hla-nomenclature-resolution-expression-status-and-allele-availability-against-current-authoritative-references`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T004 — Distinguish class I, class II, nonclassical HLA, murine MHC, and other species contexts before selecting prediction models

Distinguish class I, class II, nonclassical HLA, murine MHC, and other species contexts before selecting prediction models.

- **Routing name:** `distinguish-class-i-class-ii-nonclassical-hla-murine-mhc-and-other-species-contexts-before-selecting-prediction-models`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T005 — Capture sample, disease, vaccination, infection, tissue, and assay context for every imported immune observation

Capture sample, disease, vaccination, infection, tissue, and assay context for every imported immune observation.

- **Routing name:** `capture-sample-disease-vaccination-infection-tissue-and-assay-context-for-every-imported-immune-observation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T006 — Define intended endpoint and acceptable false-positive, false-negative, and population-exclusion risks before ranking peptides

Define intended endpoint and acceptable false-positive, false-negative, and population-exclusion risks before ranking peptides.

- **Routing name:** `define-intended-endpoint-and-acceptable-false-positive-false-negative-and-population-exclusion-risks-before-ranking-peptides`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T007 — Identify sequence ambiguity, unresolved variants, post-translational modifications, splicing, and noncanonical translation sources

Identify sequence ambiguity, unresolved variants, post-translational modifications, splicing, and noncanonical translation sources.

- **Routing name:** `identify-sequence-ambiguity-unresolved-variants-post-translational-modifications-splicing-and-noncanonical-translation-sources`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T008 — Create a versioned source manifest for antigen sequences, HLA frequencies, structures, assays, models, and databases

Create a versioned source manifest for antigen sequences, HLA frequencies, structures, assays, models, and databases.

- **Routing name:** `create-a-versioned-source-manifest-for-antigen-sequences-hla-frequencies-structures-assays-models-and-databases`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T009 — Label model training overlap, database reuse, and publication-derived evidence to prevent circular validation

Label model training overlap, database reuse, and publication-derived evidence to prevent circular validation.

- **Routing name:** `label-model-training-overlap-database-reuse-and-publication-derived-evidence-to-prevent-circular-validation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T010 — Issue a no-call when antigen identity, HLA context, endpoint, coordinate mapping, or model applicability remains unresolved

Issue a no-call when antigen identity, HLA context, endpoint, coordinate mapping, or model applicability remains unresolved.

- **Routing name:** `issue-a-no-call-when-antigen-identity-hla-context-endpoint-coordinate-mapping-or-model-applicability-remains-unresolved`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 02. MHC class I presentation prediction

### MYR-D067-T011 — Enumerate proteasome-generated candidate peptides with explicit length, flanking sequence, mutation, and source-protein provenance

Enumerate proteasome-generated candidate peptides with explicit length, flanking sequence, mutation, and source-protein provenance.

- **Routing name:** `enumerate-proteasome-generated-candidate-peptides-with-explicit-length-flanking-sequence-mutation-and-source-protein-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T012 — Predict TAP transport, cytosolic trimming, MHC class I binding, and presentation as separable biological stages

Predict TAP transport, cytosolic trimming, MHC class I binding, and presentation as separable biological stages.

- **Routing name:** `predict-tap-transport-cytosolic-trimming-mhc-class-i-binding-and-presentation-as-separable-biological-stages`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T013 — Run allele-specific class I models only for supported HLA alleles and label extrapolation to sparse alleles

Run allele-specific class I models only for supported HLA alleles and label extrapolation to sparse alleles.

- **Routing name:** `run-allele-specific-class-i-models-only-for-supported-hla-alleles-and-label-extrapolation-to-sparse-alleles`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T014 — Compare binding-affinity and percentile-rank outputs without treating thresholds as universally transferable across alleles

Compare binding-affinity and percentile-rank outputs without treating thresholds as universally transferable across alleles.

- **Routing name:** `compare-binding-affinity-and-percentile-rank-outputs-without-treating-thresholds-as-universally-transferable-across-alleles`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T015 — Account for peptide length preferences, anchor positions, source abundance, degradation, and subcellular localization where models support them

Account for peptide length preferences, anchor positions, source abundance, degradation, and subcellular localization where models support them.

- **Routing name:** `account-for-peptide-length-preferences-anchor-positions-source-abundance-degradation-and-subcellular-localization-where-models-support-them`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T016 — Prioritize mutation-containing peptides while checking whether the variant is retained after processing and presented register selection

Prioritize mutation-containing peptides while checking whether the variant is retained after processing and presented register selection.

- **Routing name:** `prioritize-mutation-containing-peptides-while-checking-whether-the-variant-is-retained-after-processing-and-presented-register-selection`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T017 — Detect peptides shared with human proteins, microbiota, common pathogens, or related antigens for cross-reactivity review

Detect peptides shared with human proteins, microbiota, common pathogens, or related antigens for cross-reactivity review.

- **Routing name:** `detect-peptides-shared-with-human-proteins-microbiota-common-pathogens-or-related-antigens-for-cross-reactivity-review`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T018 — Estimate presentation uncertainty using model ensembles, replicate predictions, and calibration data rather than one score

Estimate presentation uncertainty using model ensembles, replicate predictions, and calibration data rather than one score.

- **Routing name:** `estimate-presentation-uncertainty-using-model-ensembles-replicate-predictions-and-calibration-data-rather-than-one-score`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T019 — Validate predicted binders against independent immunopeptidomics or binding evidence while preserving assay detection limits

Validate predicted binders against independent immunopeptidomics or binding evidence while preserving assay detection limits.

- **Routing name:** `validate-predicted-binders-against-independent-immunopeptidomics-or-binding-evidence-while-preserving-assay-detection-limits`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T020 — Release class I candidates with allele, peptide, source coordinates, processing evidence, model version, calibration, and no-call flags

Release class I candidates with allele, peptide, source coordinates, processing evidence, model version, calibration, and no-call flags.

- **Routing name:** `release-class-i-candidates-with-allele-peptide-source-coordinates-processing-evidence-model-version-calibration-and-no-call-flags`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 03. MHC class II presentation prediction

### MYR-D067-T021 — Enumerate overlapping class II peptides while preserving peptide flanks, source coordinates, mutations, and nested registers

Enumerate overlapping class II peptides while preserving peptide flanks, source coordinates, mutations, and nested registers.

- **Routing name:** `enumerate-overlapping-class-ii-peptides-while-preserving-peptide-flanks-source-coordinates-mutations-and-nested-registers`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T022 — Predict HLA-DR, HLA-DQ, and HLA-DP binding using locus- and allele-appropriate models with explicit coverage gaps

Predict HLA-DR, HLA-DQ, and HLA-DP binding using locus- and allele-appropriate models with explicit coverage gaps.

- **Routing name:** `predict-hla-dr-hla-dq-and-hla-dp-binding-using-locus-and-allele-appropriate-models-with-explicit-coverage-gaps`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T023 — Identify binding cores within longer peptides rather than interpreting each peptide length as an independent epitope

Identify binding cores within longer peptides rather than interpreting each peptide length as an independent epitope.

- **Routing name:** `identify-binding-cores-within-longer-peptides-rather-than-interpreting-each-peptide-length-as-an-independent-epitope`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T024 — Account for endosomal processing, antigen uptake, protein abundance, and HLA-DM editing where evidence or models permit

Account for endosomal processing, antigen uptake, protein abundance, and HLA-DM editing where evidence or models permit.

- **Routing name:** `account-for-endosomal-processing-antigen-uptake-protein-abundance-and-hla-dm-editing-where-evidence-or-models-permit`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T025 — Compare percentile ranks across alleles cautiously and document model-specific calibration or unsupported equivalence

Compare percentile ranks across alleles cautiously and document model-specific calibration or unsupported equivalence.

- **Routing name:** `compare-percentile-ranks-across-alleles-cautiously-and-document-model-specific-calibration-or-unsupported-equivalence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T026 — Collapse nested peptides into evidence-linked core families without losing alternative registers or flanking effects

Collapse nested peptides into evidence-linked core families without losing alternative registers or flanking effects.

- **Routing name:** `collapse-nested-peptides-into-evidence-linked-core-families-without-losing-alternative-registers-or-flanking-effects`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T027 — Assess promiscuous binding across common alleles while preventing allele count from substituting for population weighting

Assess promiscuous binding across common alleles while preventing allele count from substituting for population weighting.

- **Routing name:** `assess-promiscuous-binding-across-common-alleles-while-preventing-allele-count-from-substituting-for-population-weighting`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T028 — Detect human-homologous and microbiome-shared cores requiring tolerance or cross-reactivity review

Detect human-homologous and microbiome-shared cores requiring tolerance or cross-reactivity review.

- **Routing name:** `detect-human-homologous-and-microbiome-shared-cores-requiring-tolerance-or-cross-reactivity-review`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T029 — Validate predicted class II candidates against binding, elution, proliferation, cytokine, or tetramer evidence with assay boundaries

Validate predicted class II candidates against binding, elution, proliferation, cytokine, or tetramer evidence with assay boundaries.

- **Routing name:** `validate-predicted-class-ii-candidates-against-binding-elution-proliferation-cytokine-or-tetramer-evidence-with-assay-boundaries`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T030 — Release class II candidates with locus, allele, core, peptide context, model version, uncertainty, and supporting evidence

Release class II candidates with locus, allele, core, peptide context, model version, uncertainty, and supporting evidence.

- **Routing name:** `release-class-ii-candidates-with-locus-allele-core-peptide-context-model-version-uncertainty-and-supporting-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 04. T-cell recognition and immunogenicity evidence

### MYR-D067-T031 — Distinguish MHC binding, surface presentation, T-cell receptor recognition, precursor frequency, expansion, and functional response

Distinguish MHC binding, surface presentation, T-cell receptor recognition, precursor frequency, expansion, and functional response.

- **Routing name:** `distinguish-mhc-binding-surface-presentation-t-cell-receptor-recognition-precursor-frequency-expansion-and-functional-response`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T032 — Integrate tetramer, ELISpot, intracellular cytokine, activation-induced marker, cytotoxicity, proliferation, and repertoire evidence without merging endpoints

Integrate tetramer, ELISpot, intracellular cytokine, activation-induced marker, cytotoxicity, proliferation, and repertoire evidence without merging endpoints.

- **Routing name:** `integrate-tetramer-elispot-intracellular-cytokine-activation-induced-marker-cytotoxicity-proliferation-and-repertoire-evidence-without-merging-endpoints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T033 — Normalize responder definitions, background subtraction, replicate rules, stimulation conditions, and assay limits before comparing studies

Normalize responder definitions, background subtraction, replicate rules, stimulation conditions, and assay limits before comparing studies.

- **Routing name:** `normalize-responder-definitions-background-subtraction-replicate-rules-stimulation-conditions-and-assay-limits-before-comparing-studies`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T034 — Assess whether observed responses are naive, memory, cross-reactive, infection-induced, vaccine-induced, therapeutic, or tolerized

Assess whether observed responses are naive, memory, cross-reactive, infection-induced, vaccine-induced, therapeutic, or tolerized.

- **Routing name:** `assess-whether-observed-responses-are-naive-memory-cross-reactive-infection-induced-vaccine-induced-therapeutic-or-tolerized`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T035 — Map T-cell receptor sequences to peptide–HLA specificity only when chain pairing, assay specificity, and provenance are adequate

Map T-cell receptor sequences to peptide–HLA specificity only when chain pairing, assay specificity, and provenance are adequate.

- **Routing name:** `map-t-cell-receptor-sequences-to-peptidehla-specificity-only-when-chain-pairing-assay-specificity-and-provenance-are-adequate`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T036 — Compare immunogenic and nonimmunogenic presented peptides to identify calibrated recognition features without leakage

Compare immunogenic and nonimmunogenic presented peptides to identify calibrated recognition features without leakage.

- **Routing name:** `compare-immunogenic-and-nonimmunogenic-presented-peptides-to-identify-calibrated-recognition-features-without-leakage`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T037 — Assess functional avidity, polyfunctionality, phenotype, clonality, persistence, and exhaustion separately from response magnitude

Assess functional avidity, polyfunctionality, phenotype, clonality, persistence, and exhaustion separately from response magnitude.

- **Routing name:** `assess-functional-avidity-polyfunctionality-phenotype-clonality-persistence-and-exhaustion-separately-from-response-magnitude`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T038 — Flag cytokine-only responses unsupported by peptide specificity, viability, cell-count, and negative-control evidence

Flag cytokine-only responses unsupported by peptide specificity, viability, cell-count, and negative-control evidence.

- **Routing name:** `flag-cytokine-only-responses-unsupported-by-peptide-specificity-viability-cell-count-and-negative-control-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T039 — Grade evidence by directness, assay validation, HLA restriction, independent replication, and biological context

Grade evidence by directness, assay validation, HLA restriction, independent replication, and biological context.

- **Routing name:** `grade-evidence-by-directness-assay-validation-hla-restriction-independent-replication-and-biological-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T040 — Prevent predicted presentation or one donor response from being represented as broadly immunogenic in humans

Prevent predicted presentation or one donor response from being represented as broadly immunogenic in humans.

- **Routing name:** `prevent-predicted-presentation-or-one-donor-response-from-being-represented-as-broadly-immunogenic-in-humans`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 05. B-cell epitope and antibody-accessibility analysis

### MYR-D067-T041 — Reconcile antigen sequence with native structure, oligomer, glycans, membrane orientation, conformational state, and dynamics

Reconcile antigen sequence with native structure, oligomer, glycans, membrane orientation, conformational state, and dynamics.

- **Routing name:** `reconcile-antigen-sequence-with-native-structure-oligomer-glycans-membrane-orientation-conformational-state-and-dynamics`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T042 — Map linear peptide, mutagenesis, competition, escape, cross-linking, hydrogen-exchange, and structural epitope evidence separately

Map linear peptide, mutagenesis, competition, escape, cross-linking, hydrogen-exchange, and structural epitope evidence separately.

- **Routing name:** `map-linear-peptide-mutagenesis-competition-escape-cross-linking-hydrogen-exchange-and-structural-epitope-evidence-separately`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T043 — Distinguish surface accessibility from antibody binding, neutralization, protection, immunodominance, and vaccine suitability

Distinguish surface accessibility from antibody binding, neutralization, protection, immunodominance, and vaccine suitability.

- **Routing name:** `distinguish-surface-accessibility-from-antibody-binding-neutralization-protection-immunodominance-and-vaccine-suitability`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T044 — Assess conformational and discontinuous epitopes using local structural confidence and biologically relevant antigen states

Assess conformational and discontinuous epitopes using local structural confidence and biologically relevant antigen states.

- **Routing name:** `assess-conformational-and-discontinuous-epitopes-using-local-structural-confidence-and-biologically-relevant-antigen-states`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T045 — Identify glycan shielding, quaternary interfaces, transient exposure, cleavage, and conformational masking that alter accessibility

Identify glycan shielding, quaternary interfaces, transient exposure, cleavage, and conformational masking that alter accessibility.

- **Routing name:** `identify-glycan-shielding-quaternary-interfaces-transient-exposure-cleavage-and-conformational-masking-that-alter-accessibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T046 — Map known antibody contacts and escape substitutions while controlling for antigen folding, expression, and fitness effects

Map known antibody contacts and escape substitutions while controlling for antigen folding, expression, and fitness effects.

- **Routing name:** `map-known-antibody-contacts-and-escape-substitutions-while-controlling-for-antigen-folding-expression-and-fitness-effects`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T047 — Compare conserved functional surfaces against variable decoy regions and nonneutralizing immunodominant sites

Compare conserved functional surfaces against variable decoy regions and nonneutralizing immunodominant sites.

- **Routing name:** `compare-conserved-functional-surfaces-against-variable-decoy-regions-and-nonneutralizing-immunodominant-sites`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T048 — Evaluate peptide-based epitope predictions only within their inability to represent native conformational surfaces

Evaluate peptide-based epitope predictions only within their inability to represent native conformational surfaces.

- **Routing name:** `evaluate-peptide-based-epitope-predictions-only-within-their-inability-to-represent-native-conformational-surfaces`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T049 — Grade B-cell epitope evidence by structural resolution, functional relevance, reproducibility, and antigen-context fidelity

Grade B-cell epitope evidence by structural resolution, functional relevance, reproducibility, and antigen-context fidelity.

- **Routing name:** `grade-b-cell-epitope-evidence-by-structural-resolution-functional-relevance-reproducibility-and-antigen-context-fidelity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T050 — Release epitope maps with direct evidence, model inference, accessibility uncertainty, and unsupported protective claims clearly separated

Release epitope maps with direct evidence, model inference, accessibility uncertainty, and unsupported protective claims clearly separated.

- **Routing name:** `release-epitope-maps-with-direct-evidence-model-inference-accessibility-uncertainty-and-unsupported-protective-claims-clearly-separated`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 06. Population coverage and HLA representation

### MYR-D067-T051 — Curate HLA allele-frequency data with population label, geography, sample size, genotyping resolution, and collection date

Curate HLA allele-frequency data with population label, geography, sample size, genotyping resolution, and collection date.

- **Routing name:** `curate-hla-allele-frequency-data-with-population-label-geography-sample-size-genotyping-resolution-and-collection-date`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T052 — Harmonize allele names and frequency denominators before combining studies or estimating coverage

Harmonize allele names and frequency denominators before combining studies or estimating coverage.

- **Routing name:** `harmonize-allele-names-and-frequency-denominators-before-combining-studies-or-estimating-coverage`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T053 — Calculate genotype or phenotype coverage using appropriate linkage and Hardy–Weinberg assumptions with sensitivity analyses

Calculate genotype or phenotype coverage using appropriate linkage and Hardy–Weinberg assumptions with sensitivity analyses.

- **Routing name:** `calculate-genotype-or-phenotype-coverage-using-appropriate-linkage-and-hardyweinberg-assumptions-with-sensitivity-analyses`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T054 — Weight candidate epitopes by allele frequency and binding evidence rather than raw allele count

Weight candidate epitopes by allele frequency and binding evidence rather than raw allele count.

- **Routing name:** `weight-candidate-epitopes-by-allele-frequency-and-binding-evidence-rather-than-raw-allele-count`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T055 — Assess coverage separately across geographic, ancestry, age, disease, and special-population groups where data permit

Assess coverage separately across geographic, ancestry, age, disease, and special-population groups where data permit.

- **Routing name:** `assess-coverage-separately-across-geographic-ancestry-age-disease-and-special-population-groups-where-data-permit`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T056 — Identify populations underrepresented by allele-frequency, epitope-validation, antigen-diversity, or clinical data

Identify populations underrepresented by allele-frequency, epitope-validation, antigen-diversity, or clinical data.

- **Routing name:** `identify-populations-underrepresented-by-allele-frequency-epitope-validation-antigen-diversity-or-clinical-data`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T057 — Compare minimal epitope sets using transparent set-cover objectives, redundancy, and uncertainty constraints

Compare minimal epitope sets using transparent set-cover objectives, redundancy, and uncertainty constraints.

- **Routing name:** `compare-minimal-epitope-sets-using-transparent-set-cover-objectives-redundancy-and-uncertainty-constraints`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T058 — Assess whether linked HLA haplotypes or immunodominance reduce the independence assumed by simple coverage calculations

Assess whether linked HLA haplotypes or immunodominance reduce the independence assumed by simple coverage calculations.

- **Routing name:** `assess-whether-linked-hla-haplotypes-or-immunodominance-reduce-the-independence-assumed-by-simple-coverage-calculations`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T059 — Report ranges under alternate frequency sources, binding thresholds, and model uncertainty rather than one precise percentage

Report ranges under alternate frequency sources, binding thresholds, and model uncertainty rather than one precise percentage.

- **Routing name:** `report-ranges-under-alternate-frequency-sources-binding-thresholds-and-model-uncertainty-rather-than-one-precise-percentage`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T060 — Prevent population coverage estimates from being represented as predicted clinical response rates

Prevent population coverage estimates from being represented as predicted clinical response rates.

- **Routing name:** `prevent-population-coverage-estimates-from-being-represented-as-predicted-clinical-response-rates`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 07. Cross-reactivity and immune-safety analysis

### MYR-D067-T061 — Search candidate peptides against the human proteome while preserving exact sequence, conservative substitution, and register relationships

Search candidate peptides against the human proteome while preserving exact sequence, conservative substitution, and register relationships.

- **Routing name:** `search-candidate-peptides-against-the-human-proteome-while-preserving-exact-sequence-conservative-substitution-and-register-relationships`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T062 — Compare candidate peptide–HLA surfaces with human, microbiome, food, commensal, and pathogen-derived complexes where data support it

Compare candidate peptide–HLA surfaces with human, microbiome, food, commensal, and pathogen-derived complexes where data support it.

- **Routing name:** `compare-candidate-peptidehla-surfaces-with-human-microbiome-food-commensal-and-pathogen-derived-complexes-where-data-support-it`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T063 — Assess T-cell receptor cross-reactivity using position-specific recognition evidence rather than sequence identity alone

Assess T-cell receptor cross-reactivity using position-specific recognition evidence rather than sequence identity alone.

- **Routing name:** `assess-t-cell-receptor-cross-reactivity-using-position-specific-recognition-evidence-rather-than-sequence-identity-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T064 — Flag candidates overlapping essential, tissue-restricted, developmental, cardiac, neural, reproductive, or immune-regulatory proteins

Flag candidates overlapping essential, tissue-restricted, developmental, cardiac, neural, reproductive, or immune-regulatory proteins.

- **Routing name:** `flag-candidates-overlapping-essential-tissue-restricted-developmental-cardiac-neural-reproductive-or-immune-regulatory-proteins`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T065 — Evaluate potential molecular mimicry with explicit evidence grades and avoid inferring autoimmunity from homology alone

Evaluate potential molecular mimicry with explicit evidence grades and avoid inferring autoimmunity from homology alone.

- **Routing name:** `evaluate-potential-molecular-mimicry-with-explicit-evidence-grades-and-avoid-inferring-autoimmunity-from-homology-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T066 — Screen antibody epitopes for human-protein similarity, glycan mimicry, superantigen-like interactions, and polyreactive surfaces

Screen antibody epitopes for human-protein similarity, glycan mimicry, superantigen-like interactions, and polyreactive surfaces.

- **Routing name:** `screen-antibody-epitopes-for-human-protein-similarity-glycan-mimicry-superantigen-like-interactions-and-polyreactive-surfaces`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T067 — Assess cytokine-release risk only with receptor, cell-context, potency, and empirical evidence rather than peptide scores

Assess cytokine-release risk only with receptor, cell-context, potency, and empirical evidence rather than peptide scores.

- **Routing name:** `assess-cytokine-release-risk-only-with-receptor-cell-context-potency-and-empirical-evidence-rather-than-peptide-scores`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T068 — Identify junctional, linker, tag, vector, and engineered sequence epitopes introduced by therapeutic constructs

Identify junctional, linker, tag, vector, and engineered sequence epitopes introduced by therapeutic constructs.

- **Routing name:** `identify-junctional-linker-tag-vector-and-engineered-sequence-epitopes-introduced-by-therapeutic-constructs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T069 — Generate a cross-reactivity risk register with matched human sequences, tissues, structural evidence, and confirmation needs

Generate a cross-reactivity risk register with matched human sequences, tissues, structural evidence, and confirmation needs.

- **Routing name:** `generate-a-cross-reactivity-risk-register-with-matched-human-sequences-tissues-structural-evidence-and-confirmation-needs`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T070 — Escalate plausible high-consequence cross-reactivity for qualified review without asserting clinical toxicity

Escalate plausible high-consequence cross-reactivity for qualified review without asserting clinical toxicity.

- **Routing name:** `escalate-plausible-high-consequence-cross-reactivity-for-qualified-review-without-asserting-clinical-toxicity`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 08. Model validation, calibration, and leakage control

### MYR-D067-T071 — Record model architecture, training data date, supported alleles, peptide lengths, endpoint, software version, and license

Record model architecture, training data date, supported alleles, peptide lengths, endpoint, software version, and license.

- **Routing name:** `record-model-architecture-training-data-date-supported-alleles-peptide-lengths-endpoint-software-version-and-license`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T072 — Check whether evaluation peptides, homologs, donors, antigens, or assay datasets overlap model training or tuning data

Check whether evaluation peptides, homologs, donors, antigens, or assay datasets overlap model training or tuning data.

- **Routing name:** `check-whether-evaluation-peptides-homologs-donors-antigens-or-assay-datasets-overlap-model-training-or-tuning-data`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T073 — Use antigen-, protein-, donor-, study-, or time-aware splits to prevent optimistic leakage in benchmark design

Use antigen-, protein-, donor-, study-, or time-aware splits to prevent optimistic leakage in benchmark design.

- **Routing name:** `use-antigen-protein-donor-study-or-time-aware-splits-to-prevent-optimistic-leakage-in-benchmark-design`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T074 — Assess discrimination, calibration, precision–recall, enrichment, and decision-curve behavior rather than AUROC alone

Assess discrimination, calibration, precision–recall, enrichment, and decision-curve behavior rather than AUROC alone.

- **Routing name:** `assess-discrimination-calibration-precisionrecall-enrichment-and-decision-curve-behavior-rather-than-auroc-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T075 — Report performance by allele, peptide length, affinity range, antigen class, assay type, and data density

Report performance by allele, peptide length, affinity range, antigen class, assay type, and data density.

- **Routing name:** `report-performance-by-allele-peptide-length-affinity-range-antigen-class-assay-type-and-data-density`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T076 — Calibrate probabilities or ranks only against independent data representative of the intended operational context

Calibrate probabilities or ranks only against independent data representative of the intended operational context.

- **Routing name:** `calibrate-probabilities-or-ranks-only-against-independent-data-representative-of-the-intended-operational-context`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T077 — Quantify uncertainty from model disagreement, sparse alleles, out-of-distribution sequences, and assay noise

Quantify uncertainty from model disagreement, sparse alleles, out-of-distribution sequences, and assay noise.

- **Routing name:** `quantify-uncertainty-from-model-disagreement-sparse-alleles-out-of-distribution-sequences-and-assay-noise`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T078 — Compare simple baselines and established models before claiming benefit from a complex or generative method

Compare simple baselines and established models before claiming benefit from a complex or generative method.

- **Routing name:** `compare-simple-baselines-and-established-models-before-claiming-benefit-from-a-complex-or-generative-method`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T079 — Document threshold selection against operational costs and prohibit post hoc threshold tuning on the final test set

Document threshold selection against operational costs and prohibit post hoc threshold tuning on the final test set.

- **Routing name:** `document-threshold-selection-against-operational-costs-and-prohibit-post-hoc-threshold-tuning-on-the-final-test-set`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T080 — Release model claims only with leakage checks, independent evaluation, calibration, versioning, and known failure modes

Release model claims only with leakage checks, independent evaluation, calibration, versioning, and known failure modes.

- **Routing name:** `release-model-claims-only-with-leakage-checks-independent-evaluation-calibration-versioning-and-known-failure-modes`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 09. Experimental evidence and database synthesis

### MYR-D067-T081 — Deduplicate immune records by peptide, HLA, assay, host, study, sample, and experimental condition rather than citation alone

Deduplicate immune records by peptide, HLA, assay, host, study, sample, and experimental condition rather than citation alone.

- **Routing name:** `deduplicate-immune-records-by-peptide-hla-assay-host-study-sample-and-experimental-condition-rather-than-citation-alone`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T082 — Reconcile positive and negative evidence while preserving assay sensitivity, peptide concentration, cell source, and responder criteria

Reconcile positive and negative evidence while preserving assay sensitivity, peptide concentration, cell source, and responder criteria.

- **Routing name:** `reconcile-positive-and-negative-evidence-while-preserving-assay-sensitivity-peptide-concentration-cell-source-and-responder-criteria`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T083 — Map source coordinates across sequence versions, strains, isoforms, and processing states with explicit conversion provenance

Map source coordinates across sequence versions, strains, isoforms, and processing states with explicit conversion provenance.

- **Routing name:** `map-source-coordinates-across-sequence-versions-strains-isoforms-and-processing-states-with-explicit-conversion-provenance`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T084 — Grade database records by direct assay evidence, curation status, HLA restriction, and reproducibility

Grade database records by direct assay evidence, curation status, HLA restriction, and reproducibility.

- **Routing name:** `grade-database-records-by-direct-assay-evidence-curation-status-hla-restriction-and-reproducibility`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T085 — Distinguish naturally presented epitopes from exogenous peptide stimulation and high-concentration binding assays

Distinguish naturally presented epitopes from exogenous peptide stimulation and high-concentration binding assays.

- **Routing name:** `distinguish-naturally-presented-epitopes-from-exogenous-peptide-stimulation-and-high-concentration-binding-assays`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T086 — Integrate immunopeptidomics with false-discovery control, spectral quality, source-protein ambiguity, and HLA assignment uncertainty

Integrate immunopeptidomics with false-discovery control, spectral quality, source-protein ambiguity, and HLA assignment uncertainty.

- **Routing name:** `integrate-immunopeptidomics-with-false-discovery-control-spectral-quality-source-protein-ambiguity-and-hla-assignment-uncertainty`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T087 — Identify publication bias, repeated cohorts, shared controls, and database inheritance that compromise evidence independence

Identify publication bias, repeated cohorts, shared controls, and database inheritance that compromise evidence independence.

- **Routing name:** `identify-publication-bias-repeated-cohorts-shared-controls-and-database-inheritance-that-compromise-evidence-independence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T088 — Preserve conflicting results and generate hypotheses for discordance rather than selecting the favorable observation

Preserve conflicting results and generate hypotheses for discordance rather than selecting the favorable observation.

- **Routing name:** `preserve-conflicting-results-and-generate-hypotheses-for-discordance-rather-than-selecting-the-favorable-observation`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T089 — Create evidence tables linking every candidate to source data, model outputs, assay context, and unresolved contradictions

Create evidence tables linking every candidate to source data, model outputs, assay context, and unresolved contradictions.

- **Routing name:** `create-evidence-tables-linking-every-candidate-to-source-data-model-outputs-assay-context-and-unresolved-contradictions`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T090 — Schedule evidence refreshes when HLA nomenclature, antigen sequences, model versions, or curated databases change

Schedule evidence refreshes when HLA nomenclature, antigen sequences, model versions, or curated databases change.

- **Routing name:** `schedule-evidence-refreshes-when-hla-nomenclature-antigen-sequences-model-versions-or-curated-databases-change`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

## 10. Candidate ranking and reporting

### MYR-D067-T091 — Construct a candidate matrix spanning processing, presentation, recognition, conservation, coverage, safety, and experimental evidence

Construct a candidate matrix spanning processing, presentation, recognition, conservation, coverage, safety, and experimental evidence.

- **Routing name:** `construct-a-candidate-matrix-spanning-processing-presentation-recognition-conservation-coverage-safety-and-experimental-evidence`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T092 — Normalize endpoint direction, calibration, uncertainty, missingness, and evidence directness before multi-attribute ranking

Normalize endpoint direction, calibration, uncertainty, missingness, and evidence directness before multi-attribute ranking.

- **Routing name:** `normalize-endpoint-direction-calibration-uncertainty-missingness-and-evidence-directness-before-multi-attribute-ranking`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T093 — Identify correlated predictors so multiple models trained on similar data do not create false consensus

Identify correlated predictors so multiple models trained on similar data do not create false consensus.

- **Routing name:** `identify-correlated-predictors-so-multiple-models-trained-on-similar-data-do-not-create-false-consensus`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T094 — Perform sensitivity analysis to reveal candidates whose rank depends on one model, threshold, population source, or assumption

Perform sensitivity analysis to reveal candidates whose rank depends on one model, threshold, population source, or assumption.

- **Routing name:** `perform-sensitivity-analysis-to-reveal-candidates-whose-rank-depends-on-one-model-threshold-population-source-or-assumption`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T095 — Select primary and backup epitope sets that preserve antigen, HLA, mechanism, and escape diversity where appropriate

Select primary and backup epitope sets that preserve antigen, HLA, mechanism, and escape diversity where appropriate.

- **Routing name:** `select-primary-and-backup-epitope-sets-that-preserve-antigen-hla-mechanism-and-escape-diversity-where-appropriate`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T096 — Record every filter, threshold, database version, excluded record, conflict resolution, and reviewer override

Record every filter, threshold, database version, excluded record, conflict resolution, and reviewer override.

- **Routing name:** `record-every-filter-threshold-database-version-excluded-record-conflict-resolution-and-reviewer-override`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T097 — Generate an epitope decision card containing coordinates, HLA, evidence, model applicability, safety flags, and next experiments

Generate an epitope decision card containing coordinates, HLA, evidence, model applicability, safety flags, and next experiments.

- **Routing name:** `generate-an-epitope-decision-card-containing-coordinates-hla-evidence-model-applicability-safety-flags-and-next-experiments`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T098 — Issue explicit no-call states for unsupported alleles, out-of-distribution antigens, unresolved coordinates, or insufficient controls

Issue explicit no-call states for unsupported alleles, out-of-distribution antigens, unresolved coordinates, or insufficient controls.

- **Routing name:** `issue-explicit-no-call-states-for-unsupported-alleles-out-of-distribution-antigens-unresolved-coordinates-or-insufficient-controls`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T099 — Keep computational nomination, experimental validation, clinical eligibility, and safety conclusions explicitly separated

Keep computational nomination, experimental validation, clinical eligibility, and safety conclusions explicitly separated.

- **Routing name:** `keep-computational-nomination-experimental-validation-clinical-eligibility-and-safety-conclusions-explicitly-separated`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required

### MYR-D067-T100 — Release the epitope package only after identity, model validity, evidence, coverage, safety, provenance, and review gates pass

Release the epitope package only after identity, model validity, evidence, coverage, safety, provenance, and review gates pass.

- **Routing name:** `release-the-epitope-package-only-after-identity-model-validity-evidence-coverage-safety-provenance-and-review-gates-pass`
- **Status:** `taxonomy-defined`
- **Operational readiness:** `requires-task-specific-skill-and-domain-expert-review`
- **Human review:** required
