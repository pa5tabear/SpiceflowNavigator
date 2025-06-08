# Sprint 12: RSS Feed Parser

## 1. Sprint Goal & Strategic Alignment

### 60-Minute Focus: Build and test a robust RSS feed parser capable of extracting audio episode URLs from a live podcast feed.

### Product Vision Alignment
> To analyze podcast content, we must first be able to retrieve it. This sprint creates the essential component for connecting our system to the source material. By building an RSS parser, we move from transcribing single, user-provided audio files to systematically processing entire podcast series. This directly serves the long-term goal of rating episodes for strategic insight.

---

## 2. Sprint Tasks & Acceptance Criteria (The "Inner Loop")

### Guard-Rails & Test-First Development
*   **Test-First Mandate**: A failing test must be written to validate the RSS parser's functionality before implementation.
*   **No Live Network Calls in Tests**: All tests must use a statically saved, local copy of the RSS feed XML to ensure reliability and speed. Do not hit the live `acast.com` URL during testing.

### Task 1: Save a Local Copy of the RSS Feed (5 minutes)
*   **Description**: Download the XML content from the "Shift Key" podcast feed and save it to a new file at `tests/fixtures/shift_key_rss.xml`. This file will be used as the input for your unit test.
*   **Feed URL**: `https://feeds.acast.com/public/shows/65bac3af03341c00164bf93b`
*   **Acceptance Criteria**: The file `tests/fixtures/shift_key_rss.xml` exists and contains the valid RSS feed content.

### Task 2: Create a Test for the RSS Parser (20 minutes)
*   **Description**: Create a new unit test file that attempts to use a new, not-yet-created `RSSParser` class. This test should load the local XML file from Task 1 and assert that the parser can correctly identify and extract all the MP3 URLs from the `<enclosure>` tags within the feed.
*   **Acceptance Criteria**: A new test file exists (e.g., `tests/test_rss_parser.py`) with at least one failing test that checks for the extraction of audio URLs. The test suite fails when run.

### Task 3: Implement the RSS Parser (30 minutes)
*   **Description**: Create the `RSSParser` class and the necessary logic to make the failing test from Task 2 pass. Use Python's built-in `xml.etree.ElementTree` module for this task. The parser should expose a method that takes the XML content as input and returns a list of audio URLs.
*   **Acceptance Criteria**: The test from Task 2 now passes. All other existing tests continue to pass.

---

## 3. Post-Sprint Mandates for Codex

### Root Cause Analysis (RCA)
*   **Mandate**: In your reflection, you MUST provide a detailed Root Cause Analysis (RCA) for any failures or significant challenges encountered. If the sprint is a success, you must instead analyze a key decision you made and its impact.

### Success Metrics
*   **Mandate**: You MUST populate the following metrics in your reflection:
    *   **Tests Passed:** X/Y
    *   **Code Churn:** Z lines
    *   **Time-to-complete:** N hours

### Final Sanity Check
*   **Mandate**: Before finishing, you MUST run the full test suite one last time (`python -m pytest`) to ensure all tests pass. 