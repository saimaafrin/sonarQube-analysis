from datetime import datetime
import pytz
import re
from faker import Faker
def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    """
    Create a dictionary with a fake event schedule given an event time.
    The function converts a given epoch in milliseconds into a datetime object in the current system time's timezone.
    It generates a fake event name using Faker. Then, it uses pytz and regex to check if specified timezones are valid (i.e. in pytz.all_timezones or can be parsed using regex from UTC±HH:MM format), ignoring invalid ones. If none is valid or if timezones were not specified, it selects UTC; otherwise, it randomly selects a valid one using Faker. Finally, the function returns a dictionary with the fake event name as key and a list as value, where the list itself contains a schedule, i.e. a dictionary with keys 'date', 'time', 'timezone'.
    """
    # Convert epoch milliseconds to datetime object
    dt = datetime.fromtimestamp(epoch_milliseconds / 1000)

    # Generate fake event name using Faker
    fake = Faker()
    event_name = fake.name()

    # Check if specified timezones are valid
    valid_timezones = []
    for tz in timezones:
        if tz in pytz.all_timezones or re.match(r"UTC[+-]\d{2}:\d{2}", tz):
            valid_timezones.append(tz)

    # Select a valid timezone
    if not valid_timezones:
        tz = "UTC"
    else:
        tz = random.choice(valid_timezones)

    # Generate fake event schedule
    schedule = {
        "date": dt.date(),
        "time": dt.time(),
        "timezone": tz
    }

    # Return dictionary with fake event name and schedule
    return {event_name: [schedule]}