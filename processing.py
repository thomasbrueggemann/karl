
from conversation_stage import ConversationStage
import gpt4all

class Processing(ConversationStage):
	def __init__(self):
		gpt_model = gpt4all.GPT4All("mistral-7b-openorca.Q4_0.gguf", "./")
		self.chat_session = gpt_model.chat_session()

	def start(self):
		print('Processing...')

	def stop(self):
		print('Processing stopped.')

	def __del__(self):
		self.chat_session.close()