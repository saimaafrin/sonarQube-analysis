import time
import matplotlib.pyplot as plt
def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    """
    Parses a list of time strings and plots a histogram of the seconds component.
    Raises ValueError if any time string in 'time_strings' cannot be parsed according to 'time_format'.
    Returns an Axes object with the histogram plotted if parsing is successful. Returns None if a parsing error occurs.
    """
    # Parse the time strings using the specified format
    try:
        time_objects = [time.strptime(time_string, time_format) for time_string in time_strings]
    except ValueError:
        raise ValueError("Invalid time format")

    # Extract the seconds component from the time objects
    seconds = [time_object.tm_sec for time_object in time_objects]

    # Plot the histogram of the seconds
    fig, ax = plt.subplots()
    ax.hist(seconds, bins=100)
    return ax
time_strings = ["12/12/2022 12:12:12.123", "13/12/2022 13:13:13.123", "14/12/2022 14:14:14.123"]