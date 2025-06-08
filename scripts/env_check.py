import os
import sys

if __name__ == "__main__":
    print("Python", sys.version)
    print("PATH", os.environ.get("PATH", ""))
    endpoint = os.getenv("RUNPOD_ENDPOINT", "")
    print("RUNPOD_ENDPOINT length", len(endpoint))
