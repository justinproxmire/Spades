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

class SpadesPlayer:

	def __init__(self,game_deck):
		self.gameDeck = game_deck
		self.hand = SpadesDeckTest.SpadesDeckTest.draw_hand(self.gameDeck)
		
	def get_value(self):
		return self.hand

	def play_card(self, card):
		self.hand.remove(card)
		
