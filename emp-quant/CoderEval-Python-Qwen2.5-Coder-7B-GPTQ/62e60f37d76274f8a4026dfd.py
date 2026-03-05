from datetime import datetime

class Time:
    def __init__(self, value):
        self.value = value

class Structure:
    def __init__(self, time_value):
        self.time_value = time_value

def dehydrate_time(value):
    return Structure(Time(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))