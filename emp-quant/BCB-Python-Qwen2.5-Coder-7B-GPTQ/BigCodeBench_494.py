from datetime import datetime
import pytz
import re
from faker import Faker
def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    # Initialize Faker with the given seed
    fake = Faker()
    fake.seed(seed)
    
    # Convert epoch milliseconds to datetime object
    dt_object = datetime.fromtimestamp(epoch_milliseconds / 1000.0)
    
    # Generate a fake event name
    event_name = fake.event_name()
    
    # Function to check if a timezone is valid
    def is_valid_timezone(tz):
        return tz in pytz.all_timezones or re.match(r'^UTC[+-]\d{2}:\d{2}$', tz)
    
    # Filter valid timezones
    valid_timezones = [tz for tz in timezones if is_valid_timezone(tz)]
    
    # Select a timezone if valid timezones are provided, otherwise use UTC
    if valid_timezones:
        selected_timezone = fake.random_element(elements=valid_timezones)
    else:
        selected_timezone = 'UTC'
    
    # Set the timezone for the datetime object
    dt_object = dt_object.replace(tzinfo=pytz.timezone(selected_timezone))
    
    # Create the event schedule dictionary
    event_schedule = {
        'date': dt_object.strftime('%Y-%m-%d'),
        'time': dt_object.strftime('%H:%M:%S'),
        'timezone': selected_timezone
    }
    
    # Return the dictionary with the fake event name and its schedule
    return {event_name: [event_schedule]}