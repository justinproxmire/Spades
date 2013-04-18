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
import SpadesDeck
import SpadesCard
import SpadesPlayer

if __name__ == "__main__":
    the_deck = SpadesDeck.SpadesDeck()
    player1 = SpadesPlayer.SpadesPlayer(the_deck)
    player2 = SpadesPlayer.SpadesPlayer(the_deck)
    player3 = SpadesPlayer.SpadesPlayer(the_deck)
    player4 = SpadesPlayer.SpadesPlayer(the_deck)
    
    print "Done creating players\n"
         
    