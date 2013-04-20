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
from numpy import numpy as np

class SpadesTask(Task):

	def __init__(self, enviornment):
		self.env = enviornment
		#self.lastReward = 0 ??

	def preformAction(self, action):
		self.action = self.env.preformAction(action)
		return self.action
