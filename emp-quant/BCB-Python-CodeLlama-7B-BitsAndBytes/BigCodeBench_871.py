
import numpy as np
import itertools

def task_func(data_list, file_name):
    # Check if the input list is empty
    if not data_list:
        return []

    # Create a list to store the mean values
    mean_values = []

    # Iterate through the data list and calculate the mean for each tuple position
    for i, tuple_data in enumerate(data_list):
        # Extract the numerical values from the tuple
        numerical_data = tuple_data[1:]

        # Replace missing or non-numeric values with np.nan
        numerical_data = [np.nan if not isinstance(x, (int, float)) else x for x in numerical_data]

        # Calculate the mean of the numerical data
        mean = np.nanmean(numerical_data)

        # Add the mean to the list of mean values
        mean_values.append(mean)

    # Write the mean values to a file
    with open(file_name, 'w') as f:
        for i, mean in enumerate(mean_values):
            f.write(f'Position {i}: {mean}\n')

    return mean_values