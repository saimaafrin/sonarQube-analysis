def generate_default_observer_schema_dict(manifest_dict, first_level=False):
	"""
	The values corresponding to different keys in the new dict are generated based on the value type (such as dict and list) in the manifest_dict file. Then new dictionary is returned.
	"""
	schema_dict = {}
	for key in manifest_dict:
		if first_level:
			schema_dict[key] = {}
		else:
			schema_dict[key] = {}
		if isinstance(manifest_dict[key], dict):
			schema_dict[key] = generate_default_observer_schema_dict(manifest_dict[key], False)
		elif isinstance(manifest_dict[key], list):
			schema_dict[key] = []
		else:
			schema_dict[key] = manifest_dict[key]
	return schema_dict