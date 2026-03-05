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
    """
    Generate a weather report for specified cities at a given UTC datetime.

    Parameters
    ----------
    utc_datetime : datetime
        The UTC datetime for which the weather report is generated.
    cities : list of str, optional
        The list of cities for which the weather report is generated.
        Defaults to ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'].
    weather_conditions : list of str, optional
        The list of weather conditions for each city.
        Defaults to ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy'].
    timezones : dict of str, optional
        The dictionary of timezones for each city.
        Defaults to {'New York': 'America/New_York', 'London': 'Europe/London', 'Beijing': 'Asia/Shanghai', 'Tokyo': 'Asia/Tokyo', 'Sydney': 'Australia/Sydney'}.
    seed : int, optional
        The random seed for generating the weather conditions.
        Defaults to 42.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the weather report.
        Columns include:
        'City': The name of the city.
        'Local Time': The local time of the weather report for the city, formatted as 'YYYY-MM-DD HH:MM:SS ZZZ' (ZZZ is the timezone abbreviation).
        'Weather Condition': The weather condition in the city at the given local time.

    Raises
    ------
    ValueError
        If utc_datetime is not a datetime object or if any of the other parameters are not in the expected format.
    """
    # Check if utc_datetime is a datetime object
    if not isinstance(utc_datetime, datetime):
        raise ValueError('utc_datetime must be a datetime object')

    # Check if cities, weather_conditions, and timezones are lists and dictionaries
    if not isinstance(cities, list):
        raise ValueError('cities must be a list')
    if not isinstance(weather_conditions, list):
        raise ValueError('weather_conditions must be a list')
    if not isinstance(timezones, dict):
        raise ValueError('timezones must be a dictionary')

    # Generate random weather conditions for each city
    set_seed(seed)
    weather_conditions_by_city = {city: weather_conditions[randint(0, len(weather_conditions) - 1)] for city in cities}

    # Convert UTC datetime to local time for each city
    local_times = {city: utc_datetime.astimezone(pytz.timezone(timezones[city])) for city in cities}

    # Create DataFrame with weather report
    df = pd.DataFrame({
        'City': cities,
        'Local Time': [local_time.strftime('%Y-%m-%d %H:%M:%S %Z') for local_time in local_times.values()],
        'Weather Condition': [weather_condition for weather_condition in weather_conditions_by_city.values()]
    })

    return df