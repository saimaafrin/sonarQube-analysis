from datetime import datetime, timedelta, timezone

def default_tzinfo(dt, tzinfo):
    if dt.tzinfo is None:
        return dt.replace(tzinfo=tzinfo)
    else:
        return dt