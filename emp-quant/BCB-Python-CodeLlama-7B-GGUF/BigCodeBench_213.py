
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def task_func(intervals=100, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Generate a series of random numbers over the specified intervals
    x = [random.uniform(0, 1) for _ in range(intervals)]

    # Plot the numbers as a function of elapsed time
    fig, ax = plt.subplots()
    ax.plot(x)
    ax.set_xlabel('Elapsed Time')
    ax.set_ylabel('Random Number')

    # Calculate the kurtosis of the generated numbers
    kurtosis_value = kurtosis(x)

    # Return the Axes object and the kurtosis value
    return ax, kurtosis_value