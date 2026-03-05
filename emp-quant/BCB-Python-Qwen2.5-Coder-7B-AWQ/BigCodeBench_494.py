from datetime import datetime
import pytz
import re
from faker import Faker
def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    fake = Faker()
    Faker.seed(seed)
    
    # Convert epoch milliseconds to datetime object
    dt_object = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    
    # Generate a fake event name
    event_name = fake.catch_phrase()
    
    # Function to check if a timezone is valid
    def is_valid_timezone(tz):
        return tz in pytz.all_timezones or re.match(r'^UTC[+-]\d{2}:\d{2}$', tz)
    
    # Filter out invalid timezones
    valid_timezones = [tz for tz in timezones if is_valid_timezone(tz)]
    
    # If no valid timezones are provided, use UTC
    if not valid_timezones:
        valid_timezones = ["UTC"]
    
    # Randomly select a valid timezone
    selected_timezone = fake.random_element(valid_timezones)
    
    # Create a dictionary for the event schedule
    event_schedule = {
        'date': dt_object.strftime('%Y-%m-%d'),
        'time': dt_object.strftime('%H:%M:%S'),
        'timezone': selected_timezone
    }
    
    # Return the dictionary with the fake event name and schedule
    return {event_name: [event_schedule]}