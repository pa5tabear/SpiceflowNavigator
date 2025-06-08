---
number: 19
title: "Fix the Golden Path"
goal: "Fix the `ImportError` in `job_status_checker.py` and get a green CI run on the `main` branch."
focus_minutes: 45
loc_budget: 100
test_pattern: "test_job_status_checker"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 19 · Fix the Golden Path

## 1 · Sprint Goal & Alignment
**Goal:** Fix the `ImportError` in `job_status_checker.py` and get a green CI run on the `main` branch.

**Product Vision Alignment:** 
> The entire project is blocked until we have a reliable, verifiable, end-to-end test that proves we can submit a job and check its status. This bug fix is the final step to unblock all future work on the transcription pipeline.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] `python scripts/env_check.py` ✅
- [ ] Last `ci.yml` run is green.
- [ ] Template version is `1.2 (2025-06-09)`.

### Task Table (Rule of Three)
*Propose at most 3 tasks. If more are needed, the sprint scope is too large.*

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Fix `ImportError`** | Modify `scripts/job_status_checker.py` to remove the legacy `runpod` calls and use only the correct `gradio_client` library for checking job status. |
| 2 | **Validate with Tests** | Ensure the existing test `tests/unit/test_job_status_checker.py` passes after the fix. |
| 3 | **Achieve Green CI** | The final commit must result in a fully successful CI run on the `main` branch. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `scripts/job_status_checker.py` | Bug fix: Replaced `runpod` with `gradio_client` | **Input:** `job_id` (str), **Output:** `status` (str) |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** ![CI](https://github.com/pa5tabear/SpiceflowNavigator/actions/workflows/ci.yml/badge.svg?branch=sprint-19)
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh 100` must pass.
*   **New Dependencies:** `scripts/ci/check_new_deps.sh` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under=80 -k "test_job_status_checker"` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass.

---

## 5. Post-Sprint Mandates & Anti-Fabrication

### 🔒 Guard-Rails
*   All rules in [`Docs/PROCESS/guardrails.md`](../../PROCESS/guardrails.md) apply by reference.

### ✍️ Codex Self-Reflection & Commit Rules
*   A root cause analysis (RCA) and reflection markdown file **is mandatory**.
*   Commit messages must start with `fix(sprint19):`.

### ✨ Golden Path Script
*   The Golden Path script (`scripts/run_e2e_transcription.py`) is **required** and must pass.

---
_This plan has been aligned with `TEMPLATE.md` version 1.2 (2025-06-09)._ 