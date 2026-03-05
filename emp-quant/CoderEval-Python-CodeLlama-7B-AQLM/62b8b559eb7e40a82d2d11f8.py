def minimalBases(classes):
	"""
	Returns all classes without subclasses as a list.
	"""
	minimalBases = []
	for c in classes:
		if not c.subclasses:
			minimalBases.append(c)
	return minimalBases