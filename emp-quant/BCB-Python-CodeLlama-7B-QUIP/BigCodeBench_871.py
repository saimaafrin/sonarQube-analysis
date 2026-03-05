
import numpy as np
import itertools

def task_func(data_list, file_name):
    # Check if data_list is empty
    if not data_list:
        return []

    # Initialize the list of means
    means = []

    # Iterate over the data_list and calculate the mean for each tuple
    for i, tuple in enumerate(data_list):
        # Check if the first value is a string
        if not isinstance(tuple[0], str):
            # Calculate the mean for the numerical values in the tuple
            mean = np.nanmean(tuple[1:])
            # Add the mean to the list of means
            means.append(mean)

    # Write the means to a file
    with open(file_name, 'w') as f:
        for mean in means:
            f.write(f'Position {i}: {mean}\n')

    return means