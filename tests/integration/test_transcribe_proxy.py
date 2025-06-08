import os
import wave
import pytest

from spiceflow.clients.runpod_client import RunPodClient


@pytest.mark.integration
@pytest.mark.skipif(
    not os.environ.get("RUNPOD_ENDPOINT"),
    reason="RUNPOD_ENDPOINT not set",
)
def test_transcribe_proxy(tmp_path):
    audio_file = tmp_path / "temp.wav"
    with wave.open(str(audio_file), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(b"\x00\x00" * 16000)
    client = RunPodClient()
    result = client.run(
        str(audio_file),
        model="Systran/faster-whisper-large-v3",
        task="transcribe",
        temperature=0.0,
        stream=False,
    )
    assert isinstance(result, str) and result.strip()
