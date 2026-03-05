
from datetime import datetime
import pytz
import re
from faker import Faker

def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    # Convert epoch to datetime object in the current system's timezone
    current_time = datetime.fromtimestamp(epoch_milliseconds)

    # Create a fake event name using Faker
    fake_event_name = Faker.name()

    # Check if specified timezones are valid
    for timezone in timezones:
        if not re.match(r"^[+-]?[0-9][0-9:]+$", timezone):
            raise ValueError("Invalid timezone format")
        if timezone not in pytz.all_timezones:
            raise ValueError("Invalid timezone")

    # Select a valid timezone
    if len(timezones) == 0:
        selected_timezone = "UTC"
    else:
        selected_timezone = random.choice(timezones)

    # Create a dictionary with the fake event name as key and a list as value
    event_details = {
        "name": fake_event_name,
        "schedule": [
            {
                "date": current_time.date().isoformat(),
                "time": current_time.time().isoformat(),
                "timezone": selected_timezone
            }
        ]
    }

    return event_details