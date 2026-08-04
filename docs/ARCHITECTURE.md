# Architecture

MYRIAD uses progressive disclosure so an agent can load only the information needed for the current decision.

1. **Global routing index** — fast search over 10,000 nodes.
2. **Batch layer** — ten coherent groups of ten domains.
3. **Domain layer** — 100 tasks organized into ten workstreams.
4. **Node layer** — one Markdown and one structured record per task.
5. **Skill layer** — task-specific `SKILL.md` implementations; three seed examples are included.

The taxonomy layer identifies work. The skill layer defines how an agent performs and verifies that work. Conflating the two would overstate readiness, so they remain explicitly separate.
