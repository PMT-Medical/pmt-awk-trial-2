# Repository Agent Instructions

## Purpose

This repository uses Agent Workflow Kit to make AI-assisted development repeatable, reviewable, and safe.

Agents should work from durable repository artifacts rather than relying on long chat context. The primary artifacts are GitHub Issues, Pull Requests, tests, `AGENTS.md`, skills, `docs/CONTEXT.md`, `docs/NEXT.md`, ADRs, and git history.

This `AGENTS.md` file is the source of truth for coding-agent instructions. Vendor-specific files such as `CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` should only point back here.

## Human Ownership

Humans own:

- product direction
- architecture
- security-sensitive decisions
- prioritization
- final review
- merge decisions

Agents may propose, implement, test, document, and revise bounded changes, but should not treat themselves as autonomous owners of the repository.

## Standard Workflow

Use this workflow for non-trivial changes:

1. Clarify the request against existing docs and architecture.
2. Create or update a PRD when the request is product-shaped or cross-cutting.
3. Break approved work into vertical slice issues.
4. Wait for human review before executing broad or ambiguous work.
5. Create or switch to a non-default working branch before editing files.
6. Implement one agent-ready issue at a time.
7. Open a focused pull request.
8. Run the relevant checks.
9. Address review comments and failed checks.
10. Leave final approval and merge to humans.

## Before Editing Code

Read the relevant durable context:

- the assigned GitHub issue
- linked PRD or design notes
- this `AGENTS.md`
- applicable skills in `skills/`
- `docs/CONTEXT.md` when present
- `docs/NEXT.md` when resuming work, choosing next work, or checking current open questions
- relevant ADRs in `docs/adr/`
- nearby tests and implementation files

If the issue is too vague to implement safely, ask for clarification or convert the uncertainty into explicit open questions.

Use `docs/CONTEXT.md` for stable project orientation and terminology. Use `docs/NEXT.md` for mutable handoff state: current direction, recommended next work, open questions, and settled decisions that should not be reopened casually. Update `docs/NEXT.md` when your work changes the handoff state for the next human or agent.

## Vertical Slice Rules

Implementation issues should be small enough to complete and review as one pull request.

Each slice should define:

- the user or developer-visible outcome
- files or areas likely to change
- acceptance criteria
- verification steps
- out-of-scope work
- known dependencies or sequencing constraints

Do not silently expand a slice into adjacent refactors or extra features.

## Testing And Verification

Before opening or updating a pull request:

- run the relevant test suite or targeted checks
- add or update tests when behavior changes
- document any checks that could not be run
- include manual verification steps when automated tests are not practical

If no automated tests exist for the touched area, explain the residual risk in the pull request.

## Pull Request Expectations

Pull requests should be focused and easy to audit.

Each PR should include:

- a short summary of the change
- the linked issue
- tests or verification performed
- any docs or ADR updates
- known risks or follow-up work

Avoid mixing unrelated cleanup with feature or bug work.

Do not implement directly on `main`, `master`, `trunk`, or another protected base branch. Do not mark an implementation issue complete from local branch state alone; completion requires a pull request and human-owned final approval or merge.

## Skills

Reusable workflows live in `skills/` when installed in this repository.

This repository uses Agent Workflow Kit as its workflow source of truth. Prefer `awk-*` skills for planning, issue slicing, implementation, and review. Do not substitute similarly named globally or locally installed skills unless the user explicitly asks.

Common skills may include:

- `awk-grill-with-docs` for clarifying an idea against repository context
- `awk-to-prd` for turning clarified work into a product requirements document
- `awk-to-issues` for slicing a PRD into implementation issues
- `awk-tdd` for test-first implementation
- `awk-pr-review` for reviewing a pull request

Prefer these skills over ad hoc process when they apply.

## Safety Rules

- Do not make destructive changes unless the user explicitly requests them.
- Do not alter security-sensitive behavior without human review.
- Do not introduce new dependencies without a clear reason.
- Do not hide uncertainty; write it down in the issue, PR, or docs.
- Do not rely on private chat context for decisions that future agents or reviewers need.
