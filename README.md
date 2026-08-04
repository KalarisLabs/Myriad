<div align="center">

# MYRIAD

### 10,000-Node Biotech Agent Skill Graph

**100 biotech domains Â· 1,000 workstreams Â· 10,000 atomic task nodes**

Built by **Srihari Muralikrishnan** with **ChatGPT** for **Kalaris Labs**

[![Version](https://img.shields.io/badge/version-1.0.0-19c6b3)](https://github.com/KalarisLabs/myriad/releases)
[![Nodes](https://img.shields.io/badge/agent%20nodes-10%2C000-19c6b3)](#repository-coverage)
[![Domains](https://img.shields.io/badge/biotech%20domains-100-19c6b3)](#repository-coverage)
[![Node.js](https://img.shields.io/badge/node-%3E%3D18-43853d)](https://nodejs.org/)
[![License](https://img.shields.io/badge/license-UNLICENSED-lightgrey)](#license)

</div>

---

## What is MYRIAD?

MYRIAD is a release-engineered, machine-readable taxonomy of **10,000 atomic biotechnology and pharmaceutical agent tasks** across **100 domains**.

It is designed for:

- agent routing and task discovery;
- retrieval-augmented planning;
- scientific workflow decomposition;
- agent evaluation and benchmarking;
- conversion of validated task nodes into production `SKILL.md` implementations.

> **Scientific status:** MYRIAD contains 10,000 machine-validated taxonomy records and three complete seed `SKILL.md` examples. It does **not** claim that all 10,000 nodes are experimentally, clinically, or regulatorily validated procedures. Operational use requires current primary-source resolution, context-specific validation, and qualified human review.

## Repository coverage

MYRIAD spans the biotechnology lifecycle from foundational research to regulated delivery:

- genomics, pangenomics, variant interpretation, and population genetics;
- transcriptomics, single-cell, spatial, epigenomic, proteomic, and metabolomic analysis;
- structural biology, molecular simulation, and protein engineering;
- target discovery, virtual screening, medicinal chemistry, DMPK, PKâ€“PD, and toxicology;
- CRISPR, gene therapy, RNA therapeutics, antibodies, vaccines, and cell therapies;
- upstream and downstream bioprocessing, PAT, QbD, formulation, and comparability;
- microbial, synthetic, agricultural, and environmental biotechnology;
- clinical trials, real-world evidence, pharmacovigilance, GxP, FAIR data, knowledge graphs, and AI governance.

| Metric | Count |
|---|---:|
| Domains | 100 |
| Batches | 10 |
| Workstreams | 1,000 |
| Atomic task nodes | 10,000 |
| Individual node Markdown files | 10,000 |
| Complete seed skills | 3 |

## Quick start

### Run directly with NPX

```bash
npx kalaris-myriad stats
npx kalaris-myriad list domains
npx kalaris-myriad search "variant-aware off-target" --limit 10
npx kalaris-myriad show MYR-D051-T001
```

### Install globally

```bash
npm install --global kalaris-myriad
kalaris-myriad stats
```

### Use the repository locally

```bash
git clone https://github.com/KalarisLabs/myriad.git
cd myriad
npm install
npm test
node bin/kalaris-myriad.js stats
```

## CLI

```text
kalaris-myriad stats [--json]
kalaris-myriad list domains [--json]
kalaris-myriad list tasks [--domain <1-100>] [--limit <n>] [--json]
kalaris-myriad search <query> [--domain <1-100>] [--limit <n>] [--json]
kalaris-myriad show <task-id-or-routing-name> [--json]
kalaris-myriad export --format <jsonl|json|md> --output <path> [--domain <1-100>]
kalaris-myriad validate [--json]
kalaris-myriad init [directory] [--domain <1-100>]
```

## Examples

Search within one domain:

```bash
npx kalaris-myriad search "residence-time distribution" --domain 78
```

Inspect a node as JSON:

```bash
npx kalaris-myriad show MYR-D078-T001 --json
```

Export a complete domain:

```bash
npx kalaris-myriad export \
  --domain 21 \
  --format md \
  --output protein-structure-prediction.md
```

Validate the installed release:

```bash
npx kalaris-myriad validate
```

## Repository structure

```text
.
â”œâ”€â”€ bin/                         # Dependency-free CLI
â”œâ”€â”€ data/
â”‚   â”œâ”€â”€ raw/                     # Preserved source records
â”‚   â””â”€â”€ canonical/               # Homogenized canonical graph
â”œâ”€â”€ dist/sanitized/              # Public-facing sanitized dataset
â”œâ”€â”€ docs/                        # Architecture, safety and publishing docs
â”œâ”€â”€ marketing/                   # Posters and launch copy
â”œâ”€â”€ myriad/
â”‚   â”œâ”€â”€ batches/                 # Ten standardized batches
â”‚   â””â”€â”€ domains/                 # 100 domains and 10,000 node MD files
â”œâ”€â”€ schemas/                     # JSON Schema contracts
â”œâ”€â”€ scripts/                     # Release validators
â”œâ”€â”€ skills/                      # Three complete seed SKILL.md files
â”œâ”€â”€ tests/                       # Deterministic test suite
â”œâ”€â”€ AUTHORS.md
â”œâ”€â”€ CITATION.cff
â”œâ”€â”€ CREDITS.md
â”œâ”€â”€ LICENSE.md
â”œâ”€â”€ NOTICE.md
â”œâ”€â”€ SECURITY.md
â””â”€â”€ package.json
```

## Data layers

MYRIAD intentionally preserves three representations:

1. **Raw** â€” the original 10,000 task records.
2. **Canonical** â€” a homogeneous schema adding routing, provenance, uncertainty, evidence, safety, and review contracts.
3. **Sanitized** â€” a public distribution without internal build history or legacy release artifacts.

No scientific detail is silently invented to make earlier records look more complete. The canonical layer preserves source meaning while making operational boundaries consistent.

## Agent-skill maturity

Each task node has one of two practical maturity levels:

- **Taxonomy-defined:** a bounded task with routing metadata, objective, execution boundary, provenance expectations, completion evidence, and `no-call` behavior.
- **Implemented skill:** a task with a complete production `SKILL.md`, schemas, procedural logic, tool contracts, validation, and examples.

The repository currently includes three complete seed skills:

- diploid PacBio HiFi assembly optimization;
- variant-aware CRISPR off-target scoring;
- HTS normalization, plate QC, and hit calling.

Phase 3 will progressively convert additional taxonomy nodes into complete skills.

## Safety and limitations

MYRIAD is computational-advisory infrastructure. It must not autonomously:

- execute wet-lab procedures;
- operate or alter bioreactor control systems;
- prescribe treatment or determine patient care;
- release clinical or diagnostic results;
- disposition GMP lots;
- make final regulatory-compliance determinations;
- bypass institutional biosafety, biosecurity, ethics, or authorization controls.

A task node is not a substitute for validated procedures, current primary literature, approved protocols, local SOPs, or qualified professional judgment.

See [`docs/SAFETY_AND_LIMITATIONS.md`](docs/SAFETY_AND_LIMITATIONS.md).

## Validation

The v1.0.0 release was checked for:

- exact 100-domain and 10,000-node counts;
- unique IDs, routing names, titles, and objectives;
- valid JSONL and Markdown frontmatter;
- exact per-domain and per-workstream structure;
- placeholder and near-duplicate detection;
- schema compliance;
- deterministic CLI behavior;
- npm tarball installation;
- ZIP and checksum integrity.

Run validation locally:

```bash
npm test
npm run validate
npm run pack:check
```

## Contributing

Contributions are welcome in the form of:

- task-specific `SKILL.md` implementations;
- stronger primary-source mappings;
- reproducible validators and evaluation fixtures;
- corrections to scientific scope or terminology;
- improvements to agent routing and progressive disclosure.

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

Do not submit operational wet-lab instructions, unsupported clinical recommendations, proprietary data, credentials, or regulated information you are not authorized to share.

## Citation

Citation metadata is provided in [`CITATION.cff`](CITATION.cff).

Suggested acknowledgement:

> Srihari Muralikrishnan and Kalaris Labs, *MYRIAD: 10,000-Node Biotech Agent Skill Graph*, version 1.0.0, 2026. AI systems architecture and release engineering supported by ChatGPT, OpenAI.

## Credits

- **Srihari Muralikrishnan** â€” creator, project lead, systems architect, and co-founder of Kalaris Labs.
- **ChatGPT â€” GPT-5.6 Thinking by OpenAI** â€” AI systems architecture, synthesis, normalization, validation tooling, documentation, and release engineering.
- **Kalaris Labs** â€” project home, organizational direction, and release stewardship.

See [`CREDITS.md`](CREDITS.md) and [`AUTHORS.md`](AUTHORS.md).

## Security

Please report security, biosecurity, privacy, or integrity concerns according to [`SECURITY.md`](SECURITY.md). Do not disclose sensitive vulnerabilities or controlled biological information in public issues.

## License

This v1.0.0 release is currently marked **UNLICENSED**. No permission to use, copy, modify, publish, or redistribute the repository is granted except through a separate written license from Kalaris Labs.

Choose and apply an explicit open-source or source-available license before inviting unrestricted public reuse.

---

<div align="center">

**MYRIAD â€” structured biotech work for agentic systems**

Kalaris Labs Â· Srihari Muralikrishnan Â· ChatGPT

</div>
