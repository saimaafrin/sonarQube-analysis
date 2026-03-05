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
    seconds_list = []
    for time_str in time_strings:
        try:
            parsed_time = time.strptime(time_str, time_format)
            seconds_list.append(parsed_time.tm_sec)
        except ValueError:
            raise ValueError(f"Failed to parse time string: {time_str}")
    
    if not seconds_list:
        return None
    
    fig, ax = plt.subplots()
    ax.hist(seconds_list, bins=60, range=(0, 60), edgecolor='black')
    ax.set_xlabel('Seconds')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Seconds Component')
    
    return ax
time_strings = [
    "01/01/2023 12:00:00.000000",
    "01/01/2023 12:00:01.000000",
    "01/01/2023 12:00:02.000000",
    # Add more time strings as needed
]