import time
import numpy as np
def task_func(samples=10, delay=0.1):
    """
    Make a delay for a given amount of time for a specified number of samples, measure the actual delay and calculate the statistical properties of the delay times.
    The function should output with:
        tuple: The mean and standard deviation of the delay times.
    """
    # Initialize the list to store the delay times
    delay_times = []

    # Perform the task for the specified number of samples
    for _ in range(samples):
        # Start the timer
        start_time = time.time()

        # Perform the task
        time.sleep(delay)

        # Calculate the actual delay time
        actual_delay = time.time() - start_time

        # Append the actual delay time to the list
        delay_times.append(actual_delay)

    # Calculate the mean and standard deviation of the delay times
    mean = np.mean(delay_times)
    std = np.std(delay_times)

    # Return the mean and standard deviation of the delay times
    return (mean, std)