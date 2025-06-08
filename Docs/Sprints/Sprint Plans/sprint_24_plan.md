---
number: 24
title: "Workflow: Chunk Long Audio & Transcribe in Parallel"
goal: "Enhance the workflow to process long audio files by splitting them into 10-minute chunks and transcribing each chunk."
focus_minutes: 90
loc_budget: 200
test_pattern: "test_workflow_chunking"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 85
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 24 · Workflow: Chunk Long Audio & Transcribe in Parallel

## 1 · Sprint Goal & Alignment
**Goal:** Enhance the workflow to process long audio files by splitting them into 10-minute chunks and transcribing each chunk.

**Product Vision Alignment:** 
> This is a direct step towards the MVP's core "10-min Chunk & Analyze" workflow. It enables the system to handle real-world, hour-long podcasts, which is essential for the product to be useful. This sprint builds directly on the stable transcription client delivered in Sprint 23.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] `python scripts/env_check.py` ✅
- [ ] Last `ci.yml` run for Sprint 23 is **green**. This is a hard requirement.
- [ ] Template version is `1.2 (2025-06-09)`.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Implement Audio Chunking Utility** | Create a utility that accepts an audio file path and splits it into multiple 10-minute `.wav` chunks in a temporary directory. This must be implemented **without adding new dependencies** to `requirements.txt`. |
| 2 | **Update WorkflowManager** | The `WorkflowManager` must be updated to use the chunking utility. It should iterate through each chunk, pass it to the `RunPodClient` for transcription, and save the resulting transcript. |
| 3 | **Create New Workflow Test** | A new test file matching `pytest -k {{test_pattern}}` must be created. This test will use a fixture audio file longer than 10 minutes (can be generated via script) and assert that the correct number of transcript chunks are created. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `src/spiceflow/utils/audio.py` | New module for audio processing. | **Input:** `Path`, `int` (chunk_duration_ms), **Output:** `List[Path]` |
| `src/spiceflow/workflow.py` | `WorkflowManager` updated to handle chunking and aggregate results. | **Input:** `str` (feed_url), **Output:** `None` (side effect: writes files) |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The `ci.yml` workflow must pass on the PR branch.
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh {{loc_budget}}` must pass.
*   **New Dependencies:** `{{dep_script}}` must pass (no new deps allowed).
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