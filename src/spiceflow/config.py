from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import yaml

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[2] / "config" / "rss_feeds.yml"


@dataclass
class RSSFeed:
    name: str
    url: str
    strategic_importance: int


def load_feeds(path: str | Path = DEFAULT_CONFIG_PATH) -> list[RSSFeed]:
    with open(path) as fh:
        data = yaml.safe_load(fh) or {}
    feeds = data.get("feeds")
    if not isinstance(feeds, list):
        raise ValueError("'feeds' must be a list")
    result: list[RSSFeed] = []
    for item in feeds:
        if not isinstance(item, dict):
            raise ValueError("feed entry must be a mapping")
        try:
            name = item["name"]
            url = item["url"]
            importance = item["strategic_importance"]
        except KeyError as exc:
            raise ValueError(f"missing field: {exc.args[0]}") from exc
        result.append(RSSFeed(name=name, url=url, strategic_importance=int(importance)))
    return result
