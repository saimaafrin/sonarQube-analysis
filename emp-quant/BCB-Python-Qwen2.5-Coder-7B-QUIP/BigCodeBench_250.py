
import numpy as np
import itertools
import json

def task_func(data_list, json_file_name="mean_values.json"):
    # Initialize a dictionary to store the mean values
    mean_values = {}

    # Iterate over each position in the data list
    for i, position in enumerate(itertools.count()):
        # Filter the data list to include only numeric values at the current position
        numeric_values = [item[position] for item in data_list if isinstance(item[position], (int, float))]

        # Calculate the mean of the numeric values
        mean_value = np.mean(numeric_values)

        # Store the mean value in the dictionary
        mean_values[f'Position {i}'] = mean_value

    # Optionally, export the results to a JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(mean_values, json_file, indent=4)

    # Return the dictionary with the mean values
    return mean_values