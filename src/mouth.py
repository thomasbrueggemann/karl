class Mouth:
    def say(self, words):
        if words is None or len(words) == 0:
            return None
        
        print("Karl:" + words)