from datetime import datetime, timedelta

def hydrate_time(nanoseconds, tz=None):
    """
    Convert nanoseconds to a time in fixed format.
    """
    seconds = nanoseconds / 1e9
    time = datetime(1970, 1, 1) + timedelta(seconds=seconds)
    if tz:
        time = time.replace(tzinfo=tz)
    return time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]