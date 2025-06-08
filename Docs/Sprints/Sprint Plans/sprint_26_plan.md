---
number: 26
title: "EMERGENCY FIX (ATTEMPT 3): Correctly Commit Transcript from CI"
goal: "Diagnose and fix the CI workflow to ensure it can successfully commit the generated transcript file back to the `main` branch."
focus_minutes: 60
loc_budget: 75
test_pattern: "n/a"
template_version: 1.2 (2025-06-10)
require_golden_path: false
coverage_min: 0
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 26 · EMERGENCY FIX (ATTEMPT 3): Correctly Commit Transcript from CI

## 1 · Sprint Goal & Alignment
**Goal:** Diagnose and fix the CI workflow to ensure it can successfully commit the generated transcript file back to the `main` branch.

**Product Vision Alignment:** 
> This is a **project-critical infrastructure fix**. The project is blocked and cannot move forward until we have a reliable, automated pipeline that produces our core data artifacts. This is our third attempt at this task, and its success is the only priority.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] The repeated failure of the `produce-transcript` CI job has been acknowledged.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Diagnose Push Failure** | Investigate the logs from the `produce-transcript` job in Sprint 25 to find the root cause of the `git push` failure. The cause is likely related to either git credentials, user configuration, or branch protection rules. |
| 2 | **Implement & Test Fix** | Modify the `.github/workflows/ci.yml` file to fix the push issue. The fix will likely involve correctly configuring the `github-actions` bot user and ensuring it has the necessary permissions. |
| 3 | **Verify the Bot Commit** | A new PR containing the fix must be created. After merging, a new commit authored by `github-actions[bot]` **must** appear on the `main` branch, and it must contain the `30s_clip.json` file. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `.github/workflows/ci.yml` | The `produce-transcript` job will be modified to correctly authenticate and push a commit. | N/A |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The `ci.yml` workflow on `main` must remain green.
*   **Bot Commit Exists:** A `git log` on the `main` branch after the sprint MUST show a commit authored by `github-actions[bot]`. 