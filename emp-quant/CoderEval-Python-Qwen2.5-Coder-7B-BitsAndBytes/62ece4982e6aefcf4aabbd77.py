import re
from datetime import timedelta

def parse_frequency(frequency):
    if frequency is None or frequency == "always":
        return None
    
    match = re.match(r'(\d+)\s+(\w+)', frequency)
    if not match:
        raise ValueError("Invalid frequency format")
    
    number, time_unit = match.groups()
    number = int(number)
    
    if time_unit == 'seconds':
        return timedelta(seconds=number)
    elif time_unit == 'minutes':
        return timedelta(minutes=number)
    elif time_unit == 'hours':
        return timedelta(hours=number)
    elif time_unit == 'days':
        return timedelta(days=number)
    else:
        raise ValueError("Unsupported time unit")