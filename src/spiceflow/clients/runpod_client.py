import os
import requests

class RunPodClient:
    """Lightweight helper for RunPod endpoints.

    It exposes convenience methods to start asynchronous jobs via ``/run`` and
    to poll their status via ``/status/<id>``. The base endpoint is read from the
    ``RUNPOD_ENDPOINT`` environment variable unless explicitly provided.
    """

    def __init__(self, endpoint: str | None = None) -> None:
        self.endpoint = (endpoint or os.getenv("RUNPOD_ENDPOINT", "")).rstrip("/")
        if not self.endpoint:
            raise ValueError("RUNPOD_ENDPOINT not set")

    def check_health(self, timeout: int = 5) -> bool:
        """Ping /healthz and raise RuntimeError on failure."""
        url = f"{self.endpoint}/healthz"
        try:
            resp = requests.get(url, timeout=timeout)
            resp.raise_for_status()
            return True
        except Exception as exc:
            raise RuntimeError(f"RunPod health check failed: {exc}") from exc

    # ------------------------------------------------------------------
    def run(self, payload: dict, timeout: int = 30) -> str:
        """Submit a job to ``/run`` and return the job ID."""
        url = f"{self.endpoint}/run"
        resp = requests.post(url, json=payload, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        job_id = data.get("id") or data.get("job_id")
        if not job_id:
            raise RuntimeError(f"RunPod run failed: no job id in {data}")
        return str(job_id)

    def status(self, job_id: str, timeout: int = 30) -> dict:
        """Return status dictionary for a given job ID."""
        url = f"{self.endpoint}/status/{job_id}"
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.json()
