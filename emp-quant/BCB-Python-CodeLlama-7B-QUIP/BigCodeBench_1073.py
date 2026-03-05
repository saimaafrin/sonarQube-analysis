
import time
import matplotlib.pyplot as plt

def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    ax = None
    try:
        time_objects = [time.strptime(time_string, time_format) for time_string in time_strings]
        seconds = [time_object.tm_sec for time_object in time_objects]
        ax = plt.hist(seconds, bins=50)
    except ValueError:
        raise ValueError("Invalid time format")
    return ax