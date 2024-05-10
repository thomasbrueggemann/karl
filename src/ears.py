from vosk import Model, KaldiRecognizer
import pyaudio

class Ears:

    def __init__(self):
        print("Ears are open")
        model = Model(r"/Users/thomas/Downloads/vosk-model-small-en-us-0.15")
        self.recognizer = KaldiRecognizer(model, 16000)

        mic = pyaudio.PyAudio()
        self.stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    def listen(self):
        self.stream.start_stream()
        data = self.stream.read(4096)
	
        if self.recognizer.AcceptWaveform(data):
            self.stream.stop_stream()
            
            text = self.recognizer.Result()
            print("You: " + text[14:-3])
        
            return text[14:-3]