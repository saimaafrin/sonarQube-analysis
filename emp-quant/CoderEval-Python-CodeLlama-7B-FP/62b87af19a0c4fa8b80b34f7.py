def difference(d1, d2, level=-1):
	"""
	Return a dictionary with items from d1 not contained in d2.
	"""
	if level == 0:
		return {}
	result = {}
	for k, v in d1.items():
		if k not in d2:
			result[k] = v
		elif isinstance(v, dict) and isinstance(d2[k], dict):
			result[k] = difference(v, d2[k], level-1)
	return result