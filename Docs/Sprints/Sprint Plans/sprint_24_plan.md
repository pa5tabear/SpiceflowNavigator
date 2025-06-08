---
number: 24
title: "Workflow: Transcribe First 10 Mins of Latest Podcast"
goal: "Implement a workflow that fetches the latest episode from a live RSS feed, extracts the first 10 minutes, and transcribes it."
focus_minutes: 120
loc_budget: 250
test_pattern: "test_real_podcast_workflow"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 85
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 24 · Workflow: Transcribe First 10 Mins of Latest Podcast

## 1 · Sprint Goal & Alignment
**Goal:** Implement a workflow that fetches the latest episode from a live RSS feed, extracts the first 10 minutes, and transcribes it.

**Product Vision Alignment:** 
> This is a major step towards the MVP. It moves us from testing with sample files to processing real-world data from our target sources. This task proves the viability of the entire end-to-end "Feed -> Transcribe" loop.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] `python scripts/env_check.py` ✅
- [ ] Last `ci.yml` run for Sprint 23 is **green**. This is a hard requirement.
- [ ] Template version is `1.2 (2025-06-09)`.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Fetch Latest Episode Audio** | A utility must be created that takes a feed URL, parses it, and returns the audio URL of the most recent episode. The existing `RSSParser` should be used. |
| 2 | **Download & Clip First 10 Mins** | A utility must be created to download an audio file from a URL and save only the first 10 minutes to a local temporary file. This must be implemented **without new dependencies**. |
| 3 | **Update Workflow & Test** | The `WorkflowManager` must be updated to use the new utilities to fetch, clip, and then transcribe the 10-minute audio segment from the live "Shift Key" RSS feed. The test (`-k {{test_pattern}}`) must orchestrate this and assert that a non-empty transcript is created. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `src/spiceflow/utils/rss.py` | New module to contain RSS parsing and fetching logic. | **Input:** `str` (feed_url), **Output:** `str` (audio_url) |
| `src/spiceflow/utils/audio.py` | New module for audio processing (downloading, clipping). | **Input:** `str` (audio_url), **Output:** `Path` (local_file_path) |
| `src/spiceflow/workflow.py` | `WorkflowManager` updated to use the new real-data-sourcing utilities. | **Input:** `str` (feed_url), **Output:** `None` (side effect: writes files) |

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