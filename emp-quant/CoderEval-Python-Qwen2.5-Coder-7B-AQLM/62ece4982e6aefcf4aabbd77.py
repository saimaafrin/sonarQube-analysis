import datetime

def parse_frequency(frequency):
    if frequency is None or frequency == "always":
        return None
    try:
        number, unit = frequency.split()
        number = int(number)
        if unit == "seconds":
            return datetime.timedelta(seconds=number)
        elif unit == "minutes":
            return datetime.timedelta(minutes=number)
        elif unit == "hours":
            return datetime.timedelta(hours=number)
        elif unit == "days":
            return datetime.timedelta(days=number)
        elif unit == "weeks":
            return datetime.timedelta(weeks=number)
        else:
            raise ValueError("Invalid time unit")
    except (ValueError, AttributeError):
        raise ValueError("Invalid frequency format")