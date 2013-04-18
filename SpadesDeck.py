# PROGRAM:				Spades - SpadesDeck.py
# AUTHORS:				
# DATE:						4/17/13
# DESCRIPTION:		Spades deck class. Sets up deck with their values for spades.
# MODULES:		
#			
#			
#	
# NOTES:					CS5300 - Final Project 2013
# ***********************************************

import random as r
import SpadesCard

class SpadesDeck:

	def __init__(self):
		hearts_deck = [SpadesCard.SpadesCard("Hearts", i + 2, i + 2) for i in range(13)]
		diamonds_deck = [SpadesCard.SpadesCard("Diamonds", i + 2, i + 2) for i in range(13)]
		clubs_deck = [SpadesCard.SpadesCard("Clubs", i + 2, i + 2) for i in range(13)]
		spades_deck = [SpadesCard.SpadesCard("Spades", i + 2, i + 32) for i in range(13)]

		self.deck = hearts_deck + diamonds_deck + clubs_deck + spades_deck
		r.shuffle(self.deck)

	def draw_card(self):
		return self.deck.pop()

	def draw_hand(self):
		return [self.draw_card() for i in range(13)]

if __name__ == "__main__":
	the_deck = SpadesDeck()
	print the_deck.draw_hand()
