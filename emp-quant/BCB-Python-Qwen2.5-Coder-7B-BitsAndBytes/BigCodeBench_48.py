
import time
from datetime import datetime
import random
import matplotlib.pyplot as plt

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def task_func(n, output_path=None):
    # Generate n random Unix timestamps
    timestamps = [random.randint(1609459200, 1672531200) for _ in range(n)]  # Example range: January 1, 2021 - December 31, 2022
    
    # Convert timestamps to strings formatted as UTC DATE_FORMAT
    formatted_timestamps = [datetime.utcfromtimestamp(ts).strftime(DATE_FORMAT) for ts in timestamps]
    
    # Plot a histogram of the distribution of the generated timestamps
    plt.hist(timestamps, bins=365)
    plt.xlabel('Unix Timestamp')
    plt.ylabel('Frequency')
    plt.title('Distribution of Random Unix Timestamps')
    
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    
    return formatted_timestamps