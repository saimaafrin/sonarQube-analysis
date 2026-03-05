import time
import matplotlib.pyplot as plt
def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    """
    Parses a list of time strings and plots a histogram of the seconds component.
    
    Parameters:
    - time_strings (list of str): A list of time strings to be parsed.
    - time_format (str): The format of the time strings.
    
    Returns:
    - ax (matplotlib.axes._axes.Axes or None): An Axes object with the histogram plotted if
      parsing is successful. Returns None if a parsing error occurs.
    """
    seconds = []
    for time_str in time_strings:
        try:
            parsed_time = time.strptime(time_str, time_format)
            seconds.append(parsed_time.tm_sec)
        except ValueError:
            raise ValueError(f"Failed to parse time string: {time_str}")
    
    if not seconds:
        return None
    
    fig, ax = plt.subplots()
    ax.hist(seconds, bins=20, edgecolor='black')
    ax.set_xlabel('Seconds')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Seconds')
    
    return ax
time_strings = [
    "01/01/2020 12:00:00.000000",
    "01/01/2020 12:00:10.000000",
    "01/01/2020 12:00:20.000000",
    "01/01/2020 12:00:30.000000",
    "01/01/2020 12:00:40.000000",
    "01/01/2020 12:00:50.000000"
]