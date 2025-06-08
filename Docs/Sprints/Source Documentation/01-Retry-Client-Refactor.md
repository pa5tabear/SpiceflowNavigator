# Spiceflow Navigator Sprint Plan 
## (Version 2.0 - Blended PM & Eng)

---

# Sprint 1 (RETRY): RunPod Client Refactor & Test Coverage

## 1. Sprint Review & Retrospective (The "Outer Loop")

### Product Manager's Two-Paragraph Review

**Paragraph 1: Progress & Status**
> **The previous attempt at this sprint was a failure.** The agent did not execute the sprint plan. No new directories were created, the `RunPodClient` was not refactored, and no tests were written. The project remains in the exact state it was in prior to the sprint, with an untested, misplaced client file. Our verified progress toward the MVP remains at 0%.

**Paragraph 2: Blockers, Costs & Decisions**
> The blocker is unchanged: a critical piece of client code has zero test coverage and is in the wrong location. The primary decision is to **retry the sprint**. We will not proceed with any new functionality or integration tests until this foundational piece of technical debt is resolved. The cost of this sprint remains zero, as all work is local refactoring and mock-based testing. This retry is mandatory.

### Next Steps & Human-in-the-Loop Flags
*   [ ] **RETRY**: Execute the exact tasks from the original Sprint 1 plan.
*   [ ] Refactor `RunPodClient` into `src/spiceflow/clients/runpod_client.py`.
*   [ ] Write comprehensive `pytest` unit tests for the `RunPodClient`.
*   [ ] Ensure all tests pass in CI.
*   [ ] 🚩 **FLAG**: Human review is required to confirm the sprint was actually completed this time.

---

## 2. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Achieve 100% test coverage for the RunPod API client and move it to the correct location in the codebase.

### Product Vision Alignment
> Our core principles mandate that all code be test-driven and well-structured. The previous failure to execute this sprint means the project is still not in alignment with our constitution. A reliable, tested, and properly structured API client is the mandatory first step for any further development. We cannot build on a shaky foundation. This sprint **must** be completed successfully.

---

## 3. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

*(This section is identical to the previous sprint plan. Execute these tasks exactly.)*

### Guard-Rails & Test-First Development
*   **CI-Enforced Validation**: All claims must be verified by CI.
*   **Test-First Mandate**: Failing tests must be written before implementation.

### Task 1: Create Project Structure (10 minutes)
*   **Description**: Create the necessary directories for our source code and tests.
*   **Acceptance Criteria**:
    *   [ ] The following directory structure is created: `src/spiceflow/clients`
    *   [ ] The following directory is created: `tests/clients`
    *   [ ] `__init__.py` files are added to `src/spiceflow`, `src/spiceflow/clients`, and `tests/clients` to make them packages.

### Task 2: Write Failing Tests for `RunPodClient` (20 minutes)
*   **Description**: Create a test file that defines the expected behavior of the `RunPodClient`.
*   **Acceptance Criteria**:
    *   [ ] A new test file is created at `tests/clients/test_runpod_client.py`.
    *   [ ] This file contains tests for the `__init__`, `check_health`, `run`, and `status` methods, using `pytest.MonkeyPatch` to mock `requests`.
    *   [ ] The tests are written to fail until the client is moved. `pytest -q` shows failures.

### Task 3: Refactor `RunPodClient` to Pass Tests (20 minutes)
*   **Description**: Move the existing `RunPodClient` code to its correct location and modify it to pass the newly created tests.
*   **Acceptance Criteria**:
    *   [ ] The `runpod_client.py` file is moved from the root directory to `src/spiceflow/clients/runpod_client.py`.
    *   [ ] The implementation is adjusted as needed to make all tests in `tests/clients/test_runpod_client.py` pass.
    *   [ ] `pytest -q` runs clean with all tests passing.
    
### Task 4: Cleanup (10 minutes)
*   **Description**: Remove the old `runpod_client.py` file from the root directory.
*   **Acceptance Criteria**:
    *   [ ] The `runpod_client.py` file is no longer present in the project root.
    *   [ ] The CI pipeline passes. 