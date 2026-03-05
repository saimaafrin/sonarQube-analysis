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
    dt = datetime.fromtimestamp(epoch_milliseconds / 1000.0)

    # Generate fake event name using Faker
    fake = Faker()
    event_name = fake.name()

    # Check if specified timezones are valid
    valid_timezones = []
    for tz in timezones:
        if tz in pytz.all_timezones or re.match(r'UTC[+-]\d{2}:\d{2}', tz):
            valid_timezones.append(tz)

    # Select a valid timezone if none are valid or if timezones were not specified
    if not valid_timezones:
        tz = 'UTC'
    else:
        tz = random.choice(valid_timezones)

    # Convert datetime object to specified timezone
    dt_tz = pytz.timezone(tz).localize(dt)

    # Create schedule dictionary
    schedule = {
        'date': dt_tz.date(),
        'time': dt_tz.time(),
        'timezone': tz
    }

    # Create event details dictionary
    event_details = {
        event_name: schedule
    }

    return event_details