import json
from datetime import datetime
def task_func(json_data):
    """
    Determine if the given datetime is a weekend.

    Parameters:
    - json_data (str): JSON string containing the datetime in UTC format.

    Returns:
    bool: True if the date is a weekend (Saturday or Sunday), False otherwise.

    Note:
    - The datetime to be extracted is located in the 'utc_datetime' key in the JSON data.

    Requirements:
    - json
    - datetime

    Example:
    >>> json_data = '{"utc_datetime": "2024-04-19T12:00:00"}'
    >>> task_func(json_data)
    False
    """
    # Parse the JSON data
    data = json.loads(json_data)

    # Extract the datetime from the JSON data
    utc_datetime = data['utc_datetime']

    # Convert the datetime to a datetime object
    datetime_object = datetime.strptime(utc_datetime, '%Y-%m-%dT%H:%M:%S')

    # Determine if the datetime is a weekend
    if datetime_object.weekday() == 5 or datetime_object.weekday() == 6:
        return True
    else:
        return False