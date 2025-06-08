# Blueprint: Project Charter (`README.md`)

## Project Title

SpiceFlow Navigator: A Podcast Transcription Prototype

## One-Sentence Engineering Goal

This project's purpose is to reliably transcribe podcast episodes from a list of RSS feeds by calling an external, serverless transcription API.

## Core Functionality (The "Staircase")

The application will be built incrementally and will perform the following three steps in order:

1.  **Parse RSS Feed:** Given a URL, extract the audio link for the latest episode.
2.  **Get Transcript:** Given an audio link, use a caching mechanism and an external API client to retrieve the episode's transcript.
3.  **Save Transcript:** Store the retrieved transcript in a local directory.

*Note: Any functionality beyond these three steps, such as "insight generation" or "recommendation ranking," is explicitly out of scope until this core pipeline is proven to be 100% robust and reliable.*

---

## **Principles of Development (Project Constitution)**

This project is governed by a strict set of principles to ensure focus and prevent technical debt. All team members, human and AI, must adhere to these rules.

1.  **Single Responsibility Principle:** Every file must do one thing well. We will not create monolithic scripts that mix concerns like API calls, file I/O, and business logic.
2.  **Test-Driven Development (TDD):** No feature is complete until it has a passing `pytest` test. New features should begin by writing a failing test first.
3.  **The "Staircase" Model:** We will build one small, verifiable piece of functionality at a time. We will not work on Step 2 until Step 1 is proven. We will not build a "roof" before the "foundation" is solid.
4.  **"Less is More" Philosophy:** Success is not measured by lines of code written. It is measured by the simplicity, elegance, and reliability of the solution. New dependencies and new files must be aggressively challenged and justified.
5.  **No Mocking Core Functionality:** The core pipeline must be tested against real services. We will not use placeholder data (like `SAMPLE_TRANSCRIPTS`) for the core workflow, as this creates a dangerous illusion of progress.

## Getting Started

1.  Create a virtual environment.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Set the `RUNPOD_ENDPOINT` environment variable.
4.  Run the test suite: `pytest` 