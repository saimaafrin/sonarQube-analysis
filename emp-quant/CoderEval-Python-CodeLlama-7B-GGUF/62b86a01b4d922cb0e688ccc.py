def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""
	observer_schema_dict = {}
	for key, value in manifest_dict.items():
		if isinstance(value, dict):
			observer_schema_dict[key] = generate_default_observer_schema_dict(value)
		elif isinstance(value, list):
			observer_schema_dict[key] = []
		else:
			observer_schema_dict[key] = value
	if first_level:
		observer_schema_dict['type'] = 'object'
		observer_schema_dict['properties'] = {}
		observer_schema_dict['required'] = []
	return observer_schema_dict