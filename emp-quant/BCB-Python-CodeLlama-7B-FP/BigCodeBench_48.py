import time
from datetime import datetime
import random
import matplotlib.pyplot as plt
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
def task_func(n, output_path=None):
    # Generate n random Unix timestamps
    timestamps = [random.randint(0, 1000000000) for _ in range(n)]
    # Convert timestamps to strings formatted as UTC DATE_FORMAT
    formatted_timestamps = [datetime.utcfromtimestamp(timestamp).strftime(DATE_FORMAT) for timestamp in timestamps]
    # Plot a histogram of the distribution of the generated timestamps
    plt.hist(formatted_timestamps, bins=100)
    # Save the histogram to the specified path
    if output_path:
        plt.savefig(output_path)
    # Display the plot
    else:
        plt.show()
    return formatted_timestamps