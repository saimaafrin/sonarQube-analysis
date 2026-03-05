def _dictsum(dicts):
# Create an empty dictionary to store the result
	result = {}
	
	# Iterate over each dictionary in the list of dictionaries
	for d in dicts:
		# Iterate over each key-value pair in the current dictionary
		for k, v in d.items():
			# If the key is already in the result dictionary, add the value to the existing value
			if k in result:
				result[k] += v
			# Otherwise, add the key-value pair to the result dictionary
			else:
				result[k] = v
	
	# Return the resulting dictionary
	return result