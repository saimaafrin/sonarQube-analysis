def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 1:
		return value[0]
	elif len(value) == 2:
		return (value[0], value[1])
	elif len(value) == 3:
		return (value[0], value[1], value[2])
	elif len(value) == 4:
		return (value[0], value[1], value[2], value[3])
	elif len(value) == 5:
		return (value[0], value[1], value[2], value[3], value[4])
	elif len(value) == 6:
		return (value[0], value[1], value[2], value[3], value[4], value[5])
	elif len(value) == 7:
		return (value[0], value[1], value[2], value[3], value[4], value[5], value[6])
	elif len(value) == 8:
		return (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7])
	elif len(value) == 9:
		return (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8])
	elif len(value) == 10:
		return (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9])
	elif len(value) == 11:
		return (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10])
	elif len(value) == 12:
		return (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10], value[11])
	elif len(