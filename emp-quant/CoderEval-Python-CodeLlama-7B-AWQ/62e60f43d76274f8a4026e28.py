def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if tz is None:
		tz = pytz.utc
	return tz.localize(datetime.fromtimestamp(nanoseconds / 1e9))