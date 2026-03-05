def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if dt.tzinfo is None:
		return self.localize(dt)
	else:
		return dt.astimezone(self)