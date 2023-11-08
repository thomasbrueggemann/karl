class Conversation:
	def __init__(self):
		self.current_state = 'listening'
		self.trigger_action()

	def transition_to_processing(self):
		self.current_state = 'processing'
		self.trigger_action()

	def transition_to_answering(self):
		self.current_state = 'answering'
		self.trigger_action()

	def transition_to_listening(self):
		self.current_state = 'listening'
		self.trigger_action()

	def trigger_action(self):
		if self.current_state == 'listening':
			print('Listening...')
		elif self.current_state == 'processing':
			print('Processing...')
		elif self.current_state == 'answering':
			print('Answering...')
