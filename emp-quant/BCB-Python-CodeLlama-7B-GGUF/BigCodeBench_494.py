
from datetime import datetime
import pytz
import re
from faker import Faker

def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    # Convert epoch milliseconds to datetime object in current system timezone
    dt = datetime.fromtimestamp(epoch_milliseconds / 1000.0)

    # Generate fake event name using Faker
    fake = Faker()
    event_name = fake.name()

    # Check if specified timezones are valid
    valid_timezones = []
    for tz in timezones:
        if tz in pytz.all_timezones or re.match(r"UTC\+[0-9]{2}:[0-9]{2}", tz):
            valid_timezones.append(tz)

    # Select a valid timezone if none are valid or if timezones were not specified
    if not valid_timezones:
        tz = "UTC"
    else:
        tz = random.choice(valid_timezones)

    # Create a dictionary with event details
    event_details = {
        "date": dt.date(),
        "time": dt.time(),
        "timezone": tz
    }

    # Return a dictionary with event name as key and event details as value
    return {event_name: event_details}