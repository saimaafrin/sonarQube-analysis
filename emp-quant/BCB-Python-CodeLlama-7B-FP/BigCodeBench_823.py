import time
import numpy as np
def task_func(samples=10, delay=0.1):
    """
    Make a delay for a given amount of time for a specified number of samples, measure the actual delay, and calculate the statistical properties of the delay times.
    """
    # Generate a list of random delay times
    delay_times = np.random.normal(loc=delay, scale=0.1, size=samples)

    # Measure the actual delay
    start_time = time.time()
    time.sleep(delay)
    end_time = time.time()
    actual_delay = end_time - start_time

    # Calculate the mean and standard deviation of the delay times
    mean_delay = np.mean(delay_times)
    std_delay = np.std(delay_times)

    # Return the mean and standard deviation of the delay times
    return (mean_delay, std_delay)