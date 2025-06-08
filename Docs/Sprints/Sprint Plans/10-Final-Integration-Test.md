# Sprint 10: Final Integration Test

## 1. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Execute the live integration test to get a definitive PASS/FAIL result for our core feature: podcast transcription.

### Product Vision Alignment
> After a major pivot in Sprint 9, the project is now correctly aligned with the target Gradio API. All environment and dependency issues have been resolved. This sprint is the final validation step and represents the "moment of truth" for the entire proof-of-concept. Executing the existing integration test is the single most important task on the critical path to declaring the MVP viable.

---

## 2. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Guard-Rails & Test-First Development
*   **CI-Enforced Validation**: The result of this sprint will be a CI-validated test run.
*   **Test-First Mandate**: The test for this sprint's task has already been created in Sprint 9, adhering to this principle.
*   **Golden Path Script**: Running `pytest` on the integration test functions as our golden path script for this sprint.

### Task 1: Execute the Integration Test (60 minutes)
*   **Description**: Run the integration test suite, specifically targeting `tests/integration/test_runpod_transcribe.py`.
*   **Acceptance Criteria**:
    *   [ ] The `pytest` command is executed on the `tests/integration/` directory.
    *   [ ] The test `test_transcribe_audio_file` within the suite must pass.
    *   [ ] A "pass" is defined as the test completing without error and receiving a non-empty string from the API.

---

## 3. Post-Sprint Mandates

### 1. Verification
*   **CI Pipeline**: The test run must be green.

### 2. 🚩 Mandatory Post-Sprint Analysis & Root Cause Investigation (For Codex)
*(After completing the technical tasks, you **must** write a detailed analysis in `Docs/Sprints/Codex Engineering Sprint Reviews/sprint_10_reflection.md`.)*

**Structure for your Analysis:**

**Part 1: Executive Summary of Action**
> Describe the final status of the test run (`PASS` or `FAIL`). If the test passed, **include the full transcription output** in your report.

**Part 2: Root Cause Analysis (RCA) of Failures & Challenges**
> If the test failed, provide a full RCA.
> *   **Observation:** What was the exact, observable error message or unexpected behavior? Provide logs or output.
> *   **Hypothesis:** What is your primary hypothesis for the root cause of this failure?
> *   **Failed Workarounds:** Describe any workarounds you attempted.

**Part 3: Final Analysis**
> *   **Lessons Learned:** Based on this entire season of sprints, what are the biggest lessons learned about integrating with a new, third-party AI service?
> *   **Process Recommendations:** What are the key recommendations for improving our process for future projects of this nature?

---

# 📋 PRE-SPRINT CHECKLIST
- [X] CI pipeline passing (mvp-sanity-check)
- [X] All guard-rails operational
- [X] No fabrication detected in previous sprint
- [X] Transcription environment validated (if applicable)

## 🛡️ GUARD-RAILS STATUS

### Guard-Rail 1: CI-Enforced Validation ✅
**Status**: Active - All claims verified by GitHub Actions, not chat

## 🧪 TEST-FIRST DEVELOPMENT

### Step 1: Create Failing Tests (Required)
The test for this sprint was created in Sprint 9 and is located at `tests/integration/test_runpod_transcribe.py`. No new tests are required.

### Step 2: Implementation (Only After Tests Written)
No new implementation is required. This sprint is purely for execution.

## 🛠️ SPRINT TASKS (60 MINUTES)

### Task 1: Execute Live Integration Test (60 minutes)

**Execute the test.**

**Implementation Steps:**
1. **Ensure Environment is Set**: Confirm the `RUNPOD_ENDPOINT` secret/variable is available in the execution environment.
2. **Run Pytest**: Execute `pytest tests/integration/test_runpod_transcribe.py`.
3. **Capture Output**: Ensure the output and status of the test run are logged for the reflection.

**Acceptance Criteria:**
- [ ] Test suite is executed.
- [ ] The output (pass or fail, with logs) is captured for analysis.

## 🎯 SUCCESS METRICS (CI-Enforced)

- **All Tests Pass**: `pytest -q` shows green for `test_runpod_transcribe.py`.
- **Honest Documentation**: The final result (pass/fail and output) is documented in the engineering reflection. 