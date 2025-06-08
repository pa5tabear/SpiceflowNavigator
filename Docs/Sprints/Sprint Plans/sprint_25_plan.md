---
number: 25
title: "Fix: Generate and Commit Live Transcript"
goal: "Execute the existing `chunk_and_transcribe.py` script in CI, and commit the resulting transcript and analysis files to the repository."
focus_minutes: 45
loc_budget: 50
test_pattern: "n/a"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 0
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 25 · Fix: Generate and Commit Live Transcript

## 1 · Sprint Goal & Alignment
**Goal:** Execute the existing `chunk_and_transcribe.py` script in CI, and commit the resulting transcript and analysis files to the repository.

**Product Vision Alignment:** 
> This sprint corrects a major process failure from Sprint 24. It will produce the *first real artifact* of the project—a live, transcribed podcast clip. This is the absolute minimum requirement for declaring the end-to-end pipeline functional.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] Sprint 24 has been reviewed, and its failure to produce an artifact is understood.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Update CI Workflow** | The `.github/workflows/ci.yml` file must be modified to add a new job that runs **only on merges to `main`**. |
| 2 | **Execute Script & Commit** | The new CI job must execute `scripts/chunk_and_transcribe.py`. After the script succeeds, the job must use `git` to commit the newly created `latest_shift_key_10m.json` and any files in the `reports/` directory back to the `main` branch. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `.github/workflows/ci.yml` | New job to run the transcription script and commit the output artifacts. | N/A |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The main CI workflow must remain green.
*   **Artifacts Committed:** A new commit must appear on the `main` branch authored by the "github-actions" bot, containing the `latest_shift_key_10m.json` file. 