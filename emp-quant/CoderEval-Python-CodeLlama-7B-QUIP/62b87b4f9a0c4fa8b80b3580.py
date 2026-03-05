def integral(bins, edges):
	"""
	Calculate the area of the overall graph.
	"""
	return sum(bins) * (edges[1] - edges[0])