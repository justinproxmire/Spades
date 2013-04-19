# PROGRAM:				Spades - SpadesEnv.py
# AUTHORS:				
# DATE:						4/17/13
# DESCRIPTION:		Spades environment class.  Don't really know what this does yet.
# MODULES:		
#			
#			
#	
# NOTES:					CS5300 - Final Project 2013
# ***********************************************

from pybrain.rl.environments.environment import Environment
import numpy as np
import SpadesPlayer
import SpadesDeck

class SpadesEnv(Environment):

	# the number of action values the environment accepts
	indim = 4

	# the number of sensor values the environment produces
	outdim = 1

	# discrete state space
	discreteStates = True

	# discrete action space
	discreteActions = True


	def __init__(self, game_deck):
		self.game_deck = game_deck

	def getSensors(self):
		"""
			Get the internal state of the environment.  Returns a numpy array of doubles.
		"""
		return np.array()

	def performAction(self, action):
		"""
			Action is a numpy array of doubles.  No return value.
		"""

	def reset(self):
		"""
			Resets the environment's internal state.  No return value.
		"""
		self.game_deck = SpadesDeck()