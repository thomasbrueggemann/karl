
import openai
import tempfile
from pathlib import Path
from playsound import playsound

class Mouth:
    
    def __init__(self, openai_api_key):
        self.openai_client = openai.OpenAI(api_key=openai_api_key)  

    def say(self, words):
        if words is None or len(words) == 0:
            return None
        
        print("Karl:" + words)
        
        response = self.openai_client.audio.speech.create(
            model="tts-1", voice="alloy", input=words
        )

        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=True) as temp_file:
            temp_file_path = Path(temp_file.name)
            response.stream_to_file(temp_file_path)

            playsound(temp_file.name, block=True)