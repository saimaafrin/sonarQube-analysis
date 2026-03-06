
import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

def task_func(length, range_limit=100, seed=0):
    if range_limit <= 1:
        raise ValueError("Range limit must be greater than 1")

    # Generate a list of random numbers
    random_numbers = [random.randint(1, range_limit) for _ in range(length)]

    # Sort the list of random numbers
    sorted_numbers = sorted(random_numbers)

    # Create a histogram of the distribution of the numbers
    ax = sns.histplot(sorted_numbers, bins=range_limit)

    return ax, random_numbers

# Display the plot
plt.show()