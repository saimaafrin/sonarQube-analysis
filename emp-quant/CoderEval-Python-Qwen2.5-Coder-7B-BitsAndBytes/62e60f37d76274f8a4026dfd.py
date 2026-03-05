from datetime import time

class Structure:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def dehydrate_time(value):
    """
    Use ticks in the Time class to generate the Structure class.
    """
    if isinstance(value, time):
        return Structure(value.hour, value.minute, value.second)
    else:
        raise ValueError("Input must be a datetime.time object")