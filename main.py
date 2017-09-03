import sys
from Environment import *
from random import *

def main():
	
	environmentSize = 20
	dirtPlaseList = [ 2, 4, 5, 6, 18]
	
	
	env = Environment(environmentSize, dirtPlaseList)
	env.displayInfo()

if __name__ == '__main__':
	main()