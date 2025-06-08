import os
from gradio_client import Client

class RunPodClient:
    """Client for interacting with a Gradio-based RunPod endpoint."""

    def __init__(self, endpoint: str | None = None) -> None:
        self.endpoint = (endpoint or os.getenv("RUNPOD_ENDPOINT", "")).rstrip("/")
        if not self.endpoint:
            raise ValueError("RUNPOD_ENDPOINT not set")
        self.client = Client(self.endpoint)

    # ------------------------------------------------------------------
    def run(
        self,
        file_path: str,
        model: str,
        task: str,
        temperature: float,
        stream: bool,
    ) -> str:
        """Call the Gradio predict endpoint and return the result."""

        return self.client.predict(
            file_path,
            model,
            task,
            temperature,
            stream=stream,
            api_name="/predict",
        )
