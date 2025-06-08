import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from spiceflow.clients.runpod_client import RunPodClient


class DummyClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.calls = []

    def predict(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        return "dummy-result"


def test_init_requires_endpoint(monkeypatch):
    monkeypatch.delenv("RUNPOD_ENDPOINT", raising=False)
    with pytest.raises(ValueError):
        RunPodClient()


def test_init_from_env(monkeypatch):
    dummy = DummyClient("http://api")
    monkeypatch.setenv("RUNPOD_ENDPOINT", "http://api")
    monkeypatch.setattr(
        "spiceflow.clients.runpod_client.Client", lambda endpoint: dummy
    )
    client = RunPodClient()
    assert client.endpoint == "http://api"
    assert client.client is dummy


def test_run_calls_predict(monkeypatch):
    dummy = DummyClient("http://api")
    monkeypatch.setattr(
        "spiceflow.clients.runpod_client.Client", lambda endpoint: dummy
    )
    client = RunPodClient("http://api")
    result = client.run("file.wav", "model", "task", 0.1, False)
    assert result == "dummy-result"
    assert dummy.calls == [
        (
            ("file.wav", "model", "task", 0.1),
            {"stream": False, "api_name": "/predict"},
        )
    ]


def test_status_calls_requests(monkeypatch):
    dummy = DummyClient("http://api")
    monkeypatch.setattr(
        "spiceflow.clients.runpod_client.Client", lambda endpoint: dummy
    )

    calls: list[tuple[str, int]] = []

    class FakeResp:
        def __init__(self, data: dict) -> None:
            self.data = data

        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict:
            return self.data

    def fake_get(url: str, timeout: int) -> FakeResp:
        calls.append((url, timeout))
        return FakeResp({"status": "COMPLETED"})

    monkeypatch.setattr("spiceflow.clients.runpod_client.requests.get", fake_get)
    client = RunPodClient("http://api")
    result = client.status("123")
    assert result == {"status": "COMPLETED"}
    assert calls == [("http://api/status/123", 10)]
