def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if tz is None:
		tz = get_timezone()
	return tz.localize(datetime.fromtimestamp(nanoseconds / 1e9))