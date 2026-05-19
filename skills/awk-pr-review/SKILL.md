---
name: awk-pr-review
description: Review a pull request for correctness, scope control, tests, documentation, risks, and alignment with the linked issue.
---

# PR Review

Use this skill when reviewing a pull request created by a human or agent.

Review should prioritize behavioral risk, regressions, missing tests, unclear scope, and mismatches with the linked issue. Style comments are secondary unless they affect maintainability or local conventions.

Review is a quality gate in the Agent Workflow Kit lifecycle. It should decide whether the pull request is a focused, verified implementation of the linked issue.

## Inputs

- Pull request diff
- Linked issue or PRD
- Repository `AGENTS.md`
- Relevant tests and CI results
- Relevant docs and ADRs

## Required Reads

Read:

- the PR summary
- linked issue and acceptance criteria
- linked PRD or parent issue when present
- changed files
- relevant tests
- CI results or local verification output
- `AGENTS.md`
- docs or ADRs touched by the change

From the linked issue, extract:

- outcome
- execution mode
- workflow state
- blocked-by relationships
- scope
- out-of-scope work
- acceptance criteria
- verification expectations
- risks

From the pull request, extract:

- linked issue
- summary
- scope checklist
- verification performed
- documentation updates
- risk notes
- reviewer notes

## Review Gate

Before reviewing implementation details, confirm:

- the PR links to exactly one primary implementation issue or clearly explains why not
- the linked issue was `agent-ready` or otherwise approved for work
- the issue execution mode allowed the implemented work
- blockers were resolved, removed, or explicitly documented
- the PR body follows the repository's pull request template
- the PR does not silently include out-of-scope work

If the PR fails this gate, lead with that finding.

## Workflow

1. Run the review gate.
2. Confirm the PR maps to one focused issue or explain the scope mismatch.
3. Compare implementation behavior against each acceptance criterion.
4. Inspect tests or manual verification for meaningful coverage of changed behavior.
5. Check documentation and ADR updates where durable context changed.
6. Check whether execution mode, blockers, and workflow state were respected.
7. Identify regressions, security risks, migration risks, and operational risks.
8. Verify failed or missing checks are called out.
9. Provide findings ordered by severity with file and line references when possible.

## Acceptance Criteria Matrix

Build a short matrix while reviewing:

```text
Acceptance criterion | Covered by change | Verified by | Gap or risk
```

Use the matrix to identify missing implementation, weak tests, or undocumented manual verification.

## Scope Review

Check the PR against the issue's scope and out-of-scope sections.

Flag:

- unrelated cleanup
- extra features
- architecture changes not called out in the issue
- docs or template changes that should have been separate issues
- changes that satisfy a follow-up slice before its blocker is complete

## Verification Review

Verification is adequate when it maps to the issue's acceptance criteria.

Prefer:

- automated tests for behavior changes
- targeted checks for narrow implementation changes
- manual verification only when automation is not practical
- clear explanation of skipped checks

Flag verification that:

- only proves files changed, not behavior
- does not exercise the acceptance criteria
- relies on hidden local state
- omits failed or skipped checks

## Review Priorities

Prioritize:

- correctness bugs
- missing or weak verification
- scope expansion
- stale blockers or wrong execution mode
- unsafe architecture or data changes
- undocumented decisions
- unclear follow-up requirements

Deprioritize:

- personal style preferences
- unrelated refactors
- speculative future improvements

## Human Stop Points

Escalate when:

- security-sensitive behavior changed
- data migration or compatibility risk exists
- architecture changed without an ADR or explicit review
- the PR cannot be reviewed because the linked issue is missing or vague
- the PR implements human-decision work without evidence of the human decision
- blockers remain unresolved

## Outputs

Produce:

- ordered review findings
- open questions
- acceptance criteria matrix
- test or verification gaps
- scope assessment
- blocker and execution-mode assessment
- approval recommendation only when the PR is within scope and adequately verified

## Finding Format

Lead with findings. Order by severity.

Use this shape:

```md
## Findings

1. Severity: blocker | major | minor
   File/line: path:line when available
   Issue: What is wrong?
   Why it matters: What can break or become unclear?
   Suggested fix: What should change?

## Open Questions

- ...

## Verification Gaps

- ...

## Approval Recommendation

Approve | Request changes | Needs human decision
```

If there are no findings, say that clearly and mention remaining residual risk.

## Completion Criteria

This skill is complete when reviewers have a clear list of blocking issues, non-blocking concerns, and remaining verification risk.
