def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if value is None:
		return True
	if isinstance(value, str):
		return re.match(r'^[a-zA-Z0-9\-_]+$', value)
	return False