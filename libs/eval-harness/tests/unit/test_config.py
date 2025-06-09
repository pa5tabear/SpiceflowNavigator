import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from spiceflow import config


def test_config_loader_structured(tmp_path):
    sample = tmp_path / "feeds.yml"
    sample.write_text(
        """
feeds:
  - name: Example
    url: https://example.com/feed
    strategic_importance: 2
"""
    )
    feeds = config.load_feeds(sample)
    assert feeds[0].name == "Example"
    assert feeds[0].url == "https://example.com/feed"
    assert feeds[0].strategic_importance == 2
