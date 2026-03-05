import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
def task_func(intervals=100, seed=0):
    """
    Generates a series of random numbers over a specified number of intervals with a delay of 1 second between each interval. It then plots these numbers as a function of elapsed time and returns the Axes object along with the kurtosis value of the generated numbers.
    """
    # Set the random seed for reproducibility
    random.seed(seed)

    # Initialize the list to store the generated numbers
    numbers = []

    # Generate the random numbers
    for i in range(intervals):
        numbers.append(random.random())
        time.sleep(1)

    # Plot the numbers as a function of elapsed time
    fig, ax = plt.subplots()
    ax.plot(numbers)
    ax.set_xlabel('Elapsed Time')
    ax.set_ylabel('Random Number')
    ax.set_title('Random Number Generation and Kurtosis')

    # Calculate the kurtosis of the generated numbers
    kurtosis_value = kurtosis(numbers)

    # Return the Axes object and the kurtosis value
    return ax, kurtosis_value