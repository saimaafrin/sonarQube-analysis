def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if dt.tzinfo is None:
		raise ValueError('Naive datetime is passed')
	offset = dt.utcoffset()
	return dt + offset