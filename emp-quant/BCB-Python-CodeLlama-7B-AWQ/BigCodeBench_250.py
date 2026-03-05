import numpy as np
import itertools
import json
def task_func(data_list, json_file_name="mean_values.json"):
    """
    Calculate the mean of the numeric values for each position in the provided data list and return the results.
    Optionally, the results can be exported to a specified JSON file.

    Args:
        data_list (list): A list of lists, where each sublist contains numeric values.
        json_file_name (str, optional): The name of the JSON file to export the results to. Defaults to "mean_values.json".

    Returns:
        dict: A dictionary with keys in the format 'Position {i}' and values being the mean of the numeric values
        at position i in the provided data list.
    """
    # Calculate the mean of the numeric values for each position in the data list
    means = {}
    for i, sublist in enumerate(data_list):
        means[f"Position {i}"] = np.mean(sublist)

    # Export the results to a JSON file if specified
    if json_file_name:
        with open(json_file_name, "w") as f:
            json.dump(means, f)

    return means
data_list = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8, 10],
    [3, 6, 9, 12, 15],
]