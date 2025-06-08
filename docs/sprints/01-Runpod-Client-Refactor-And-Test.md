# Spiceflow Navigator Sprint Plan 
## (Version 2.0 - Blended PM & Eng)

---

# Sprint 1: RunPod Client Refactor & Test Coverage

## 1. Sprint Review & Retrospective (The "Outer Loop")

### Product Manager's Two-Paragraph Review

**Paragraph 1: Progress & Status**
> A `runpod_client.py` file has been merged into the root directory. This represents initial progress on the "Get Transcript" functionality. However, the work is not compliant with our project constitution, as it was not developed using TDD and violates the Single Responsibility Principle by being placed in the root directory. There are currently no passing tests that verify its functionality, and thus our verified progress toward the MVP goal is 0%.

**Paragraph 2: Blockers, Costs & Decisions**
> The primary blocker is the lack of test coverage and proper code structure for the existing `RunPodClient`. This introduces significant technical debt and risk. Before any new functionality is developed, we must refactor this client into a dedicated `spiceflow/clients` module and write comprehensive tests for it. This sprint will incur no direct API costs as it is focused on refactoring and testing against a mocked or firewalled endpoint.

### Next Steps & Human-in-the-Loop Flags
*   Refactor `RunPodClient` into `src/spiceflow/clients/runpod_client.py`.
*   Write comprehensive `pytest` tests for the `RunPodClient`.
*   Ensure all tests pass in CI.
*   🚩 **FLAG**: Human review is required to confirm that the final, tested client correctly aligns with the RunPod API's actual interface.

---

## 2. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Achieve 100% test coverage for the RunPod API client and move it to the correct location in the codebase.

### Product Vision Alignment
> Our core principles mandate that all code be test-driven and well-structured. The current `runpod_client.py` violates these principles. This sprint brings the project back into alignment with our constitution. By ensuring our API client is robust and reliable, we build a solid foundation for the core "Get Transcript" functionality, which is on the critical path to the MVP. We cannot build on a shaky foundation.

---

## 3. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Guard-Rails & Test-First Development
*   **CI-Enforced Validation**: All claims must be verified by CI.
*   **Test-First Mandate**: Failing tests must be written before implementation.
*   **Golden Path Script**: Not applicable for this refactoring sprint.

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
    *   [ ] This file contains tests for the `__init__`, `check_health`, `run`, and `status` methods.
    *   [ ] These tests use `pytest.MonkeyPatch` and a mock `requests.Response` object to avoid making real network calls.
    *   [ ] The tests are written to fail until the client is moved and potentially refactored. `pytest -q` shows failures.

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