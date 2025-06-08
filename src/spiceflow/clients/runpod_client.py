import os
from pathlib import Path
from gradio_client import Client
import requests


class RunPodClient:
    """Client for interacting with a Gradio-based RunPod endpoint."""

    def __init__(self, endpoint: str | None = None) -> None:
        self.endpoint = (endpoint or os.getenv("RUNPOD_ENDPOINT", "")).rstrip("/")
        if not self.endpoint:
            raise ValueError("RUNPOD_ENDPOINT not set")
        self.client = Client(self.endpoint)

    # ------------------------------------------------------------------
    def transcribe(
        self,
        file_path: str | Path,
        *,
        model: str = "Systran/faster-whisper-large-v3",
        task: str = "transcribe",
        timeout: int = 10,
        stream: bool = False,
    ) -> str:
        """Return the transcript for the given audio file."""

        requests.get(self.endpoint, timeout=timeout).raise_for_status()
        return self.client.predict(
            str(file_path),
            model,
            task,
            0.0,
            stream=stream,
            api_name="/predict",
        )
