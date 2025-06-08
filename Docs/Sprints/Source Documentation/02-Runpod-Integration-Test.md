# Spiceflow Navigator Sprint Plan 
## (Version 2.0 - Blended PM & Eng)

---

# Sprint 2: Live RunPod API Integration Test

## 1. Sprint Review & Retrospective (The "Outer Loop")

### Product Manager's Two-Paragraph Review

**Paragraph 1: Progress & Status**
> After a failed first attempt, the retry of Sprint 1 was a complete success. The agent successfully refactored the `RunPodClient` into the `src/spiceflow/clients` module and implemented a comprehensive suite of unit tests, achieving 100% pass rate. The project is now well-structured and aligned with our TDD principles. The verified progress toward the MVP is still 0%, but we have now built a solid, trustworthy foundation for our core API client.

**Paragraph 2: Blockers, Costs & Decisions**
> There are no technical blockers. The primary dependency is the external RunPod service. This sprint will incur minor API costs for the first time as we perform a live end-to-end test. The key decision is to proceed with this live test, accepting the small cost, to get our first signal of real-world viability. A `RUNPOD_ENDPOINT` environment variable must be correctly set for the test to run.

### Next Steps & Human-in-the-Loop Flags
*   [ ] Write a single, targeted integration test that calls the live RunPod API.
*   [ ] Use the pre-agreed short audio file for the test.
*   [ ] Verify that a transcript is successfully returned.
*   [ ] 🚩 **FLAG**: Human review of the test result is critical. A passing test represents the first verifiable progress of the entire project.

---

## 2. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Prove end-to-end connectivity to the RunPod API by successfully transcribing one short audio file.

### Product Vision Alignment
> The entire purpose of this application is to reliably transcribe audio. All previous work has been foundational. This sprint is the first to touch the core functionality. Success in this sprint provides the first piece of "Executable Truth"—proof that our most critical assumption (that we can connect to and get a response from our chosen API) is correct. It is the single most important next step on the critical path to the MVP.

---

## 3. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Guard-Rails & Test-First Development
*   **CI-Enforced Validation**: The test must be runnable in a CI environment.
*   **Test-First Mandate**: The integration test will be written before any potential client modifications.

### Task 1: Create Integration Test File (30 minutes)
*   **Description**: Create a new test file for our live integration test. This test will use the existing `RunPodClient` to call the actual RunPod API endpoint.
*   **Acceptance Criteria**:
    *   [ ] A new test file is created at `tests/integration/test_runpod_api.py`.
    *   [ ] The test will be marked with `@pytest.mark.integration` to allow it to be run separately from unit tests.
    *   [ ] The test will be skipped using `@pytest.mark.skipif(not os.environ.get("RUNPOD_ENDPOINT"), ...)` if the endpoint is not configured.
    *   [ ] The test will instantiate the real `RunPodClient`.
    *   [ ] It will call the client with the specified audio URL: `https://filesamples.com/samples/audio/mp3/sample1.mp3`
    *   [ ] The test will assert that the returned transcript is a non-empty string.
    *   [ ] The test must be written to fail if the API call is unsuccessful.

### Task 2: Configure `pytest.ini` (10 minutes)
*   **Description**: Update the `pytest.ini` file to register the `integration` marker, allowing us to include or exclude these tests from runs.
*   **Acceptance Criteria**:
    *   [ ] The `pytest.ini` file is updated to include a `markers` section.
    *   [ ] The `integration` marker is defined with a clear description (e.g., "tests that call live external APIs").

### Task 3: Run the Test and Verify (20 minutes)
*   **Description**: Execute the `pytest` suite, specifically targeting the integration test, and confirm that it passes.
*   **Acceptance Criteria**:
    *   [ ] The command `pytest -m integration` is run.
    *   [ ] The test passes, indicating a successful round-trip communication with the RunPod API.
    *   [ ] If the test fails, the output/error is logged for human review. 