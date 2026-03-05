def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	if value is None:
		return None
	if isinstance(value, timedelta):
		return value.total_seconds()
	return value