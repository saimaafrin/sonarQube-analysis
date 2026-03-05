
import pandas as pd
import pytz
from datetime import datetime
from random import randint, seed as set_seed

def task_func(
    utc_datetime,
    cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'],
    weather_conditions=['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy'],
    timezones={
        'New York': 'America/New_York',
        'London': 'Europe/London',
        'Beijing': 'Asia/Shanghai',
        'Tokyo': 'Asia/Tokyo',
        'Sydney': 'Australia/Sydney'
    },
    seed=42
):
    # Set the seed for random number generation
    set_seed(seed)

    # Check if utc_datetime is a datetime object
    if not isinstance(utc_datetime, datetime):
        raise ValueError("utc_datetime must be a datetime object")

    # Create an empty list to store the weather report data
    weather_report = []

    # Loop through each city to generate the weather report
    for city in cities:
        # Get the timezone for the city
        timezone = timezones.get(city)
        if timezone is None:
            raise ValueError(f"Unknown city: {city}")

        # Convert the UTC datetime to the local timezone
        local_time = utc_datetime.astimezone(pytz.timezone(timezone))

        # Select a random weather condition
        weather_condition = weather_conditions[randint(0, len(weather_conditions) - 1)]

        # Append the weather report data to the list
        weather_report.append({
            'City': city,
            'Local Time': local_time.strftime('%Y-%m-%d %H:%M:%S %Z'),
            'Weather Condition': weather_condition
        })

    # Create a pandas DataFrame from the weather report data
    df = pd.DataFrame(weather_report)

    return df