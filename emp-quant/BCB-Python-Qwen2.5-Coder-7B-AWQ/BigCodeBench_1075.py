import datetime
import numpy as np
import matplotlib.pyplot as plt
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_strings):
    """
    Compute the differences in seconds with integer values between consecutive datetime strings and plot these differences as a bar chart.
    
    Parameters:
    time_strings (list): A list of datetime strings in the format specified in TIME_FORMAT.
    
    Returns:
    matplotlib.axes.Axes: The axes object of the plotted bar chart.
    """
    # Convert the list of datetime strings to a list of datetime objects
    datetime_objects = [datetime.datetime.strptime(ts, TIME_FORMAT) for ts in time_strings]
    
    # Calculate the differences in seconds between consecutive datetime objects
    time_differences = [(datetime_objects[i] - datetime_objects[i-1]).total_seconds() for i in range(1, len(datetime_objects))]
    
    # Convert the differences to integers
    time_differences_int = [int(td) for td in time_differences]
    
    # Create a bar chart of the time differences
    fig, ax = plt.subplots()
    ax.bar(range(len(time_differences_int)), time_differences_int)
    
    # Set the x-axis labels to the original datetime strings
    ax.set_xticks(range(len(time_strings)-1))
    ax.set_xticklabels(time_strings[1:])
    
    # Set the title and labels
    ax.set_title('Time Differences Between Consecutive Datetime Strings')
    ax.set_xlabel('Datetime String Index')
    ax.set_ylabel('Time Difference (seconds)')
    
    return ax