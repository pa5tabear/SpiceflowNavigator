# Sprint 09: Refactor Client for Gradio API

- **Season:** 1
- **Sprint:** 9
- **Codename:** Gradio Pivot
- **Theme:** Major Refactor & API Alignment
- **Status:** READY
- **Start Date:** 2024-07-26
- **End Date:** 2024-07-26
- **Review Date:** 2024-07-26

## 1. Sprint Goal

This sprint's goal is to completely refactor the `RunPodClient` to correctly interact with the target **Gradio application API**. This involves replacing the `requests`-based implementation with one that uses the `gradio_client` library.

## 2. Business & Engineering Context

New information has revealed that the target RunPod service is a Gradio application, not a standard serverless REST endpoint. Our previous client was built on an incorrect assumption and is incompatible. This sprint represents a necessary pivot to align our codebase with the actual target API. This change, while a refactor, is a positive one as it simplifies our client by removing the need for manual polling and API key authorization.

The API documentation for the Gradio endpoint is available at the "Use via API" link on the Whisper Playground page.

## 3. Tasks

### Task 1: Update Dependencies

- **Action:** Add the `gradio_client` library to the `requirements.txt` file.

### Task 2: Refactor `RunPodClient`

- **File:** `src/spiceflow/clients/runpod_client.py`
- **Action:** Completely rewrite the `RunPodClient` class.
- **Acceptance Criteria:**
    1.  The `__init__` method should now instantiate a `gradio_client.Client` object, pointing to the `RUNPOD_ENDPOINT` URL.
    2.  The `check_health` and `status` methods are now obsolete and must be **removed**.
    3.  The `run` method must be completely rewritten:
        - Its new signature should be: `def run(self, file_path: str, model: str, task: str, temperature: float, stream: bool) -> str:`
        - It must call the `gradio_client.Client.predict` method.
        - The `api_name` parameter for `predict` must be hardcoded to `'/predict'`, as shown in the documentation.
        - The other parameters (`file_path`, `model`, etc.) should be passed directly to `predict`.
        - The method should return the result from `predict`.

### Task 3: Update Unit Tests

- **File:** `tests/clients/test_runpod_client.py`
- **Action:** Completely rewrite the unit tests for `RunPodClient`.
- **Acceptance Criteria:**
    1.  Tests must now mock `gradio_client.Client`.
    2.  Create a test that verifies the `RunPodClient.run` method calls `predict` on the mock client with the exact parameters it received.
    3.  Verify that the `api_name` is correctly passed as `'/predict'`.

### Task 4: Update Integration Test

- **File:** `tests/integration/test_runpod_transcribe.py`
- **Action:** Update the integration test to use the new `RunPodClient`.
- **Acceptance Criteria:**
    1.  The test should be modified to call the new `run` method with valid parameters.
    2.  Use a public URL to a sample `.wav` file for the `file_path` parameter. A good one is `https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav`.
    3.  Use the default values from the Gradio documentation for the other parameters (`model`, `task`, etc.).
    4.  The test should assert that the returned result is a non-empty string.
    5.  The `RUNPOD_API_KEY` is no longer needed for this test. The `RUNPOD_ENDPOINT` variable is still required.

## 4. Sprint Review

### Engineering Review (Codex)

- **Standard Reflection:**
  - What was the result of the sprint?
  - What was the outcome of running the test suite (both unit and integration)?
  - Were there any surprises during the refactor?
- **Root Cause Analysis (RCA):**
  - Why did we initially build a client for the wrong API type? (e.g., Lack of initial information, incorrect assumption about "RunPod API" meaning the serverless REST API.)
  - What process change can we implement to ensure we have the correct API specification *before* we begin writing client code in the future?

### Product & Test Review (PM)

- The PM will review the changes and the successful test run to confirm the application is now correctly integrated with the Gradio service. 