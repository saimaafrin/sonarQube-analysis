
import time
import matplotlib.pyplot as plt

def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    try:
        # Parse the time strings and extract the seconds component
        seconds = [time.strptime(ts, time_format)[4] for ts in time_strings]
    except ValueError as e:
        # Raise the exception if parsing fails
        raise ValueError(f"Error parsing time strings: {e}")
    
    # Create a histogram of the seconds component
    fig, ax = plt.subplots()
    ax.hist(seconds, bins=24*60, edgecolor='k')
    ax.set_xlabel('Seconds')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Seconds')
    
    return ax