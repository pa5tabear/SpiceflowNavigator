#!/usr/bin/env python
"""Generate a short non-silent WAV file for tests."""

import argparse
import math
import struct
import wave
from pathlib import Path


def generate(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    framerate = 16000
    duration = 1
    amplitude = 32767
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(framerate)
        for i in range(framerate * duration):
            sample = int(amplitude * math.sin(2 * math.pi * 440 * i / framerate))
            wf.writeframes(struct.pack("<h", sample))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output",
        nargs="?",
        default="tests/fixtures/test_audio.wav",
        help="Path to output WAV file",
    )
    args = parser.parse_args()
    generate(Path(args.output))


if __name__ == "__main__":
    main()
