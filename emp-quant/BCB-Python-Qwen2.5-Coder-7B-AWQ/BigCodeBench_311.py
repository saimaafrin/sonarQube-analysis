import numpy as np
import random
from scipy import stats
def task_func(list_of_lists, size=5, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Flatten the list of lists and filter out empty lists
    flattened_list = [item for sublist in list_of_lists if sublist]
    
    # If there are no non-empty lists, fill with random integers
    if not flattened_list:
        flattened_list = [random.randint(0, 100) for _ in range(size)]
    
    # Calculate mean, median, and mode
    mean_value = np.mean(flattened_list)
    median_value = np.median(flattened_list)
    mode_value = stats.mode(flattened_list)[0][0]
    
    # Return the results in a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }