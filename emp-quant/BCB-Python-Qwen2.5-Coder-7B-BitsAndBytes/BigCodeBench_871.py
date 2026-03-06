
import numpy as np
import itertools

def task_func(data_list, file_name):
    if not data_list:
        with open(file_name, 'w') as f:
            pass
        return []

    # Initialize a list to store means
    means = []
    
    # Extract the number of elements in each tuple (excluding the first element)
    num_elements = len(data_list[0]) - 1
    
    # Create a list to hold the sum and count for each position
    sums = [0] * num_elements
    counts = [0] * num_elements
    
    # Iterate over each tuple in the list
    for item in data_list:
        for i in range(1, len(item)):
            try:
                value = float(item[i])
                sums[i-1] += value
                counts[i-1] += 1
            except ValueError:
                sums[i-1] += np.nan
                counts[i-1] += 1
    
    # Calculate the mean for each position
    for i in range(num_elements):
        if counts[i] == 0:
            means.append(np.nan)
        else:
            means.append(sums[i] / counts[i])
    
    # Write the results to the specified text file
    with open(file_name, 'w') as f:
        for i, mean in enumerate(means):
            f.write(f'Position {i+1}: {mean}\n')
    
    return means