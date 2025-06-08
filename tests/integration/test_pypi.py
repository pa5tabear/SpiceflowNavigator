import sys
import time

sys.modules.pop("requests", None)
import requests

def test_pypi_reachable():
    start = time.time()
    resp = requests.get("https://pypi.org/simple/requests/", timeout=2)
    duration = time.time() - start
    assert resp.status_code == 200 and duration < 2
