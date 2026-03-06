
import datetime
import numpy as np
import matplotlib.pyplot as plt

# Constants
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"

def task_func(time_strings):
    # Convert time strings to datetime objects
    datetime_objects = [datetime.datetime.strptime(ts, TIME_FORMAT) for ts in time_strings]
    
    # Calculate time differences in seconds
    time_differences = [(datetime_objects[i] - datetime_objects[i-1]).total_seconds() for i in range(1, len(datetime_objects))]
    
    # Create a bar chart of the time differences
    fig, ax = plt.subplots()
    ax.bar(range(len(time_differences)), time_differences)
    
    return ax