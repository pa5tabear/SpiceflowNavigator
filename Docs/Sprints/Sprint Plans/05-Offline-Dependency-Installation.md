# Sprint 5: Dependency Installation Investigation

## 1. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Discover and execute a reliable method for installing dependencies, then verify the installation and secret access.

### Product Vision Alignment
> Our core blocker is dependency installation. This sprint is a direct investigation to find a working strategy. By systematically testing the most likely solutions (online-first, then offline), we will acquire the knowledge needed to create a stable foundation.

---

## 2. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Task 1: Attempt Online Installation (20 minutes)
*   **Description**: First, we will test the hypothesis that the "Internet Access ON" setting works. This is the simplest and most direct approach.
*   **Acceptance Criteria**:
    *   [ ] The command `pip install -r requirements.txt` is executed.
    *   [ ] The outcome is recorded. If it succeeds, proceed directly to Task 3. If it fails, proceed to Task 2.

### Task 2: Attempt Offline Installation (Fallback only) (20 minutes)
*   **Description**: This task is a fallback. **Only run this if Task 1 failed.** This will test the hypothesis that dependencies must be installed from a local source.
*   **Acceptance Criteria**:
    *   [ ] This task is skipped if Task 1 was successful.
    *   [ ] A `vendor/` directory is present in the workspace root.
    *   [ ] The command `pip install --no-index --find-links=vendor/ -r requirements.txt` is executed.
    *   [ ] The success or failure of this command is recorded.

### Task 3: Re-run the Diagnostic Tool (10 minutes)
*   **Description**: After attempting one or both of the installation methods, run the diagnostic script again to verify the final state of the environment.
*   **Acceptance Criteria**:
    *   [ ] The command `python scripts/diagnose_environment.py` is executed.
    *   [ ] The "Dependency Check" section of the report must show `✅` for all packages for the sprint to be a success.

### Task 4: Write Mandatory Post-Sprint Analysis (10 minutes)
*   **Description**: Write the mandatory reflection document for this sprint, analyzing the results of the installation attempts.
*   **Acceptance Criteria**:
    *   [ ] A new file is created at `Docs/Sprints/Codex Engineering Sprint Reviews/sprint_05_reflection.md`.
    *   [ ] The reflection's "Observation" section **must state which installation method was successful (Online or Offline)**.
    *   [ ] The section must include the **full, raw text output** from the final run of the `diagnose_environment.py` script as evidence.
    *   [ ] If both methods failed, the "Proposed Next Sprint" should focus on analyzing the specific errors from both `pip` commands. 