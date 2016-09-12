class ConsoleUI:
	def __init__(self):
		pass

	def refresh(self, state, action, reward, new_state, state_terminal):
		print state, action, reward, new_state, state_terminal
	