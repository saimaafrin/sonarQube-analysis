
from datetime import datetime
import pytz
import re
from faker import Faker

def task_func(epoch_milliseconds, seed=0, timezones=["UTC"]):
    fake = Faker()
    Faker.seed(seed)
    
    # Convert epoch milliseconds to datetime object
    dt_object = datetime.fromtimestamp(epoch_milliseconds / 1000)
    
    # Generate a fake event name
    event_name = fake.catch_phrase()
    
    # Validate timezones
    valid_timezones = [tz for tz in timezones if tz in pytz.all_timezones or re.match(r'^UTC[+-]\d{2}:\d{2}$', tz)]
    
    # Select a timezone
    if not valid_timezones:
        selected_timezone = pytz.utc
    else:
        selected_timezone = pytz.timezone(fake.random_element(valid_timezones))
    
    # Format datetime object to string
    formatted_date = dt_object.strftime('%Y-%m-%d')
    formatted_time = dt_object.strftime('%H:%M:%S')
    
    # Create event schedule dictionary
    event_schedule = {
        'date': formatted_date,
        'time': formatted_time,
        'timezone': selected_timezone.zone
    }
    
    # Return dictionary with event name as key and event details as value
    return {event_name: [event_schedule]}