
class Vehicle:
	
	curr_speed = 0

	def __init__ (self, color, max_speed, milage):
		self.color = color
		self.max_speed = max_speed
		self.milage = milage
	def accelerate(self, x=None):
		if x:
			self.curr_speed += x
		else:
			self.curr_speed += 10
		print("Vrrrrm... ")

class Owner:
	def __init__(self,owner):
		self.owner = owner

class Van:
	pass

class Bus(Vehicle):
	num_seats = 16

class MiniBus(Vehicle, Owner):
	special_ed = True

myMiniBus = MiniBus("Blue", 100, 11, "Brennan")
print(vars(myMiniBus))

#myCar = Vehicle("Blue", 100, 11)
#myBus = Bus("Yellow",25,20)
#print(myBus.color, myBus.num_seats)

#print(myCar.__dir__())
#vars = vars(myCar)
#print(vars["color"])

'''
print(myCar.color)
print(myCar.curr_speed)
myCar.accelerate(25)
print(myCar.curr_speed)
myCar.accelerate()
print(myCar.curr_speed)
'''