---
name: grill-with-docs
description: Clarify a rough idea against repository docs, domain language, and existing decisions before creating a PRD or implementation issue.
---

# Grill With Docs

Use this skill when a request is still vague, product-shaped, or likely to affect multiple parts of the repository.

The goal is to surface contradictions, missing terms, and open questions before committing to an implementation direction.

## Inputs

- Rough idea, issue, feature request, or design sketch
- Existing `AGENTS.md` or equivalent instructions file
- Any existing context documents or decision records

## Workflow

1. Restate the request in the repository's own language.
2. Identify which docs, decisions, and code areas appear relevant.
3. Answer what can be answered by reading the repo rather than asking the human.
4. Surface contradictions, missing terminology, and decisions that require human input.
5. Ask one focused question at a time, starting with whatever most reduces uncertainty.
6. Continue until the request is clear enough to write a PRD or cut an issue.

## Outputs

- Clarified request restated in repo language
- List of resolved questions (answered from docs)
- List of open questions requiring human input
- Suggested terminology updates or new terms for the context document
- A brief summary suitable for opening a PRD or investigation issue
