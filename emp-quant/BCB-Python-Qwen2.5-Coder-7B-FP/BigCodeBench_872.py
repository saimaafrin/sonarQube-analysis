import numpy as np
import itertools
def task_func(data_list):
    if not data_list:
        return []
    
    # Initialize a list to store the sum of numeric values at each position
    sum_values = [0] * max(len(tup) for tup in data_list)
    # Initialize a list to store the count of numeric values at each position
    count_values = [0] * max(len(tup) for tup in data_list)
    
    for tup in data_list:
        for i, value in enumerate(tup):
            try:
                # Convert value to float and add to sum
                sum_values[i] += float(value)
                count_values[i] += 1
            except ValueError:
                # Ignore non-numeric values
                continue
    
    # Calculate the mean for each position, treating missing values as zeros
    mean_values = [sum_values[i] / count_values[i] if count_values[i] > 0 else np.nan for i in range(len(sum_values))]
    
    return mean_values