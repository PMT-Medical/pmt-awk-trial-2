# Project Context

This file is durable context for humans and agents working in this repository.

Keep it concise. Link to deeper docs, ADRs, issues, and code instead of duplicating everything here.

`AGENTS.md` is the source of truth for coding-agent operating instructions such as workflow rules, build commands, test commands, and safety rules. Use this file for durable project context that helps a fresh human or agent understand the repository's domain, vocabulary, relationships, constraints, and stable orientation.

If `AGENTS.md`, README files, ADRs, or runbooks already cover a topic well, link to them instead of copying their content.

Put mutable state — current implementation status, open questions, and recommended next work — in `docs/NEXT.md`, not here.

## Context Scope

orientation-context

## Durable Orientation

`pmt-awk-trial-2` hosts the **synthetic context-reduction trial pack** assembled under PRD #26.

The trial pack is a minimal, self-contained set of repository artifacts designed so that a fresh agent can orient from bounded durable context — `AGENTS.md`, this file, `docs/NEXT.md`, and a scoped GitHub issue — without relying on long chat history. The follow-up experiment (**runner trial**) assigns a fresh agent a scoped implementation issue and measures whether the agent completes it correctly while staying within the bounded search surface.

The trial pack consists of two companion slices:

- **Docs slice (issue #27):** `README.md`, `docs/CONTEXT.md`, and `docs/NEXT.md` — the durable orientation layer.
- **Code/test slice:** a small code surface and automated tests — the behavioral verification target for the runner trial.

Both slices are developed on `feature/prd-26` and reviewed together before the branch is merged to `main`.

This repository also retains its earlier AWK install trial seed state (custom issue templates, labels, and a locally installed skill). That seed state is preserved and is part of the bounded surface the runner trial may exercise. See `README.md` for the full seed inventory.

## Domain Language

| Term | Meaning |
|------|---------|
| Trial pack | The complete set of repo artifacts (docs + code + tests) assembled for a bounded agent trial. |
| Context-reduction trial | A trial that measures whether agents can complete scoped work from durable docs alone, without long chat context. |
| Runner trial | The follow-up experiment: a fresh agent is given a scoped issue and must orient from the trial pack alone. |
| Bounded search surface | The explicit set of files an agent should read. Runner issues list this surface in a "Runner Context" section. |
| Docs slice | The markdown-only portion of the trial pack (issue #27). |
| Code/test slice | The code and test portion of the trial pack; the behavioral verification layer. |

## Relationship Map

The trial pack layers are ordered by reading sequence:

1. `AGENTS.md` — operating rules for any agent in this repo
2. `docs/CONTEXT.md` (this file) — stable orientation, terminology, and constraints
3. `docs/NEXT.md` — mutable handoff state and recommended next work
4. Scoped GitHub issue — the concrete assignment, including "Runner Context" listing which files to read

The code/test slice provides the behavioral target: the runner trial gives the agent an issue that points at the code surface, and the automated tests verify the agent's output.

## Important Constraints

- The trial pack is intentionally small. Do not expand the code or test surface without a new PRD slice.
- Docs must remain consistent with `AGENTS.md`. If `AGENTS.md` changes materially, update this file.
- Runner issues must include a "Runner Context" section so agents know the bounded search surface upfront.
- This repository does not have a build or deploy pipeline. All verification is local (test suite or manual checks).

## Links

- [`AGENTS.md`](../AGENTS.md) — coding-agent operating instructions (source of truth)
- [`docs/NEXT.md`](NEXT.md) — mutable handoff state
- [`docs/adr/`](adr/) — architecture decision records
- `README.md` — repository overview and navigation
