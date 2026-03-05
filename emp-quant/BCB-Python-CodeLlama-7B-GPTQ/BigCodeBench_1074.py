import pytz
from dateutil.parser import parse
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_string, from_tz, to_tz):
    """
    Converts a time string from one timezone to another, considering various cases such as daylight saving time.
    Note that:
        - The example assumes no daylight saving time shift between the given timezones at the specified date and time.
        - The function should output with:
            str: The converted time string in the format 'dd/mm/yy HH:MM:SS.fff'.
            The conversion takes into account any differences in daylight saving rules between the source and target timezones.
    """
    # Parse the time string
    time_obj = parse(time_string, TIME_FORMAT)

    # Convert the time object to the target timezone
    converted_time = time_obj.astimezone(pytz.timezone(to_tz))

    # Format the converted time object
    converted_time_str = converted_time.strftime(TIME_FORMAT)

    return converted_time_str