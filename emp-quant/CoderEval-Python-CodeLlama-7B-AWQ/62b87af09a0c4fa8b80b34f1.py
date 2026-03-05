def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self.is_empty():
		raise ValueError("Histogram is empty")
	if not isinstance(coord, tuple):
		raise TypeError("Coordinates must be a tuple")
	if len(coord) != len(self.coord_names):
		raise ValueError("Coordinates must have the same length as the histogram")
	if not all(isinstance(c, (int, float)) for c in coord):
		raise TypeError("Coordinates must be numeric")
	if not all(c >= self.coord_min[i] and c <= self.coord_max[i] for i, c in enumerate(coord)):
		raise ValueError("Coordinates must be within the histogram edges")
	if not isinstance(weight, (int, float)):
		raise TypeError("Weight must be numeric")
	if weight < 0:
		raise ValueError("Weight must be non-negative")
	self.data[coord] += weight