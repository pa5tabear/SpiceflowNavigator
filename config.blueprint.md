# Blueprint: Configuration (`config.py`)

## Principle

This file establishes a clean separation between the application's logic and the user's specific data. It should be simple, easy to edit, and contain no complex logic.

## Requirements

1.  **Create a file named `config.py`.**
2.  Inside this file, define a variable named `PODCAST_FEEDS`.
    *   This variable must be a Python list of strings.
    *   It should contain exactly one example podcast feed URL, with a comment indicating that more can be added.
3.  Define a second variable named `LEARNING_GOALS`.
    *   This variable must be a Python list of strings.
    *   It should contain exactly one example goal, with a comment explaining its purpose.

## Implementation Notes for Codex

*   Do not include the old `SAMPLE_TRANSCRIPTS` variable. This was a source of fabrication and must not be reintroduced.
*   Keep the variable names simple and clear. The goal is readability for a human user who will be editing this file. 