from datetime import datetime, timezone

def ensure_timezone(dt):
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt

def format_dt(dt):
    dt = ensure_timezone(dt)
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')