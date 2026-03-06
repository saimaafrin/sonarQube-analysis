
import numpy as np
import itertools

def task_func(data_list):
    if not data_list:
        return []
    
    # Initialize a list to store the sum of numeric values at each position
    sums = [0] * max(len(tup) for tup in data_list)
    # Initialize a list to store the count of numeric values at each position
    counts = [0] * max(len(tup) for tup in data_list)
    
    for tup in data_list:
        for i, value in enumerate(tup):
            try:
                # Convert value to float and add to the sum
                sums[i] += float(value)
                counts[i] += 1
            except ValueError:
                # Ignore non-numeric values
                continue
    
    # Calculate the mean for each position
    means = [sums[i] / counts[i] if counts[i] > 0 else np.nan for i in range(max(len(tup) for tup in data_list))]
    
    return means