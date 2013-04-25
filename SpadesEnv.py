# PROGRAM:				Spades - SpadesEnv.py
# AUTHORS:				
# DATE:						4/17/13
# DESCRIPTION:		Spades environment class.
# MODULES:		
#			
#			
#	
# NOTES:					CS5300 - Final Project 2013
# ***********************************************

from pybrain.rl.environments.environment import Environment
import numpy as np
import SpadesPlayer
import SpadesDeckTest

class SpadesEnv(Environment):

	# the number of action values the environment accepts
	indim = 2

	# the number of sensor values the environment produces
	outdim = 3

	# discrete state space
	discreteStates = True

	# discrete action space
	discreteActions = True


	def __init__(self, game_deck):
		self.game_deck = game_deck
		self.trick = []
		
	def getSensors(self):
		"""
			Get the internal state of the environment.  Returns a numpy array of doubles.
		"""
		print self.trick
		the_trick =  [np.float32(self.trick[i]["cardPlayed"].card_val) if i < len(self.trick) else float(0) for i in range(1)]
		print the_trick
		return the_trick

	def performAction(self, action):
		"""
			Action is a numpy array of doubles.  No return value.
		"""

	def reset(self):
		"""
			Resets the environment's internal state.  No return value.
		"""
		self.game_deck = SpadesDeckTest.SpadesDeckTest.reset()
		print self.game_deck
		self.trick = []
		
		
