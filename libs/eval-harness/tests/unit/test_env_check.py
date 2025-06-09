import sys
from pathlib import Path
import types
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import scripts.env_check as env_check


def test_env_check_pass(monkeypatch):
    monkeypatch.setenv("RUNPOD_ENDPOINT", "y")

    def fake_get(url, timeout):
        return types.SimpleNamespace(raise_for_status=lambda: None)

    monkeypatch.setattr(env_check.requests, "get", fake_get)

    with pytest.raises(SystemExit) as exc:
        env_check.main()
    assert exc.value.code == 0


def test_env_check_fail(monkeypatch):
    monkeypatch.setenv("RUNPOD_ENDPOINT", "y")

    def fake_get(url, timeout):
        raise env_check.requests.RequestException("offline")

    monkeypatch.setattr(env_check.requests, "get", fake_get)

    with pytest.raises(SystemExit) as exc:
        env_check.main()
    assert exc.value.code == 1


def test_env_check_missing_env(monkeypatch):
    monkeypatch.delenv("RUNPOD_ENDPOINT", raising=False)
    monkeypatch.setattr(env_check.requests, "get", lambda *a, **k: None)

    with pytest.raises(SystemExit) as exc:
        env_check.main()
    assert exc.value.code == 1
