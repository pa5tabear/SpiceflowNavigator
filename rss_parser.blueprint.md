# Blueprint: RSS Feed Parser (`rss_parser.py`)

## Principle

This module will have one responsibility: to interact with podcast RSS feeds. It should handle the complexity of parsing RSS XML and finding the correct audio URL, and it should be easily testable in isolation. This replaces the old `select_episode.py` script with a proper, reusable module.

## Requirements

1.  **Create a file named `rss_parser.py`.**
2.  Inside this file, create a function named `fetch_latest_episode_url`.
    *   This function must accept one argument: `feed_url` (a string).
    *   It must use the `feedparser` library to parse the XML from the given URL.
    *   It must correctly identify the audio URL for the *most recent* episode in the feed. The `feedparser` library provides date information for entries.
    *   It must return the audio URL as a string.
    *   It must include robust error handling (e.g., using a `try...except` block) for cases where the URL is invalid or the feed is malformed, and it should return `None` in these cases.

## Implementation Notes for Codex

*   This module should not perform any downloading or API calls. Its only job is to parse the feed and return a URL.
*   The logic for finding the audio URL within an entry's `enclosures` should be robust, as this was a point of failure in the old codebase. 