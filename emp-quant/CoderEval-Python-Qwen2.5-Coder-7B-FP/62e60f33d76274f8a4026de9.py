def dehydrate_point(value):
# If the value is a string, we need to check if it's a valid hexadecimal number
	if isinstance(value, str) and all(c in '0123456789ABCDEFabcdef' for c in value):
		return {'type': 'hex', 'value': value}
	
	# If the value is an integer, we can directly return it as a dictionary
	elif isinstance(value, int):
		return {'type': 'int', 'value': value}
	
	# If the value is a float, we can also directly return it as a dictionary
	elif isinstance(value, float):
		return {'type': 'float', 'value': value}
	
	# If the value is a boolean, we can convert it to a string and return it as a dictionary
	elif isinstance(value, bool):
		return {'type': 'bool', 'value': str(value).lower()}
	
	# If the value is None, we can return it as a dictionary with type 'none'
	elif value is None:
		return {'type': 'none'}
	
	# If the value is a list, we can recursively call this function for each element in the list
	elif isinstance(value, list):
		return {'type': 'list', 'value': [dehydrate_point(v) for v in value]}
	
	# If the value is a dictionary, we can recursively call this function for each key-value pair in the dictionary
	elif isinstance(value, dict):
		return {'type': 'dict', 'value': {k: dehydrate_point(v) for k, v in value.items()}}
	
	# If the value is of any other type, we raise a TypeError
	else:
		raise TypeError(f"Unsupported data type: {type(value)}")