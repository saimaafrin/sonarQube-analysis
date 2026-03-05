import numpy as np
import random
from scipy import stats
def task_func(list_of_lists, size=5, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Flatten the list of lists and handle empty lists
    all_values = []
    for sublist in list_of_lists:
        if not sublist:
            # Fill empty list with random integers
            sublist = [random.randint(0, 100) for _ in range(size)]
        all_values.extend(sublist)
    
    # Calculate mean, median, and mode
    mean_value = np.mean(all_values)
    median_value = np.median(all_values)
    mode_value = stats.mode(all_values)[0][0]  # Get the mode value
    
    # Return the results in a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }