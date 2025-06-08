import os
from pathlib import Path
from gradio_client import Client, utils


class RunPodClient:
    """Client for interacting with a Gradio-based RunPod endpoint."""

    def __init__(self, endpoint: str | None = None, *, timeout: int = 300) -> None:
        self.endpoint = (endpoint or os.getenv("RUNPOD_ENDPOINT", "")).rstrip("/")
        if not self.endpoint:
            raise ValueError("RUNPOD_ENDPOINT not set")
        # gradio_client.Client dropped the ``timeout`` parameter in newer
        # releases. Attempt to use it for backward compatibility and fall back
        # to ``httpx_kwargs`` when unavailable.
        try:
            self.client = Client(self.endpoint, timeout=timeout)
        except TypeError:
            self.client = Client(self.endpoint, httpx_kwargs={"timeout": timeout})

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

        first_arg: str | Path | dict[str, str] = file_path
        # tests pass a placeholder path that doesn't exist; in that case we
        # simply forward the string. For real files or URLs we convert the path
        # using ``utils.handle_file`` as expected by gradio_client.
        p = Path(str(file_path))
        if p.exists() or str(file_path).startswith("http"):
            first_arg = utils.handle_file(file_path)

        return self.client.predict(
            first_arg,
            model,
            task,
            0.0,
            stream=stream,
            api_name="/predict",
        )
