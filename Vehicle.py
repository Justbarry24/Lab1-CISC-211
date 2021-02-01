from abc import ABC, abstractmethod
class Vehicle(ABC):
	def __init__(self,length, top_speed, location, direction):
		self._length = length
		self._top_speed = top_speed
		self._location = location
		self._direction = direction
		self._current_speed = 0
		if(self._length != 3):
			raise Exception()

		
    

	def get_length(self):
		return self._length
	
	def get_top_speed(self):
		return self._top_speed
	
	def get_location(self):
		return self._location

	def get_direction(self):
		return self._direction
	
		
	def get_current_speed(self):
		return self._current_speed
	
	def turn_left(self):
		if self._direction == "NORTH":
			self._direction = "WEST"
		elif self._direction == "WEST":
			self._direction = "SOUTH"
		elif self._direction == "SOUTH":
			self._direction = "EAST"
		else: 
			self._direction = "NORTH"

	def turn_right(self):
		if self._direction == "NORTH":
			self._direction = "EAST"
		elif self._direction == "EAST":
			self._direction = "SOUTH"
		elif self._direction == "SOUTH":
			self._direction = "WEST"
		else:
			self._direction = "NORTH"
	
	#will be defined in skateboard and helicopter
	@abstractmethod
	def move():
		pass
	#will be defined in skateboard and helicopter
	@abstractmethod
	def accelerate():
		pass
	#will be defined in skateboard and helicopter
	@abstractmethod
	def decelerate():
		pass
