import numpy as np
import itertools
import json
def task_func(data_list, json_file_name="mean_values.json"):
    # Initialize a list to store the mean values
    mean_values = []
    
    # Iterate over each position in the data list
    for i in range(len(data_list[0])):
        # Extract the numeric values at the current position
        values = [item[i] for item in data_list if isinstance(item[i], (int, float))]
        
        # Calculate the mean of the numeric values
        if values:
            mean_value = np.mean(values)
        else:
            mean_value = None
        
        # Append the mean value to the list
        mean_values.append(mean_value)
    
    # Create a dictionary with keys in the format 'Position {i}' and values being the mean of the numeric values
    result_dict = {f'Position {i}': mean_value for i, mean_value in enumerate(mean_values)}
    
    # Export the results to a specified JSON file
    with open(json_file_name, 'w') as json_file:
        json.dump(result_dict, json_file, indent=4)
    
    # Return the result dictionary
    return result_dict