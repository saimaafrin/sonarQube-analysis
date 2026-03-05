from datetime import time

class Structure:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

def dehydrate_time(value):
    return Structure(value.hour, value.minute, value.second)