def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	if not isinstance(labels, dict):
		raise ValueError("labels must be a dict")
	for key, value in labels.items():
		validate_key(key)
		validate_value(value)