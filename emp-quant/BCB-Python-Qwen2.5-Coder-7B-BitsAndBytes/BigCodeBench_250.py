
import numpy as np
import itertools
import json

def task_func(data_list, json_file_name="mean_values.json"):
    # Convert the list of strings to a list of lists of floats
    data_matrix = [list(map(float, item.split(','))) for item in data_list]
    
    # Calculate the mean of each position
    means = [np.mean(column) for column in zip(*data_matrix)]
    
    # Create a dictionary with the results
    result_dict = {'Position {}'.format(i+1): mean for i, mean in enumerate(means)}
    
    # Export the results to a JSON file if specified
    if json_file_name:
        with open(json_file_name, 'w') as json_file:
            json.dump(result_dict, json_file)
    
    return result_dict