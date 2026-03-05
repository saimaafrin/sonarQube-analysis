def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if tz is None:
		return datetime.time(
			nanoseconds // 1000000000 % 60,
			nanoseconds // 1000000 % 60,
			nanoseconds // 1000 % 60,
			nanoseconds % 1000
		)
	else:
		return datetime.time(
			nanoseconds // 1000000000 % 60,
			nanoseconds // 1000000 % 60,
			nanoseconds // 1000 % 60,
			nanoseconds % 1000,
			tz
		)