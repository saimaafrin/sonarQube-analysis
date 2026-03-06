
import numpy as np
import random
from scipy import stats

def task_func(list_of_lists, size=5, seed=0):
    # Check if the input is a list of lists
    if not isinstance(list_of_lists, list):
        raise ValueError("Input must be a list of lists")

    # Initialize the dictionary to store the statistics
    statistics = {}

    # Loop through each inner list and calculate the statistics
    for inner_list in list_of_lists:
        # Check if the inner list is empty
        if not inner_list:
            # If the inner list is empty, fill it with random integers
            inner_list = random.sample(range(100), size)

        # Calculate the mean, median, and mode of the inner list
        mean = np.mean(inner_list)
        median = np.median(inner_list)
        mode = stats.mode(inner_list)

        # Add the statistics to the dictionary
        statistics[inner_list] = {"mean": mean, "median": median, "mode": mode}

    return statistics