
import numpy as np
import random
from scipy import stats

def task_func(list_of_lists, size=5, seed=0):
    # Check if list_of_lists is empty
    if not list_of_lists:
        # If empty, fill with size random integers between 0 and 100
        list_of_lists = [random.randint(0, 100) for _ in range(size)]

    # Calculate mean, median, and mode of list_of_lists
    mean = np.mean(list_of_lists)
    median = np.median(list_of_lists)
    mode = stats.mode(list_of_lists)

    # Return dictionary with mean, median, and mode
    return {"mean": mean, "median": median, "mode": mode}