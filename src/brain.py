
import gpt4all

class Brain:
    def __init__(self):
        self.gpt_model = gpt4all.GPT4All("mistral-7b-openorca.Q4_0.gguf", "./")
        self.chat_session = self.gpt_model.chat_session(system_prompt="You are a little robot called 'Karl'")
        
    def process(self, words):
        if words is None or len(words) == 0:
            return None
        
        response = self.gpt_model.generate(prompt=words, temp=0)
            
        return response