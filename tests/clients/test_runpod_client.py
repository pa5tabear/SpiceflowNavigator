import sys
from pathlib import Path
import pytest
import types

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from spiceflow.clients.runpod_client import RunPodClient


class DummyClient:
    def __init__(self, endpoint, timeout=0):
        self.endpoint = endpoint
        self.timeout = timeout
        self.calls = []

    def predict(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        return "dummy-result"


def test_init_requires_endpoint(monkeypatch):
    monkeypatch.delenv("RUNPOD_ENDPOINT", raising=False)
    with pytest.raises(ValueError):
        RunPodClient()


def test_init_from_env(monkeypatch):
    dummy = DummyClient("http://api", timeout=0)
    monkeypatch.setenv("RUNPOD_ENDPOINT", "http://api")

    captured = {}

    def dummy_client(endpoint, httpx_kwargs=None, **kwargs):
        captured["timeout"] = httpx_kwargs.get("timeout") if httpx_kwargs else None
        return dummy

    monkeypatch.setattr("spiceflow.clients.runpod_client.Client", dummy_client)
    client = RunPodClient()
    assert client.endpoint == "http://api"
    assert client.client is dummy
    assert captured["timeout"] >= 300


def test_transcribe_calls_predict(monkeypatch):
    dummy = DummyClient("http://api")
    monkeypatch.setattr(
        "spiceflow.clients.runpod_client.Client",
        lambda endpoint, httpx_kwargs=None, **kwargs: dummy,
    )
    monkeypatch.setattr(
        "spiceflow.clients.runpod_client.utils.handle_file", lambda p: p
    )
    client = RunPodClient("http://api")
    result = client.transcribe("file.wav")
    assert result == "dummy-result"
    assert dummy.calls == [
        (
            ("file.wav", "Systran/faster-whisper-large-v3", "transcribe", 0.0),
            {"stream": False, "api_name": "/predict"},
        )
    ]

    from spiceflow.analyzer import StrategicAnalyzer
    from spiceflow.config import load_feeds

    StrategicAnalyzer().analyze("Roadmap")
    feeds = load_feeds(Path("config/rss_feeds.yml"))
    assert feeds

    from spiceflow import cli
    from spiceflow.workflow import WorkflowManager
    from spiceflow.rss_parser import RSSParser

    dummy_c = types.SimpleNamespace(transcribe=lambda p: "ok")
    monkeypatch.setattr(cli, "RunPodClient", lambda: dummy_c)
    cli.main(["http://foo/bar.wav"])

    wm = WorkflowManager(
        "http://feed",
        transcripts_dir=Path("tmp"),
        parser=RSSParser(),
        client=dummy_c,
    )
    monkeypatch.setattr(
        "spiceflow.workflow.requests.get",
        lambda url: types.SimpleNamespace(
            text="<rss></rss>", raise_for_status=lambda: None
        ),
    )
    wm.get_recent_audio_urls()
    wm._path_for_url("http://example.com/a.mp3")
