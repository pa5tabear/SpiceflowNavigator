# Sprint 13: Markdown-Driven Transcription Workflow

## 1. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Create an automated, end-to-end workflow that uses the RSS feed to generate and populate Markdown files with podcast transcriptions.

### Product Vision Alignment
> This sprint delivers the core user-facing experience of the application. It replaces the command line with an elegant, file-based workflow, exactly as specified in the product vision. By automating the entire process from RSS feed to final transcript, we create a system that can be run on a schedule, continuously providing value and strategic insights without manual intervention.

---

## 2. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Guard-Rails & Test-First Development
*   **Test-First Mandate**: A failing test must be written to validate the new workflow manager before implementation.
*   **No Live Network Calls in Tests**: All tests must mock the `RunPodClient` and use the local `shift_key_rss.xml` fixture.

### Task 1: Create a Test for the Workflow Manager (20 minutes)
*   **Description**: Create a new test file, `tests/test_workflow.py`. This test will validate a new `WorkflowManager` class. The test should mock the `RSSParser` to return a predefined list of audio URLs and mock the `RunPodClient` to return a sample transcription. It should assert that the `WorkflowManager`, when run, creates new files in a `transcripts/` directory with the correct content.
*   **Acceptance Criteria**: A new test file exists with at least one failing test that checks for the creation and population of Markdown files. The test suite fails when run.

### Task 2: Implement the Workflow Manager (35 minutes)
*   **Description**: Create a new `src/spiceflow/workflow.py` module containing the `WorkflowManager` class. This class will:
    1.  Initialize the `RSSParser` and the `RunPodClient`.
    2.  Use the parser to get a list of the 2 most recent episode audio URLs.
    3.  For each episode, check if a corresponding file exists in `transcripts/`.
    4.  If the file does *not* exist, use the `RunPodClient` to fetch the transcription.
    5.  Create a new Markdown file (e.g., `transcripts/2024-07-27-episode-title.md`) and populate it with the audio URL and the full transcription.
*   **Acceptance Criteria**: The test from Task 1 now passes. All other existing tests continue to pass.

### Task 3: Create an Executable Script (5 minutes)
*   **Description**: Create a new file, `run_workflow.py`, in the root directory. This script should import and execute the `WorkflowManager`.
*   **Acceptance Criteria**: The file `run_workflow.py` exists and successfully triggers the transcription workflow when executed.

---

## 3. Post-Sprint Mandates for Codex

### Root Cause Analysis (RCA)
*   **Mandate**: You MUST provide a detailed Root Cause Analysis (RCA). This sprint, you must specifically address the **process failure** from Sprint 12 where no reflection was provided. Explain why it happened and what steps you will take to ensure it does not happen again.

### Success Metrics
*   **Mandate**: You MUST populate the following metrics in your reflection:
    *   **Tests Passed:** X/Y
    *   **Code Churn:** Z lines
    *   **Time-to-complete:** N hours

### Final Sanity Check
*   **Mandate**: Before finishing, you MUST run the full test suite one last time (`python -m pytest`) to ensure all tests pass. 