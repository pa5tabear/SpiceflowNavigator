# Sprint 15: End-to-End Vertical Slice (RE-RUN)

## 1. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Deliver a functional, vertical slice that runs a full workflow: RSS feed processing → dummy transcript generation → strategic analysis with a mocked LLM → and writing a summary to a Markdown file.

### Product Vision Alignment
> The project currently has good documentation but lacks a demonstrable, end-to-end capability. This sprint pivots from component-by-component blueprinting to shipping a tangible, albeit mocked, vertical slice of the application. This is on the critical path to creating the "Daily Briefing" user experience, as it connects the ingest, analysis, and output steps for the first time.

---

## 2. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Guard-Rails & Test-First Development
*   **CI-Enforced Validation**: All claims must be verified by CI.
*   **Test-First Mandate**: Failing tests must be written before implementation.
*   **Golden Path Script**: A new `run_workflow.py` will serve as the Golden Path test.

### Task 1: Implement CI Quality Gates & `env_check` (15 minutes)
*   **Description**: Harden the CI pipeline and create the environment check script.
*   **Acceptance Criteria**:
    *   [ ] `.github/workflows/ci.yml` is updated to include `ruff --fail-level error` and `pytest --cov=src --cov-fail-under=80`.
    *   [ ] `scripts/env_check.py` is created and checks for the `RUNPOD_ENDPOINT` secret. It exits with an error if not found.
    *   [ ] `tests/integration/test_runpod_transcribe.py` is updated to use the correct `/health` endpoint.

### Task 2: Implement RSS Parser & Analyzer (30 minutes)
*   **Description**: Turn the blueprints into running code with mocked dependencies.
*   **Acceptance Criteria**:
    *   [ ] `config/strategic_topics.yml` is created and loaded by the analyzer.
    *   [ ] `src/spiceflow/rss_parser.py` is created with passing tests.
    *   [ ] `src/spiceflow/analyzer.py` is created with a mockable LLM client interface and passing tests that verify its behavior with both good and malformed mock LLM responses.

### Task 3: Implement Golden Path Workflow (15 minutes)
*   **Description**: Connect all the pieces in an end-to-end workflow script.
*   **Acceptance Criteria**:
    *   [ ] `run_workflow.py` is created.
    *   [ ] When run, it uses the `RSSParser` to get feeds, uses a dummy transcript, passes it to the `StrategicAnalyzer`, and writes a final Markdown summary to the `transcripts/` directory.
    *   [ ] All old `*.blueprint.md` files are deleted.

---

## 3. Post-Sprint Mandates

### 1. Verification
*   **CI Pipeline**: Must be green, including new ruff and coverage checks.
*   **Golden Path**: The `run_workflow.py` script must be executed successfully and generate an output file.
*   **Output Validation**: The generated Markdown file in `transcripts/` must exist and contain a recognizable analysis.

### 2. 🚩 Mandatory Post-Sprint Analysis & Root Cause Investigation (For Codex)
*(After completing the technical tasks, the engineering agent **must** write a detailed analysis in `Docs/Sprints/Codex Engineering Sprint Reviews/sprint_15_reflection.md`)*

**Structure for your Analysis:**

**Part 1: Executive Summary of Action**
> Briefly describe the tasks you executed and their final status.

**Part 2: Root Cause Analysis (RCA) of Failures & Challenges**
> Provide an RCA for the **complete failure of Sprint 14**. Explain why no deliverables were met and what process changes you have made to ensure this does not happen again.

**Part 3: Proposed Next Sprint (Problem Decomposition)**
> Based on your successful completion of the vertical slice, propose a plan for the next sprint. The goal should be to replace one of the mocked components (e.g., the dummy transcript) with a real implementation. 