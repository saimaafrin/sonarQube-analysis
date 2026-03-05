import time
import numpy as np
def task_func(samples=10, delay=0.1):
    """
    Make a delay for a given amount of time for a specified number of samples, measure the actual delay and calculate the statistical properties of the delay times.
    """
    # Initialize the list to store the delay times
    delay_times = []

    # Loop over the specified number of samples
    for i in range(samples):
        # Start the timer
        start_time = time.time()

        # Do some work
        time.sleep(delay)

        # End the timer
        end_time = time.time()

        # Calculate the delay time
        delay_time = end_time - start_time

        # Append the delay time to the list
        delay_times.append(delay_time)

    # Calculate the mean and standard deviation of the delay times
    mean = np.mean(delay_times)
    std = np.std(delay_times)

    # Return the mean and standard deviation of the delay times
    return (mean, std)