import numpy as np
import itertools
import json
def task_func(data_list, json_file_name="mean_values.json"):
    # Convert the list of strings to a list of lists of integers
    data = [list(map(int, item.split(','))) for item in data_list]
    
    # Calculate the mean of each position
    mean_values = {f'Position {i}': np.mean([row[i] for row in data]) for i in range(len(data[0]))}
    
    # Optionally, export the results to a specified JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(mean_values, json_file, indent=4)
    
    return mean_values