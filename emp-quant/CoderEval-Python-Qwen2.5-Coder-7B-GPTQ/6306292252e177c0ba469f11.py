from datetime import timezone

def ensure_timezone(dt):
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt

def format_dt(dt):
    formatted_time = ensure_timezone(dt).strftime('%H:%M:%S')
    return formatted_time