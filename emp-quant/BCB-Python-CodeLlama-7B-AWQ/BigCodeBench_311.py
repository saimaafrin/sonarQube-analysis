import numpy as np
import random
from scipy import stats
def task_func(list_of_lists, size=5, seed=0):
    """
    Calculate the mean, median, and mode of values in a list of lists.
    If a list is empty, fill it with SIZE (default: 5) random integers between 0 and 100, and then calculate the statistics.
    """
    # Check if the input is a list of lists
    if not isinstance(list_of_lists, list):
        raise ValueError("Input must be a list of lists")

    # Check if the input is empty
    if not list_of_lists:
        # Fill the list with random integers between 0 and 100
        list_of_lists = [random.randint(0, 100) for _ in range(size)]

    # Calculate the mean, median, and mode of the values
    mean = np.mean(list_of_lists)
    median = np.median(list_of_lists)
    mode = stats.mode(list_of_lists)

    # Return a dictionary with the mean, median, and mode of the values
    return {"mean": mean, "median": median, "mode": mode}
list_of_lists = [[], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]