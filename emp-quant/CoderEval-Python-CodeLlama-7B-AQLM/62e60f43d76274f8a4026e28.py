def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	seconds = nanoseconds / 1000000000
	nanoseconds = nanoseconds % 1000000000
	return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(seconds)) + \
		"." + str(nanoseconds).zfill(9) + \
		("Z" if tz is None else tz)