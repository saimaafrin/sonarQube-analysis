def default_tzinfo(dt, tzinfo):
# If the datetime is already aware, return it unchanged.
	if dt.tzinfo is not None:
		return dt

	# Otherwise, attach the specified timezone and return the result.
	return dt.replace(tzinfo=tzinfo)