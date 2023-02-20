class Coordinate:
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	def getValues(self):
		x, y = self.x, self.y
		return x, y

	def changeValues(self, x, y):
		if x:
			self.x = x
		if y:
			self.y = y