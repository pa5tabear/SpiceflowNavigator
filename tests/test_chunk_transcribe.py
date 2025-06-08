import json
import sys
from pathlib import Path
import types

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import scripts.chunk_and_transcribe as mod


def test_chunk_and_transcribe(monkeypatch, tmp_path):
    xml = "<rss><channel><item><enclosure url='http://example.com/a.mp3'/></item></channel></rss>"

    def fake_get(url, timeout=10, stream=False):
        return types.SimpleNamespace(text=xml, raise_for_status=lambda: None)

    monkeypatch.setattr(mod.requests, "get", fake_get)

    audio_path = tmp_path / "clip.mp3"
    def fake_download(url, path):
        path.write_text("audio")
    monkeypatch.setattr(mod, "download_clip", fake_download)

    result_json = tmp_path / "out.json"
    monkeypatch.setattr(mod, "OUTPUT_AUDIO", audio_path)
    monkeypatch.setattr(mod, "TRANSCRIPT_PATH", result_json)

    dummy_client = types.SimpleNamespace(transcribe=lambda p: "hi")
    monkeypatch.setattr(mod, "RunPodClient", lambda: dummy_client)

    mod.main()
    data = json.loads(result_json.read_text())
    assert data["transcript"] == "hi"
