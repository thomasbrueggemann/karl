
import speech_recognition as sr

class Ears:
    __energy_threshold = 1000 # Energy level for mic to detect

    def __init__(self):
        self.recorder = sr.Recognizer()
        self.recorder.energy_threshold = self.__energy_threshold
        # Dynamic energy compensation lowers the energy threshold dramatically to a point where the SpeechRecognizer never stops recording.
        self.recorder.dynamic_energy_threshold = False

    def listen(self):
        with sr.Microphone() as source:

            self.recorder.adjust_for_ambient_noise(source)

            print(">")
            audio = self.recorder.listen(source)

        result = self.recorder.recognize_whisper(audio, language="english")

        if result is None or len(result) == 0:
            return None
        
        print("You:" + result)
        return result