# UnifiedRover
A tool for running rover code in a modular way.  Simply replace a module.

TODO: replace "stupid" placeholder modules with actual modules to control the rover, do image processing, and train NNs

The goal of this repository is allow all different sorts of rover code to work together.
The rover code is sectioned off into modules, all controlled by the main.py file.
Each module has certain functions that main.py calls to allow it to interact with other modules.
Every module of the same type needs to have the same functions.  
This way, changing the imports in main.py lets you switch between 
  -a simulator, a webcam, or a real rover (by changing the World module)
  -different types of image processing on image states (by changing ImageProcessor)
  -different learning algorithms (by changing Learner)
  -different UIs (by changing UI)

TUTORIAL

There are four componenents to Q learning in a rover
1. the World defines what states and actions are possible
2. the State Processor does image processing on the state before learning
3. the Learner reads in a state, outputs an action, and learns
4. the UI displays the results to the screen

To replace what's above with your own module,
write a module that has the same functions as the examples provided here
then, replace the imports in main.py so that your module is used instead

EXAMPLE
To replace StupidLearner with a neural network in Tensorflow,
make a new file called smartlearner
write a class called SmartLearner, with the same functions and variables
let the SmartLearner use tensorflow to train on the states/actions instead of... doing nothing like the "StupidLearner"
change the import to 'from smartlearner import SmartLearner' in main.py
Run the code, and your rover is now Smart!
