def _fromutc(self, dt):
    """
    Given a timezone datetime in UTC, calculates a timezone datetime in a new timezone.
    """
    return dt.astimezone(self._new_timezone)