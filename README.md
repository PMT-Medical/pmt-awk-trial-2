# pmt-awk-trial-2

This is a synthetic Agent Workflow Kit (AWK) target repository for the next live local `awk-runner` smoke test.

## Purpose

This repository exists to validate AWK's local-runner path against a safe, disposable target before that workflow is exercised on a real codebase.

The next expected use of this repo is a live smoke test where a local `awk-runner` reads PRD-backed slice issues, works on feature and slice branches, and leaves durable pull request evidence in this synthetic repository.

The seeded files in this repo still preserve overlap conditions from the earlier install trial, but those artifacts now serve the runner trial rather than a standalone install validation. They remain useful for exercising AWK behavior in a repository that already contains some agent-facing scaffolding.

## Current Validation Goal

- Prove that the local `awk-runner` can treat this repository as a synthetic target for a live smoke test
- Keep the repository orientation aligned with the local-runner direction from AWK ADR 0011 and ADR 0012
- Preserve durable context for a fresh operator without relying on prior chat history

## Seed State

This repo is intentionally pre-seeded with a few files from the earlier install-trial phase:

- **Issue template merge/preserve behavior** — existing `.github/ISSUE_TEMPLATE/` files with custom fields
- **Labels overlap handling** — a `github/labels.yml` with custom labels; the install should propose additions only and never delete existing labels
- **Skill overlap detection** — a locally installed `skills/grill-with-docs/SKILL.md` that overlaps with the AWK-namespaced `awk-grill-with-docs` skill

| Path | Purpose |
|------|---------|
| `.github/ISSUE_TEMPLATE/bug_report.yml` | Existing issue template with custom fields |
| `github/labels.yml` | Existing labels with two custom labels (`priority:high`, `team:backend`) |
| `skills/grill-with-docs/SKILL.md` | Locally installed skill overlapping with `awk-grill-with-docs` |

These files are historical seed material, not the active validation target by themselves.

## What This Repo Is Not

- Not a production codebase
- Not intended for real product development work
- Not the place to implement `awk-runner` itself
- Not a signal that Copilot automation is the active path for this trial

Historical Copilot-related files may still exist in `.github/`, but this repository's active validation path is the local runner described in AWK ADR 0011 and ADR 0012. Use [`AGENTS.md`](AGENTS.md), [`docs/CONTEXT.md`](docs/CONTEXT.md), and [`docs/NEXT.md`](docs/NEXT.md) for the current workflow framing.

## Trial Notes

Trial notes and handoff state for the local runner trial should be captured in `docs/` as work proceeds, with mutable next-step guidance in `docs/NEXT.md`.
