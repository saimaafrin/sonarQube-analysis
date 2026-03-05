def _fromutc(self, dt):
	"""
	Given a timezone datetime in a given timezone, calculates a timezone datetime in a new timezone.
	"""
	if dt.tzinfo is None:
		return self.localize(dt, is_dst=None)
	else:
		return self.normalize(dt.astimezone(self))