
import time
from datetime import datetime
import random
import matplotlib.pyplot as plt
# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
def task_func(n, output_path=None):
    # Generate n random timestamps
    timestamps = [random.randint(0, 1000000000) for _ in range(n)]
    # Convert timestamps to strings
    timestamp_strings = [datetime.utcfromtimestamp(ts).strftime(DATE_FORMAT) for ts in timestamps]
    # Plot histogram
    plt.hist(timestamp_strings, bins=100)
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    return timestamp_strings