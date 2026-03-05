def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	if not isinstance(labels, dict):
		raise ValueError("labels must be a dict")
	for key, value in labels.items():
		if not isinstance(key, str):
			raise ValueError("labels keys must be strings")
		if not isinstance(value, str):
			raise ValueError("labels values must be strings")
	return labels