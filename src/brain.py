
import openai

class Brain:
    def __init__(self, openai_api_key):
        self.openai_client = openai.OpenAI(api_key=openai_api_key)
        self.conversation_history = []
        
    def process(self, words):
        if words is None or len(words) == 0:
            return None
        
        self.conversation_history.append({
            "role": "user",
            "content": words,
        })
            
        completion = self.openai_client.chat.completions.create(
            model="gpt-4",
            messages=self.conversation_history,
            max_tokens=200
        )

        self.conversation_history.append(completion.choices[0].message)

        return completion.choices[0].message.content