import json
from datetime import datetime
def task_func(json_data):
    # Load the JSON data
    data = json.loads(json_data)
    
    # Extract the 'utc_datetime' string
    utc_datetime_str = data['utc_datetime']
    
    # Convert the string to a datetime object
    utc_datetime = datetime.strptime(utc_datetime_str, '%Y-%m-%dT%H:%M:%SZ')
    
    # Check if the day of the week is Saturday or Sunday
    return utc_datetime.weekday() >= 5  # 5 and 6 represent Saturday and Sunday respectively