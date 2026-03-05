import time
import matplotlib.pyplot as plt
def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    """
    Parses a list of time strings and plots a histogram of the seconds component.
    Raises ValueError if any time string in 'time_strings' cannot be parsed according to 'time_format'.
    Returns an Axes object with the histogram plotted if parsing is successful. Returns None if a parsing error occurs.
    """
    # Parse the time strings using the specified format
    times = [time.strptime(time_string, time_format) for time_string in time_strings]

    # Extract the seconds component from the parsed times
    seconds = [time.tm_sec for time in times]

    # Create a histogram of the seconds
    ax = plt.hist(seconds, bins=100)

    # Return the Axes object with the histogram plotted
    return ax
time_strings = ["12/12/2022 12:12:12.123", "13/12/2022 13:13:13.123", "14/12/2022 14:14:14.123"]