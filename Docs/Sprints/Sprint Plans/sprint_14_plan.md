# Sprint 14 – End-to-End Vertical Slice

## Context
The repo contains good scaffolding and documentation, but lacks end-to-end functionality. The docs-to-code ratio is too high, and key modules like the RSS parser exist only as blueprints. The CI process is missing critical quality gates for linting and test coverage. This sprint will pivot from blueprinting to shipping a tangible, albeit mocked, vertical slice of the application.

## Objective
Deliver a functional, vertical slice that runs a full workflow: RSS feed processing → dummy transcript generation → strategic analysis with a mocked LLM → and writing a summary to a Markdown file.

## Acceptance Criteria
- [ ] CI workflow `ci.yml` green.
- [ ] Tests `pytest -k "test_analyzer or test_rss_parser or test_runpod"` pass.
- [ ] Net new non-test LOC ≤ 200.
- [ ] No new top-level dependencies.
- [ ] `ruff --fail-level error` clean.
- [ ] Coverage ≥ 80 %.

## Deliverables
| path | max LOC | note |
|---|---|---|
| `config/strategic_topics.yml` | 20 | New YAML file for strategic goals. Externalizes configuration from code. |
| `src/spiceflow/rss_parser.py` | 80 | New file. Implementation of the RSS parser, replacing the old blueprint. |
| `src/spiceflow/analyzer.py` | 120 | New file. `StrategicAnalyzer` with error handling and a mockable LLM client interface. |
| `run_workflow.py` | 60 | Updated to run the new end-to-end pipeline. |
| `tests/unit/test_rss_parser.py` | 80 | New file. Unit tests for the parser. |
| `tests/unit/test_analyzer.py` | 120 | New file. Tests `StrategicAnalyzer`, mocking all LLM calls. |
| `tests/integration/test_runpod_transcribe.py` | 40 | Updated to fix the `/health` URL for the RunPod health check. |
| `.github/workflows/ci.yml` | 40 | Updated to add `ruff` and `pytest --cov` gates. |

## Process Rules
- Run `python scripts/env_check.py` first; fail fast on ❌.
- Stop immediately once all acceptance boxes tick ✅; do not optimise further.
- Commit messages start with `feat:` or `fix:`; PR title = Sprint 14 result.
- **Task:** Delete all `*.blueprint.md` files from the repository. 