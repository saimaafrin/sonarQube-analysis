from datetime import datetime, timedelta
import pytz
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_time, end_time):
    """
    Plots the hourly difference between UTC and specified global time zones across a date range.
    
    Parameters:
    start_time (str): The start date and time in 'YYYY-MM-DD HH:MM:SS' format.
    end_time (str): The end date and time in 'YYYY-MM-DD HH:MM:SS' format.
    
    Returns:
    matplotlib.axes.Axes: The Axes object with the plotted time differences in hours between UTC and other time zones.
    """
    # Define the time zones
    time_zones = ['UTC', 'America/Los_Angeles', 'Europe/Paris', 'Asia/Kolkata', 'Australia/Sydney']
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    
    # Convert start and end times to datetime objects
    start_dt = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_dt = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Loop through each time zone and plot the difference
    for tz, color in zip(time_zones, colors):
        if tz == 'UTC':
            continue  # Skip UTC as it is the reference
        tz_info = pytz.timezone(tz)
        utc_dt = start_dt
        while utc_dt <= end_dt:
            local_dt = utc_dt.astimezone(tz_info)
            diff = (local_dt - utc_dt).total_seconds() / 3600
            ax.plot(utc_dt, diff, color=color, marker='o')
            utc_dt += timedelta(hours=1)
    
    # Set labels and title
    ax.set_xlabel('UTC Time')
    ax.set_ylabel('Time Difference (hours)')
    ax.set_title('Hourly Time Difference Between UTC and Specified Time Zones')
    
    # Format the x-axis to show dates and times
    ax.xaxis_date()
    fig.autofmt_xdate()
    
    return ax