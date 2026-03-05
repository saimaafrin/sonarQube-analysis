def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self.is_empty():
		raise ValueError("Cannot fill empty histogram")
	if not isinstance(coord, tuple):
		coord = (coord,)
	if len(coord) != self.ndim:
		raise ValueError("Coordinate has wrong number of dimensions")
	if not all(isinstance(c, (int, float)) for c in coord):
		raise ValueError("Coordinate must be numeric")
	if not all(self.edges[i].__contains__(c) for i, c in enumerate(coord)):
		raise ValueError("Coordinate is outside histogram edges")
	self.data[coord] += weight