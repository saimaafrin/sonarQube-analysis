import numpy as np
import itertools
import json
def task_func(data_list, json_file_name="mean_values.json"):
    # Convert the list of strings to a list of lists of integers
    data_matrix = [list(map(int, item.split(','))) for item in data_list]
    
    # Calculate the mean of each position
    mean_values = {f'Position {i+1}': np.mean(column) for i, column in enumerate(zip(*data_matrix))}
    
    # Optionally, export the results to a JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(mean_values, json_file, indent=4)
    
    return mean_values
data_list = [
    "1,2,3",
    "4,5,6",
    "7,8,9"
]