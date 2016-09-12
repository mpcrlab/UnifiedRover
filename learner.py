from random import randrange

class StupidLearner:
	def __init__(self):
		self.state_size = (12, )
		self.action_size = (3, )

	def get_action(self, state):
		actions = [0] * 3
		idx = randrange(3)
		actions[idx] = 1
		return actions

	def train(self, state, action, reward, new_state, state_terminal):
		pass