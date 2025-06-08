# Sprint 08: RunPod Client-Side API Alignment

- **Season:** 1
- **Sprint:** 8
- **Codename:** Client-Side API Alignment
- **Theme:** Technical Debt & Correctness
- **Status:** READY
- **Start Date:** 2024-07-26
- **End Date:** 2024-07-26
- **Review Date:** 2024-07-26

## 1. Sprint Goal

This sprint's goal is to correct critical bugs in our `runpod_client.py` by aligning it with the official RunPod Serverless API documentation. This is a proactive measure to prevent inevitable failures in our live integration tests.

## 2. Business & Engineering Context

During a proactive review, we compared our existing `runpod_client.py` against the official RunPod API documentation. This review uncovered several critical discrepancies that would cause any live API call to fail. The most significant issues are:

1.  **Missing Authorization:** Our client does not send the required `Authorization: Bearer <API_KEY>` header.
2.  **Incorrect Payload Structure:** The `run` method sends a raw payload, but the API expects the payload to be nested within an `{"input": ...}` object.
3.  **Incorrect Health Endpoint:** The client checks an undocumented `/healthz` endpoint instead of the official `/health` endpoint.

Fixing these issues now is crucial for making any further progress. This is a classic example of paying down technical debt to enable future work.

## 3. Tasks

### Task 1: Refactor `runpod_client.py` for API Compliance

Codex is to modify the `src/spiceflow/clients/runpod_client.py` file to address the discrepancies found.

#### Acceptance Criteria:

1.  **Authorization Header:** The client must read the `RUNPOD_API_KEY` from the environment.
    - An appropriate `Authorization: Bearer <key>` header must be added to **all** requests made to the RunPod API (`/run`, `/status`, and `/health`).
2.  **Payload Wrapping:** The `run()` method must be modified to automatically wrap the `payload` dictionary it receives inside an `{"input": ...}` dictionary before sending it. The method signature should not change; the wrapping should be an internal implementation detail.
3.  **Health Endpoint:** The `check_health()` method must be updated to use the documented `/health` endpoint (not `/healthz`). It should still perform a basic success/failure check.
4.  **Unit Tests:** The corresponding unit tests in `tests/clients/test_runpod_client.py` must be updated to reflect these changes. Specifically, tests should now verify:
    - That the `Authorization` header is correctly added to all outgoing mock requests.
    - That the payload in the mock `run` request is correctly wrapped in `{"input": ...}`.
    - That the health check now calls the `/health` endpoint on the mock object.

## 4. Sprint Review

### Engineering Review (Codex)

- **Standard Reflection:**
  - What was the result of the sprint?
  - What was the outcome of running the test suite?
  - Were there any surprises?
  - What, if anything, would you do differently next time?
- **Root Cause Analysis (RCA):**
  - Why did these bugs exist in the first place? (e.g., Was the initial implementation rushed? Was it written without access to documentation?)
  - Why did our previous test suites (Sprints 1 & 2) not catch these bugs? (e.g., Did they rely too heavily on mocking? Were the mocks incomplete?)
  - What specific changes in our testing strategy can prevent similar bugs from going undetected in the future?

### Product & Test Review (PM)

- The PM will review the changes and the reflection to confirm that the client is now aligned with the API specification and that the engineering team has a plan to improve testing rigor. 