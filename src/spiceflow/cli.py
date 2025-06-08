import argparse
from spiceflow.clients.runpod_client import RunPodClient


def main(argv=None):
    """Entry point for the CLI."""
    parser = argparse.ArgumentParser(description="Transcribe audio using RunPod")
    parser.add_argument("audio_url", help="URL of the audio file to transcribe")
    args = parser.parse_args(argv)

    client = RunPodClient()
    result = client.run(
        args.audio_url,
        model="Systran/faster-whisper-large-v3",
        task="transcribe",
        temperature=0.0,
        stream=False,
    )
    print(result)


if __name__ == "__main__":
    main()
