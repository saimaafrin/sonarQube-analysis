def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self.is_empty():
		return
	if coord < self.min_coord or coord > self.max_coord:
		return
	self.histogram[coord - self.min_coord] += weight