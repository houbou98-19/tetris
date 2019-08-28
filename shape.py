class Shape:
	def __init__(self, position, rotation, type):
		self.position = position
		self.type = type
		self.rotationCycle = rotation
		
		
	def move():
		pass
		
	def rotate(self):
		self.rotationCycle = self.rotationCycle + 1
		print("rotationCycle: " + str(self.rotationCycle))
		while self.rotationCycle >= 3:
			self.rotationCycle = self.rotationCycle - 4
			print("rotationCycle: " + str(self.rotationCycle))
			
	def collision():
		pass
		
	def show(self): #for us to know. NOT in final game. Although could be taken from to put in with pygame
	
		y = len(self.formations[0])
		x = len(self.formations[0][0])
		i = 0
		j = 0
		
		while i < y:
			#print(i)
			while j < x:
			#	print(j)
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
	def __str__(self): #for us to know. NOT in final game
		return str(self.type) + " in position " + str(self.position) + " with the color of " + str(self.color) + " and rotation cycle " + str(self.rotationCycle)

	
		
class O(Shape):
	
	def __init__(self, position, rotation, color):
		
		self.color = (255,0,0)
		Shape.__init__(self, position, rotation, "O")
		self.formations =  [[[1,1,0,0],
							 [1,1,0,0],
							 [0,0,0,0]],
							 
							 ] #O just needs one formation. and fix the string.
	
	
	def getRotation(self):
		return self.rotationCycle
class L(Shape):
	
	def __init__(self, position, rotation, color):
		
		self.color = (0,255,0)
		Shape.__init__(self, position, rotation, "L")
		self.formations =  [[[0,0,0,0],
							 [1,0,0,0],
							 [1,0,0,0],
							 [1,1,0,0]],
							 
							[[0,0,0,0],
							 [0,0,0,0],
							 [1,1,1,0],
							 [1,0,0,0]],
							 
							[[0,0,0,0],
							 [1,1,0,0],
							 [0,1,0,0],
							 [0,1,0,0]],
							 
							[[0,0,0,0],
							 [0,0,0,0],
							 [0,0,1,0],
							 [1,1,1,0]]]