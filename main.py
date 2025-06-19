import os
from audio_downloader import download_audio
from transcribe import transcribe_audio
from translator import translate_text

# 4. Full pipeline
def generate_translated_script(youtube_url, target_lang):
    print("[INFO] Downloading audio...")
    audio_path = download_audio(youtube_url)

    print("[INFO] Transcribing audio...")
    original_script = transcribe_audio(audio_path)

    print("[INFO] Translating script...")
    translated_script = translate_text(original_script,target_lang)

    return translated_script

# Example usage
if __name__ == "__main__":
    url = input("Enter YouTube video URL: ").strip()
    dest= input("Enter your target language:")
    translated_script = generate_translated_script(url,dest)
    print("\n[Translated Script]:\n", translated_script)
