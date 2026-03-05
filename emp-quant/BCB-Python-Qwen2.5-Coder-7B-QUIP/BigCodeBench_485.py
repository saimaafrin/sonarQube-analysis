
from datetime import datetime, timedelta
import pytz
import numpy as np
import matplotlib.pyplot as plt

def task_func(start_time, end_time):
    # Define the time zones to compare with UTC
    timezones = ['America/Los_Angeles', 'Europe/Paris', 'Asia/Kolkata', 'Australia/Sydney']
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    
    # Create a date range
    date_range = pd.date_range(start=start_time, end=end_time, freq='D')
    
    # Initialize a figure and axis
    fig, ax = plt.subplots()
    
    # Calculate the time difference between UTC and each time zone for each day
    for tz, color in zip(timezones, colors):
        # Get the time difference for the current time zone
        time_diff = [abs((dt - datetime(1970, 1, 1, tzinfo=pytz.timezone(tz)).astimezone(pytz.utc)).total_seconds() / 3600) for dt in date_range]
        # Plot the time difference
        ax.plot(date_range, time_diff, label=tz, color=color)
    
    # Set the plot title and labels
    ax.set_title('Hourly Time Difference Between UTC and Time Zones')
    ax.set_xlabel('Date')
    ax.set_ylabel('Time Difference (hours)')
    
    # Show the plot
    plt.show()
    
    # Return the axes object
    return ax