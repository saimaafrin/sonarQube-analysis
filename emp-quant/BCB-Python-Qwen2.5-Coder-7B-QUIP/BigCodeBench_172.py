
import json
from datetime import datetime

def task_func(json_data):
    # Load the JSON data
    data = json.loads(json_data)
    
    # Extract the datetime string from the 'utc_datetime' key
    utc_datetime_str = data['utc_datetime']
    
    # Convert the datetime string to a datetime object
    utc_datetime = datetime.strptime(utc_datetime_str, '%Y-%m-%dT%H:%M:%S')
    
    # Check if the day of the week is Saturday or Sunday
    if utc_datetime.weekday() == 5 or utc_datetime.weekday() == 6:
        return True
    else:
        return False