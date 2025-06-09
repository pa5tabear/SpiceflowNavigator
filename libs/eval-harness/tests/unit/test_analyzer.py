import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from spiceflow.analyzer import StrategicAnalyzer


def test_analyze_selects_keyword_sentence():
    text = "Intro. Our growth strategy focuses on revenue. Final line."
    analyzer = StrategicAnalyzer()
    summary = analyzer.analyze(text)
    assert "growth strategy" in summary


def test_analyze_defaults_to_first_sentence():
    text = "Hello world. Nothing special here."
    analyzer = StrategicAnalyzer(keywords=["nonexistent"])
    summary = analyzer.analyze(text)
    assert summary.startswith("Hello world.")


def test_analyze_respects_max_words():
    text = "Strategy growth revenue competition. Extra details." * 3
    analyzer = StrategicAnalyzer()
    summary = analyzer.analyze(text, max_words=5)
    assert len(summary.split()) <= 5

