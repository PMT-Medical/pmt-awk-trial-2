# Current Handoff

This file captures current project handoff state for humans and agents.

Use it to recover the latest direction in a fresh chat without relying on private conversation history.

Keep this file current, concise, and mutable. Put stable terminology, durable context, and project orientation in `docs/CONTEXT.md`. Put accepted decisions in `docs/adr/`. Put executable work in GitHub Issues and reviewed implementation history in Pull Requests.

## Current State

- PRD #10 (`math_utils` module) is in progress. Slice #11 (`add`) is implemented and under review in PR #13.
- `pyproject.toml` added with `pythonpath = ["."]` so `pytest -q` works on a clean checkout.
- Slice #12 (`multiply`) is not yet started.

## Most Recent Direction

Implementing PRD #10 as vertical slices targeting `feature/prd-10`. Each slice PR targets that branch; `feature/prd-10` merges to `main` after all slices land.

## Recommended Next Work

1. Merge PR #13 (slice #11 — `add`), then **manually close issue #11** (GitHub will not auto-close it because the PR targets `feature/prd-10`, not `main`).
2. Implement slice #12 (`multiply` in `math_utils.py`) — branch from `feature/prd-10`, target `feature/prd-10`.
3. After all slices land, open `feature/prd-10` → `main` PR to complete PRD #10.

## Open Questions

<!-- Keep unresolved questions visible until they are answered, moved to issues, or explicitly deferred. -->
<!-- - Open question -->

## Do Not Reopen Without Reason

- All PRD #10 slice PRs target `feature/prd-10`, not `main`. This is intentional — slices integrate there before a single feature PR lands on `main`.
- Issue auto-close via "Closes #N" only works when the PR merges to the default branch (`main`). Slice PRs must close their issues manually.
