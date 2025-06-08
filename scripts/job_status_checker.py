import os
import sys
from spiceflow.clients.runpod_client import RunPodClient


def main(job_id: str | None = None) -> None:
    if not job_id:
        print("Usage: job_status_checker.py JOB_ID", file=sys.stderr)
        sys.exit(1)

    if not os.getenv("RUNPOD_API_KEY"):
        raise RuntimeError("RUNPOD_API_KEY not set")

    endpoint_env = os.getenv("RUNPOD_ENDPOINT")
    if not endpoint_env:
        raise RuntimeError("RUNPOD_ENDPOINT not set")
    client = RunPodClient(endpoint_env)
    status = client.status(job_id)["status"]

    print(status)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
