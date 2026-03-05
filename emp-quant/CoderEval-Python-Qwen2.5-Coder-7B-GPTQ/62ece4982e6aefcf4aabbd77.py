import re
from datetime import timedelta

def parse_frequency(frequency):
    if frequency is None or frequency == "always":
        return None
    
    match = re.match(r'(\d+)\s+(\w+)', frequency)
    if not match:
        raise ValueError("Invalid frequency format")
    
    number, unit = match.groups()
    try:
        number = int(number)
    except ValueError:
        raise ValueError("Number part of frequency must be an integer")
    
    if unit == 'seconds':
        return timedelta(seconds=number)
    elif unit == 'minutes':
        return timedelta(minutes=number)
    elif unit == 'hours':
        return timedelta(hours=number)
    elif unit == 'days':
        return timedelta(days=number)
    else:
        raise ValueError("Unsupported time unit")