import subprocess

def download_audio(video_url, filename="audio.mp3"):
    try:
        print("[INFO] Downloading audio with yt-dlp...")
        command = [
            "yt-dlp",
            "-x", "--audio-format", "mp3",
            "-o", filename,
            video_url
        ]
        subprocess.run(command, check=True)
        print("[INFO] Audio downloaded successfully.")
        return filename
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to download audio: {e}")
        return None
