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
import SpadesCard as SpadesCard

class SpadesDeck:

	def __init__(self):
		deck = [SpadesCard] * 52
		print deck;

if __name__ == "__main__":
	thedeck = SpadesDeck()