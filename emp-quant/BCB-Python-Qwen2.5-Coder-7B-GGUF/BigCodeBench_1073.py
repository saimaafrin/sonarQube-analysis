
import time
import matplotlib.pyplot as plt

def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    try:
        seconds = [int(time.strptime(ts, time_format).tm_sec) for ts in time_strings]
    except ValueError as e:
        raise ValueError("Error parsing time strings: " + str(e))
    
    fig, ax = plt.subplots()
    ax.hist(seconds, bins=60, range=(0, 60), edgecolor='black')
    ax.set_xlabel('Seconds')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Seconds Component')
    
    return ax