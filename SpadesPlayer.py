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
from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners.valuebased import ActionValueTable


class SpadesPlayer:

	def __init__(self,game_deck):
		self.gameDeck = game_deck
		self.hand = SpadesDeckTest.SpadesDeckTest.draw_hand(self.gameDeck)
		self.gamesWon = 0
		self.gamesTied = 0
		self.av_table = ActionValueTable(4, 1)
		self.av_table.initialize(0.0)
		self.env = SpadesEnv()
		self.task = SpadesTask(self.env)
		self.agent = None
		self.learner = None


	def get_value(self):
		return self.hand

	def play_card(self, card):
		self.hand.remove(card)
		
