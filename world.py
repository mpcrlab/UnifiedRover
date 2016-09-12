import numpy as np

class BoxSimulatorWorld:
	def __init__(self):
		self.state_size = (12, )
		self.action_size = (3, )

		self.leftTransitions = {
			"000":"001",
			"001":"002",
			"002":"102",
			"102":"103",
			"103":"203",
			"203":"200",
			"200":"210",
			"210":"310",
			"310":"320",
			"320":"020",
			"020":"030",
			"030":"000"
		}
		
		self.rightTransitions = {
			"001":"000",
			"002":"001",
			"102":"002",
			"103":"102",
			"203":"103",
			"200":"203",
			"210":"200",
			"310":"210",
			"320":"310",
			"020":"320",
			"030":"020",
			"000":"030"
		}

	def flatten(self, string):
		total_arr = np.zeros((12))
		for i in xrange(len(string)):
			intc = int(string[i])
			total_arr[(i * 4) + intc] = 1
		return total_arr

	def unflatten(self, li):
		string = ""
		for i in xrange(3):
			if li[(i * 4) + 0] == 1:
				string += "0"
			elif li[(i * 4) + 1] == 1:
				string += "1"
			elif li[(i * 4) + 2] == 1:
				string += "2"
			elif li[(i * 4) + 3] == 1:
				string += "3"
		return string

	def get_initial_state(self):
		return self.flatten("000")

	def take_action(self, state, action):
		state = self.unflatten(state)
		reward = 1 if state == "020" else 0
		terminal = 1 if state == "020" else 0
		if(np.argmax(action) == 1): #left
			return reward, self.flatten(self.leftTransitions[state]), terminal
		elif(np.argmax(action) == 2): #right
			return reward, self.flatten(self.rightTransitions[state]), terminal
		return reward, self.flatten(state), terminal

