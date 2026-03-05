
from datetime import datetime
import pytz
import re
from faker import Faker

def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    # Initialize Faker with the seed
    fake = Faker()
    fake.seed(seed)

    # Convert epoch milliseconds to datetime
    event_time = datetime.fromtimestamp(epoch_milliseconds / 1000.0)

    # Define a regex pattern for valid timezones
    timezone_pattern = re.compile(r'^UTC[+-]\d{2}:\d{2}$')

    # Filter valid timezones
    valid_timezones = [tz for tz in timezones if tz in pytz.all_timezones or timezone_pattern.match(tz)]

    # If no valid timezones are found, use UTC
    if not valid_timezones:
        timezone = 'UTC'
    else:
        # Randomly select a valid timezone
        timezone = fake.timezone(value=valid_timezones)

    # Create a fake event name
    event_name = fake.word()

    # Create a schedule dictionary
    schedule = {
        'date': event_time.strftime('%Y-%m-%d'),
        'time': event_time.strftime('%H:%M'),
        'timezone': timezone
    }

    # Return the dictionary with the fake event name and schedule
    return {event_name: [schedule]}