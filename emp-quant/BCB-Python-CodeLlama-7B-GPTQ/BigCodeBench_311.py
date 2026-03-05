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

    # Initialize the output dictionary
    output = {}

    # Iterate over the lists in the input
    for lst in list_of_lists:
        # Check if the list is empty
        if not lst:
            # Fill the list with random integers between 0 and 100
            lst = [random.randint(0, 100) for _ in range(size)]

        # Calculate the mean, median, and mode of the list
        output[lst] = {
            "mean": np.mean(lst),
            "median": np.median(lst),
            "mode": stats.mode(lst)
        }

    return output
list_of_lists = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [],
    [],
    [],
    [],
    []
]