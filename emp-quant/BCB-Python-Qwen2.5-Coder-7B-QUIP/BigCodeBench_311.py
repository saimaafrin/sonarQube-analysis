
import numpy as np
import random
from scipy import stats

def task_func(list_of_lists, size=5, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Initialize an empty list to store all values
    all_values = []

    # Process each list in the list_of_lists
    for sublist in list_of_lists:
        if not sublist:  # If the sublist is empty
            # Fill it with 'size' random integers between 0 and 100
            sublist = [random.randint(0, 100) for _ in range(size)]
        all_values.extend(sublist)

    # Calculate the mean, median, and mode
    mean_value = np.mean(all_values)
    median_value = np.median(all_values)
    mode_value = stats.mode(all_values)[0]

    # Return the results as a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }