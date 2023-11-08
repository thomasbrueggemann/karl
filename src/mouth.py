
import pyttsx3

class Mouth:
    def say(self, words):
        if words is None or len(words) == 0:
            return None
        
        print("Karl:" + words)
        
        engine = pyttsx3.init()
        engine.say(words)
        engine.runAndWait()