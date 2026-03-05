def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if coord < self.min or coord > self.max:
		return
	self.hist[coord] += weight