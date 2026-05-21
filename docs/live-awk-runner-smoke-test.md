# Live `awk-runner` Smoke Test

This runbook is the smallest safe way to start a live local `awk-runner` smoke test against this synthetic target repository.

Use it when you want durable GitHub evidence that AWK can read a PRD, pick up ready slice issues, work on slice branches, and hand back a feature PR for human review.

## Trial Input

- Repository: `PMT-Medical/pmt-awk-trial-2`
- PRD issue number: `21`
- Expected feature branch: `feature/prd-21`
- Provider choices: `claude` or `codex`
- Default provider: if you omit `--provider`, the CLI uses `claude`

## Minimum Prerequisites

Before you start, confirm all of the following:

- You have a local checkout of this repository and can inspect the current issues and pull requests on GitHub.
- You have a local checkout of `agent-workflow-kit` or another local installation that exposes the current `awk-runner` CLI.
- `gh` is authenticated for the target repository and can open issues, create pull requests, and push branches.
- The provider CLI you intend to use is installed and authenticated locally:
  - `claude` if you will use the default provider or pass `--provider claude`
  - `codex` if you will pass `--provider codex`
- PRD `#21` is still the active trial PRD and is not already labeled `completed`.
- The PRD already has at least one open child slice issue that is ready for agent execution:
  - labeled `agent-ready`
  - labeled `execution:agent`
  - not labeled `completed`
  - not blocked by an unresolved dependency

If there are no open ready slices under PRD `#21`, stop and ask a human maintainer whether a new smoke-test slice should be created before you run the runner.

## Preflight Readiness Check

Run the non-destructive readiness check first:

```bash
python /path/to/agent-workflow-kit/scripts/awk-runner.py 21
```

Expected result:

- the command prints PRD `#21`
- the command lists one or more slice issue numbers
- the command exits without `ERROR:`

Do not continue to the live run if the readiness check fails.

## Start The Live Run

Run the full smoke test only after the preflight passes.

Default provider (`claude`):

```bash
python /path/to/agent-workflow-kit/scripts/awk-runner.py 21 --run
```

Explicit provider selection:

```bash
python /path/to/agent-workflow-kit/scripts/awk-runner.py 21 --run --provider claude
python /path/to/agent-workflow-kit/scripts/awk-runner.py 21 --run --provider codex
```

The `--provider` flag is optional. When it is omitted, `awk-runner` defaults to `claude`.

## Expected Durable GitHub Evidence

A successful smoke test should leave durable evidence in GitHub, not only terminal output.

Look for all of the following:

- PRD `#21` moves into `agent-in-progress` while the run is active.
- The runner works slice issues on `slice/...` branches and targets `feature/prd-21`, not `main`.
- Each successful slice ends with a focused slice pull request and a merge into `feature/prd-21`.
- Completed slice issues are closed and labeled `completed`.
- After all ready slices are merged, PRD `#21` is labeled `pr-open` and `needs-review`.
- A feature pull request from `feature/prd-21` to `main` is opened for human review.
- PRD `#21` receives a durable completion comment that links the feature PR and names the merged slice issues.

The run is successful when those GitHub artifacts exist and the final feature PR is ready for a human reviewer. Human approval and merge into `main` remain out of scope for the smoke test itself.

## Stop Conditions And Human Judgment

Stop and hand off to a human maintainer if any of the following happens:

- the readiness check fails for PRD `#21`
- the PRD has no open ready slice issues
- the runner exits with `BLOCKED:` or applies `blocked:human`
- a slice reveals a scope question, architecture decision, security-sensitive change, or other human-owned judgment call
- the runner produces a merge conflict or any ambiguity about whether a slice should continue
- the final feature PR exists but needs human review or human merge approval

Do not treat the smoke test as complete from terminal output alone. The GitHub artifacts above are the durable success signal.
