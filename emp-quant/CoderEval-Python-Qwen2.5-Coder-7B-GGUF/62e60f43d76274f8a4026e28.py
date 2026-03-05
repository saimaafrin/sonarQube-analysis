from datetime import datetime, timedelta

def hydrate_time(nanoseconds, tz=None):
    seconds, nanoseconds = divmod(nanoseconds, 1e9)
    microseconds = nanoseconds // 1e3
    milliseconds = nanoseconds // 1e6
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    
    time_str = f"{days}d {hours}h {minutes}m {seconds}s {milliseconds}ms {microseconds}us"
    
    if tz:
        dt = datetime(1970, 1, 1) + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)
        dt = dt.replace(tzinfo=tz)
        time_str += f" {dt.strftime('%Z%z')}"
    
    return time_str