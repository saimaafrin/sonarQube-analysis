import json
from datetime import datetime
def task_func(json_data):
    """
    Determine if the given datetime is a weekend.
    """
    utc_datetime = json_data['utc_datetime']
    date = datetime.strptime(utc_datetime, '%Y-%m-%dT%H:%M:%S.%fZ')
    if date.weekday() in [5, 6]:
        return True
    else:
        return False
json_data = {
    'utc_datetime': '2023-03-12T15:30:00.000Z'
}