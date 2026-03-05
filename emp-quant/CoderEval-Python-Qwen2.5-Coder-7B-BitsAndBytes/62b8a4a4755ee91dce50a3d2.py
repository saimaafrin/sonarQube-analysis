import pytz

def _fromutc(self, dt, new_tz_str):
    """
    Given a timezone datetime in UTC, calculates a timezone datetime in a new timezone.
    """
    utc_dt = dt.replace(tzinfo=pytz.utc)
    new_tz = pytz.timezone(new_tz_str)
    return utc_dt.astimezone(new_tz)