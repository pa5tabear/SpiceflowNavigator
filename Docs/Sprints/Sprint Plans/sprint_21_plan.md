---
number: 21
title: "RETRY: Lock Whisper integration (proxy mode)"
goal: "Fix the CI by correctly implementing the proxy-only architecture defined in Sprint 20."
focus_minutes: 60
loc_budget: 100
test_pattern: "test_transcribe_proxy"
template_version: 1.2 (2025-06-09)
require_golden_path: true
coverage_min: 80
dep_script: scripts/ci/check_new_deps.sh
---

# Sprint 21 · RETRY: Lock Whisper integration (proxy mode)

## 1 · Sprint Goal & Alignment
**Goal:** Fix the CI by correctly implementing the proxy-only architecture defined in Sprint 20.

**Product Vision Alignment:** 
> Sprint 20 failed because the required code deletions and refactoring were not performed. The project remains **BLOCKED** by a failing CI pipeline. This sprint is a second attempt to complete the crucial pivot to a proxy-only architecture, which will unblock all future development.

---

## 2 · Tasks & Acceptance Criteria

### 🚨 CRITICAL NOTE FOR CODEX 🚨
> The previous sprint failed because tasks #1 and #3 were not completed. You MUST delete the legacy code as specified.

### Task Table (Rule of Three)
| # | Task | Key Acceptance Criteria (Enforced by CI) |
|---|---|---|
| 1 | **DELETE Legacy Code** | The `status()` method and the `requests` import **MUST BE DELETED** from `src/spiceflow/clients/runpod_client.py`. The file should only contain the `__init__` and `transcribe` methods. |
| 2 | **Fix Health Check** | The check for `RUNPOD_API_KEY` **MUST BE DELETED** from `scripts/env_check.py`. |
| 3 | **Validate with Test** | The integration test `tests/integration/test_transcribe_proxy.py` must pass, proving the refactored client works. |

---

## 3 · New or Changed Interfaces
| Interface / Component | Change Description | Contract (Inputs / Outputs) |
|---|---|---|
| `src/spiceflow/clients/runpod_client.py` | **Deletion**: Removed `status()` method and `requests` dependency. | **Input:** `file_path: Path`, **Output:** `transcript: str` |
| `scripts/env_check.py` | **Deletion**: Removed API key check. | No change to inputs/outputs. |

---

## 4 · 🎯 SUCCESS METRICS (CI-ENFORCED)

*   **CI Badge:** ![CI](https://github.com/pa5tabear/SpiceflowNavigator/actions/workflows/ci.yml/badge.svg?branch=sprint-21)
*   **LOC Budget:** `scripts/ci/check_loc_budget.sh 100` must pass.
*   **New Dependencies:** `scripts/ci/check_new_deps.sh` must pass.
*   **Test Execution & Coverage:** `pytest --cov=src --cov-fail-under=80 -k "test_transcribe_proxy"` must pass.
*   **Linter:** `ruff format --check` and `ruff --fail-level error` must pass.

---

## 5. Post-Sprint Mandates & Anti-Fabrication
*   All other rules from the `TEMPLATE.md` apply.
*   Commit messages must start with `fix(sprint21):`.

---
_This plan has been aligned with `TEMPLATE.md` version 1.2 (2025-06-09)._ 