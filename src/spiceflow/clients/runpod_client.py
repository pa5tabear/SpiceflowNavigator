import os
from pathlib import Path
from gradio_client import Client
from gradio_client import utils


class RunPodClient:
    """Client for interacting with a Gradio-based RunPod endpoint."""

    def __init__(self, endpoint: str | None = None, *, timeout: int = 300) -> None:
        self.endpoint = (endpoint or os.getenv("RUNPOD_ENDPOINT", "")).rstrip("/")
        if not self.endpoint:
            raise ValueError("RUNPOD_ENDPOINT not set")
        self.client = Client(
            self.endpoint,
            httpx_kwargs={"timeout": max(timeout, 300)},
        )

    # ------------------------------------------------------------------
    def transcribe(self, file_path: str | Path) -> str:
        """Return the transcript for the given audio file."""

        return self.client.predict(
            utils.handle_file(str(file_path)),
            "Systran/faster-whisper-large-v3",
            "transcribe",
            0.0,
            stream=False,
            api_name="/predict",
        )
