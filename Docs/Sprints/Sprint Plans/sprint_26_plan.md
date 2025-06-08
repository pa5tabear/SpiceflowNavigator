---
number: 26
title: "CI Workflow: Auto-PR for New Transcripts"
goal: "Create a CI job that, on pushes to main, automatically generates a new PR with the latest 30-second podcast transcript."
focus_minutes: 60
loc_budget: 120 # covers YAML and script changes
test_pattern: "n/a"
template_version: 1.2 (2025-06-10)
require_golden_path: false
coverage_min: 0
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 26 · CI Workflow: Auto-PR for New Transcripts

## 1 · Sprint Goal & Alignment
**Goal:** Create a CI job that, on pushes to main, automatically generates a new PR with the latest 30-second podcast transcript.

**Product Vision Alignment:** 
> This sprint builds a fully automated, robust data pipeline. By creating a pull request instead of pushing to main, we work with our security model, not against it. This creates a safe, auditable process for ingesting real-world data, which is the foundation of our product.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] The failure of the "direct push to main" approach is understood.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Update CI Workflow for Auto-PR** | Modify `.github/workflows/ci.yml`. The new `produce-transcript` job must:<br>- Have `permissions` for `contents: write` and `pull-requests: write`.<br>- Run only on pushes to `main` where the actor is not the bot.<br>- Create a new branch, commit the transcript, and push the branch. |
| 2 | **Open PR via `gh` CLI** | The CI job must use the `gh pr create` command to open a pull request from the new data branch to `main`. The PR should be labeled appropriately (e.g., `automation`, `data`). |
| 3 | **Ensure Script Saves to Correct Path** | The `scripts/chunk_and_transcribe.py` script must save its output to a structured path like `transcripts/shift_key/latest_30s.json` to avoid naming collisions. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `.github/workflows/ci.yml` | The `produce-transcript` job is replaced with a new, more robust version that creates a Pull Request. | N/A |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The `ci.yml` workflow on `main` must remain green.
*   **Pull Request Created:** A new Pull Request, authored by `github-actions[bot]`, must be automatically opened after the sprint is merged.
*   **PR Contains Artifact:** The new PR must contain the `latest_30s.json` transcript file. 