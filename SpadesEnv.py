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
import SpadesPlayer

class SpadesEnv(Environment):

	def __init__(self, game_deck):
		self.game_deck = game_deck
		self.in_dim = None
		self.out_dim = None

	

