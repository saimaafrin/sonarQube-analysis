def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	self.time_units = [int(time_unit) for time_unit in self.time_units]
	return self