# Project Context

This file is durable context for humans and agents working in this repository.

Keep it concise. Link to deeper docs, ADRs, issues, and code instead of duplicating everything here.

`AGENTS.md` is the source of truth for coding-agent operating instructions such as workflow rules, build commands, test commands, and safety rules. Use this file for durable project context that helps a fresh human or agent understand the repository's domain, vocabulary, relationships, constraints, and stable orientation.

If `AGENTS.md`, README files, ADRs, or runbooks already cover a topic well, link to them instead of copying their content.

Put mutable state — current implementation status, open questions, and recommended next work — in `docs/NEXT.md`, not here.

## Context Scope

orientation-context

## Durable Orientation

This repository is a synthetic AWK target used to validate the next live local `awk-runner` smoke test. It is not a product codebase and it is not the implementation home for `awk-runner` itself.

Humans and agents use this repository as a safe trial surface for AWK's durable workflow artifacts:

- a PRD issue defines the feature-sized goal
- vertical slice issues define bounded implementation work
- slice pull requests target a feature branch such as `feature/prd-21`
- durable docs in this repository explain the trial target without relying on chat history

`README.md` gives the top-level purpose statement. `docs/NEXT.md` records the mutable handoff state for the current runner trial.

## Domain Language

- `synthetic target`: a disposable repository used to validate workflow behavior rather than deliver product value
- `local runner`: the AWK execution runtime that launches implementation and review agents from a local machine instead of GitHub-hosted automation
- `smoke test`: a live end-to-end validation that the basic runner loop works on a real repository surface
- `PRD run`: the feature-level unit of runner orchestration described in ADR 0012
- `feature branch`: the per-PRD integration branch, named `feature/prd-{N}`, that receives slice PRs during a runner trial
- `slice issue`: one agent-ready vertical slice that is small enough for one focused pull request

## Relationship Map

In this repository, the runner trial is the main concept. A human-approved PRD defines the trial feature, slice issues break that feature into executable units, and the local runner is expected to move those slices through implementation and review on a feature branch. This repository supplies the durable target surface where those artifacts and branch conventions can be observed safely.

Historical seed files from the earlier install-trial phase remain in place because they make the target repo slightly messy in realistic ways. They are supporting context, not the primary goal of the current validation.

## Important Constraints

- Keep the repository framed around the local-runner validation path adopted in upstream ADR 0011 and ADR 0012.
- Do not treat legacy Copilot-related files in `.github/` as the active execution path for this trial. They are historical artifacts unless a later issue says otherwise.
- Keep durable orientation here and mutable next-step guidance in `docs/NEXT.md`.
- Avoid expanding this synthetic repo into a full operator runbook or real application codebase.

## Operational Notes

There is no production deployment surface here. The relevant operator concern is whether a fresh human can identify this repository as the current synthetic target for the next local runner smoke test and find the current handoff state quickly.

## Links

- [README.md](../README.md)
- [AGENTS.md](../AGENTS.md)
- [docs/NEXT.md](./NEXT.md)
- [Parent PRD #21](https://github.com/PMT-Medical/pmt-awk-trial-2/issues/21)
- [AWK ADR 0011: Local runner before Kubernetes or Copilot-specific expansion](https://github.com/PMT-Medical/agent-workflow-kit/blob/main/docs/adr/0011-local-runner-before-kubernetes.md)
- [AWK ADR 0012: PRD-level runner and feature branch pattern](https://github.com/PMT-Medical/agent-workflow-kit/blob/main/docs/adr/0012-prd-level-runner-and-feature-branch-pattern.md)
