def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if matcher.groupdict()['default']:
		return matcher.groupdict()['default']
	else:
		return matcher.groupdict()['name']