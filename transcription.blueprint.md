# Blueprint: Transcription & Caching (`transcription.py`)

## Principle

This feature is the core of the application. It must be broken down into two distinct, single-responsibility modules to ensure it is robust and testable. It replaces the tangled logic of the old `run_transcription.py` script with a clean, professional architecture.

## Requirements

### Part 1: The Transcript Cache (`transcript_cache.py`)

1.  **Create a file named `transcript_cache.py`.**
2.  This file will manage all file system interactions for storing and retrieving transcripts.
3.  Create a class named `TranscriptCache`.
    *   It should have a `__init__` method that takes a `cache_dir` path (e.g., `./transcripts`).
    *   It should have a method `get(audio_url: str) -> str | None`. This method will generate a safe filename from the `audio_url`, check for its existence in the `cache_dir`, and return the content if found, otherwise `None`.
    *   It should have a method `save(audio_url: str, transcript: str)`. This method will generate the same safe filename and save the `transcript` text to that file in the `cache_dir`.

### Part 2: The Transcription Service (`transcription_service.py`)

1.  **Create a file named `transcription_service.py`.**
2.  This file will manage the interaction with the RunPod API and will use the `TranscriptCache`.
3.  Create a class named `TranscriptionService`.
    *   It should have a `__init__` method that takes a `RunPodClient` instance and a `TranscriptCache` instance.
    *   It should have a single public method: `get_transcript(audio_url: str) -> str`.
    *   This method's logic should be:
        1.  First, call the `transcript_cache.get()` method to check if the transcript is already cached. If it is, return it immediately.
        2.  If it's not in the cache, call the `runpod_client` to get a new transcript from the `audio_url`.
        3.  If the API call is successful, use the `transcript_cache.save()` method to save the new transcript.
        4.  Return the new transcript.

## Implementation Notes for Codex

*   This architecture explicitly separates the caching logic (file I/O) from the API logic (network calls). This is critical.
*   The `TranscriptionService` should not know *how* the cache works, only that it can `.get()` and `.save()`.
*   The `TranscriptCache` should not know anything about the RunPod API. Its only job is to read and write files based on a URL.
*   This design makes each component independently testable. We can test the cache with fake files, and we can test the service by giving it a mock cache and a mock API client. 