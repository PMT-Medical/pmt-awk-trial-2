---
name: awk-to-issues
description: Break an approved PRD, plan, or investigation result into small vertical slice issues that agents can implement one pull request at a time.
---

# To Issues

Use this skill when a PRD or approved plan needs to become implementation work.

The output should be independently reviewable vertical slice issues, not a large task list that only makes sense with hidden chat context.

This skill is the handoff point between planning and implementation. Treat the issue bodies as the durable contract that a future agent will execute.

## Inputs

- Approved PRD, plan, or investigation result
- Target issue tracker
- Repository `AGENTS.md`
- `docs/CONTEXT.md` and ADRs when present
- Existing issue template for vertical slices

## Required Reads

Read:

- the full PRD or source plan
- `AGENTS.md`
- relevant durable docs and ADRs
- existing labels and issue templates
- nearby code or tests if needed to understand realistic slice boundaries

## Workflow

1. Extract the PRD's goals, non-goals, requirements, acceptance criteria, risks, and open questions.
2. Separate implementation work from decisions, investigations, migrations, and follow-up cleanup.
3. Identify the thinnest useful end-to-end outcomes.
4. Draft vertical slices that are independently testable and reviewable.
5. Assign each slice an execution mode:
   - `Agent-executable`: an agent can complete the slice after approval without more human decisions.
   - `Human-decision required`: a human decision, review, credential, product judgment, or architecture call is required before implementation can proceed.
   - `Mixed agent and human work`: part of the work is agent-executable, but explicit human checkpoints remain.
6. Assign each slice a workflow state:
   - `proposed`: drafted but not approved.
   - `agent-ready`: approved and ready for an agent.
   - `blocked`: waiting on another issue, human decision, or external dependency.
   - `agent-in-progress`: currently being implemented by an agent.
   - `pr-open`: pull request exists.
   - `needs-review`: waiting for review.
   - `needs-fix`: review comments or failed checks require changes.
   - `completed`: accepted and merged or otherwise closed.
7. Assign a recommended AWK skill for every issue that will be run by an agent:
   - Use `awk-tdd` for agent-executable implementation slices with defined verification.
   - Use `awk-pr-review` for review-only work.
   - Use `awk-grill-with-docs`, `awk-to-prd`, or `awk-to-issues` when the next step is clarification, PRD creation, or slicing rather than implementation.
   - If no AWK skill fits, say so explicitly and describe the expected manual or repository-specific workflow.
8. Build the blocker graph:
   - `Blocked by`: prerequisite issues or decisions.
   - `Blocks`: later slices that should wait for this slice.
   - `Can run in parallel with`: slices that do not depend on this one.
   - `Follow-up slices`: useful next work after this slice lands.
9. Decide which relationships can be represented by the target issue tracker:
   - Use GitHub parent/sub-issue relationships for parent PRDs or planning issues when available.
   - Use GitHub blocked-by/blocking relationships for issue dependencies when available.
   - Keep parallel work and follow-up slices in the issue body unless they need their own issue links.
10. Review dependency order and remove hidden sequencing.
11. Present the proposed issue breakdown for human review before creating issues.
12. After approval, create or draft issues using the vertical slice issue template. For agent-executable slices, apply `agent-ready` + `execution:agent` at creation time — the step-11 human review is the readiness gate.

## Extraction Pass

Build a short working table from the PRD before drafting issues:

```text
Requirement | Acceptance signal | Likely slice | Verification | Open risk
```

Use this table to catch requirements that have no verification path or no slice.

If an item cannot be tied to acceptance criteria, verification, or a concrete outcome, keep it out of agent-ready issues and list it as a human review question.

## Planning Matrix

Before publishing issues, produce a planning matrix that can be mapped onto a GitHub project board or Kanban view:

```text
Slice | Execution mode | Workflow state | Recommended skill | Blocked by | Blocks | Parallel with | Labels
```

Use the matrix to find:

- agent-executable work that can start immediately
- human-decision work that should not be assigned to an agent yet
- issue chains that must be created in dependency order
- work that can run in parallel
- labels needed for filtering a board

This does not need to use Matt's exact AFK/HITL terminology. Prefer plain labels and fields that are understandable on a GitHub issue board.

When GitHub native relationships are available, publish issues in an order that allows the relationships to be set after issue numbers exist.
Parent planning issues should receive vertical slices as sub-issues.
Blocking dependencies should be set as GitHub issue dependencies.
If the agent cannot set native relationships through the available UI, CLI, or API permissions, keep the relationship fields in the issue body and call out the missing native metadata for human follow-up.

## Slice Rules

Each slice should:

- deliver one visible user or developer outcome
- be small enough for one focused pull request
- require implementation on a non-default working branch
- require a pull request before the slice can be marked complete
- include acceptance criteria
- include verification steps
- state out-of-scope work
- identify dependencies and blockers
- avoid bundling unrelated refactors

Prefer thin vertical slices over horizontal tasks.

Good slice:

```text
Users can create a saved search and see it on their dashboard.
```

Weak horizontal slices:

```text
Add saved-search database tables.
Build saved-search API.
Build saved-search UI.
```

Horizontal work may appear inside a slice's scope only when it supports that slice's visible outcome.

## Issue Body Contract

Each generated issue must use the target repository's vertical slice issue shape.

Use this structure:

