import os
import sys
from pathlib import Path
from types import SimpleNamespace
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

# Provide a lightweight stand-in for the requests module so that the client can
# be imported without the real dependency installed.
requests_stub = SimpleNamespace(get=lambda *a, **k: None, post=lambda *a, **k: None)
sys.modules.setdefault("requests", requests_stub)

from spiceflow.clients.runpod_client import RunPodClient


class DummyResponse:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json_data = json_data or {}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}")

    def json(self):
        return self._json_data


def test_init_requires_endpoint(monkeypatch):
    monkeypatch.delenv("RUNPOD_ENDPOINT", raising=False)
    with pytest.raises(ValueError):
        RunPodClient()


def test_init_from_env(monkeypatch):
    monkeypatch.setenv("RUNPOD_ENDPOINT", "http://api")
    client = RunPodClient()
    assert client.endpoint == "http://api"


def test_check_health_success(monkeypatch):
    def fake_get(url, timeout):
        assert url == "http://api/healthz"
        return DummyResponse()

    client = RunPodClient("http://api")
    import requests
    monkeypatch.setattr(requests, "get", fake_get)
    assert client.check_health() is True


def test_check_health_failure(monkeypatch):
    def fake_get(url, timeout):
        raise Exception("boom")

    client = RunPodClient("http://api")
    import requests
    monkeypatch.setattr(requests, "get", fake_get)
    with pytest.raises(RuntimeError):
        client.check_health()


def test_run_success(monkeypatch):
    def fake_post(url, json, timeout):
        assert url == "http://api/run"
        assert json == {"foo": "bar"}
        return DummyResponse(json_data={"id": "123"})

    client = RunPodClient("http://api")
    import requests
    monkeypatch.setattr(requests, "post", fake_post)
    assert client.run({"foo": "bar"}) == "123"


def test_run_missing_id(monkeypatch):
    def fake_post(url, json, timeout):
        return DummyResponse(json_data={})

    client = RunPodClient("http://api")
    import requests
    monkeypatch.setattr(requests, "post", fake_post)
    with pytest.raises(RuntimeError):
        client.run({})


def test_status(monkeypatch):
    def fake_get(url, timeout):
        assert url == "http://api/status/123"
        return DummyResponse(json_data={"status": "done"})

    client = RunPodClient("http://api")
    import requests
    monkeypatch.setattr(requests, "get", fake_get)
    assert client.status("123") == {"status": "done"}
