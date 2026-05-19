---
name: awk-grill-with-docs
description: Clarify a rough idea against repository docs, domain language, ADRs, and current implementation before a PRD or implementation issue is created.
---

# Grill With Docs

Use this skill when a request is still ambiguous, product-shaped, architecture-sensitive, or likely to affect multiple parts of a repository.

The goal is to turn vague intent into durable context: clarified requirements, sharpened terminology, open questions, and documentation updates that future agents can read.

Do not jump directly to a PRD or implementation plan. First, challenge the request against the repository's existing language, decisions, and behavior.

## Inputs

- Rough idea, issue, bug report, feature request, or design sketch
- Target repository path
- Existing `AGENTS.md`
- Existing `docs/CONTEXT.md` when present
- Existing ADRs in `docs/adr/` when present

## Required Reads

Before asking detailed questions, read:

- `AGENTS.md`
- `docs/CONTEXT.md` if present
- relevant ADRs
- linked issues, PRDs, or design notes
- nearby code or tests when the request references a known area

Vendor-specific files are not source of truth. If present, use them only as pointers back to `AGENTS.md`.

## Workflow

1. Restate the request in the repository's domain language.
2. Identify which docs, ADRs, code areas, and tests appear relevant.
3. Answer anything that can be answered by reading the repository instead of asking the human.
4. Surface contradictions, missing terms, and architecture-sensitive decisions.
5. Ask focused questions one at a time, starting with the question that most reduces uncertainty.
6. For each question, include your recommended answer and why.
7. Stress-test answers with concrete scenarios and edge cases.
8. Update or propose updates to durable docs when terminology or decisions become stable.
9. Summarize the clarified brief, remaining open questions, and recommended next artifact.

## Question Categories

Use these categories to find uncertainty:

- product intent: what problem is being solved, for whom, and why now
- users and workflows: who acts, what changes, and what stays the same
- domain language: ambiguous terms, overloaded nouns, and glossary conflicts
- scope boundaries: goals, non-goals, and adjacent work to avoid
- architecture: module boundaries, integration points, data flow, and reversibility
- data and security: sensitive data, permissions, migrations, compliance, and audit needs
- execution mode: what can be agent-executable and what needs human decision
- verification: tests, checks, manual validation, and observability
- rollout: migration, compatibility, feature flags, and rollback
- issue slicing: likely vertical slices, blockers, and sequencing

Do not ask every category mechanically. Ask the smallest set of questions needed to make the next artifact reliable.

## Documentation Rules

Use durable docs carefully:

- `docs/CONTEXT.md` should capture stable domain terms, project vocabulary, and durable orientation.
- ADRs should capture meaningful decisions that are hard to reverse, surprising without context, or the result of real tradeoffs.
- PRDs should capture product-shaped requirements and acceptance criteria.
- GitHub issues should capture executable vertical slices and workflow state.

Do not put implementation scratch notes into `docs/CONTEXT.md`. Do not create an ADR for every minor preference.

## Clarified Brief Contract

When the grilling session is complete, produce a clarified brief:

```md
## Clarified Problem

What problem are we solving, for whom, and why?

## Confirmed Language

Terms that should be used consistently.

## Goals

- ...

## Non-goals

- ...

## Key Decisions

- Decision and rationale.

## Human Decisions Still Needed

- ...

## Likely Execution Shape

- Likely agent-executable work
- Likely human-decision work
- Likely blockers

## Verification Expectations

Tests, checks, or manual validation that should matter later.

## Durable Documentation Updates

Proposed or completed updates to `docs/CONTEXT.md`, ADRs, PRDs, or issues.

## Recommended Next Step

Create PRD | create investigation issue | create vertical slice | stop
```

## Outputs

Produce one or more of:

- clarified brief
- decision list
- open question list
- proposed `docs/CONTEXT.md` edits
- proposed ADR candidate
- recommendation to create a PRD
- recommendation to create one or more investigation issues

## Human Stop Points

Stop for human review when:

- the request changes architecture boundaries
- a security, data, compliance, or migration decision is needed
- terminology is disputed or unclear
- the next step should be a PRD rather than direct implementation
- the user is asking for implementation but the workflow state or execution mode is unclear

## Completion Criteria

This skill is complete when a future agent could read the durable artifacts and understand what problem is being solved, what remains undecided, and what artifact should be created next.
