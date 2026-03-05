
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
    event_name = fake.event_name()
    
    # Validate timezones
    valid_timezones = []
    for tz in timezones:
        if tz in pytz.all_timezones:
            valid_timezones.append(tz)
        elif re.match(r'^UTC[+-]\d{2}:\d{2}$', tz):
            valid_timezones.append(tz)
    
    # Select a timezone if none are valid
    if not valid_timezones:
        timezone = pytz.utc
    else:
        timezone = pytz.timezone(fake.random_element(valid_timezones))
    
    # Format the date and time
    formatted_date = dt_object.strftime('%Y-%m-%d')
    formatted_time = dt_object.strftime('%H:%M:%S')
    
    # Create the event schedule dictionary
    event_schedule = {
        'date': formatted_date,
        'time': formatted_time,
        'timezone': timezone.zone
    }
    
    # Return the dictionary with the fake event name as key and the event schedule as value
    return {event_name: [event_schedule]}