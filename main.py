import sys
from Environment import *
from Vacuum_Agent import *
from random import *

def main():
	
	environmentSize = 2
	dirtPlaceList = [[0, 0], [0, 1], [1, 0], [1, 1]]
	
	
	for dirtType in range(len(dirtPlaceList)):
		for location in range(2):
			env = Environment(environmentSize, dirtPlaceList[dirtType])	
			agent = Vacuum_Agent(env, location);
			for time_step in range(1000):
				agent.run()
				agent.addScore(env.getScore())
				
			print("Score: ", agent.getScore())

if __name__ == '__main__':
	main()