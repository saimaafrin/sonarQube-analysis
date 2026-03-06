def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if value is None:
		return True
	if not isinstance(value, str):
		return False
	return re.match(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$', value) is not None