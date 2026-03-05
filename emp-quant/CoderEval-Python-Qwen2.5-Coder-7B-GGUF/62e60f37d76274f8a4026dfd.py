from datetime import datetime, timedelta

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_ticks(self):
        return (self.hours * 3600 + self.minutes * 60 + self.seconds) * 10000

class Structure:
    def __init__(self, ticks):
        self.ticks = ticks

def dehydrate_time(value):
    hours, minutes, seconds = map(int, value.split(':'))
    time_obj = Time(hours, minutes, seconds)
    ticks = time_obj.to_ticks()
    return Structure(ticks)