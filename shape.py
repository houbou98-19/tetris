class Shape:
	def __init__(self, position, rotation, type):
		self.position = position
		self.type = type
		self.rotationCycle = rotation
		
		
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
	
	def __init__(self, position, rotation, color):
		
		self.color = (255,0,0)
		Shape.__init__(self, position, rotation, "O")
		self.formations =  [['00', '00'],['00','00']]
		
		
	def who(self): #for us to know. NOT in final game
		print(str(self.type) + " in position " + str(self.position) + " with the color of " + str(self.color) + " and rotation cycle " + str(self.rotationCycle))

	def show(self): #for us to know. NOT in final game
	
		y = len(self.formations[0])
		x = len(self.formations[0][0])
		i = 0
		j = 0
		
		while i < y:
			while j < x:
				print(self.formations[self.rotationCycle-1][i][j], end='')
				j +=1
			print("")
			j = 0
			i += 1
		#print(str(x)+":"+str(y))
		#print(self.formations[self.rotationCycle-1])

		'''
		print(self.formations[0][0][0])
		print(self.formations[0][0][1])
		print(self.formations[0][1][0])
		print(self.formations[0][1][1])
		'''
		
