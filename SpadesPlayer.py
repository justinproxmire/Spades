# PROGRAM:				Spades - SpadesPlayer.py
# AUTHORS:				
# DATE:						4/17/13
# DESCRIPTION:		
# MODULES:		
#			
#			
#	
# NOTES:					CS5300 - Final Project 2013
# ***********************************************

import SpadesDeckTest
import SpadesEnv
import SpadesTask
import copy
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners.valuebased import ActionValueTable


class SpadesPlayer:

	def __init__(self,game_deck, game_env):
		self.gameDeck = game_deck
		self.hand = SpadesDeckTest.SpadesDeckTest.draw_hand(self.gameDeck)
		self.gamesWon = 0
		self.gamesTied = 0
		self.av_table = ActionValueTable(4, 1)
		self.av_table.initialize(0.0)
		self.env = game_env
		self.task = SpadesTask.SpadesTask(game_env)
		self.agent = None
		self.learner = None


	def get_value(self):
		return self.hand

	def play_card(self, cardindex):
		retCard = copy.copy(self.hand[cardindex])
		self.hand.remove(self.hand[cardindex])
		return retCard
		
