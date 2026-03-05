def hydrate_time(nanoseconds, tz=None):
if tz is None:
		tz = timezone.utc
	return datetime.fromtimestamp(nanoseconds / 1e9, tz)