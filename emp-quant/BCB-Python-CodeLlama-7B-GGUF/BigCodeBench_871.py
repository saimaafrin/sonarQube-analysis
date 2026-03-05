
import numpy as np
import itertools

def task_func(data_list, file_name):
    # Check if the input list is empty
    if not data_list:
        return []

    # Create a list to store the mean values
    mean_values = []

    # Iterate through the data list
    for tuple_data in data_list:
        # Extract the numerical values from the tuple
        numerical_values = tuple_data[1:]

        # Replace missing or non-numeric values with np.nan
        numerical_values = [np.nan if np.isnan(x) or not isinstance(x, (int, float)) else x for x in numerical_values]

        # Calculate the mean of the numerical values
        mean_value = np.nanmean(numerical_values)

        # Append the mean value to the list
        mean_values.append(mean_value)

    # Write the mean values to a file
    with open(file_name, 'w') as f:
        for mean_value in mean_values:
            f.write(f'Position {mean_value}: {mean_value}\n')

    return mean_values