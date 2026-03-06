
from datetime import datetime
import pytz
import re
from faker import Faker

def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    # Initialize Faker with the provided seed
    fake = Faker()
    fake.seed(seed)
    
    # Convert epoch milliseconds to datetime object
    dt_object = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    
    # Generate a fake event name
    event_name = fake.event_name()
    
    # Function to validate timezone
    def is_valid_timezone(tz_str):
        try:
            pytz.timezone(tz_str)
            return True
        except pytz.exceptions.UnknownTimeZoneError:
            match = re.match(r'UTC[+-]\d{2}:\d{2}', tz_str)
            return bool(match)
    
    # Filter out invalid timezones
    valid_timezones = [tz for tz in timezones if is_valid_timezone(tz)]
    
    # Select a random timezone if none are valid or if no timezones were specified
    selected_timezone = fake.random_element(valid_timezones) if valid_timezones else "UTC"
    
    # Create the event schedule dictionary
    event_schedule = {
        'date': dt_object.strftime('%Y-%m-%d'),
        'time': dt_object.strftime('%H:%M:%S'),
        'timezone': selected_timezone
    }
    
    # Return the result as a dictionary with the event name as the key
    return {event_name: [event_schedule]}