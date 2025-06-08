import sys
import time

sys.modules.pop("requests", None)
import requests

def test_runpod_api_ping():
    start = time.time()
    resp = requests.get("https://api.runpod.ai/status", timeout=2)
    duration = time.time() - start
    assert resp.status_code == 200 and duration < 2
