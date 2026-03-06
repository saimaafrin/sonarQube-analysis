
import numpy as np
import itertools
import json

def task_func(data_list, json_file_name="mean_values.json"):
    # Calculate the mean of the numeric values for each position in the provided data list
    mean_values = {f"Position {i}": np.mean(data_list[i]) for i in range(len(data_list))}

    # Optionally, export the results to a specified JSON file
    if json_file_name:
        with open(json_file_name, "w") as f:
            json.dump(mean_values, f)

    return mean_values

mean_values = task_func(data_list)
print(mean_values)