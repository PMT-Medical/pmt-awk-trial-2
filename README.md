# pmt-awk-trial-2

This is a synthetic test repository used as a target for the second Agent Workflow Kit (AWK) install trial.

## Purpose

This repo exists to stress-test `awk-install` overlap scenarios that the first trial (`PMT-Medical/pmt-api-cmd`) did not cover. It is intentionally seeded with pre-existing scaffolding to exercise:

- **Issue template merge/preserve behavior** — existing `.github/ISSUE_TEMPLATE/` files with custom fields
- **Labels overlap handling** — a `github/labels.yml` with custom labels; the install should propose additions only and never delete existing labels
- **Skill overlap detection** — a locally installed `skills/grill-with-docs/SKILL.md` that overlaps with the AWK-namespaced `awk-grill-with-docs` skill

## Seed State

| Path | Purpose |
|------|---------|
| `.github/ISSUE_TEMPLATE/bug_report.yml` | Existing issue template with custom fields |
| `github/labels.yml` | Existing labels with two custom labels (`priority:high`, `team:backend`) |
| `skills/grill-with-docs/SKILL.md` | Locally installed skill overlapping with `awk-grill-with-docs` |

## What This Repo Is Not

- Not a production codebase
- Not an AWK-installed repository (AWK resources are deliberately absent from the seed state)
- Not intended for any real development work

## Trial Notes

Trial notes will be captured in `docs/trials/` during and after the AWK install trial run.
