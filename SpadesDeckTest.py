# PROGRAM:                Spades - SpadesDeckTest.py
# AUTHORS:                
# DATE:                        4/17/13
# DESCRIPTION:        Spades deck class for testing.  Sets up deck with their values for spades.
# MODULES:        
#            
#            
#    
# NOTES:                    CS5300 - Final Project 2013
# ***********************************************

import random as r
import SpadesCard

class SpadesDeckTest:

    def __init__(self):
        hearts_deck = [SpadesCard.SpadesCard("Hearts", i, i) for i in xrange(2,6)]
        diamonds_deck = [SpadesCard.SpadesCard("Diamonds", i, i) for i in xrange(2,6)]
        clubs_deck = [SpadesCard.SpadesCard("Clubs", i, i) for i in xrange(2,6)]
        spades_deck = [SpadesCard.SpadesCard("Spades", i, i + 30) for i in xrange(2,6)]

        self.deck = hearts_deck + diamonds_deck + clubs_deck + spades_deck
        r.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop() 

    def draw_hand(self):
        hand =  [self.draw_card() for i in range(4)]
        hand.sort(key=lambda x: x.card_val)
        return hand
    
    def reset(self):
        hearts_deck = [SpadesCard.SpadesCard("Hearts", i, i) for i in xrange(2,6)]
        diamonds_deck = [SpadesCard.SpadesCard("Diamonds", i, i) for i in xrange(2,6)]
        clubs_deck = [SpadesCard.SpadesCard("Clubs", i, i) for i in xrange(2,6)]
        spades_deck = [SpadesCard.SpadesCard("Spades", i, i + 30) for i in xrange(2,6)]

        self.deck = hearts_deck + diamonds_deck + clubs_deck + spades_deck
        r.shuffle(self.deck)