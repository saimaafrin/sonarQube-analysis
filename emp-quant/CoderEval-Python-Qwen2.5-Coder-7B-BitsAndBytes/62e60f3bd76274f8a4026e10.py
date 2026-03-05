from datetime import timedelta

class Structure:
    def __init__(self, days=0, seconds=0, microseconds=0):
        self.days = days
        self.seconds = seconds
        self.microseconds = microseconds

def dehydrate_timedelta(value):
    return Structure(days=value.days, seconds=value.seconds, microseconds=value.microseconds)