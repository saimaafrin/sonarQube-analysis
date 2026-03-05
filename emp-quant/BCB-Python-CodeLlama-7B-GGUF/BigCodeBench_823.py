
import time
import numpy as np

def task_func(samples=10, delay=0.1):
    # Measure the actual delay
    start_time = time.time()
    for i in range(samples):
        # Do some work
        time.sleep(delay)
    end_time = time.time()
    actual_delay = end_time - start_time

    # Calculate the statistical properties of the delay times
    delay_times = np.array([actual_delay] * samples)
    mean = np.mean(delay_times)
    std = np.std(delay_times)

    return mean, std