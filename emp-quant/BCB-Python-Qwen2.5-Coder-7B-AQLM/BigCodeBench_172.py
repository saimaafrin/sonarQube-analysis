
import json
from datetime import datetime

def task_func(json_data):
    # Load the JSON data
    data = json.loads(json_data)
    
    # Extract the datetime string from the 'utc_datetime' key
    datetime_str = data['utc_datetime']
    
    # Convert the datetime string to a datetime object
    dt_object = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    
    # Check if the day of the week is Saturday or Sunday
    if dt_object.weekday() == 5 or dt_object.weekday() == 6:
        return True
    else:
        return False