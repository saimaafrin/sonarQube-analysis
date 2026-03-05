import numpy as np
import itertools
def task_func(data_list, file_name):
    if not data_list:
        with open(file_name, 'w') as file:
            pass
        return []

    # Initialize a list to store the means
    means = []

    # Iterate over each position (excluding the first string element)
    for position in range(1, len(data_list[0])):
        # Extract the numeric values at the current position
        values = [item[position] for item in data_list if isinstance(item[position], (int, float))]

        # Calculate the mean, replacing missing values with np.nan
        if values:
            mean_value = np.mean(values)
        else:
            mean_value = np.nan

        # Append the mean to the list
        means.append(mean_value)

        # Write the result to the file
        with open(file_name, 'a') as file:
            file.write(f'Position {position}: {mean_value}\n')

    return means