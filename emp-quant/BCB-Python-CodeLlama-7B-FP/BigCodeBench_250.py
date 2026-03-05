import numpy as np
import itertools
import json
def task_func(data_list, json_file_name="mean_values.json"):
    """
    Calculate the mean of the numeric values for each position in the provided data list and return the results.
    Optionally, the results can be exported to a specified JSON file.
    """
    # Create a dictionary to store the mean values
    mean_values = {}

    # Iterate over the data list and calculate the mean for each position
    for i, position in enumerate(data_list):
        # Extract the numeric values from the current position
        numeric_values = [value for value in position if isinstance(value, (int, float))]

        # Calculate the mean of the numeric values
        mean_value = np.mean(numeric_values) if numeric_values else None

        # Add the mean value to the dictionary
        mean_values[f"Position {i}"] = mean_value

    # Export the mean values to a JSON file if specified
    if json_file_name:
        with open(json_file_name, "w") as f:
            json.dump(mean_values, f)

    return mean_values
data_list = [
    ["Apple", "Banana", "Cherry"],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]