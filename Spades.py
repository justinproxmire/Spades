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
import SpadesTask
import SpadesEnv
import SpadesDeckTest
import SpadesCard
import SpadesPlayer.SpadesPlayer as sp
import random as r

from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.learners import Q, SARSA
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer, DiscreteStateDependentExplorer

gamesPlayed = 0

if __name__ == "__main__":
	
    the_deck = SpadesDeckTest.SpadesDeckTest()

		players = [sp(the_deck) for x in range(4)]
		players[0].learner = Q(0.0, 0.0)
		players[0].learner._setExplorer(EpsilonGreedyExplorer(0.0,0.0))
		players[0].agent = LearningAgent(players[0].av_table, players[0].learner)

		players[1].learner = Q(0.0, 0.0)
		players[1].learner._setExplorer(EpsilonGreedyExplorer(0.0,0.0))
		players[1].agent = LearningAgent(players[1].av_table, players[1].learner)

		players[2].learner = Q(0.0, 0.0)
		players[2].learner._setExplorer(EpsilonGreedyExplorer(0.0,0.0))
		players[2].agent = LearningAgent(players[2].av_table, players[2].learner)
		
		players[3].learner = Q(0.0, 0.0)
		players[3].learner._setExplorer(EpsilonGreedyExplorer(0.0,0.0))
		players[3].agent = LearningAgent(players[3].av_table, players[3].learner)

    print "Done creating players\n"

