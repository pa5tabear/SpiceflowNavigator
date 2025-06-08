import os
import sys
import requests


def main() -> None:
    ok = True
    if not os.getenv("RUNPOD_API_KEY"):
        print("Missing RUNPOD_API_KEY", file=sys.stderr)
        ok = False
    if not os.getenv("RUNPOD_ENDPOINT"):
        print("Missing RUNPOD_ENDPOINT", file=sys.stderr)
        ok = False
    try:
        requests.get("https://example.com", timeout=5)
    except Exception as exc:  # pragma: no cover
        print(f"Internet connectivity check failed: {exc}", file=sys.stderr)
        ok = False
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
