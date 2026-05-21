# Current Handoff

This file captures current project handoff state for humans and agents.

Use it to recover the latest direction in a fresh chat without relying on private conversation history.

Keep this file current, concise, and mutable. Put stable terminology, durable context, and project orientation in `docs/CONTEXT.md`. Put accepted decisions in `docs/adr/`. Put executable work in GitHub Issues and reviewed implementation history in Pull Requests.

## Current State

- This repository is the synthetic target for the next live local `awk-runner` smoke test.
- The parent PRD for the trial is `#21`, and slice pull requests for that PRD target `feature/prd-21`.
- The repo-local operator runbook now lives in `docs/live-awk-runner-smoke-test.md`.

## Most Recent Direction

The current direction is to keep this repository usable as the safe live target for the first local `awk-runner` smoke test aligned with upstream ADR 0012. Slice `#23` adds the repo-local runbook so a fresh operator can prepare the run without extra chat context.

## Recommended Next Work

1. Run the local `awk-runner` smoke test for PRD `#21` against `feature/prd-21` using `docs/live-awk-runner-smoke-test.md`.
2. Capture the resulting GitHub evidence and any operator-facing gaps in durable docs or follow-up issues.

## Open Questions

- Which parts of the first live smoke test should be recorded in this repo versus upstream AWK docs?

## Do Not Reopen Without Reason

- The active execution path for this trial is the local runner, not historical Copilot automation.
- Slice pull requests for PRD `#21` target `feature/prd-21`, not `main`.
- This repository is a synthetic workflow-validation target, not the implementation home for `awk-runner`.
