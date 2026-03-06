def validate_key(key):
	"""
	Validate the given key against the corresponding regular expression.
	"""
	if key in _key_regex:
		return _key_regex[key].match(key)
	else:
		return None