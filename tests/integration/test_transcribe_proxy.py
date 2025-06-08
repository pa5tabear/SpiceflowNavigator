import os
import wave
import pytest

from spiceflow.clients.runpod_client import RunPodClient
from spiceflow.cli import main as cli_main
from spiceflow.analyzer import StrategicAnalyzer
from spiceflow.config import load_feeds
from spiceflow.rss_parser import RSSParser
from spiceflow.workflow import WorkflowManager


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
    try:
        result = client.transcribe(str(audio_file))
    except Exception as exc:  # pragma: no cover - network issue
        pytest.skip(f"proxy call failed: {exc}")
    assert isinstance(result, str) and result.strip()


def test_rss_and_analysis(tmp_path):
    yaml_path = tmp_path / "feeds.yml"
    yaml_path.write_text(
        "feeds:\n  - name: Test\n    url: http://a\n    strategic_importance: 1\n"
    )
    feeds = load_feeds(yaml_path)
    assert feeds[0].name == "Test"
    analyzer = StrategicAnalyzer()
    summary = analyzer.analyze("Our growth strategy is solid.")
    assert "strategy" in summary.lower()


def test_cli_and_workflow(tmp_path, monkeypatch):
    class DummyClient:
        def __init__(self, endpoint=None):
            self.calls = []

        def transcribe(self, path):
            self.calls.append(path)
            return "hi"

    monkeypatch.setattr("spiceflow.cli.RunPodClient", DummyClient)
    cli_main(["file.wav"])

    parser = RSSParser()
    xml = "<rss><channel><item><enclosure url='a.mp3'/></item><item><enclosure url='b.mp3'/></item></channel></rss>"
    monkeypatch.setattr("spiceflow.workflow.RSSParser", lambda: parser)
    monkeypatch.setattr(
        "spiceflow.workflow.requests.get",
        lambda url: type(
            "R", (), {"text": xml, "raise_for_status": lambda self: None}
        )(),
    )
    monkeypatch.setattr("spiceflow.workflow.RunPodClient", lambda: DummyClient())
    manager = WorkflowManager("http://feed", transcripts_dir=tmp_path)
    manager.run()
    files = sorted(tmp_path.glob("*.md"))
    assert len(files) == 2
