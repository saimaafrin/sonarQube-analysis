def generate_default_observer_schema_dict(manifest_dict, first_level=False):
# Initialize an empty dictionary
	default_observer_schema_dict = {}

	# Iterate over each key-value pair in the manifest_dict
	for key, value in manifest_dict.items():
		if isinstance(value, dict):
			# If the value is a dictionary, recursively call the function to generate the default schema for this sub-dictionary
			default_observer_schema_dict[key] = generate_default_observer_schema_dict(value)
		elif isinstance(value, list):
			# If the value is a list, check if it contains any dictionaries
			if value and isinstance(value[0], dict):
				# If the list contains dictionaries, recursively call the function to generate the default schema for these sub-dictionaries
				default_observer_schema_dict[key] = [generate_default_observer_schema_dict(item) for item in value]
			else:
				# If the list does not contain dictionaries, set the default value to None
				default_observer_schema_dict[key] = None
		else:
			# If the value is neither a dictionary nor a list, set the default value to None
			default_observer_schema_dict[key] = None

	return default_observer_schema_dict