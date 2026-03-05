from datetime import datetime, timedelta
import pytz
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_time, end_time):
    """
    Plots the hourly difference between UTC and specified global time zones across a date range.
    
    Parameters:
    start_time (datetime): The start of the date range.
    end_time (datetime): The end of the date range.
    
    Returns:
    matplotlib.axes.Axes: The Axes object with the plotted time differences in hours between UTC and other time zones.
    """
    # Define the time zones
    time_zones = {
        "UTC": pytz.utc,
        "America/Los_Angeles": pytz.timezone("America/Los_Angeles"),
        "Europe/Paris": pytz.timezone("Europe/Paris"),
        "Asia/Kolkata": pytz.timezone("Asia/Kolkata"),
        "Australia/Sydney": pytz.timezone("Australia/Sydney")
    }
    
    # Define the colors for each time zone
    colors = ["b", "g", "r", "c", "m", "y", "k"]
    
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Loop through each time zone and plot the difference
    for i, (tz_name, tz) in enumerate(time_zones.items()):
        # Initialize an empty list to store the time differences
        time_diffs = []
        
        # Loop through each hour in the date range
        current_time = start_time
        while current_time <= end_time:
            # Get the current time in the specified time zone
            current_tz_time = current_time.astimezone(tz)
            
            # Calculate the time difference in hours
            diff = current_tz_time.hour - current_time.hour
            
            # Append the time difference to the list
            time_diffs.append(diff)
            
            # Move to the next hour
            current_time += timedelta(hours=1)
        
        # Plot the time differences
        ax.plot(time_diffs, label=tz_name, color=colors[i % len(colors)])
    
    # Set the title and labels
    ax.set_title("Hourly Time Difference Between UTC and Specified Time Zones")
    ax.set_xlabel("Hour")
    ax.set_ylabel("Time Difference (hours)")
    
    # Add a legend
    ax.legend()
    
    # Show the plot
    plt.show()
    
    # Return the axis object
    return ax