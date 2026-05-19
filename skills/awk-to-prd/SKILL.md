---
name: awk-to-prd
description: Turn clarified product or workflow intent into a durable PRD that can be reviewed by humans and later sliced into implementation issues.
---

# To PRD

Use this skill after enough context exists to describe the problem, goals, non-goals, constraints, risks, and acceptance criteria.

Do not treat the PRD as chat output only. The PRD should become a durable repository or issue-tracker artifact.

The PRD should be written so `awk-to-issues` can later convert it into vertical slices with execution modes, workflow states, and blocker relationships.

## Inputs

- Clarified conversation context or approved investigation result
- Relevant GitHub issue, if one exists
- `AGENTS.md`
- `docs/CONTEXT.md`
- relevant ADRs
- any prototype, design note, or user workflow notes

## Required Reads

Read:

- `AGENTS.md`
- linked source issue or request
- `docs/CONTEXT.md` if present
- relevant ADRs
- relevant existing tests or code areas when implementation constraints matter

## Workflow

1. Identify the audience and problem.
2. State goals and non-goals separately.
3. Describe expected user or developer workflows.
4. Capture known constraints and architecture-sensitive decisions.
5. Convert requirements into acceptance criteria that can later drive vertical slices.
6. Map requirements to acceptance criteria and likely verification.
7. Identify likely execution modes:
   - likely agent-executable
   - likely human-decision required
   - likely mixed agent and human work
8. List risks, dependencies, sequencing concerns, and open questions.
9. Run the sliceability check before marking the PRD ready.
10. Publish or draft the PRD using the repository's PRD issue template.
11. Mark the PRD as ready for human review, not ready for implementation unless explicitly approved.

## Requirements Mapping

Before finalizing the PRD, build a short table:

```text
Requirement | Acceptance criterion | Verification signal | Likely execution mode | Open blocker
```

Use this table to catch vague requirements, missing verification, and work that should become an investigation or human-decision issue instead of an agent-ready implementation slice.

The table does not need to be exhaustive for tiny PRDs, but it should exist for product-shaped or cross-cutting work.

## Sliceability Check

The PRD is sliceable when:

- each goal has at least one acceptance criterion
- each requirement has a verification signal
- non-goals are explicit enough to prevent scope creep
- human decisions are named rather than hidden inside implementation
- likely blockers are visible
- likely agent-executable work can be separated from human-decision work
- the PRD can plausibly become multiple vertical slices or one explicitly small slice

## PRD Shape

Include:

- problem
- goals
- non-goals
- users and workflows
- existing context
- requirements
- acceptance criteria
- sliceability notes
- risks and constraints
- open questions

Use the target repository's PRD issue template when creating a GitHub issue.

## PRD Body Contract

Use this structure for markdown drafts:

```md
## Problem

What problem are we solving, and for whom?

## Goals

- ...

## Non-goals

- ...

## Users And Workflows

Who uses this, and what workflow changes?

## Existing Context

Relevant docs, ADRs, issues, PRs, code areas, or prior decisions.

## Requirements

- ...

## Acceptance Criteria

- ...

## Sliceability Notes

Requirement | Acceptance criterion | Verification signal | Likely execution mode | Open blocker

## Risks And Constraints

Technical, product, security, migration, operational, or sequencing risks.

## Open Questions

Questions that need human decision or investigation.

## Readiness

- [ ] Existing repository context has been reviewed.
- [ ] Architecture-sensitive decisions are called out.
- [ ] This can be sliced into independently reviewable issues.
- [ ] Human review is complete before implementation starts.
```

## Human Stop Points

Stop for review when:

- goals and non-goals are not explicit
- acceptance criteria are too vague to slice
- the PRD introduces architecture, security, data, or migration decisions
- the PRD depends on assumptions that only humans can validate
- any requirement lacks a verification signal
- the likely execution mode is unclear for major work areas

## Outputs

Produce:

- a PRD issue or PRD markdown draft
- a requirements mapping table
- sliceability notes
- links to updated durable docs, if changed
- a recommendation for whether the PRD is ready for `awk-to-issues`

## Completion Criteria

This skill is complete when the PRD can be reviewed independently of chat context and can be used as the input to vertical issue slicing.
