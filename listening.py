import io
import os
from conversation_stage import ConversationStage
import speech_recognition as sr
import whisper
import torch

from datetime import datetime, timedelta
from queue import Queue
from tempfile import NamedTemporaryFile
from time import sleep
from sys import platform

class Listening(ConversationStage):
    __default_microphone = 'default'
    __phrase_timeout = 3 # How much empty space between recordings before we consider it a new line in the transcription
    __record_timeout = 2 # How real time the recording is in seconds
    __energy_threshold = 1000 # Energy level for mic to detect
    __whisper_model = 'base' # tiny, base, small, medium, large
    
    def __init__(self):
        self.phrase_time = None
        self.last_sample = bytes()
        self.data_queue = Queue()

        self.recorder = sr.Recognizer()
        self.recorder.energy_threshold = self.__energy_threshold
        # Dynamic energy compensation lowers the energy threshold dramatically to a point where the SpeechRecognizer never stops recording.
        self.recorder.dynamic_energy_threshold = False

        if 'linux' in platform:
            mic_name = self.__default_microphone
            if not mic_name or mic_name == 'list':
                print("Available microphone devices are: ")
                for index, name in enumerate(sr.Microphone.list_microphone_names()):
                    print(f"Microphone with name \"{name}\" found")
                return
            else:
                for index, name in enumerate(sr.Microphone.list_microphone_names()):
                    if mic_name in name:
                        self.source = sr.Microphone(sample_rate=16000, device_index=index)
                        break
        else:
            self.source = sr.Microphone(sample_rate=16000)

        if model != "large":
            model = model + ".en"
        
        self.audio_model = whisper.load_model(model)
        self.temp_file = NamedTemporaryFile().name

        self.recorder.adjust_for_ambient_noise(self.source)

    def start(self):

        def record_callback(_, audio:sr.AudioData) -> None:
            """
            Threaded callback function to receive audio data when recordings finish.
            audio: An AudioData containing the recorded bytes.
            """
            # Grab the raw bytes and push it into the thread safe queue.
            data = audio.get_raw_data()
            self.data_queue.put(data)
        
        self.recorder.listen_in_background(self.source, record_callback, phrase_time_limit=self.__record_timeout)
        
        while True:
            now = datetime.utcnow()

            # Pull raw recorded audio from the queue.
            if not data_queue.empty():
                phrase_complete = False

                # If enough time has passed between recordings, consider the phrase complete.
                # Clear the current working audio buffer to start over with the new data.
                if phrase_time and now - phrase_time > timedelta(seconds=phrase_timeout):
                    last_sample = bytes()
                    phrase_complete = True

                # This is the last time we received new audio data from the queue.
                phrase_time = now

                # Concatenate our current audio data with the latest audio data.
                while not data_queue.empty():
                    data = data_queue.get()
                    last_sample += data

                # Use AudioData to convert the raw data to wav data.
                audio_data = sr.AudioData(last_sample, source.SAMPLE_RATE, source.SAMPLE_WIDTH)
                wav_data = io.BytesIO(audio_data.get_wav_data())

                # Write wav data to the temporary file as bytes.
                with open(temp_file, 'w+b') as f:
                    f.write(wav_data.read())

                # Read the transcription.
                result = audio_model.transcribe(temp_file, fp16=torch.cuda.is_available())
                text = result['text'].strip()

                # If we detected a pause between recordings, add a new item to our transcription.
                # Otherwise edit the existing one.
                if phrase_complete:
                    transcription.append(text)
                    #print(transcription)
                    if len(text) > 0:
                        print("Question: " + text)
                        response = gpt_model.generate(text)
                        print("Answer: " + response)
                    
                else:
                    transcription[-1] = text

                # Clear the console to reprint the updated transcription.
                #os.system('cls' if os.name=='nt' else 'clear')
                #for line in transcription:
                #    print(line)
                
                # Flush stdout.
                #print('', end='', flush=True)

                # Infinite loops are bad for processors, must sleep.
                sleep(0.25)

    def __del__(self):
        self.source.stop()
