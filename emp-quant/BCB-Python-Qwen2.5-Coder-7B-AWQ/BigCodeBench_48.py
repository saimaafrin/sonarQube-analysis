import time
from datetime import datetime
import random
import matplotlib.pyplot as plt
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
def task_func(n, output_path=None):
    # Generate n random Unix timestamps
    timestamps = [random.randint(0, int(time.time())) for _ in range(n)]
    
    # Convert timestamps to strings formatted as UTC DATE_FORMAT
    formatted_timestamps = [datetime.utcfromtimestamp(ts).strftime(DATE_FORMAT) for ts in timestamps]
    
    # Plot a histogram of the distribution of the generated timestamps
    plt.hist(timestamps, bins=10, edgecolor='black')
    plt.xlabel('Unix Timestamp')
    plt.ylabel('Frequency')
    plt.title('Distribution of Random Unix Timestamps')
    
    # If an output path is provided, save the histogram to the specified path
    if output_path:
        plt.savefig(output_path)
    else:
        # Otherwise, display the plot
        plt.show()
    
    # Return the list of n formatted timestamps
    return formatted_timestamps