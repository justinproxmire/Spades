# PROGRAM:				Spades - SpadesTask.py
# AUTHORS:				
# DATE:						4/17/13
# DESCRIPTION:		
# MODULES:		
#			
#			
#	
# NOTES:					CS5300 - Final Project 2013
# ***********************************************

from scipy import clip, asarray
from pybrain.rl.environments.task import Task
import numpy as np

class SpadesTask(Task):

	def __init__(self, enviornment):
		self.env = enviornment
		#self.lastReward = 0 ??

	def performAction(self, action):
		self.action = self.env.performAction(action)
		return self.action
	

	def getObservation(self):
		""" A filtered mapping to getSample of the underlying environment. """
		sensors = self.env.getSensors()
		return sensors
	
	#def getReward(self):
		#if self.action == 0:
			#give rewards 
			
	@property
	def indim(self):
		return self.env.indim

	@property
	def outdim(self):
		return self.env.outdim
