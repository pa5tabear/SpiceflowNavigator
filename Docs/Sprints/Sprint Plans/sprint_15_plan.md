# Sprint 15 – Live Transcription E2E Test

## Context
Sprint 14 was a failure, producing no deliverables. The project lacks a working end-to-end capability and has critical CI gaps. Per the Project Owner's directive, the project will now focus on de-risking the most critical component first: live transcription. All downstream logic, like strategic analysis, is postponed.

## Objective
Deliver a single, executable script that ingests the live "Shift Key" RSS feed, fetches the audio URL for the most recent episode, submits it to the real RunPod API for transcription, and prints the returned transcript to the console.

## Acceptance Criteria
- [ ] CI workflow `ci.yml` green.
- [ ] Tests `pytest -k "test_rss_parser or test_runpod"` pass.
- [ ] Net new non-test LOC ≤ 150.
- [ ] No new top-level dependencies.
- [ ] `ruff --fail-level error` clean.
- [ ] Coverage ≥ 80 %.

## Deliverables
| path | max LOC | note |
|---|---|---|
| `src/spiceflow/rss_parser.py` | 80 | New file. Implementation of the RSS parser. |
| `run_live_transcription.py` | 70 | New file. The Golden Path script for this sprint. |
| `tests/unit/test_rss_parser.py` | 80 | New file. Unit tests for the parser. |
| `tests/integration/test_runpod_transcribe.py` | 40 | Updated to fix the `/health` URL for the RunPod health check. |
| `.github/workflows/ci.yml` | 40 | Updated to add `ruff` and `pytest --cov` gates. |
| `scripts/env_check.py` | 50 | New script to check for secrets and network access. |


## Process Rules
- Run `python scripts/env_check.py` first; fail fast on ❌.
- Stop immediately once all acceptance boxes tick ✅; do not optimise further.
- Commit messages start with `feat:` or `fix:`; PR title = Sprint 15 result.
- **Task:** This sprint must use the real RSS feed URL and the live RunPod endpoint. Any mocking should be for unit tests only. 