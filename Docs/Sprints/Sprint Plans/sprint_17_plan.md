# Sprint 17 – Process Hardening & Config Alignment

## Context
Sprint 16 successfully delivered a script to initiate a transcription job, but the pre-flight check failed because a mandatory `env_check.py` script was missing. The `gh` CI check also failed. Furthermore, the `config/rss_feeds.yml` created in the sprint diverged from the project's standard structured format. Before adding new features, we must stabilize the process and align the configuration.

## Objective
Deliver a green pre-flight checklist and a standardized configuration file.

## Acceptance Criteria
- [ ] CI workflow `ci.yml` green.
- [ ] Tests `pytest -k test_env_check or test_config_loader` pass.
- [ ] Net new non-test LOC ≤ 100.
- [ ] No new top-level dependencies.
- [ ] `ruff --fail-level error` clean.
- [ ] Coverage ≥ 80 %.

## Deliverables
| path | max LOC | note |
|---|---|---|
| `scripts/env_check.py` | 50 | New script to check for secrets and network access. |
| `config/rss_feeds.yml` | 20 | Update to the structured format (name, url, etc.). |
| `src/spiceflow/config.py` | 50 | New module to safely load and validate the structured config. |
| `tests/unit/test_config.py`| 50 | Unit tests for the new config loader. |
| `run_transcription_job.py` | - | Refactor to use the new config loader. |

## Process Rules
*   Run `python scripts/env_check.py` first; fail fast on ❌.
*   Stop immediately once all acceptance boxes tick ✅; do not optimise further.
*   Commit messages start with `feat:` or `fix:`; PR title = Sprint 17 result. 