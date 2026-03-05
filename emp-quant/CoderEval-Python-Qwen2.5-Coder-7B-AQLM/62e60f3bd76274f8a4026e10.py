from datetime import timedelta

class Structure:
    def __init__(self, days, seconds, microseconds):
        self.days = days
        self.seconds = seconds
        self.microseconds = microseconds

def dehydrate_timedelta(value):
    return Structure(value.days, value.seconds, value.microseconds)