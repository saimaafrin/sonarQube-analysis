
import time
from datetime import datetime
import random
import matplotlib.pyplot as plt
# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
def task_func(n, output_path=None):
    timestamps = []
    for i in range(n):
        timestamp = datetime.fromtimestamp(random.randint(0, time.time()))
        timestamps.append(timestamp.strftime(DATE_FORMAT))
    if output_path:
        with open(output_path, "w") as f:
            for timestamp in timestamps:
                f.write(timestamp + "\n")
    else:
        plt.hist(timestamps, bins=100)
        plt.show()
    return timestamps