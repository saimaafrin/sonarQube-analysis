from datetime import timedelta

def hydrate_time(nanoseconds, tz=None):
    seconds = nanoseconds // 1_000_000_000
    microseconds = (nanoseconds % 1_000_000_000) // 1_000
    milliseconds = (nanoseconds % 1_000_000_000) % 1_000
    return f"{seconds:02d}:{microseconds:06d}.{milliseconds:03d}"