---
number: 22
title: "Fix Faulty Integration Test"
goal: "Get a green CI run by fixing the assertion in `test_transcribe_proxy.py`."
focus_minutes: 30
loc_budget: 20
test_pattern: "test_transcribe_proxy"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 22 · Fix Faulty Integration Test

## 1 · Sprint Goal & Alignment
**Goal:** Get a green CI run by fixing the assertion in `test_transcribe_proxy.py`.

**Product Vision Alignment:** 
> The core application logic is now correct, but a faulty test is blocking our CI and preventing us from moving forward. This sprint unblocks the entire project by fixing this single failing test, which will finally provide verifiable proof of our end-to-end transcription capability.

---

## 2 · Tasks & Acceptance Criteria
| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **Fix Test Assertion** | Modify `tests/integration/test_transcribe_proxy.py`. Instead of creating a silent audio file, the test **must** use the real audio file located at `tests/fixtures/sample.mp3`. |
| 2 | **Update Test Assertion** | The assertion in the test must be changed to check if the transcription result contains the word "climate", which is known to be in the `sample.mp3` fixture. `assert "climate" in result.lower()` |
| 3 | **Achieve Green CI** | The final commit **must** result in a fully successful CI run on the `main` branch. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `tests/integration/test_transcribe_proxy.py` | Test fix | Changed the audio source from a generated silent file to a real fixture (`sample.mp3`) and updated the assertion to match the fixture's content. |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)
*   **CI Badge:** ![CI](https://github.com/pa5tabear/SpiceflowNavigator/actions/workflows/ci.yml/badge.svg?branch=sprint-22)
*   All other metrics from the `TEMPLATE.md` apply.

---

## 5. Post-Sprint Mandates & Anti-Fabrication
*   All rules from the `TEMPLATE.md` apply.
*   Commit messages must start with `fix(sprint22):`. 