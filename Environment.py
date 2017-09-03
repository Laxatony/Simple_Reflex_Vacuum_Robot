class Environment:

	def __init__(self, size, dirtPlaceList):
		self.size = size
		self.dirtPlaceList = dirtPlaceList
	
	def displayInfo(self):
		print("Floor Size: ", self.size)
		print("DirtPlaceList: ", self.dirtPlaceList)
