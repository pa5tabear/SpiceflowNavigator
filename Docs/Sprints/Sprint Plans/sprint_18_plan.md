# Sprint 18 – Prove Live End-to-End Job Submission

---
number: 18
title: "Prove Live End-to-End Job Submission"
goal: "Execute a script that submits a real transcription job and then immediately verifies its 'QUEUED' or 'IN_PROGRESS' status via the API."
focus_minutes: 60
loc_budget: 150
test_pattern: "test_e2e_submission_and_status_check"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 80
dep_script: "scripts/ci/check_new_deps.sh"
---

# Sprint 18 · Prove Live End-to-End Job Submission

## 1 · Sprint Goal & Alignment
**Goal:** Execute a script that submits a real transcription job and then immediately verifies its 'QUEUED' or 'IN_PROGRESS' status via the API.

**Product Vision Alignment:** 
> After hardening our process in Sprint 17, we now return to the critical path. We still lack evidence that our core transcription workflow functions. This sprint will provide that proof by not only submitting a job but immediately verifying its status. This is the bedrock upon which all future features will be built.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] `python scripts/env_check.py` ✅
- [ ] Last `ci.yml` run is green.
- [ ] Template version is `1.2 (2025-06-09)`.

### Task Table (Rule of Three)
| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Create `job_status_checker.py`** | A new script is created that takes a `job_id` and uses `runpod.get_job()` to fetch and print the job's status to stdout. |
| 2 | **Create Golden Path Script** | Create `scripts/run_e2e_transcription.py` that a) runs env check, b) calls `run_transcription_job.py` to get a job_id, and c) immediately calls `job_status_checker.py` with that id. |
| 3 | **Add Integration Test** | A new integration test in `tests/integration/` executes the golden path script and asserts the final output is a valid status string (e.g., 'IN_PROGRESS', 'COMPLETED'). This test will be skipped if secrets are not present. |

---

## 3 · New or Changed Interfaces
<!-- Append new rows; do not edit previous sprint entries -->
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `scripts/job_status_checker.py`| New script. | **Input:** `job_id` (string). **Output:** Job status (string) to stdout. |
| `scripts/run_e2e_transcription.py`| New script. | **Input:** None. **Output:** Final job status to stdout. |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** ![CI](https://github.com/pa5tabear/SpiceflowNavigator/actions/workflows/ci.yml/badge.svg?branch=sprint-18)
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh 150` must pass.
*   **New Dependencies:** `scripts/ci/check_new_deps.sh` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under=80 -k test_e2e_submission_and_status_check` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass.

---

## 5. Post-Sprint Mandates & Anti-Fabrication

### 🔒 Guard-Rails
*   All rules in [`Docs/PROCESS/guardrails.md`](../../PROCESS/guardrails.md) apply by reference.

### ✍️ Codex Self-Reflection & Commit Rules
*   A root cause analysis (RCA) and reflection markdown file **is mandatory**.
*   Commit messages must start with `feat(sprint18):` or `fix(sprint18):`.

### ✨ Golden Path Script
{% if require_golden_path %}
*   The Golden Path script (`scripts/run_e2e_transcription.py`) is **required** and must pass.
{% else %}
*   The Golden Path script is **not required** for this sprint.
{% endif %} 