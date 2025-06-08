import os
import importlib.util
import http.client
from typing import List, Dict

REQUIRED_PACKAGES = ["pytest", "requests", "python-dotenv", "feedparser"]


def check_dependencies(packages: List[str]) -> Dict[str, bool]:
    results = {}
    for pkg in packages:
        spec = importlib.util.find_spec(pkg)
        results[pkg] = spec is not None
    return results


def check_secret(name: str) -> str | None:
    value = os.environ.get(name)
    if value and value.strip():
        return value
    return None


def check_network(host: str = "www.google.com", port: int = 80, timeout: int = 3) -> bool:
    try:
        conn = http.client.HTTPConnection(host, port, timeout=timeout)
        conn.request("HEAD", "/")
        conn.close()
        return True
    except Exception:
        return False


def format_status(passed: bool) -> str:
    return "✅" if passed else "❌"


def main() -> None:
    pkg_results = check_dependencies(REQUIRED_PACKAGES)
    endpoint = check_secret("RUNPOD_ENDPOINT")
    network_ok = check_network()

    print("# Environment Diagnostic Report\n")
    print("## Dependency Check")
    for pkg in REQUIRED_PACKAGES:
        print(f"*   [{format_status(pkg_results[pkg])}] {pkg}")

    print("\n## Secrets Check")
    if endpoint:
        display = endpoint[:12] + ("..." if len(endpoint) > 12 else "")
        print(f"*   [✅] RUNPOD_ENDPOINT: {display}")
    else:
        print("*   [❌] RUNPOD_ENDPOINT: Not Found")

    print("\n## Network Check")
    if network_ok:
        print("*   [✅] Internet Connectivity: Connected to www.google.com")
    else:
        print("*   [❌] Internet Connectivity: Failed to connect to www.google.com")

    print("\n## Summary")
    if all(pkg_results.values()) and endpoint and network_ok:
        conclusion = (
            "The environment has required dependencies, network access, and secrets."
        )
    else:
        conclusion = (
            "The environment is missing critical dependencies and/or network access."
        )
    action = (
        "Please ensure dependencies are pre-installed or that network access is enabled. "
        "RUNPOD_ENDPOINT must be injected as a secret."
    )
    print(f"*   **Conclusion:** {conclusion}")
    print(f"*   **Action Required:** {action}")


if __name__ == "__main__":
    main()
