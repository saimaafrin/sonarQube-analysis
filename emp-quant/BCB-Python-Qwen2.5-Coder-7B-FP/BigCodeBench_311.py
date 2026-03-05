import numpy as np
import random
from scipy import stats
def task_func(list_of_lists, size=5, seed=0):
    # Set the random seed for reproducibility
    random.seed(seed)
    
    # Initialize an empty list to store all values
    all_values = []
    
    # Iterate over each list in the list of lists
    for lst in list_of_lists:
        if not lst:  # If the list is empty
            # Fill it with 'size' random integers between 0 and 100
            lst = [random.randint(0, 100) for _ in range(size)]
        
        # Extend the all_values list with the current list
        all_values.extend(lst)
    
    # Calculate the mean, median, and mode of the all_values list
    mean_value = np.mean(all_values)
    median_value = np.median(all_values)
    mode_value = stats.mode(all_values)[0][0]  # Get the mode value
    
    # Return the results in a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }