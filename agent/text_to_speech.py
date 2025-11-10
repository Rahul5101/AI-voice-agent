from TTS.api import TTS
import uuid
from pathlib import Path

class SpeechSynthesizer:
    def __init__(self, model_name="tts_models/en/vctk/vits"):
        self.tts = TTS(model_name)
        self.output_dir = Path("static/voices")
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def synthesize(self, text: str):
        filename = f"{uuid.uuid4()}.wav"
        file_path = self.output_dir / filename
        self.tts.tts_to_file(text=text, file_path=str(file_path),speaker=self.tts.speakers[0])
        return f"/static/voices/{filename}"
 