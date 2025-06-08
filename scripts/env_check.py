import os
import sys
import requests


def main() -> None:
    ok = True
    endpoint = os.getenv("RUNPOD_ENDPOINT")
    if not endpoint:
        print("Missing RUNPOD_ENDPOINT", file=sys.stderr)
        ok = False
    else:
        try:
            requests.get(endpoint, timeout=5).raise_for_status()
        except Exception as exc:  # pragma: no cover
            print(f"Health check failed: {exc}", file=sys.stderr)
            ok = False
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
