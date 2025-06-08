# Sprint 14 – Strategic Analyzer

## Context
The repository now contains a `WorkflowManager` that automatically generates raw podcast transcripts as Markdown files. All 8 unit tests are passing. The core backend and workflow are stable. The immediate blocker to delivering business value is the lack of an analysis layer on top of the raw text.

## Objective
Deliver a `StrategicAnalyzer` class that takes a transcript string as input and returns a concise, AI-generated summary of its strategic relevance.

## Acceptance Criteria
- [ ] CI workflow `ci.yml` green.
- [ ] Tests `pytest -k test_analyzer` pass.
- [ ] Net new non-test LOC ≤ 80.
- [ ] No new top-level dependencies.
- [ ] `ruff --fail-level error` clean.
- [ ] Coverage ≥ 80 %.

## Deliverables
| path | max LOC | note |
|---|---|---|
| `src/spiceflow/analyzer.py` | 80 | implementation |
| `tests/unit/test_analyzer.py` | 80 | unit tests |

## Process Rules
- Run `python scripts/env_check.py` first; fail fast on ❌.
- Stop immediately once all acceptance boxes tick ✅; do not optimise further.
- Commit messages start with `feat:` or `fix:`; PR title = Sprint 14 result. 