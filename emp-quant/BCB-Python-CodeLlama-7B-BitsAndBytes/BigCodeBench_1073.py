
import time
import matplotlib.pyplot as plt

def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    # Parse the time strings using the specified format
    times = [time.strptime(time_string, time_format) for time_string in time_strings]

    # Extract the seconds component from the parsed times
    seconds = [time.mktime(time_struct) % 60 for time_struct in times]

    # Create a histogram of the seconds
    ax = plt.hist(seconds, bins=60)

    # Return the Axes object with the histogram plotted
    return ax

# Plot the histogram
plt.show()