#main.py - controls everything

#TUTORIAL

#There are four componenents to Q learning in a rover
#1. the World defines what states and actions are possible
#2. the State Processor does image processing on the state before learning
#3. the Learner reads in a state, outputs an action, and learns
#4. the UI displays the results to the screen

#below is an example of four simple componenets working together
#1. BoxSimulatorWorld is a computer simulation of a rover in a box
	#-it has 12 states
#2. NoneImageProcessor does nothing, since no image processing is needed on a the simulation states
#3. StupidLearner picks a random action, and does no learning. Hence the name "Stupid"
#4. ConsoleUI prints out the state, action, reward, etc. to the terminal. Not much of a UI

#^^this is just a start.  
#To replace what's above with your own module,
#write a module that has the same functions as the examples provided here
#then, replace the imports below so that your module is used instead

#EXAMPLE
#To replace StupidLearner with a neural network in Tensorflow,
#make a new file called smartlearner
#write a class called SmartLearner, with the same functions and variables
#let the SmartLearner use tensorflow to train on the states/actions instead of... doing nothing like the "StupidLearner"
#change the import below to 'from smartlearner import SmartLearner'
#Run the code, and your rover is now Smart!

#BELOW IS WHERE TO CHANGE INDIVIDUAL COMPONENTS

from world import BoxSimulatorWorld
from state_processor import NoneImageProcessor
from learner import StupidLearner
from ui import ConsoleUI

world = BoxSimulatorWorld()
image_processor = NoneImageProcessor()
learner = StupidLearner()
ui = ConsoleUI()

#BELOW IS THE ACTUAL IMPLEMENTATION

state = None
action = None
reward = None
new_state = None
state_terminal = True

#checks to make sure everything is compatible
assert image_processor.convert_size(world.state_size) == learner.state_size
assert world.action_size == learner.action_size

def refresh_ui():
	ui.refresh(state, action, reward, new_state, state_terminal)

while True:
	if state_terminal:
		state = world.get_initial_state()
		state = image_processor.process(state)
	refresh_ui()
	action = learner.get_action(state)
	reward, new_state, state_terminal = world.take_action(state, action)
	new_state = image_processor.process(new_state)
	refresh_ui()
	learner.train(state, action, reward, new_state, state_terminal)
	state = new_state
