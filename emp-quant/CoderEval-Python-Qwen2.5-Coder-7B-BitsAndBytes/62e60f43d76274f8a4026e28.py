from datetime import timedelta

def hydrate_time(nanoseconds, tz=None):
    seconds = nanoseconds // 1_000_000_000
    microseconds = (nanoseconds % 1_000_000_000) // 1_000
    return timedelta(seconds=seconds, microseconds=microseconds).replace(tzinfo=tz)