def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if value is None:
		return None
	if not isinstance(value, str):
		raise ValueError("Expected a string value.")
	if not re.match(r"^[a-zA-Z0-9_-]+$", value):
		raise ValueError("Expected a string value.")
	return value