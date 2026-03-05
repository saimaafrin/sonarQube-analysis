def _dictsum(dicts):
	"""
	Sum values with the same key in the dictionaries. And return a new dictionary.
    Example:
        given two dictionaries: dict1: {'a': 1, 'b': 2}, dict2: {'a': 5, 'b': 0}
        return a dictionary: dic:{'a': 6, 'b': 2}
    Returns: dict
	"""
	new_dict = {}
	for key in dicts[0]:
		sum_value = 0
		for i in range(len(dicts)):
			sum_value += dicts[i].get(key, 0)
		new_dict[key] = sum_value
	return new_dict