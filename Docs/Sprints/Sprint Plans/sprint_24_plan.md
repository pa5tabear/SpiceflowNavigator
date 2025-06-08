---
number: 24
title: "Infra: Repair PM Tooling & Merge S23 Fix"
goal: "Repair the PM's command-line tooling and merge the validated fix for the RunPod client."
focus_minutes: 60
loc_budget: 50
test_pattern: "test_runpod_client"
template_version: 1.2 (2025-06-09)
require_golden_path: false
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 24 · Infra: Repair PM Tooling & Merge S23 Fix

## 1 · Sprint Goal & Alignment
**Goal:** Repair the PM's command-line tooling and merge the validated fix for the RunPod client.

**Product Vision Alignment:** 
> This is a critical infrastructure sprint. A functional PM/QA tooling environment is essential for maintaining velocity and ensuring quality. This sprint unblocks the PM and allows the valuable work from Sprint 23 to be safely integrated.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] CI status of `codex/fix-runpodclient-and-integration-test` manually confirmed as green by Project Owner.
- [ ] Template version is `1.2 (2025-06-09)`.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 0 | **Repair `gh` & `jq` CLI** | `gh --version` must execute successfully and return a 2.x version. `jq --version` must also execute successfully. |
| 1 | **Merge Sprint 23 Branch** | The `codex/fix-runpodclient-and-integration-test` branch must be merged into `main`. |
| 2 | **Confirm Post-Merge CI is Green** | The `ci.yml` workflow on the `main` branch must be green after the merge, validating that the fix works as expected. The test run must pass `pytest -k {{test_pattern}}`.|

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| (various) | Merges the changes from Sprint 23. Refer to the S23 review. | (various) |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The `ci.yml` workflow on `main` must be green post-merge.
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh {{loc_budget}}` must pass.
*   **New Dependencies:** `{{dep_script}}` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under={{coverage_min}} -k {{test_pattern}}` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass.

## 🚨 CODEX PROMPT TEMPLATE

(Content from template)

## 🔒 ANTI-FABRICATION ENFORCEMENT

(Content from template)

## 📊 FINAL CHECKLIST

(Content from template)

## 🎉 CELEBRATION CRITERIA

(Content from template) 