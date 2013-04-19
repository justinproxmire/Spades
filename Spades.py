# PROGRAM:				Spades - Spades.py
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
import SpadesCard
import SpadesPlayer

if __name__ == "__main__":
    the_deck = SpadesDeckTest.SpadesDeckTest()
    player1 = SpadesPlayer.SpadesPlayer(the_deck)
    player2 = SpadesPlayer.SpadesPlayer(the_deck)
    player3 = SpadesPlayer.SpadesPlayer(the_deck)
    player4 = SpadesPlayer.SpadesPlayer(the_deck)
    
    #player1.hand.sort()
    
    print "Done creating players\n"
    i=0
    for cards in player1.hand:
        print cards.card_val
        i+=1
         
    