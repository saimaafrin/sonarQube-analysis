def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	return np.sum(bins * np.diff(edges))