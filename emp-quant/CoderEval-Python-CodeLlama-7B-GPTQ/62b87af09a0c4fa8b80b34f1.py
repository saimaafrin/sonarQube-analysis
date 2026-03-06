def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if coord[0] < 0 or coord[0] >= self.n_bins[0]:
		return
	if coord[1] < 0 or coord[1] >= self.n_bins[1]:
		return
	if coord[2] < 0 or coord[2] >= self.n_bins[2]:
		return
	self.hist[coord[0], coord[1], coord[2]] += weight