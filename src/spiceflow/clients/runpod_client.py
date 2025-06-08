import os
from pathlib import Path
from gradio_client import Client


class RunPodClient:
    """Client for interacting with a Gradio-based RunPod endpoint."""

    def __init__(self, endpoint: str | None = None, *, timeout: int = 300) -> None:
        self.endpoint = (endpoint or os.getenv("RUNPOD_ENDPOINT", "")).rstrip("/")
        if not self.endpoint:
            raise ValueError("RUNPOD_ENDPOINT not set")
        self.client = Client(self.endpoint, timeout=timeout)

    # ------------------------------------------------------------------
    def transcribe(
        self,
        file_path: str | Path,
        *,
        model: str = "Systran/faster-whisper-large-v3",
        task: str = "transcribe",
        stream: bool = False,
    ) -> str:
        """Return the transcript for the given audio file."""

        return self.client.predict(
            str(file_path),
            model,
            task,
            0.0,
            stream=stream,
            api_name="/predict",
        )
