---
number: 23
title: "Surgical Fix of RunPod Client and Integration Test"
goal: "Achieve a stable, green CI run by fixing the RunPodClient and implementing a valid, focused integration test."
focus_minutes: 60
loc_budget: 100
test_pattern: "test_runpod_client"
template_version: 1.2 (2025-06-09)
require_golden_path: false
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 23 · Surgical Fix of RunPod Client and Integration Test

## 1 · Sprint Goal & Alignment
**Goal:** Achieve a stable, green CI run by fixing the RunPodClient and implementing a valid, focused integration test.

**Product Vision Alignment:** 
> This sprint is critical because a stable, green CI is the mandatory prerequisite for any new feature development, including the "10-min Chunk & Analyze" workflow which is the core of the MVP. We are currently blocked until this is resolved.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] `python scripts/env_check.py` ✅
- [ ] Last `ci.yml` run is green. (Known Failure: This is what the sprint will fix)
- [ ] Template version is `1.2 (2025-06-09)`.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Fix `RunPodClient` Timeout** | The `gradio_client.Client` must be initialized with a `timeout` of at least 300 seconds. The `requests.get` call inside the `transcribe` method must be removed. |
| 2 | **Replace Flawed Integration Test** | `tests/integration/test_transcribe_proxy.py` must be deleted. A new test `tests/integration/test_runpod_client.py` must be created that runs a real transcription against the live proxy using a non-silent audio fixture and asserts the result is a non-empty string. It must pass when `pytest -k {{test_pattern}}` is run. |
| 3 | **Create Test Audio Fixture** | A script `scripts/generate_test_audio.py` must be created to generate a non-silent `.wav` file. This file must be saved to `tests/fixtures/test_audio.wav` and used in the new integration test. **The audio file itself must NOT be committed to git.** |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `src/spiceflow/clients/runpod_client.py` | `__init__` now sets a timeout on the `Client`. `transcribe` method signature simplified. | **Input:** `str | Path`, **Output:** `str` |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The `ci.yml` workflow must pass on the PR branch.
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh {{loc_budget}}` must pass.
*   **New Dependencies:** `{{dep_script}}` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under={{coverage_min}} -k {{test_pattern}}` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass.

---
## 5. Post-Sprint Mandates & Anti-Fabrication

(Content from template)

## 🚨 CODEX PROMPT TEMPLATE

(Content from template)

## 🔒 ANTI-FABRICATION ENFORCEMENT

(Content from template)

## 📊 FINAL CHECKLIST

(Content from template)

## 🎉 CELEBRATION CRITERIA

(Content from template) 