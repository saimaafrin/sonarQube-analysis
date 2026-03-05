
import time
import matplotlib.pyplot as plt

def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    # Parse the time strings using the specified format
    times = [time.strptime(t, time_format) for t in time_strings]

    # Extract the seconds component from the parsed times
    seconds = [t.tm_sec for t in times]

    # Create a histogram of the seconds
    ax = plt.hist(seconds, bins=100)

    # Return the Axes object with the histogram plotted
    return ax

# Parse the time strings and plot the histogram
ax = task_func(time_strings)

# Show the plot
plt.show()