---
number: 20
title: "Lock Whisper integration (proxy mode)"
goal: "Deliver a passing integration test that transcribes tests/fixtures/sample.mp3 through the public proxy and asserts the result contains 'climate'."
focus_minutes: 60
loc_budget: 120
test_pattern: "test_transcribe_proxy"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 20 · Lock Whisper integration (proxy mode)

## 1 · Sprint Goal & Alignment
**Goal:** Deliver a passing integration test that transcribes `tests/fixtures/sample.mp3` through the public proxy and asserts the result contains "climate".

**Product Vision Alignment:** 
> Mixing two RunPod surfaces (Gradio Proxy and the Job API) is causing auth confusion and blocking CI. By choosing the simpler proxy-only approach, we can unblock the project, remove all API key and polling complexity, fix the health-check route, and finally make our Golden-Path test suite pass. This delivers verifiable, end-to-end value.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] Last `ci.yml` run is green.
- [ ] Template version is `1.2 (2025-06-09)`.

### Task Table (Rule of Three)
| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Refactor `runpod_client`** | `src/spiceflow/clients/runpod_client.py` is modified to contain only one public method: `transcribe(file: Path) -> str`. The client should call the Gradio `predict` endpoint with `stream=False`. All API key logic and `status()` polling methods are removed. |
| 2 | **Create Integration Test** | A new integration test, `tests/integration/test_transcribe_proxy.py`, is created. It calls `transcribe()` with `tests/fixtures/sample.mp3` and asserts the returned string contains the word "climate". |
| 3 | **Update Health Checks** | The health-check test is updated to perform a `GET` on the proxy's root URL and assert the status code is less than 500. `env_check.py` is modified to remove any checks for `RUNPOD_API_KEY`. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `src/spiceflow/clients/runpod_client.py` | Refactor to proxy-only. Removed `status()`. | **Input:** `file_path: Path`, **Output:** `transcript: str` |
| `scripts/env_check.py` | Simplification | Removed API key check. |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** ![CI](https://github.com/pa5tabear/SpiceflowNavigator/actions/workflows/ci.yml/badge.svg?branch=sprint-20)
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh 120` must pass.
*   **New Dependencies:** `scripts/ci/check_new_deps.sh` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under=80 -k "test_transcribe_proxy"` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass.

---

## 5. Post-Sprint Mandates & Anti-Fabrication

### ✍️ Codex Self-Reflection & Commit Rules
*   A root cause analysis (RCA) and reflection markdown file **is mandatory**.
*   The reflection must state: **"Option A chosen; Option B deferred (see BACKLOG.md)"**.
*   Commit messages must start with `feat(sprint20):`.

### ✨ Golden Path Script
*   The Golden Path script (`scripts/run_e2e_transcription.py`) is **required** and must pass.

---
_This plan has been aligned with `TEMPLATE.md` version 1.2 (2025-06-09)._ 