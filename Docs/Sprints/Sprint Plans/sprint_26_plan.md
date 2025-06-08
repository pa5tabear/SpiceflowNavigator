---
number: 26
title: "Feature: Generate and Commit First Transcript"
goal: "Prove the transcription script works by having Codex run it and commit the resulting 30-second transcript file to the repository."
focus_minutes: 30
loc_budget: 80
test_pattern: "n/a"
template_version: 1.2 (2025-06-10)
require_golden_path: false
coverage_min: 0
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 26 · Feature: Generate and Commit First Transcript

## 1 · Sprint Goal & Alignment
**Goal:** Prove the transcription script works by having Codex run it and commit the resulting 30-second transcript file to the repository.

**Product Vision Alignment:** 
> This sprint delivers the project's first, tangible data artifact. By manually running the script and committing the output, we take the simplest path to proving the end-to-end transcription process is functional before investing in more complex automation.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] The previous, complex CI automation plan has been abandoned in favor of this simpler, manual approach.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Run Transcription Script** | In its local environment, Codex must run the `scripts/chunk_and_transcribe.py` script, ensuring it is configured for the 30-second clip. |
| 2 | **Commit Transcript File** | Codex must add the generated JSON transcript file (e.g., `transcripts/shift_key/latest_30s.json`) to their git commit. |
| 3 | **Open a Standard PR** | Codex must open a standard Pull Request containing the new transcript file. The PR's CI checks must all pass. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `transcripts/` | New directory to hold transcript artifacts. | N/A |
| `transcripts/shift_key/latest_30s.json` | The first real data artifact committed to the project. | JSON |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The `ci.yml` workflow on the Pull Request must be green.
*   **Artifact in PR:** The Pull Request's file manifest must include the new transcript JSON file.
*   **Artifact on `main`:** After merging, the transcript file must exist on the `main` branch. 