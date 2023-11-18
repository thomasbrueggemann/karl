
import speech_recognition as sr
import openai
import tempfile
from pathlib import Path

class Ears:
    __energy_threshold = 1000 # Energy level for mic to detect
    __listen_timeout = 2 # Seconds to listen for
    __pause_threshold = 0.75 # Seconds of non-speaking audio before a phrase is considered complete
    __dynamic_energy_threshold = False # Dynamic energy compensation lowers the energy threshold dramatically to a point where the SpeechRecognizer never stops recording.

    def __init__(self, openai_api_key):
        self.openai_client = openai.OpenAI(api_key=openai_api_key)

        self.recorder = sr.Recognizer()
        self.recorder.energy_threshold = self.__energy_threshold
        self.recorder.pause_threshold = self.__pause_threshold
        self.recorder.dynamic_energy_threshold = self.__dynamic_energy_threshold


    def listen(self):
        with sr.Microphone() as source:
            self.recorder.adjust_for_ambient_noise(source, duration=1)

            print(">")
            audio = self.recorder.listen(source, timeout=self.__listen_timeout)

        print("...")

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=True) as temp_file:
            temp_file.write(audio.get_wav_data())
            temp_file_path = Path(temp_file.name)

            transcription = self.openai_client.audio.transcriptions.create(model="whisper-1", file=temp_file_path)
            result = transcription.text

        if result is None or len(result) == 0:
            return None

        print("You:" + result)

        return result