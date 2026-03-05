import numpy as np
import itertools
def task_func(data_list):
    if not data_list:
        return []
    
    # Initialize a list to store the sum and count of numeric values at each position
    sums = [0] * max(len(tup) for tup in data_list)
    counts = [0] * max(len(tup) for tup in data_list)
    
    # Iterate over each tuple in the list
    for tup in data_list:
        # Iterate over each element in the tuple
        for i, value in enumerate(tup):
            # Check if the value is numeric
            if isinstance(value, (int, float)):
                # Add the value to the sum and increment the count for this position
                sums[i] += value
                counts[i] += 1
    
    # Calculate the mean for each position, treating non-numeric positions as np.nan
    means = [sums[i] / counts[i] if counts[i] > 0 else np.nan for i in range(len(sums))]
    
    return means