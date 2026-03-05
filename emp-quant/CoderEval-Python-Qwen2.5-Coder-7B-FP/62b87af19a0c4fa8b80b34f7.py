def difference(d1, d2, level=-1):
# If the current item is a dictionary, recurse
	if isinstance(d1, dict) and isinstance(d2, dict):
		return {k: difference(v, d2.get(k), level+1) for k, v in d1.items() if k not in d2 or difference(v, d2[k], level+1)}
	
	# If the current item is a list, return the difference of each element
	elif isinstance(d1, list) and isinstance(d2, list):
		return [difference(i, j, level+1) for i, j in zip(d1, d2)]
	
	# Otherwise, return the difference between the two items
	else:
		return d1 - d2