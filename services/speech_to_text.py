import whisper
import os

# Load Whisper model (small model)
model = whisper.load_model("base")

def convert_speech_to_text(audio_file):
    """
    Converts speech audio into text using Whisper.
    """
    result = model.transcribe(audio_file)
    return result["text"]
