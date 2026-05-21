# pmt-awk-trial-2

This repository hosts the **synthetic context-reduction trial pack** built under [PRD #26](../../issues/26).

## What Is the Trial Pack?

The trial pack is a minimal, self-contained set of repository artifacts — durable docs, a small code surface, and automated tests — designed so that agents can orient from bounded context rather than long chat history.

The intended use is a **follow-up runner trial**: a fresh agent is handed this repository and a scoped issue, and must complete the work using only `AGENTS.md`, `docs/CONTEXT.md`, `docs/NEXT.md`, and the GitHub issue. Success is measured by whether the agent stays within the bounded search surface and produces a correct, reviewable pull request.

The trial pack ships as two companion slices on `feature/prd-26`:

| Slice | Description |
|-------|-------------|
| Docs slice (issue #27) | `README.md`, `docs/CONTEXT.md`, `docs/NEXT.md` — the durable orientation layer |
| Code/test slice | A minimal code surface and automated tests — the behavioral verification layer |

See `docs/CONTEXT.md` for stable terminology and `docs/NEXT.md` for the current handoff state.

## Repository History

This repository originally served as a target for the second Agent Workflow Kit (AWK) install trial. That trial exercised overlap scenarios not covered by the first trial (`PMT-Medical/pmt-api-cmd`):

- **Issue template merge/preserve behavior** — existing `.github/ISSUE_TEMPLATE/` files with custom fields
- **Labels overlap handling** — a `github/labels.yml` with custom labels; the install should propose additions only and never delete existing labels
- **Skill overlap detection** — a locally installed `skills/grill-with-docs/SKILL.md` that overlaps with the AWK-namespaced `awk-grill-with-docs` skill

The AWK install trial artifacts remain in the repository. The context-reduction trial pack builds on top of that seed state without removing it.

## Navigation

| Artifact | Purpose |
|----------|---------|
| `AGENTS.md` | Coding-agent operating instructions (source of truth) |
| `docs/CONTEXT.md` | Durable project orientation and domain language |
| `docs/NEXT.md` | Mutable handoff state: current direction, next work, open questions |
| `docs/adr/` | Architecture decision records |
