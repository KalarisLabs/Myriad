<div align="center">

# MYRIAD

### A 10,000-node biotech agent skill graph

**100 domains / 1,000 workstreams / 10,000 atomic task nodes**

[![npm version](https://img.shields.io/npm/v/kalaris-myriad?label=npm&color=CB3837&cacheSeconds=300&refresh=120)](https://www.npmjs.com/package/kalaris-myriad)
[![npm downloads](https://img.shields.io/npm/dm/kalaris-myriad?label=downloads&color=0B63F6&cacheSeconds=300&refresh=120)](https://www.npmjs.com/package/kalaris-myriad)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D18-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![CI](https://github.com/KalarisLabs/myriad/actions/workflows/ci.yml/badge.svg)](https://github.com/KalarisLabs/myriad/actions/workflows/ci.yml)
[![GitHub](https://img.shields.io/badge/GitHub-KalarisLabs%2Fmyriad-181717?logo=github)](https://github.com/KalarisLabs/myriad)
[![License](https://img.shields.io/badge/license-Apache--2.0%20%2B%20CC%20BY%204.0-2563EB)](#license)

**Built by Srihari Muralikrishnan with ChatGPT for Kalaris Labs**

</div>

---

## Try it in 10 seconds

```bash
npx kalaris-myriad stats
```

```text
MYRIAD 1.2.0
100 domains / 1,000 workstreams / 10,000 tasks / 10 batches
Maturity: taxonomy-defined; full seed skills: 3
```

Search the graph:

```bash
npx kalaris-myriad search "variant-aware off-target" --limit 5
```

Inspect a node:

```bash
npx kalaris-myriad show MYR-D051-T041
```

Export a domain:

```bash
npx kalaris-myriad export \
  --domain 21 \
  --format md \
  --output protein-structure-prediction.md
```

---

## What MYRIAD is

MYRIAD is a release-engineered, machine-readable map of work across biotechnology and pharmaceutical development.

It turns broad fields such as genome assembly, protein engineering, drug discovery, bioprocessing, clinical development, and regulatory science into bounded, searchable agent tasks.

Each task node provides a stable routing surface for:

- agent discovery and delegation;
- retrieval-augmented planning;
- workflow decomposition;
- evaluation and benchmarking;
- conversion into complete production `SKILL.md` implementations.

### What MYRIAD is not

MYRIAD is not a collection of 10,000 experimentally validated wet-lab protocols.

The graph currently contains:

| Maturity level | Count | Meaning |
|---|---:|---|
| Taxonomy-defined nodes | 10,000 | Bounded tasks with routing metadata, objectives, provenance expectations, review boundaries, and completion evidence |
| Implemented seed skills | 3 | Complete procedural `SKILL.md` examples with schemas, tool contracts, validation logic, and examples |

Operational use still requires current primary sources, validated local procedures, appropriate authorization, and qualified human review.

---

## The graph at a glance

```text
100 domains
  x 10 workstreams per domain
  x 10 atomic tasks per workstream
  = 10,000 task nodes
```

| Layer | Count |
|---|---:|
| Biotech and pharmaceutical domains | 100 |
| Standardized batches | 10 |
| Workstreams | 1,000 |
| Atomic task nodes | 10,000 |
| Individual node Markdown files | 10,000 |
| Complete seed `SKILL.md` implementations | 3 |

---

## Coverage

<table>
<tr>
<td width="50%" valign="top">

### Molecular and omics

- Genome assembly and pangenomics
- Germline, somatic, and structural variation
- Population and rare-disease genomics
- Bulk, single-cell, and spatial transcriptomics
- Epigenomics and multi-omics
- Proteomics, PTM analysis, and metabolomics

### Structure and discovery

- Protein structure prediction
- Cryo-EM, crystallography, and NMR
- Molecular dynamics and QM/MM
- Protein and antibody engineering
- Target identification and validation
- Virtual screening, docking, QSAR, and free energy

</td>
<td width="50%" valign="top">

### Therapeutics and development

- Medicinal chemistry, ADME, DMPK, and PK-PD
- Predictive toxicology and biomarkers
- CRISPR, base editing, and prime editing
- Gene therapy, RNA therapeutics, and delivery
- Antibodies, ADCs, degraders, vaccines, and cell therapy

### Manufacturing and translation

- Cell-line and upstream process development
- Bioreactor control, PAT, QbD, and purification
- Formulation, stability, and comparability
- Microbial, synthetic, agricultural, and environmental biotech
- Clinical trials, RWE, pharmacovigilance, GxP, FAIR data, and AI governance

</td>
</tr>
</table>

---

## Use MYRIAD

### Explore in a browser

**Live explorer:** https://myriad-explorer.vercel.app

The dependency-free explorer reads the canonical graph directly and provides search,
domain/workstream filtering, shareable task URLs, JSON export, task/CLI copy actions,
and links to canonical GitHub nodes.

```bash
npm run explorer
```

Then open <http://localhost:4173/explorer/>. A local server is required so the browser
can load the canonical JSONL data.

### Run without installing

```bash
npx kalaris-myriad <command>
```

### Install globally

```bash
npm install --global kalaris-myriad
kalaris-myriad stats
```

### Clone for local development

```bash
git clone https://github.com/KalarisLabs/myriad.git
cd myriad
npm ci
npm test
npm run validate
```

---

## CLI reference

| Command | Purpose |
|---|---|
| `kalaris-myriad stats [--json]` | Show release counts and maturity |
| `kalaris-myriad list domains [--json]` | List all 100 domains |
| `kalaris-myriad list tasks [--domain N] [--limit N]` | Browse task nodes |
| `kalaris-myriad search <query> [--domain N] [--limit N]` | Search titles, objectives, and routing names |
| `kalaris-myriad show <id-or-name> [--json]` | Inspect one task node |
| `kalaris-myriad export --format <jsonl\|json\|md> --output <path>` | Export all or part of the graph |
| `kalaris-myriad validate [--json]` | Validate the installed release |
| `kalaris-myriad init [directory] [--domain N]` | Initialize a working subset |

<details>
<summary><strong>More command examples</strong></summary>

Search only the bioreactor domain:

```bash
npx kalaris-myriad search "residence-time distribution" --domain 78
```

Return machine-readable output:

```bash
npx kalaris-myriad show MYR-D078-T001 --json
```

Export one domain to JSONL:

```bash
npx kalaris-myriad export \
  --domain 51 \
  --format jsonl \
  --output crispr-guide-design.jsonl
```

Validate a globally installed release:

```bash
kalaris-myriad validate --json
```

</details>

---

## One graph, three representations

MYRIAD preserves three layers deliberately:

| Layer | Purpose |
|---|---|
| `data/raw/` | Original source records from the ten taxonomy batches |
| `data/canonical/` | Homogenized records with consistent routing, provenance, uncertainty, safety, and review contracts |
| `dist/sanitized/` | Public-facing distribution without internal build history or legacy release artifacts |

Earlier nodes were not padded with invented scientific detail merely to make every batch look equally verbose. Source meaning is preserved, while the canonical layer normalizes operational boundaries.

---

## Repository map

```text
.
|-- bin/                 Dependency-free command-line interface
|-- data/
|   |-- raw/             Preserved source records
|   `-- canonical/       Homogenized 10,000-node graph
|-- dist/sanitized/      Public-facing distribution
|-- docs/                Architecture, QA, safety, and release documentation
|-- lib/                 CLI and data-access implementation
|-- myriad/
|   |-- batches/         Ten standardized batches
|   `-- domains/         100 domains and 10,000 node Markdown files
|-- references/          Controlled reference documentation
|-- schemas/             JSON Schema contracts
|-- scripts/             Release and scientific-structure validators
|-- skills/              Complete seed SKILL.md implementations
|-- tests/               Deterministic Node.js tests
|-- CITATION.cff
|-- CREDITS.md
|-- LICENSE.md
|-- NOTICE.md
|-- SECURITY.md
`-- package.json
```

---

## Seed skills

Three nodes have been expanded into complete reference implementations:

1. **Diploid PacBio HiFi assembly optimization**
2. **Variant-aware CRISPR off-target scoring**
3. **HTS normalization, plate QC, and hit calling**

These demonstrate the target shape for Phase 3: strict frontmatter, input schemas, procedural stages, decision gates, provenance, failure handling, outputs, and human-review boundaries.

---

## Design principles

### Precise routing

Task names communicate when a node should activate and what decision artifact it produces.

### Progressive disclosure

Agents can begin with the global index, narrow to a domain or workstream, and load a full node only when needed.

### Evidence before confidence

A score, prediction, or model output is never treated as experimental, clinical, manufacturing, or regulatory proof.

### Fail closed

Nodes support explicit `pass`, `warning`, `fail`, and `no-call` outcomes rather than forcing unsupported conclusions.

### Human authority remains explicit

The graph does not authorize autonomous wet-lab execution, clinical decisions, GMP disposition, regulatory determinations, or safety overrides.

---

## Validation

The release validator checks:

- exactly 100 domains and 10,000 task nodes;
- exactly 100 tasks per domain;
- globally unique IDs, routing names, titles, and objectives;
- valid JSONL and node Markdown frontmatter;
- required execution boundaries and completion evidence;
- placeholder and near-duplicate detection;
- schema compliance;
- deterministic CLI behavior;
- npm package contents.

Run everything locally:

```bash
npm ci
npm test
npm run validate
npm run pack:check
```

See [`docs/QUALITY_ASSURANCE_REPORT.md`](docs/QUALITY_ASSURANCE_REPORT.md) for the readable release summary.

---

## Safety boundary

MYRIAD is computational-advisory infrastructure.

It must not autonomously:

- execute wet-lab procedures;
- operate or alter bioreactor controls;
- prescribe treatment or determine patient care;
- release clinical or diagnostic results;
- disposition GMP lots;
- issue final regulatory-compliance determinations;
- bypass institutional biosafety, biosecurity, ethics, privacy, or authorization controls.

A node is not a substitute for current primary literature, validated protocols, local SOPs, approved lab systems, or qualified professional judgment.

Read [`docs/SAFETY_AND_LIMITATIONS.md`](docs/SAFETY_AND_LIMITATIONS.md).

---

## Build with MYRIAD

Good contributions include:

- implementing a taxonomy node as a complete `SKILL.md`;
- improving source mappings and version resolution;
- adding reproducible evaluation fixtures;
- correcting scientific scope or terminology;
- improving routing, schemas, validators, or documentation.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

Do not submit credentials, proprietary datasets, controlled information, unsupported clinical recommendations, or operational procedures you are not authorized to disclose.

---

## Citation

Citation metadata is available in [`CITATION.cff`](CITATION.cff).

Suggested acknowledgement:

> Srihari Muralikrishnan and Kalaris Labs. MYRIAD: A 10,000-Node Biotech Agent Skill Graph. Version 1.0.2, 2026. AI systems architecture and release engineering supported by ChatGPT, OpenAI.

---

## Credits

- **Srihari Muralikrishnan** - creator, project lead, systems architect, and co-founder of Kalaris Labs.
- **ChatGPT - GPT-5.6 Thinking by OpenAI** - AI systems architecture, synthesis, normalization, validation tooling, documentation, and release engineering.
- **Kalaris Labs** - project home, organizational direction, and release stewardship.

See [`AUTHORS.md`](AUTHORS.md) and [`CREDITS.md`](CREDITS.md).

---

## License

MYRIAD uses a split, attribution-preserving license:

- **Software and executable tooling:** [Apache License 2.0](LICENSE-APACHE-2.0.txt)
- **Task graph, datasets, and documentation:** [CC BY 4.0](LICENSE-CC-BY-4.0.txt)

Public use, modification, redistribution, and commercial use are allowed under
the applicable license. Preserve the required notices and credit:

> MYRIAD by Srihari Muralikrishnan and Kalaris Labs.  
> https://github.com/KalarisLabs/myriad

See [`LICENSE.md`](LICENSE.md) for the file-by-file scope and attribution
requirements.
---

<div align="center">

### Search the graph. Inspect the node. Build the skill.

```bash
npx kalaris-myriad search "your biotech problem"
```

**Kalaris Labs / Srihari Muralikrishnan / ChatGPT**

</div>
