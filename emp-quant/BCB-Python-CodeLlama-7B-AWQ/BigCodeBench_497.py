from datetime import datetime, timedelta
import pytz
import calendar
def task_func(days_in_past=7):
    """
    Get the weekday of the date 'days_in_past' days ago from today.
    This function computes the date that is 'days_in_past' number of days ago from the current system time's date in UTC.
    It then determines the weekday of this target date using calendar and returns its name as a string.
    """
    if days_in_past < 0:
        raise ValueError("ValueError: If 'days_in_past' is negative.")

    # Get the current date in UTC
    now = datetime.now(pytz.utc)

    # Compute the target date
    target_date = now - timedelta(days=days_in_past)

    # Get the weekday of the target date
    weekday = calendar.day_name[target_date.weekday()]

    return weekday