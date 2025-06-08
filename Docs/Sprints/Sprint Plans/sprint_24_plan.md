---
number: 24
title: "Infra Fix & Feature: Transcribe First 10 Mins of Jenkins Podcast"
goal: "Fix PM tooling, merge the stable client, and deliver a feature that transcribes the first 10 minutes of the latest 'Shift Key' episode."
focus_minutes: 60
loc_budget: 120 # 40 for infra + 80 for feature
test_pattern: "test_runpod_client|test_chunk_transcribe"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 85
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 24 · Infra Fix & Feature: Transcribe First 10 Mins of Jenkins Podcast

## 1 · Sprint Goal & Alignment
**Goal:** Fix PM tooling, merge the stable client, and deliver a feature that transcribes the first 10 minutes of the latest 'Shift Key' episode.

**Product Vision Alignment:** 
> This sprint is a highly efficient combination of stabilizing the development process and delivering immediate business value. It fixes the PM tooling, integrates the proven transcription client, and immediately uses it to process real-world podcast data, which is the core of the MVP.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] CI status of `codex/fix-runpodclient-and-integration-test` manually confirmed as green by Project Owner.
- [ ] Template version is `1.2 (2025-06-09)`.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 0 | **Fix `gh` CLI in CI** | `gh --version` exits 0. `gh run list --limit 1` successfully returns JSON in the CI environment. |
| 1 | **Merge S23 Branch & Confirm Green CI** | The `codex/fix-runpodclient-and-integration-test` branch is merged into `main`. The post-merge CI run on `main` must be green. `pytest -k test_runpod_client` must pass. |
| 2 | **Feature: 10-min Jenkins Clip** | A script, `scripts/chunk_and_transcribe.py`, is created that fetches the latest 'Shift Key' episode, saves the first 10 minutes, transcribes it, and saves the transcript as `latest_shift_key_10m.json`. A test, `test_chunk_transcribe.py`, must pass. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `.github/workflows/ci.yml` | New step to install `gh` CLI. | N/A |
| `scripts/chunk_and_transcribe.py` | New script for the end-to-end feature slice. | **Input:** `None`, **Output:** Creates `latest_shift_key_10m.json` |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The `ci.yml` workflow on `main` must be green post-merge.
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh {{loc_budget}}` must pass.
*   **New Dependencies:** `{{dep_script}}` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under={{coverage_min}} -k "test_runpod_client or test_chunk_transcribe"` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass.

## 🚨 CODEX PROMPT TEMPLATE

(Content from template)

## 🔒 ANTI-FABRICATION ENFORCEMENT

(Content from template)

## 📊 FINAL CHECKLIST

(Content from template)

## 🎉 CELEBRATION CRITERIA

(Content from template) 