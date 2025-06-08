# Sprint 11: Command-Line Interface (CLI)

## 1. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Create a simple, user-facing command-line interface (CLI) to interact with the transcription service, moving the project from a library to a usable tool.

### Product Vision Alignment
> The core transcription functionality is now proven. To deliver value, users must be able to interact with it. Building a CLI is the first and most direct way to expose our working `RunPodClient`. This moves the project into an "alpha" stage and provides a concrete tool that can be used and tested for the full end-to-end user workflow.

---

## 2. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Guard-Rails & Test-First Development
*   **Test-First Mandate**: A failing test must be written to validate the CLI's behavior before implementation.

### Task 1: Create a Test for the CLI (20 minutes)
*   **Description**: Create a unit test to verify the CLI script works as expected without making a live network call.
*   **Acceptance Criteria**:
    *   [ ] A new test file is created at `tests/test_cli.py`.
    *   [ ] The initial test should assert `False` to prove it fails before implementation.
    *   [ ] The final test must use `unittest.mock.patch` to mock the `RunPodClient`.
    *   [ ] The test should call the main function of the CLI script with a dummy audio URL.
    *   [ ] It must assert that the `run` method on the mocked `RunPodClient` was called with the correct audio URL.
    *   [ ] It must assert that the CLI prints the mocked return value from the `run` method.

### Task 2: Create the CLI Application (40 minutes)
*   **Description**: Create a new executable file that uses the `argparse` module and our `RunPodClient` to allow users to request transcriptions from their terminal.
*   **Acceptance Criteria**:
    *   [ ] A new file is created at `src/spiceflow/cli.py`.
    *   [ ] The test in `tests/test_cli.py` must now pass.
    *   [ ] The file must be executable (`if __name__ == "__main__":`).
    *   [ ] The CLI must accept a single positional argument: `audio_url`.
    *   [ ] The CLI should use the existing `RunPodClient` to send the request to the Gradio service.
    *   [ ] The CLI must print the transcription result received from the client to standard output.
    *   [ ] The other parameters for the `RunPodClient.run` method (e.g., `model`, `task`, `temperature`) can be hardcoded to the default values for this initial version.

---

## 3. Post-Sprint Mandates

### 1. Verification
*   **CI Pipeline**: All new and existing tests must pass.

### 2. 🚩 Mandatory Post-Sprint Analysis & Root Cause Investigation (For Codex)
*(Write your analysis in `Docs/Sprints/Codex Engineering Sprint Reviews/sprint_11_reflection.md`.)*

**Structure for your Analysis:**
**Part 1: Executive Summary of Action**
> Describe the creation of the CLI file and its corresponding test. State whether all tests passed.
**Part 2: Root Cause Analysis (RCA) of Failures & Challenges**
> If any challenges were faced (e.g., with mocking the CLI or argument parsing), provide a full RCA.

---

# 📋 PRE-SPRINT CHECKLIST
- [X] CI pipeline passing (mvp-sanity-check)
- [X] All guard-rails operational
- [X] No fabrication detected in previous sprint
- [X] PoC Validated in Sprint 10

## 🛡️ GUARD-RAILS STATUS

### Guard-Rail 1: CI-Enforced Validation ✅
**Status**: Active - All claims verified by GitHub Actions, not chat

### Guard-Rail 2: Test-First Development ✅
**Status**: Mandatory - This sprint requires creating a failing test before implementation.

---

## 🎯 SUCCESS METRICS (CI-Enforced)

- **All Tests Pass**: `pytest -q` shows green for all tests, including `tests/test_cli.py`.
- **Honest Documentation**: The engineering reflection is completed. 