```md
## Outcome

One sentence describing the user or developer-visible result.

## Background

Parent PRD, related issues, relevant docs or ADRs, and any context required to understand the slice without chat history.

## Execution Mode

Agent-executable | Human-decision required | Mixed agent and human work

## Workflow State

Proposed | agent-ready | blocked | agent-in-progress | pr-open | needs-review | needs-fix | completed

## Recommended Skill

Recommended: awk-tdd | awk-pr-review | awk-grill-with-docs | awk-to-prd | awk-to-issues | None

Rationale: Why this skill is the right next procedure for the assigned agent.

## Scope

What should change in this slice. Include expected behavior and likely areas, but avoid brittle implementation instructions unless the PRD already decided them.

## Out Of Scope

What this PR must not include.

## Acceptance Criteria

- [ ] Concrete condition 1
- [ ] Concrete condition 2
- [ ] Concrete condition 3

## Verification

Commands, tests, checks, or manual verification expected for this slice.

## Delivery Workflow

- [ ] Create or switch to a non-default working branch before editing files.
- [ ] Open a focused pull request for this slice before marking the issue completed.
- [ ] Leave final approval and merge to a human maintainer.

## Dependencies And Sequencing

Blocked by: None | #123 | human decision | external dependency
Blocks: None | #124
Can run in parallel with: None | #125
Follow-up slices: None | title or issue reference

Native GitHub relationships to set, if available:
- Parent issue: None | #122
- Blocked by dependencies: None | #123
- Blocking dependencies: None | #124

## Risks

Known risk areas and what the implementer should watch.

## Agent Readiness

- [ ] The task has one clear goal.
- [ ] Expected verification is defined.
- [ ] Out-of-scope work is explicit.
- [ ] The issue is small enough for one focused pull request.
- [ ] The slice requires a branch and pull request before completion.
```

The issue body should be self-contained. A future agent should not need the original chat to understand the task.

For `agent-ready` + `execution:agent` implementation slices, default the recommended skill to `awk-tdd` unless the issue is explicitly review-only, planning-only, or a better AWK skill is named by the source plan.

## Label Guidance

Recommend labels based on readiness:

- `vertical-slice` for every implementation slice
- `execution:agent` when an approved slice can be completed by an agent without additional human decisions
- `execution:human` when a human decision or action is required before implementation
- `execution:mixed` when the slice has agent work plus explicit human checkpoints
- `agent-ready` when all readiness checks are satisfied
- `blocked` when a dependency or human decision prevents implementation
- `blocked:issue` when blocked by another issue or PR
- `blocked:human` when blocked by human product, architecture, security, or review input
- `blocked:external` when blocked by a vendor, credential, environment, or dependency outside the repo
- `needs-review` when the issue draft needs human validation
- `investigation` when the item is research rather than implementation
- `needs-slicing` only for parent PRDs or plans that still need breakdown

Workflow state labels should be mutually understandable on a Kanban board. Execution labels describe who can move the work. Blocker labels describe why work cannot proceed.

For agent-executable slices approved in step 11, apply `agent-ready` + `execution:agent` at issue creation time. The step-11 human review is the readiness gate — once approved, the slice is ready and these labels should be set when the issue is created, not as a separate step afterwards. For issues created outside the AWK workflow (bug reports, manually created issues), `agent-ready` is still a separate human assessment step because no upstream PRD approval exists.

## Anti-Patterns

Avoid:

- horizontal slices such as "build all database changes" or "build all UI"
- issues that require private chat context to understand
- vague tickets such as "implement feature"
- issues with no verification path
- issues that silently rely on unapproved architecture decisions
- "misc cleanup" issues attached to feature work
- labels that imply agent readiness before human approval (this applies to the pre-approval proposed phase; after step-11 approval, applying `agent-ready` + `execution:agent` at creation is correct)
- dependency chains that are only described in chat
- native GitHub relationship metadata that disagrees with the issue body
- marking mixed or human-decision work as fully agent-executable

## Human Stop Points

Stop for review when:

- slice size is uncertain
- dependency order is unclear
- any slice requires architecture, security, data, or migration decisions
- the issue set changes the PRD scope
- any acceptance criterion cannot be represented in at least one issue
- any issue lacks verification
- any blocker cannot be represented as an issue, decision, or external dependency

## Outputs

Produce:

- extraction table
- planning matrix
- proposed issue list with readiness state
- execution mode for each issue
- dependency order
- blocker relationships
- native GitHub relationship actions or follow-up notes
- label recommendations
- created or draft GitHub issues
- unresolved questions that must stay attached to the parent PRD

## Final Response Shape

When presenting the breakdown, use:

```md
## Proposed Slices

1. Title
   Execution mode: Agent-executable | Human-decision required | Mixed agent and human work
   Workflow state: proposed | agent-ready | blocked
   Recommended skill: awk-tdd | awk-pr-review | awk-grill-with-docs | awk-to-prd | awk-to-issues | None
   Blocked by: None | #123 | human decision | external dependency
   Blocks: None | #124
   Can run in parallel with: None | #125
   Labels: vertical-slice, execution:agent, agent-ready
   Why this slice exists: ...

## Questions Before Publishing

- ...

## Recommended Labels

- ...
```

Only create issues after the human approves the slice list.

## Completion Criteria

This skill is complete when a human can approve the issue set and an agent can pick up one issue without needing the original conversation.
