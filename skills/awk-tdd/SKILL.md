---
name: awk-tdd
description: Implement a bug fix or feature slice with a red-green-refactor loop, using tests as the quality gate.
---

# Test-Driven Development

Use this skill when implementing an agent-ready issue where behavior can be verified with automated tests or a tight manual verification loop.

The goal is to make progress in small, observable steps rather than writing broad implementation first and testing later.

This skill is for execution, not planning. If the assigned issue is not ready for execution, stop and report why.

## Inputs

- One assigned vertical slice issue
- Repository `AGENTS.md`
- Relevant code and tests
- Test command or verification command
- Acceptance criteria from the issue

## Required Reads

Read:

- assigned issue
- linked PRD or parent issue
- `AGENTS.md`
- relevant skills, docs, and ADRs
- nearby implementation and test files

From the assigned issue, extract:

- outcome
- execution mode
- workflow state
- blocked-by relationships
- scope
- out-of-scope work
- acceptance criteria
- verification expectations
- risks

## Readiness Gate

Before changing files, confirm:

- execution mode is `Agent-executable` or the human-owned parts are already resolved
- workflow state is `agent-ready`
- `Blocked by` is `None` or all blockers are completed
- acceptance criteria are concrete enough to verify
- verification commands or manual checks are known
- out-of-scope work is explicit
- implementation will happen on a non-default working branch, not directly on `main`, `master`, `trunk`, or another protected base branch
- a pull request will be opened for this slice before it is marked complete
- final approval and merge remain human-owned

Stop if any readiness condition fails. Do not implement blocked, proposed, human-decision, or mixed work unless the human explicitly resolves the blocker and authorizes the agent-executable portion.

If the repository is currently on a default or protected base branch, create or switch to a focused working branch before editing files. If branch creation is not possible, stop and report the blocker instead of implementing on the base branch.

## Implementation Plan

Before editing code, produce a short plan:

```md
## TDD Plan

Acceptance criteria to cover:

- ...

Test or verification cycles:

1. Behavior:
   RED:
   GREEN:
   Verification:

Out of scope:

- ...

Risks:

- ...
```

Keep the plan small. It should describe behavior, not private implementation details.

## Workflow

1. Pass the readiness gate.
2. Confirm the current branch is a non-default working branch for this slice.
3. Identify the smallest behavior that proves the slice is moving.
4. Write or update one test for that behavior.
5. Run the test and confirm the expected failure.
6. Implement the smallest change that makes the test pass.
7. Rerun the test and relevant surrounding checks.
8. Repeat one behavior at a time.
9. Refactor only after the relevant tests are green.
10. Update docs if the behavior or workflow changed.
11. Read the repository pull request template, if one exists, before creating or updating the PR body.
12. Open or prepare a focused pull request that maps changes back to the issue.
13. Run the PR body finalization gate before reporting completion.

## TDD Cycle

Use one behavior per cycle:

```text
RED: write or update one behavior test, then confirm it fails for the expected reason
GREEN: implement the smallest change that passes the test
VERIFY: rerun the targeted test and any relevant surrounding checks
REFLECT: decide whether the next acceptance criterion needs another cycle
```

Do not write all tests first and then all implementation. That creates horizontal slices inside a vertical issue.

## Test Rules

Good tests should:

- verify observable behavior
- use public interfaces where practical
- stay stable across internal refactors
- be named in the repository's domain language
- cover the acceptance criteria that matter most

Avoid tests that:

- assert private implementation details
- mock internal collaborators unnecessarily
- duplicate the implementation
- lock in speculative future behavior

If automated tests are not practical, define a tight manual verification loop before editing. Manual checks should still map to acceptance criteria.

## Scope Control

During implementation:

- implement only the assigned issue
- keep follow-up work out of the PR
- do not resolve unrelated cleanup unless required for the acceptance criteria
- do not change architecture boundaries without human review
- update `docs/CONTEXT.md` or ADRs only when durable context actually changes
- record any newly discovered blocker on the issue or PR

## Human Stop Points

Stop for review when:

- no practical verification path exists
- the issue's acceptance criteria cannot be tested
- implementation requires changing the approved scope
- the code reveals an architecture decision that was not in the issue
- blockers or workflow state are stale
- the issue is `Human-decision required` and the decision is unresolved
- tests reveal behavior that contradicts the linked PRD or ADRs

## Outputs

Produce:

- focused implementation
- tests or explicit verification steps
- docs updates when needed
- a pull request opened from the working branch, or a clear blocker explaining why the PR could not be opened
- a pull request body that follows the repository pull request template, links the issue, and lists checks run

## PR Summary Contract

Use the repository's pull request template. If `.github/PULL_REQUEST_TEMPLATE.md` or another repository PR template exists, read it before creating or updating the PR body and keep the PR body shaped like that template.

At minimum, include:

- linked issue
- acceptance criteria covered
- scope boundaries and out-of-scope work avoided
- tests or checks run
- skipped checks and why
- docs, ADR, context, or handoff updates
- risks and residual uncertainty
- follow-up issues for out-of-scope work

If durable context changed, call it out explicitly in the PR body. This includes updates to `docs/CONTEXT.md`, `docs/NEXT.md`, ADRs, reusable skills, install resources, templates, or other workflow artifacts that future humans or agents will rely on. Do this even when the primary issue is about workflow behavior rather than documentation.

## PR Body Finalization Gate

Before reporting completion, compare the PR body against the repository pull request template when one exists.

The PR body is not complete until it records:

- the linked issue or clearly explained relationship to the issue
- the focused scope of the PR and any out-of-scope work moved elsewhere
- architecture-sensitive decisions, docs changes, ADR changes, context changes, or handoff changes included in the diff
- verification performed, including commands, targeted checks, or manual checks
- skipped checks and why they were skipped
- risks, compatibility concerns, operational concerns, or residual uncertainty
- follow-up work that remains outside the PR

If the template has sections or checkboxes for this information, fill them in directly. If a section does not apply, say so briefly instead of omitting it. Preserve the existing requirement that final approval and merge are human-owned.

## Final Response Shape

When reporting completion, use:

```md
Implemented:

- ...

Verification:

- command or manual check

Issue mapping:

- acceptance criterion -> change/test

Residual risk:

- ...
```

## Completion Criteria

This skill is complete when the issue's acceptance criteria are met, relevant checks pass, and residual risk is documented in the pull request.

Do not mark an issue completed from local branch state alone. Completion requires a pull request and human-owned final approval or merge.
