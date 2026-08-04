# Data model

## Raw records

`data/raw/all-tasks.raw.jsonl` preserves the source Phase 2 records unchanged.

## Canonical records

`data/canonical/all-tasks.jsonl` adds routing, execution-contract, maturity, and provenance objects while preserving each original title and objective.

## Sanitized records

`dist/sanitized/all-tasks.sanitized.jsonl` is a reduced public-facing form. It removes internal normalization provenance and retains the task, routing, safety, no-call, and maturity fields required for agent use.

## Maturity semantics

- `taxonomy-defined` means the task has a stable identity and scope.
- `requires-task-specific-skill-and-domain-expert-review` means it is not yet an independently validated operational procedure.
- `scientific_validation_claim: none` prevents the release from claiming peer review or empirical validation that has not occurred.
