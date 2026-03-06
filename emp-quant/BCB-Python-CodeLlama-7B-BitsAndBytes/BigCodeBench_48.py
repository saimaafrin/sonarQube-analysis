
import time
from datetime import datetime
import random
import matplotlib.pyplot as plt
# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
def task_func(n, output_path=None):
    # Generate n random timestamps
    timestamps = [datetime.fromtimestamp(random.randint(0, time.time())) for _ in range(n)]
    # Convert timestamps to strings in UTC format
    formatted_timestamps = [t.strftime(DATE_FORMAT) for t in timestamps]
    # Plot the histogram
    plt.hist(formatted_timestamps, bins=100)
    # Save the plot to a file if an output path is provided
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    return formatted_timestamps