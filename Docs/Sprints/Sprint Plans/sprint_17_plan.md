---
number: 17
title: "Prove Live End-to-End Job Submission"
goal: "Execute a script that submits a real transcription job and then immediately verifies its 'QUEUED' or 'IN_PROGRESS' status via the API."
focus_minutes: 60
loc_budget: 150
test_pattern: "test_e2e_submission_and_status_check"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint {{number}} · {{title}}

## 1 · Sprint Goal & Alignment
**Goal:** {{goal}}

**Product Vision Alignment:** 
> We currently lack evidence that our core transcription workflow functions. This sprint is the highest possible priority. It closes the loop by not only submitting a job but immediately verifying its status, providing the first piece of concrete proof that the system works end-to-end. This is the bedrock upon which all future features will be built.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] `python scripts/env_check.py` ✅ (Note: This script must be created in Task 1)
- [ ] Last `ci.yml` run is green.
- [ ] Template version is `{{template_version}}`.

### Task Table (Rule of Three)
| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Create `env_check.py` & `config.py`** | Create `scripts/env_check.py` to validate secrets. Create `src/spiceflow/config.py` to load a standardized, structured `config/rss_feeds.yml`. |
| 2 | **Create `job_status_checker.py`** | Create a new script that takes a `job_id` and uses the `runpod.get_job()` function to fetch and print the job's status. |
| 3 | **Create Golden Path Script** | Create `scripts/run_e2e_transcription.py` that a) runs env check, b) calls `run_transcription_job.py` to get a job_id, and c) immediately calls `job_status_checker.py` with that id, asserting the status is not 'FAILED'. |

---

## 3 · New or Changed Interfaces
<!-- Append new rows; do not edit previous sprint entries -->
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `scripts/env_check.py` | New script. | **Input:** Environment variables. **Output:** Exits 0 on success, 1 on failure. |
| `src/spiceflow/config.py`| New module. | **Input:** `config/rss_feeds.yml`. **Output:** Validated config object. |
| `scripts/job_status_checker.py`| New script. | **Input:** `job_id` (string). **Output:** Job status (string) to stdout. |
| `scripts/run_e2e_transcription.py`| New script. | **Input:** None. **Output:** Final job status to stdout. |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** ![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg?branch=sprint-{{number}})
*   **Golden Path Execution:** The new `scripts/run_e2e_transcription.py` must be the final, successful step in the CI pipeline.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under={{coverage_min}} -k {{test_pattern}}` must pass.

---

## 5. Post-Sprint Mandates & Anti-Fabrication

### 🔒 Guard-Rails
*   All rules in [`Docs/PROCESS/guardrails.md`](../PROCESS/guardrails.md) apply by reference.

### ✍️ Codex Self-Reflection & Commit Rules
*   A root cause analysis (RCA) and reflection markdown file **is mandatory**.
*   Commit messages must start with `feat(sprint{{number}}):` or `fix(sprint{{number}}):`.

### ✨ Golden Path Script
{% if require_golden_path %}
*   The Golden Path script (`scripts/run_e2e_transcription.py`) is **required** and must pass.
{% else %}
*   The Golden Path script is **not required** for this sprint.
{% endif %} 