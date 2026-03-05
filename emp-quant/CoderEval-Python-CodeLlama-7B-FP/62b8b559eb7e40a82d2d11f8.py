def minimalBases(classes):
	"""
	Returns all classes without subclasses as a list.
	"""
	minimal = []
	for c in classes:
		if not c.subclasses:
			minimal.append(c)
	return minimal