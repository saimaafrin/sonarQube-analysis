
import numpy as np
import itertools

def task_func(data_list):
    # Initialize a list to hold the means
    means = []
    
    # Determine the maximum length of tuples in the list
    max_len = max(len(t) for t in data_list) if data_list else 0
    
    # Iterate over each position up to the maximum length
    for i in range(max_len):
        # Extract the i-th element from each tuple, ignoring non-numeric values
        values = [item[i] if i < len(item) else 0 for item in data_list if i < len(item)]
        numeric_values = [val for val in values if isinstance(val, (int, float))]
        
        # Calculate the mean of the numeric values, or set to np.nan if none are present
        mean_value = np.mean(numeric_values) if numeric_values else np.nan
        
        # Append the mean value to the list
        means.append(mean_value)
    
    return means