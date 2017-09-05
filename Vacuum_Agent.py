from enum import Enum
from Environment import *
from random import *

class Vacuum_Agent:
	
	direction = {"LEFT": -1, "RIGHT": 1}
		
	def __init__(self, env, pos):
		self.env = env
		self.position = pos
		self.movingDirection = randrange(2)
		self.score = 0
	
	def addScore(self, score):
		self.score = self.score + score
		
	def getScore(self):
		return self.score
	
	def isFloorDirty(self):
		return self.env.mapList[self.position]
		
	def move(self):
		if self.position == 0: #LeftMost
			self.movingDirection = self.direction["RIGHT"]
		if self.position == (self.env.size-1): #RightMost
			self.movingDirection = self.direction["LEFT"]
			
		self.position = self.position + self.movingDirection
				
	def run(self):
		#print("Pos: ", self.position)
		#print(self.env.mapList, '\n')
		if self.isFloorDirty() == 1:
			self.env.mapList[self.position] = 0 #Clean current floor
		else:
			self.move()
		