import json
from datetime import datetime
def task_func(json_data):
    """
    Determine if the given datetime is a weekend.
    """
    utc_datetime = json_data['utc_datetime']
    date = datetime.fromisoformat(utc_datetime)
    return date.weekday() in [5, 6]