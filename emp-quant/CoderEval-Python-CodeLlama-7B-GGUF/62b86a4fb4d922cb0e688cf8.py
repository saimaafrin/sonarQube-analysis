def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if value is None:
		return True
	if not isinstance(value, str):
		return False
	return bool(re.match(r'^[a-zA-Z0-9_-]+$', value))