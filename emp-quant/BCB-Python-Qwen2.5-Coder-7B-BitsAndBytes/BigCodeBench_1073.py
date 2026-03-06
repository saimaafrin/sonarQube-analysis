
import time
import matplotlib.pyplot as plt

def task_func(time_strings, time_format="%d/%m/%Y %H:%M:%S.%f"):
    try:
        # Extract seconds from each time string
        seconds = [int(time.strptime(ts, time_format).tm_sec) for ts in time_strings]
        
        # Create a figure and an axes object
        fig, ax = plt.subplots()
        
        # Plot a histogram of the seconds
        ax.hist(seconds, bins=60)
        
        # Set labels and title
        ax.set_xlabel('Seconds')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of Seconds Component')
        
        return ax
    
    except ValueError as e:
        print(f"Error parsing time strings: {e}")
        return None