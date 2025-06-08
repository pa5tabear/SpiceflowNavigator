# Sandbox Blocker

The acceptance criteria require hitting a RunPod API endpoint that returns HTTP 200 in under two seconds.
All publicly documented URLs such as `https://api.runpod.ai/status`, `/health`, and `/healthz` respond with HTTP 404.
Without a working endpoint we cannot implement `tests/integration/test_ping.py` to satisfy the requirement.

Proposed next step: confirm the correct RunPod status URL or relax the requirement to allow any reachable endpoint.
