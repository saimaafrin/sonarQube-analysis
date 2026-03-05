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
		raise ValueError("Coordinate must have length %d" % self.ndim)
	for i, c in enumerate(coord):
		if c < self.edges[i][0] or c >= self.edges[i][-1]:
			return
	self.histogram[tuple(i for i, e in enumerate(coord) if e in e)] += weight