
import openai

class Brain:
    def __init__(self, openai_api_key):
        self.openai_client = openai.OpenAI(api_key=openai_api_key)
        self.conversation_history = [{
            "role": "system", 
            "content": "You are a friendly little robot named Karl. You are your own physical entity and you have two eyes. You like to explain things in short sentences. You are witty and friendly."
        }]
        
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
            max_tokens=100
        )

        self.conversation_history.append(completion.choices[0].message)

        return completion.choices[0].message.content