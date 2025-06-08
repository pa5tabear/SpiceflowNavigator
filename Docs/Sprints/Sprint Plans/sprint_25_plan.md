---
number: 25
title: "Fix: Generate and Commit a *Test* Transcript in CI"
goal: "Create a resilient CI job that can run the transcription script, commit a short-clip transcript, and not enter an infinite loop."
focus_minutes: 60
loc_budget: 120 # includes YAML changes
test_pattern: "test_chunk_transcribe"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 85
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 25 · Fix: Generate and Commit a *Test* Transcript in CI

## 1 · Sprint Goal & Alignment
**Goal:** Create a resilient CI job that can run the transcription script, commit a short-clip transcript, and not enter an infinite loop.

**Product Vision Alignment:** 
> This sprint builds the final, critical piece of infrastructure required for a fully automated data pipeline. It makes our CI process not just a *validator*, but a *producer* of real data, while implementing the necessary safeguards to ensure it is robust and reliable.

---

## 2 · Tasks & Acceptance Criteria

### Pre-flight (must pass before Task 1)
- [ ] The risks of a naive CI-producer job (timeouts, permissions, loops) are understood.

### Task Table (Rule of Three)

| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Create "Short-Clip" Mode** | The `scripts/chunk_and_transcribe.py` script must be modified. If the `CI` environment variable is `true`, it should only download and process the first **30 seconds** of the podcast. Otherwise, it should process 10 minutes. |
| 2 | **Create `produce-transcript` CI Job** | The `.github/workflows/ci.yml` file must be updated with a new job that runs the script. This job MUST: <br> - Have `permissions: contents: write`. <br> - Have `timeout-minutes: 20`. <br> - Only run `if: github.actor != 'github-actions[bot]'` on pushes to `main`. |
| 3 | **Commit with `[skip ci]`** | The `produce-transcript` job must, upon success, commit the resulting JSON transcript with a commit message that includes the `[skip ci]` tag to prevent infinite loops. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `scripts/chunk_and_transcribe.py` | Now has a `CI=true` mode for a shorter, 30-second clip. | **Input:** `CI` env var, **Output:** `30s_clip.json` or `10m_clip.json` |
| `.github/workflows/ci.yml` | New `produce-transcript` job with write permissions and anti-loop logic. | N/A |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** The main CI workflow must remain green.
*   **Artifacts Committed:** A new commit must appear on the `main` branch authored by the bot, containing the 30-second transcript.
*   **No Loop:** The bot's commit must **not** trigger a new CI run. 