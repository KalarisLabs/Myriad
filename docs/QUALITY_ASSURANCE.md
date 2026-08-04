# Quality assurance

The final release validator checks:

- JSONL parseability and UTF-8 normalization.
- Exactly 100 domains, 100 tasks per domain, 10 workstreams per domain, and 10 tasks per workstream.
- Exact ID, domain-code, slug, and routing-name syntax.
- Global uniqueness of IDs, routing names, titles, and objectives.
- Non-empty goals, objectives, routing descriptions, keywords, and completion contracts.
- Placeholder and unfinished-text scans.
- Explicit human-review, no-call, uncertainty, provenance, and prohibited-action controls.
- Markdown and JSON artifact coverage for every domain and every node.
- Batch manifests, portable validators, checksums, package tests, and CLI behavior.

## What validation does not claim

Automated checks cannot establish that every scientific statement is experimentally correct in every context. The release therefore preserves source text, adds no unsupported task-specific scientific claims, labels maturity honestly, requires primary-source resolution at execution time, and mandates qualified review before operational use.
