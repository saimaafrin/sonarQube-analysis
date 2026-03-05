def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 0:
		return []
	else:
		return [value[0]] + dehydrate_point(value[1:])