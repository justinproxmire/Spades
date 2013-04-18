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
		heartsDeck = [SpadesCard.SpadesCard("Hearts", i + 2, i + 2) for i in range(13)]
		diamondsDeck = [SpadesCard.SpadesCard("Diamonds", i + 2, i + 2) for i in range(13)]
		clubsDeck = [SpadesCard.SpadesCard("Clubs", i + 2, i + 2) for i in range(13)]
		spadesDeck = [SpadesCard.SpadesCard("Spades", i + 2, i + 32) for i in range(13)]

		self.deck = heartsDeck + diamondsDeck + clubsDeck + spadesDeck
		r.shuffle(self.deck)

	def DrawCard(self):
		return self.deck.pop()

	def DrawHand(self):
		return [self.drawCard() for i in range(13)]

if __name__ == "__main__":
	thedeck = SpadesDeck()
	print thedeck.DrawHand()
