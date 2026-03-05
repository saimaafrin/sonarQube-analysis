import time
from datetime import datetime
import random
import matplotlib.pyplot as plt
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
def task_func(n, output_path=None):
    # Generate n random Unix timestamps
    timestamps = [random.randint(1, int(time.time())) for _ in range(n)]
    
    # Convert timestamps to strings formatted as UTC DATE_FORMAT
    formatted_timestamps = [datetime.utcfromtimestamp(ts).strftime(DATE_FORMAT) for ts in timestamps]
    
    # Plot a histogram of the distribution of the generated timestamps
    plt.hist(timestamps, bins='auto', color='blue', alpha=0.7)
    plt.title('Distribution of Random Unix Timestamps')
    plt.xlabel('Unix Timestamp')
    plt.ylabel('Frequency')
    
    # Save the histogram to the specified path if output_path is provided
    if output_path:
        plt.savefig(output_path)
    else:
        # Display the plot
        plt.show()
    
    # Return the list of formatted timestamps
    return formatted_timestamps