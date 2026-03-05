
import json
from datetime import datetime

def is_weekend(utc_datetime):
    """
    Determine if the given datetime is a weekend.

    Args:
        utc_datetime (datetime): The datetime to be checked.

    Returns:
        bool: True if the date is a weekend (Saturday or Sunday), False otherwise.
    """
    return utc_datetime.weekday() in [5, 6]

def task_func(json_data):
    """
    Extract the 'utc_datetime' key from the JSON data and pass it to the is_weekend function.

    Args:
        json_data (dict): The JSON data containing the 'utc_datetime' key.

    Returns:
        bool: The result of the is_weekend function.
    """
    utc_datetime = json_data['utc_datetime']
    return is_weekend(utc_datetime)

json_data = {'utc_datetime': '2022-03-12T12:00:00Z'}
print(task_func(json_data))  # Output: True