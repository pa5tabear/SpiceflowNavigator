import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from spiceflow import cli


def test_cli(monkeypatch, capsys):
    dummy_url = "http://example.com/audio.wav"
    with patch("spiceflow.cli.RunPodClient") as MockClient:
        instance = MockClient.return_value
        instance.run.return_value = "dummy-transcript"

        cli.main([dummy_url])

        instance.run.assert_called_once_with(
            dummy_url,
            model="Systran/faster-whisper-large-v3",
            task="transcribe",
            temperature=0.0,
            stream=False,
        )

    captured = capsys.readouterr()
    assert captured.out.strip() == "dummy-transcript"
