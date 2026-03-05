def _validate_labels(labels):
# Check that all keys are valid
	for key in labels:
		if not validate_key(key):
			return False

	# Check that all values are valid
	for value in labels.values():
		if not validate_value(value):
			return False

	return True