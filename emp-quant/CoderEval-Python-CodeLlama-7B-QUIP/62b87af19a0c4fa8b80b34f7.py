def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	if level == -1:
		level = len(d1)
	if level == 0:
		return {}
	d = {}
	for k in d1:
		if k not in d2:
			d[k] = d1[k]
	return d