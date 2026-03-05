import datetime
import numpy as np
import matplotlib.pyplot as plt
TIME_FORMAT = "%d/%m/%y %H:%M:%S.%f"
def task_func(time_strings):
    # Convert the datetime strings to datetime objects
    time_objects = [datetime.datetime.strptime(time_string, TIME_FORMAT) for time_string in time_strings]
    # Calculate the time differences between consecutive datetime objects
    time_differences = [time_objects[i+1] - time_objects[i] for i in range(len(time_objects)-1)]
    # Convert the time differences to seconds with integer values
    time_differences_seconds = [int(time_difference.total_seconds()) for time_difference in time_differences]
    # Plot the time differences as a bar chart
    ax = plt.bar(time_differences_seconds)
    return ax
time_strings = ["01/01/2020 00:00:00.000", "01/01/2020 00:00:01.000", "01/01/2020 00:00:02.000", "01/01/2020 00:00:03.000", "01/01/2020 00:00:04.000"]