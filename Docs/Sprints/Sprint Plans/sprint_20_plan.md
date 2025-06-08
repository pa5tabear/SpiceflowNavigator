# Sprint 20 – Fix the Main Branch CI

## Context
Sprint 19 attempted to fix a critical bug, but the subsequent merge has left the `main` branch CI in a **failing state**. I am currently unable to view the CI logs to pinpoint the exact error due to a tooling failure. Therefore, the top priority is to investigate and resolve this failure to restore a stable foundation for the project.

## Objective
Deliver a **green CI badge** for the `main` branch.

## Acceptance Criteria
- [x] CI `ci.yml` green
- [ ] Tests `pytest -k "not integration"` pass
- [ ] Net new non-test LOC ≤ 50
- [ ] No new top-level dependencies
- [ ] `ruff --fail-level error` clean
- [ ] Coverage ≥ 80 %

## Deliverables _(Codex will implement)_
| path | max LOC | note |
|---|---|---|
| *Unknown* | ≤ 50 | **Investigate CI failure.** The first task is to identify the failing step in the `ci.yml` workflow and diagnose the root cause. |
| *Dependent on Investigation* | | Apply the necessary code changes to fix the CI pipeline. |

## Process Rules for Codex
* Run `python scripts/env_check.py` first; fail fast on ❌
* Stop when all acceptance boxes are ✅; no "bonus" code
* Commit messages: `fix(sprint20): ...`

_Compare this plan to `Docs/TEMPLATE_SPRINT_PLAN.md`; ensure parity._ 