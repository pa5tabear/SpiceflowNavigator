---
number: 22
title: "Surgical Fix: Stabilize Whisper Client"
goal: "Get a green CI run by implementing the verbatim patches from the PR #20 code review."
focus_minutes: 60
loc_budget: 40
test_pattern: "test_proxy_transcription"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 22 · Surgical Fix: Stabilize Whisper Client

## 1 · Sprint Goal & Alignment
**Goal:** Get a green CI run by implementing the verbatim patches from the PR #20 code review.

**Product Vision Alignment:** 
> A detailed code review has provided a precise, line-by-line fix for all known bugs in our client and tests. This sprint implements those fixes exactly as specified to eliminate all known failure points, unblock the CI pipeline, and finally stabilize our core transcription service.

---

## 2 · Tasks & Acceptance Criteria
| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Patch `runpod_client.py`** | Modify the `transcribe` method to exactly match the provided `diff`. It must include the health-check, timeout, `stream=False` default, and keyword arguments for model/task. The `status()` method must remain deleted. |
| 2 | **Patch `test_transcribe_proxy.py`** | Modify the integration test to exactly match the provided `diff`. It must include the `@pytest.mark.skipif` decorator and the health-check assertion. |
| 3 | **Patch `env_check.py`** | Modify the script to exactly match the provided `diff`. It must remove the API key check and replace it with a health check against the proxy root URL. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `src/spiceflow/clients/runpod_client.py` | Patched | Added health check, timeout, and kwargs. |
| `tests/integration/test_transcribe_proxy.py` | Patched | Added skip-logic and health check. |
| `scripts/env_check.py` | Patched | Replaced API key check with proxy health check. |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)
*   **CI Badge:** ![CI](https://github.com/pa5tabear/SpiceflowNavigator/actions/workflows/ci.yml/badge.svg?branch=sprint-22)
*   The `test_proxy_transcription` test must pass.
*   All other metrics from `TEMPLATE.md` apply.

---

## 5. Post-Sprint Mandates & Anti-Fabrication
*   Commit message must be `fix(sprint22): stabilize whisper client per review`.
*   All other rules from the `TEMPLATE.md` apply. 