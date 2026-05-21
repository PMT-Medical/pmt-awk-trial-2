# Current Handoff

This file captures current project handoff state for humans and agents.

Use it to recover the latest direction in a fresh chat without relying on private conversation history.

Keep this file current, concise, and mutable. Put stable terminology, durable context, and project orientation in `docs/CONTEXT.md`. Put accepted decisions in `docs/adr/`. Put executable work in GitHub Issues and reviewed implementation history in Pull Requests.

## Current State

- This repository has been reframed as the synthetic target for the next live local `awk-runner` smoke test.
- Durable orientation now lives in `README.md` and `docs/CONTEXT.md` and points at the local-runner path rather than the older install-trial framing.
- The active feature branch for the parent PRD is `feature/prd-21`, and slice work should branch from that base rather than from `main`.
- Historical Copilot-related files may still exist in `.github/`, but they are not the active validation path for this trial.

## Most Recent Direction

The current direction is to use this repo as the safe live target for the first local `awk-runner` smoke test aligned with AWK ADR 0011 and ADR 0012. Slice issue #22 updates the durable docs so a fresh operator understands that goal immediately and does not fall back to the retired Copilot-centric interpretation.

## Recommended Next Work

1. Use slice issue #23 to add the repo-local live runner trial runbook needed for the operator-facing smoke test.
2. Run the local `awk-runner` smoke test for PRD #21 against `feature/prd-21` once the runbook and remaining prerequisites are in place.
3. Capture trial evidence and any operator-facing gaps in durable docs or follow-up issues rather than in chat-only notes.

## Open Questions

- What exact minimal operator steps belong in the repo-local runbook for slice #23, and what should stay in upstream runner docs instead?
- Which parts of the first live smoke test need durable evidence in this repo versus in the upstream AWK repository?

## Do Not Reopen Without Reason

- The active execution path for this trial is the local runner, not Copilot automation.
- Slice pull requests for PRD #21 should target `feature/prd-21`, consistent with AWK ADR 0012.
- This repository is a synthetic target for workflow validation, not the implementation home for `awk-runner`.
