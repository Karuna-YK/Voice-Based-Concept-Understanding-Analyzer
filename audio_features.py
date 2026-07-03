import librosa

def extract_audio_features(audio_path):
    y, sr = librosa.load(audio_path)

    duration = librosa.get_duration(y=y, sr=sr)

    return {
        "Duration": round(duration, 2),
        "Sample Rate": sr
    }