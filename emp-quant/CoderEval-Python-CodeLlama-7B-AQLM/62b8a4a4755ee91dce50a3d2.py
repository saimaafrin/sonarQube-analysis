def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if dt.tzinfo is None:
		raise ValueError("dt must be a timezone aware datetime")
	if self.tzinfo is None:
		raise ValueError("self must be a timezone aware datetime")
	if dt.tzinfo == self.tzinfo:
		return dt
	offset = self.utcoffset(dt) - dt.utcoffset(dt)
	return dt + offset