import os
import sys
import time
import pytest

# Ensure we use the real requests module for this live test.
sys.modules.pop("requests", None)
try:
    import requests  # noqa: F401
except Exception:  # pragma: no cover - skip if requests is missing
    pytest.skip("requests library not installed", allow_module_level=True)

from spiceflow.clients.runpod_client import RunPodClient

AUDIO_URL = "https://filesamples.com/samples/audio/mp3/sample1.mp3"


@pytest.mark.integration
@pytest.mark.skipif(
    not os.environ.get("RUNPOD_ENDPOINT"),
    reason="RUNPOD_ENDPOINT not set",
)
def test_runpod_live_transcription():
    """Verify that the RunPod API returns a transcript for a sample audio."""
    client = RunPodClient()
    job_id = client.run({"input": {"audio_url": AUDIO_URL}})

    # Poll for completion with a timeout
    status = {}
    for _ in range(30):
        status = client.status(job_id)
        if status.get("status") in {"COMPLETED", "completed"}:
            break
        time.sleep(2)
    else:
        pytest.fail(f"Job {job_id} did not complete: {status}")

    transcript = None
    output = status.get("output") or {}
    transcript = output.get("transcript") or output.get("text")
    assert isinstance(transcript, str) and transcript.strip()
