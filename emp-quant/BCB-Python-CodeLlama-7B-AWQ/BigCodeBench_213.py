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
        # Generate a random number between 0 and 1
        number = random.uniform(0, 1)

        # Add the number to the list
        numbers.append(number)

        # Wait for 1 second before generating the next number
        time.sleep(1)

    # Plot the numbers as a function of elapsed time
    fig, ax = plt.subplots()
    ax.plot(numbers)

    # Calculate the kurtosis of the generated numbers
    kurtosis_value = kurtosis(numbers)

    # Return the Axes object and the kurtosis value
    return ax, kurtosis_value
intervals = 100
seed = 0