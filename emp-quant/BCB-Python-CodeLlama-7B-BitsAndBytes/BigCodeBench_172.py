
import json
from datetime import datetime

def task_func(json_data):
    # Parse the JSON data
    data = json.loads(json_data)

    # Extract the datetime from the JSON data
    utc_datetime = data['utc_datetime']

    # Convert the datetime to a Python datetime object
    python_datetime = datetime.fromisoformat(utc_datetime)

    # Check if the datetime is a weekend
    if python_datetime.weekday() in [5, 6]:
        return True
    else:
        return False