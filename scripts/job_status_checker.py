import os
import sys
import runpod


def main(job_id: str | None = None) -> None:
    if not job_id:
        print("Usage: job_status_checker.py JOB_ID", file=sys.stderr)
        sys.exit(1)

    api_key = os.getenv("RUNPOD_API_KEY")
    if not api_key:
        raise RuntimeError("RUNPOD_API_KEY not set")
    runpod.api_key = api_key

    endpoint_env = os.getenv("RUNPOD_ENDPOINT")
    if not endpoint_env:
        raise RuntimeError("RUNPOD_ENDPOINT not set")
    if endpoint_env.startswith("http"):
        endpoint_id = endpoint_env.split("//", 1)[1].split(".")[0].split("-")[0]
    else:
        endpoint_id = endpoint_env

    status: str
    if hasattr(runpod, "get_job"):
        status = runpod.get_job(job_id)["status"]  # type: ignore[attr-defined]
    else:
        from runpod.endpoint.runner import RunPodClient

        client = RunPodClient()
        status = client.get(f"{endpoint_id}/status/{job_id}")["status"]

    print(status)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
