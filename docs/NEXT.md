# Current Handoff

This file captures current project handoff state for humans and agents.

Use it to recover the latest direction in a fresh chat without relying on private conversation history.

Keep this file current, concise, and mutable. Put stable terminology, durable context, and project orientation in `docs/CONTEXT.md`. Put accepted decisions in `docs/adr/`. Put executable work in GitHub Issues and reviewed implementation history in Pull Requests.

## Current State

- The synthetic context-reduction trial pack (PRD #26) is in progress on branch `feature/prd-26`.
- **Docs slice (issue #27)** is the active work item: `README.md`, `docs/CONTEXT.md`, and `docs/NEXT.md` are being filled with durable orientation for the runner trial.
- The **companion code/test slice** is queued as the next slice on `feature/prd-26`. It will add a small code surface and automated tests as the behavioral verification target for the runner trial.
- Both slices are markdown-safe to review independently but are part of the same trial pack and will be merged to `main` together via `feature/prd-26`.

## Most Recent Direction

PRD #26 was approved. It establishes this repository as the host for a synthetic context-reduction trial pack and defines the two-slice structure:

1. **Issue #27 (docs slice)** — reframe repo docs around the trial pack concept so a fresh agent can orient from bounded context alone.
2. **Code/test slice** — add a minimal code surface and automated tests as the behavioral verification layer.

After both slices land on `feature/prd-26`, that branch will be reviewed and merged to `main`, completing the trial pack setup.

## Recommended Next Work

1. Review and merge the docs slice PR (issue #27) into `feature/prd-26`.
2. Implement the companion code/test slice on `feature/prd-26`.
3. Review and merge `feature/prd-26` into `main`.
4. Design and run the runner trial: assign a fresh agent a scoped issue against this repo and verify that it can orient from the trial pack alone.

## Open Questions

- Runner trial scoping: what specific behavior should the runner issue ask the agent to implement or verify against the code/test slice?
- Success criteria: how do we measure whether the agent stayed within the bounded search surface during the runner trial?
- Tooling: does the runner trial need any harness configuration, or is it driven purely through the GitHub issue?

## Do Not Reopen Without Reason

- The trial pack is intentionally small. The code/test slice adds only a minimal surface. Do not expand without a new PRD slice.
- `feature/prd-26` is the integration branch for all PRD #26 slices. Individual slice PRs target this branch, not `main`.
- The AWK install trial seed state (custom templates, labels, skill) is preserved intentionally — it is part of the bounded surface the runner trial may exercise.
