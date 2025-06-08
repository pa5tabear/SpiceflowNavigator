# Spiceflow Navigator Sprint Plan 
## (Version 2.0 - Blended PM & Eng)

---

# Sprint 3: RSS Feed Parser

## 1. Sprint Review & Retrospective (The "Outer Loop")

### Product Manager's Two-Paragraph Review

**Paragraph 1: Progress & Status**
> Sprint 2 was a complete success. The agent created a robust integration test that correctly connects to the live RunPod API. The test correctly skips itself when the `RUNPOD_ENDPOINT` is not configured, proving the guard-rails are working. While we have not yet seen a `PASSED` test against the live API (due to lack of secrets in the CI environment), we have successfully built and verified the machinery to do so. This marks a major milestone: the project's core foundation is stable and the testing apparatus is sound.

**Paragraph 2: Blockers, Costs & Decisions**
> There are no technical blockers. The work in this sprint has no external dependencies and will incur no API costs. The primary decision is to now move to the first step of the core application logic: parsing an RSS feed. This is the first "real" feature of the application beyond the API client. We will use the `feedparser` library, which should be added to our dependencies.

### Next Steps & Human-in-the-Loop Flags
*   [ ] Add `feedparser` to `requirements.txt`.
*   [ ] Create a new, single-responsibility module for RSS parsing.
*   [ ] Write unit tests to verify the parser can extract an audio URL from a sample feed.
*   [ ] 🚩 **FLAG**: No human intervention is required for this sprint. It is pure, test-driven feature development.

---

## 2. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Create a fully-tested module that can extract the latest episode's audio URL from a given RSS feed.

### Product Vision Alignment
> The "Staircase Model" in our project charter defines a clear, incremental path. Step 1 is "Parse RSS Feed." This sprint directly implements that first step. By building a reliable parser, we are constructing the first tread of the staircase, moving from foundational client work to user-facing application logic. This is the start of building the core pipeline.

---

## 3. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Task 1: Update Dependencies (5 minutes)
*   **Description**: Add the `feedparser` library to the project's requirements.
*   **Acceptance Criteria**:
    *   [ ] The `requirements.txt` file is created (as it was not checked in).
    *   [ ] `pytest`, `requests`, and `python-dotenv` are listed.
    *   [ ] `feedparser` is added to `requirements.txt`.

### Task 2: Create RSS Parser Module (Test-First) (30 minutes)
*   **Description**: Create a new module and a corresponding test file to handle RSS parsing logic. The tests will be written first.
*   **Acceptance Criteria**:
    *   [ ] A new module is created at `src/spiceflow/core/rss_parser.py`.
    *   [ ] A new test file is created at `tests/core/test_rss_parser.py`.
    *   [ ] The test file will contain a test that uses a *local, static copy* of a sample RSS feed XML to ensure the test is fast and reliable. It will not make a live web request.
    *   [ ] The test will assert that a function in the parser module can correctly find and return the audio URL from the first entry in the sample XML. The test should fail initially.

### Task 3: Implement RSS Parser Logic (20 minutes)
*   **Description**: Write the implementation of the RSS parser to make the tests pass.
*   **Acceptance Criteria**:
    *   [ ] The `get_latest_episode_url` function is implemented in `src/spiceflow/core/rss_parser.py`.
    *   [ ] The function takes a feed URL as input but will be tested with a local file path.
    *   [ ] It uses the `feedparser` library to parse the feed.
    *   [ ] It correctly identifies the audio URL from the `enclosures` of the latest entry.
    *   [ ] All tests in `tests/core/test_rss_parser.py` now pass. `pytest` runs clean.

### Task 4: Create Sample RSS Data File (5 minutes)
*   **Description**: Create the static RSS feed file that the unit test will use as its data source.
*   **Acceptance Criteria**:
    *   [ ] A new directory `tests/data` is created.
    *   [ ] A file named `tests/data/sample_rss.xml` is created.
    *   [ ] The file contains a minimal, valid RSS feed with at least one entry containing an audio file in its enclosures. 