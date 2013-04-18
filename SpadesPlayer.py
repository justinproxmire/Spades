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

import SpadesDeck

class SpadesPlayer:

	def __init__(self,gameDeck):
		self.hand = []
		self.gameDeck = gameDeck

	def gethand(self):
		self.hand = SpadesDeck.DrawHand()

	def getValue(self):
		return self.hand