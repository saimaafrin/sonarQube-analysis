from datetime import datetime, timedelta
import pytz
import calendar
def task_func(days_in_past=7):
    """
    Get the weekday of the date 'days_in_past' days ago from today.

    Parameters:
    days_in_past (int): The number of days in the past to calculate the weekday for.

    Returns:
    str: The name of the weekday (e.g., 'Monday', 'Tuesday') for the computed date.

    Raises:
    ValueError: If 'days_in_past' is negative.
    """
    if days_in_past < 0:
        raise ValueError("days_in_past must be a non-negative integer")

    # Get the current UTC date and time
    utc_now = datetime.now(pytz.utc)

    # Calculate the date 'days_in_past' days ago
    target_date = utc_now - timedelta(days=days_in_past)

    # Get the weekday as an integer (0=Monday, 6=Sunday)
    weekday_int = target_date.weekday()

    # Map the integer to the weekday name
    weekday_name = calendar.day_name[weekday_int]

    return weekday_name