
import numpy as np
import itertools

def task_func(data_list, file_name):
    # Check if the input list is empty
    if not data_list:
        with open(file_name, 'w') as f:
            pass
        return []

    # Initialize a list to store the means
    means = []

    # Get the number of positions in the tuples
    num_positions = len(data_list[0])

    # Iterate over each position (except the first)
    for i in range(1, num_positions):
        # Extract the numeric values at the current position
        values = [item[i] for item in data_list if isinstance(item[i], (int, float))]

        # Replace missing or non-numeric values with np.nan
        values = [np.nan if not isinstance(item[i], (int, float)) else item[i] for item in data_list]

        # Calculate the mean of the numeric values
        mean_value = np.mean(values)

        # Append the mean value to the list
        means.append(mean_value)

        # Write the result to the text file
        with open(file_name, 'a') as f:
            f.write(f'Position {i}: {mean_value}\n')

    return means