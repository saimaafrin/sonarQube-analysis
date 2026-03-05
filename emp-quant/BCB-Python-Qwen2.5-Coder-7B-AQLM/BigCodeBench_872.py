
import numpy as np
import itertools

def task_func(data_list):
    if not data_list:
        return []
    
    # Initialize a list to store the means
    means = []
    
    # Determine the maximum length of tuples in the list
    max_length = max(len(tup) for tup in data_list)
    
    # Iterate over each position up to the maximum length
    for pos in range(max_length):
        # Extract values at the current position from all tuples
        values = [tup[pos] for tup in data_list if pos < len(tup)]
        
        # Filter out non-numeric values and convert the rest to floats
        numeric_values = [float(val) for val in values if val.replace('.', '', 1).isdigit()]
        
        # Calculate the mean of the numeric values, or np.nan if there are none
        if numeric_values:
            mean_value = np.mean(numeric_values)
        else:
            mean_value = np.nan
        
        # Append the mean value to the list
        means.append(mean_value)
    
    return means