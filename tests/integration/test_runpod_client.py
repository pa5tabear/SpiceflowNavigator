import os
from pathlib import Path
import pytest

from spiceflow.clients.runpod_client import RunPodClient

TEST_AUDIO = Path(__file__).resolve().parents[1] / "fixtures" / "test_audio.wav"


@pytest.mark.integration
@pytest.mark.skipif(
    not os.environ.get("RUNPOD_ENDPOINT"), reason="RUNPOD_ENDPOINT not set"
)
def test_runpod_client_transcribe_live():
    assert TEST_AUDIO.exists(), "Test audio file missing"
    client = RunPodClient()
    result = client.transcribe(str(TEST_AUDIO))
    assert isinstance(result, str) and result.strip()
