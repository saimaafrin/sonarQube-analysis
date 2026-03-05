import pytz

def _fromutc(self, dt):
    """
    Given a timezone datetime in UTC, calculates a timezone datetime in a new timezone.
    """
    return dt.astimezone(pytz.timezone('new_timezone'))