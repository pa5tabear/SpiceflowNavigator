import os
import subprocess
import sys
from pathlib import Path


def main() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(Path(__file__).resolve().parents[1] / "src")

    subprocess.run([sys.executable, "scripts/env_check.py"], check=True, env=env)

    result = subprocess.run(
        [sys.executable, "run_transcription_job.py"],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    job_id = result.stdout.strip()

    status_result = subprocess.run(
        [sys.executable, "scripts/job_status_checker.py", job_id],
        capture_output=True,
        text=True,
        check=True,
        env=env,
    )
    print(status_result.stdout.strip())


if __name__ == "__main__":
    main()
