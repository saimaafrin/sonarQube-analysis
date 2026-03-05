
from datetime import datetime, timedelta
import pytz
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_time, end_time):
    # Create a list of time zones to plot
    time_zones = ['UTC', 'America/Los_Angeles', 'Europe/Paris', 'Asia/Kolkata', 'Australia/Sydney']

    # Create a list of dates to plot
    dates = [start_time + timedelta(days=x) for x in range(end_time - start_time.days)]

    # Create a list of time differences between UTC and each time zone
    time_diffs = []
    for tz in time_zones:
        time_diffs.append([])
        for date in dates:
            tz_dt = pytz.timezone(tz).localize(date)
            utc_dt = pytz.utc.localize(date)
            time_diffs[-1].append(tz_dt - utc_dt)

    # Plot the time differences
    fig, ax = plt.subplots()
    for i, tz in enumerate(time_zones):
        ax.plot(dates, time_diffs[i], color=['b', 'g', 'r', 'c', 'm', 'y', 'k'][i])
        ax.set_xlabel('Date')
        ax.set_ylabel('Time Difference (hours)')
        ax.set_title(f'Time Differences between UTC and {tz}')
    return ax