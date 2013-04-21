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
import SpadesPlayer
import random as r

from pybrain.rl.agents import LearningAgent
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.learners import Q, SARSA
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer, DiscreteStateDependentExplorer

gamesPlayed = 0
lastWinner = None

#only need to pass in environment? as players each have their own task and agent
def playGame(env):

    tricksWon = [0] * 4
    currentPlayer = lastWinner if lastWinner else r.randint(0, 3)
    for x in range (4):
        for i in range (4):
            currentPlayer = currentPlayer % 4 == 0 if 0 else currentPlayer
            print "Player",currentPlayer,"'s Turn"

            thePlayer = players[currentPlayer]
            thePlayer.agent.integrateObservation(thePlayer.task.getObservation())
            card_played = thePlayer.play_card(thePlayer.agent.getAction())
            env.trick.append({'playerIndex': currentPlayer, 'cardPlayed': card_played})

        currentPlayer += 1
        env.trick.sort(key = lambda x: x.cardPlayed.card_val)
        tricksWon[env.trick[0].playerIndex] += 1
    return tricksWon.index(tricksWon.max())

if __name__ == "__main__":

    the_deck = SpadesDeckTest.SpadesDeckTest()
    the_env = SpadesEnv.SpadesEnv(the_deck)

    players = [SpadesPlayer.SpadesPlayer(the_deck, the_env) for x in range(4)]
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

    winner_count = [0,0,0,0]
    for i in range(1000):
        winner = playGame(the_env)
        winner_count[winner]+=1
    print winner_count

