---
number: 22
title: "Golden Path: Live RSS to Transcript"
goal: "Get a green CI run by successfully transcribing the latest episode from a live RSS feed."
focus_minutes: 90
loc_budget: 150
test_pattern: "test_golden_path"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 75 # Lowering slightly due to complexity of mocking network calls
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 22 · Golden Path: Live RSS to Transcript

## 1 · Sprint Goal & Alignment
**Goal:** Get a green CI run by successfully transcribing the latest episode from a live RSS feed.

**Product Vision Alignment:** 
> This sprint leapfrogs the simple test fix and aims for the ultimate proof of value: demonstrating a full, live workflow. By successfully parsing a real RSS feed and transcribing its latest episode, we will unblock the project and deliver the first tangible piece of the "Daily Briefing" MVP.

---

## 2 · Tasks & Acceptance Criteria
| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Create Golden Path Test** | A new integration test, `tests/integration/test_golden_path.py`, will be created. It must not use mocks for `RSSParser` or `RunPodClient`. |
| 2 | **Implement Live Workflow** | The test will use the `RSSParser` to fetch and parse the "Shift Key" feed (`https://feeds.acast.com/public/shows/65bac3af03341c00164bf93b`). It will then extract the audio URL for the most recent episode. |
| 3 | **Assert Real Transcript** | The test will pass the extracted audio URL to the `RunPodClient.transcribe()` method. The test will pass if the method returns a string transcript that is longer than 100 characters, proving a real, non-trivial transcription occurred. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `tests/integration/test_golden_path.py` | New Test | A full-stack integration test that calls the live RSS feed and the live transcription service. |
| `src/spiceflow/clients/runpod_client.py` | Minor fix | The `transcribe` method may need to accept a URL string directly, not just a `Path` object. |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)
*   **CI Badge:** ![CI](https://github.com/pa5tabear/SpiceflowNavigator/actions/workflows/ci.yml/badge.svg?branch=sprint-22)
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under=75 -k "test_golden_path"` must pass.
*   All other metrics from the `TEMPLATE.md` apply.

---

## 5. Post-Sprint Mandates & Anti-Fabrication
*   Commit messages must start with `feat(sprint22):`.
*   All other rules from the `TEMPLATE.md` apply. 