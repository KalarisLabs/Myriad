# Agent-skill design principles

The release applies four maintainability tactics:

1. Route by when a task is needed, not by a vague category label.
2. Use progressive disclosure so agents load only the relevant batch, domain, node, or skill.
3. Keep durable task structure separate from volatile tools, model versions, databases, standards, and guidance.
4. Require a clear goal, constraints, completion evidence, and no-call conditions while avoiding brittle runtime-specific instructions.

These tactics were informed by a user-provided PostHog article by Ian Vanagas, *What nobody tells you about writing agent skills* (August 3, 2026). The article is credited but not redistributed.
