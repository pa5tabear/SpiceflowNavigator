"""Generate short strategic summaries from transcripts."""

from __future__ import annotations

import re
from textwrap import shorten


class StrategicAnalyzer:
    """Heuristic analyzer for podcast transcripts."""

    def __init__(self, keywords: list[str] | None = None) -> None:
        default = [
            "strategy",
            "revenue",
            "growth",
            "roadmap",
            "competition",
        ]
        self.keywords = [k.lower() for k in (keywords or default)]

    # ------------------------------------------------------------------
    def analyze(self, transcript: str, max_words: int = 40) -> str:
        """Return a short summary focusing on strategic sentences."""

        sentences = re.split(r"(?<=[.!?])\s+", transcript.strip())
        picked: list[str] = []
        for sentence in sentences:
            text = sentence.lower()
            if any(k in text for k in self.keywords):
                picked.append(sentence.strip())
                if len(" ".join(picked).split()) >= max_words:
                    break
        if not picked:
            picked = sentences[:1]
        summary = " ".join(picked)
        return shorten(summary, width=max_words * 6, placeholder="...")

