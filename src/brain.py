
import gpt4all

class Brain:
    def __init__(self):
        self.gpt_model = gpt4all.GPT4All("mistral-7b-openorca.Q4_0.gguf", "./")
        
    def process(self, words):
        if words is None or len(words) == 0:
            return None
        
        with self.gpt_model.chat_session():
            response = self.gpt_model.generate(words)
            
        return response