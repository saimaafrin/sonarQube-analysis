
import numpy as np
import itertools
import json

def task_func(data_list, json_file_name="mean_values.json"):
    # Calculate the mean of the numeric values for each position in the provided data list
    means = {}
    for i, data in enumerate(data_list):
        means[f"Position {i}"] = np.mean(data)

    # Export the results to a JSON file
    if json_file_name:
        with open(json_file_name, "w") as f:
            json.dump(means, f)

    return means