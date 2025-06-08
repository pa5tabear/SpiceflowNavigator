# Sprint 17: Process Hardening & Config Alignment

## 1. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Remediate process gaps from Sprint 16 by creating a mandatory environment check script and aligning the `rss_feeds.yml` configuration with the project standard.

### Product Vision Alignment
> A stable, repeatable process is the bedrock of the product vision. Sprint 16 revealed two critical gaps: a missing pre-flight check and a configuration file that diverged from the established standard. This sprint is on the critical path to ensure the reliability and maintainability of our development loop. Without these fixes, future sprints will be built on an unstable foundation.

---

## 2. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Guard-Rails & Test-First Development
*   **CI-Enforced Validation**: All claims must be verified by CI.
*   **Test-First Mandate**: Failing tests must be written before implementation.
*   **Golden Path Script**: Not applicable for this process-focused sprint.

### Task 1: Create `env_check.py` Script (20 minutes)
*   **Description**: Create a new script at `scripts/env_check.py` that verifies the presence of `RUNPOD_API_KEY` and `RUNPOD_ENDPOINT` environment variables, and confirms basic internet connectivity.
*   **Acceptance Criteria**:
    *   [ ] The script exits with code 0 if all checks pass.
    *   [ ] The script prints a clear error and exits with code 1 if any check fails.
    *   [ ] `pytest -k test_env_check` runs clean.

### Task 2: Standardize and Load Configuration (40 minutes)
*   **Description**: Update `config/rss_feeds.yml` to the structured format. Create a new module `src/spiceflow/config.py` to load and validate this file. Refactor `run_transcription_job.py` to use the new config loader.
*   **Acceptance Criteria**:
    *   [ ] A failing test is created in `tests/unit/test_config.py` that asserts the structured data is loaded correctly.
    *   [ ] `src/spiceflow/config.py` is implemented to make the test pass.
    *   [ ] `run_transcription_job.py` is refactored to use the new loader and runs without error.
    *   [ ] `pytest -k test_config_loader` runs clean.

---

## 3. Post-Sprint Mandates

### 1. Verification
*   **CI Pipeline**: Must be green.
*   **Golden Path**: Not applicable.
*   **Output Validation**: The `run_transcription_job.py` script must still successfully launch a job when secrets are present.

### 2. 🚩 Mandatory Post-Sprint Analysis & Root Cause Investigation (For Codex)
*(After completing the technical tasks, the engineering agent **must** write a detailed analysis in `Docs/Sprints/Codex Engineering Sprint Reviews/sprint_17_reflection.md`)*

---
## 🎯 SUCCESS METRICS (CI-Enforced)

- **All Tests Pass**: `pytest -q` shows green.
- **Ruff Linting**: `ruff --fail-level error` reports clean.
- **Test Coverage**: `pytest --cov` reports >= 80%.
- **CI Pipeline**: GitHub Actions shows all checks passing. 