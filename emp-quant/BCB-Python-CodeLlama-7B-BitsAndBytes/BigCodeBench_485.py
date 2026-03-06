
from datetime import datetime, timedelta
import pytz
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_time, end_time):
    # Define the time zones to compare
    time_zones = ['UTC', 'America/Los_Angeles', 'Europe/Paris', 'Asia/Kolkata', 'Australia/Sydney']

    # Create a list of dates within the specified date range
    dates = [start_time + timedelta(days=x) for x in range(0, (end_time - start_time).days + 1)]

    # Create a list of time differences between UTC and each time zone for each date
    time_diffs = []
    for date in dates:
        utc_date = datetime(date.year, date.month, date.day, tzinfo=pytz.utc)
        time_diffs.append([(utc_date - pytz.timezone(tz).localize(utc_date)).total_seconds() / 3600 for tz in time_zones])

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Plot the time differences for each time zone
    for i, tz in enumerate(time_zones):
        ax.plot(dates, time_diffs[i], color=['b', 'g', 'r', 'c', 'm', 'y', 'k'][i])
        ax.set_xlabel('Date')
        ax.set_ylabel('Time Difference (hours)')
        ax.set_title(f'Time Differences between UTC and {tz}')

    return ax