import pyttsx3

class Mouth:
    
    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, words):
        if words is None or len(words) == 0:
            return None
        
        print("Karl:" + words)
        
        self.engine.say(words)
        self.engine.runAndWait()