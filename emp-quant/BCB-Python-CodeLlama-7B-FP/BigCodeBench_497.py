from datetime import datetime, timedelta
import pytz
import calendar
def task_func(days_in_past=7):
    """
    Get the weekday of the date 'days_in_past' days ago from today.
    This function computes the date that is 'days_in_past' number of days ago from the current system time's date in UTC.
    It then determines the weekday of this target date using calendar and returns its name as a string.
    The function should raise the exception for: ValueError: If 'days_in_past' is negative.
    The function should output with:
        weekday (str)     : The name of the weekday (e.g., 'Monday', 'Tuesday') for the computed date.
    """
    if days_in_past < 0:
        raise ValueError("'days_in_past' must be non-negative")

    # Compute the date that is 'days_in_past' days ago from today
    today = datetime.now(pytz.utc)
    target_date = today - timedelta(days=days_in_past)

    # Determine the weekday of the target date
    weekday = calendar.day_name[target_date.weekday()]

    return weekday