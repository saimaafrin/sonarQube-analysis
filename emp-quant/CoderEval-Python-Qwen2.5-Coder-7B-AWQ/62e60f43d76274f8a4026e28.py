from datetime import timedelta

def hydrate_time(nanoseconds, tz=None):
    seconds = nanoseconds / 1e9
    return timedelta(seconds=seconds).isoformat(timespec='ns')