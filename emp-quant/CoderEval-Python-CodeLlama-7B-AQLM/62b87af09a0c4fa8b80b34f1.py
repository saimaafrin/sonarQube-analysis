def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self.is_empty():
		raise ValueError("Cannot fill empty histogram")
	if not isinstance(coord, tuple):
		raise TypeError("Coordinates must be a tuple")
	if len(coord) != self.ndim:
		raise ValueError("Coordinates must have %d dimensions" % self.ndim)
	if not all(isinstance(c, int) for c in coord):
		raise TypeError("Coordinates must be integers")
	if not all(0 <= c < self.shape[i] for i, c in enumerate(coord)):
		raise ValueError("Coordinates must be inside histogram edges")
	self._data[coord] += weight