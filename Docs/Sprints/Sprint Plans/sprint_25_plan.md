---
number: 25
title: "Feature: Generate Daily Briefing Markdown Report"
goal: "Create a user-facing Markdown report that summarizes the latest transcribed podcast episode."
focus_minutes: 60
loc_budget: 150
test_pattern: "test_report_generator"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 85
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 25 · Feature: Generate Daily Briefing Markdown Report

## 1 · Sprint Goal & Alignment
**Goal:** Create a user-facing Markdown report that summarizes the latest transcribed podcast episode.

**Product Vision Alignment:** 
> This sprint delivers the first concrete, user-facing artifact envisioned in the "Daily Briefing" concept. It takes the raw data generated in Sprint 24 and transforms it into actionable intelligence for the user, closing the loop on the core value proposition.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] Sprint 24 has been successfully reviewed and CI is green on `main`.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Create Report Generator Module** | A new module `src/spiceflow/reporting.py` is created. It will contain a function that reads the latest transcript JSON and generates a formatted Markdown string. |
| 2 | **Define Markdown Report Structure** | The generated Markdown report must contain: a title, the episode's publication date, a link to the original audio, the full 10-minute transcript, and the summary from the `StrategicAnalyzer`. |
| 3 | **Update Workflow & Add Test** | The main workflow script (`scripts/chunk_and_transcribe.py`) is updated to call the new report generator. A new test (`-k {{test_pattern}}`) asserts that the Markdown file is created and contains all the required sections. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `src/spiceflow/reporting.py` | New module for generating user-facing reports. | **Input:** `Path` (to transcript json), **Output:** `str` (markdown) |
| `scripts/chunk_and_transcribe.py` | Updated to integrate the reporting step. | N/A |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The `ci.yml` workflow on the PR branch must be green.
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh {{loc_budget}}` must pass.
*   **New Dependencies:** `{{dep_script}}` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under={{coverage_min}} -k {{test_pattern}}` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass. 