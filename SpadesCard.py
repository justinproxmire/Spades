# PROGRAM:				Spades - SpadesCard.py
# AUTHORS:				Justin Proxmire, Josh Inniger, Justin Hill
# DATE:						4/17/13
# DESCRIPTION:		Spades deck class. Sets up deck with their values for spades.
# MODULES:				N/A (initialization only)
# NOTES:					CS5300 - Final Project 2013
# ***********************************************

class SpadesCard:

	def __init__(self, suit, face_val, card_val):
		self.suit = suit
		self.face_val = face_val
		self.card_val = card_val
