class Shape:
	def __init__(self, position, rotation, type):
		self.position = position
		self.rotation = rotation
		self.type = type
		self.rotationCycle = 0
		
		
	def move():
		pass
		
	def rotate():
		self.rotationCycle = self.rotationCycle + 1
		print("rotationCycle: " + self.rotationCycle)
		while self.rotationCycle >= 4:
			self.rotationCycle = self.rotationCycle - 4
			print("rotationCycle: " + self.rotationCycle)


			
	def collision():
		pass
		
class O(Shape):
	
	def __init__(self, position, rotation, type, color):
		self.type = type
		self.color = color
		self.position = position
		self.rotation = rotation
		super().__init__(position, rotation, type)
		
	def who(self):
		print(str(self.type) + " in position " + str(self.position) + " with the color of " + str(self.color) + " and rotation cycle " + str(self.rotation))

'''
x = O([3,4], 1, "O", [255,0,0])

x.who()
'''