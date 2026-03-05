from datetime import datetime, tzoffset

def default_tzinfo(dt, tzinfo):
    if not dt.tzinfo:
        return dt.replace(tzinfo=tzinfo)
    return dt