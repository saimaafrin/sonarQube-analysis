
import numpy as np
import itertools
import json

def task_func(data_list, json_file_name="mean_values.json"):
    # Convert the list of strings to a list of lists of integers
    data_matrix = np.array([[int(value) for value in sublist.split()] for sublist in data_list])
    
    # Calculate the mean for each position
    mean_values = np.mean(data_matrix, axis=0)
    
    # Create a dictionary with the results
    result_dict = {f'Position {i+1}': mean_value for i, mean_value in enumerate(mean_values)}
    
    # Export the results to a JSON file if specified
    if json_file_name:
        with open(json_file_name, 'w') as json_file:
            json.dump(result_dict, json_file, indent=4)
    
    return result_dict