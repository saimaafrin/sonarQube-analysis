import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
def task_func(length, range_limit=100, seed=0):
    """
    Create a list of random numbers, sort them, and record the distribution of the numbers in a histogram using default settings in a deterministic seaborn plot.
    Return the axes object and the list of random numbers.
    """
    if range_limit <= 1:
        raise ValueError("range_limit must be greater than 1")

    # Generate a list of random numbers
    numbers = [random.randint(1, range_limit) for _ in range(length)]

    # Sort the list
    numbers.sort()

    # Create a histogram of the numbers
    ax = sns.histplot(numbers, bins=range_limit)

    # Set the title and labels
    ax.set_title("Histogram of Random Numbers")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    return ax, numbers
length = 1000
range_limit = 100
seed = 0