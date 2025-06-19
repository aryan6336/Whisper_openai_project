import whisper

# 2. Transcribe audio using Whisper
def transcribe_audio(path):
    model = whisper.load_model("base")  # or 'small', 'medium', 'large'
    result = model.transcribe(path)
    return result['text']