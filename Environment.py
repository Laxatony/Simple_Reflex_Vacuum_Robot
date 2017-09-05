class Environment:

	def __init__(self, size, dirtPlaceList):
		#Should add foolproof mechanism to prevent unexpected inputs
		
		self.size = size
		self.mapList = [0] * self.size
		self.dirtPlaceList = dirtPlaceList
		self.score = 0
		
		for dirtFloorIndex in range(len(self.dirtPlaceList)):
			self.mapList[dirtFloorIndex] = self.dirtPlaceList[dirtFloorIndex]
			
		print("Environment Setting:")
		print("	Floor Size: ", self.size)
		print("	DirtPlaceList: ", self.dirtPlaceList)
		print("	Floor Condition: ", self.mapList, '\n')
		
	def getScore(self):
		self.score = 0
		for i in range(self.size):
			if self.mapList[i] == 0:
				self.score = self.score + 1
				
		return self.score
