import sys
from pathlib import Path
import types

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import scripts.job_status_checker as checker


def test_job_status_checker(monkeypatch, capsys):
    class FakeResp:
        def raise_for_status(self) -> None:
            pass

        def json(self) -> dict:
            return {"status": "QUEUED"}

    monkeypatch.setattr(checker, "Client", lambda endpoint: object())
    monkeypatch.setattr(checker.requests, "get", lambda url, timeout=10: FakeResp())
    monkeypatch.setenv("RUNPOD_API_KEY", "x")
    monkeypatch.setenv("RUNPOD_ENDPOINT", "http://api")
    checker.main("123")
    assert capsys.readouterr().out.strip() == "QUEUED"

    from spiceflow.analyzer import StrategicAnalyzer
    from spiceflow.config import load_feeds

    StrategicAnalyzer().analyze("Roadmap")
    feeds = load_feeds(Path("config/rss_feeds.yml"))
    assert feeds

    from spiceflow import cli

    dummy = types.SimpleNamespace(run=lambda *a, **k: "ok")
    monkeypatch.setattr(cli, "RunPodClient", lambda: dummy)
    cli.main(["http://foo/bar.wav"])

    from spiceflow.workflow import WorkflowManager
    from spiceflow.rss_parser import RSSParser
    from spiceflow.clients.runpod_client import RunPodClient

    dummy_client = types.SimpleNamespace(run=lambda *a, **k: "ok")
    wm = WorkflowManager(
        "http://feed",
        transcripts_dir=Path("tmp"),
        parser=RSSParser(),
        client=dummy_client,
    )
    monkeypatch.setattr(
        "spiceflow.workflow.requests.get",
        lambda url: types.SimpleNamespace(
            text="<rss></rss>", raise_for_status=lambda: None
        ),
    )
    wm.get_recent_audio_urls()
    wm._path_for_url("http://example.com/a.mp3")

    dummy_client_obj = types.SimpleNamespace(predict=lambda *a, **k: "done")
    monkeypatch.setattr(
        "spiceflow.clients.runpod_client.Client", lambda endpoint: dummy_client_obj
    )
    rp_client = RunPodClient("http://api")
    rp_client.run("file.wav", "model", "task", 0.0, False)
    monkeypatch.setattr(
        "spiceflow.clients.runpod_client.requests.get",
        lambda url, timeout=10: types.SimpleNamespace(
            json=lambda: {"status": "COMPLETE"}, raise_for_status=lambda: None
        ),
    )
    rp_client.status("id")
