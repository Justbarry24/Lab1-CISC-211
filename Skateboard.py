from Vehicle import Vehicle
class Skateboard(Vehicle):
	def __init__(self, top_speed,location, direction):
		super().__init__(3, top_speed,location,direction)
	
	def accelerate(self):
		if self.get_current_speed() == 0:
			self._current_speed = .5*self.get_top_speed()
		else:
			self._current_speed = self.get_top_speed()
		return self._current_speed
	
	def decelerate(self):
		self._current_speed = 0
	
	def move(self):
		a = self._location[1]
		c = self.get_current_speed
		if self._direction == "NORTH":
			a += c
		if self._direction == "EAST":
			pass
		if self._direction == "SOUTH":
			pass
		if self._direction == "WEST":
			pass
		return self._location
		

		