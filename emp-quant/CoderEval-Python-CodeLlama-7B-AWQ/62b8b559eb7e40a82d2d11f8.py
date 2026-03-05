def minimalBases(classes):
	"""
	Returns all classes without subclasses as a list.
	"""
	minimal = []
	for c in classes:
		if not any(c in s for s in classes):
			minimal.append(c)
	return minimal