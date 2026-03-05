
import numpy as np
import itertools

def task_func(data_list, file_name):
    if not data_list:
        with open(file_name, 'w') as file:
            pass
        return []
    
    # Extract numerical data from each tuple, replacing non-numeric values with np.nan
    numerical_data = []
    for item in data_list:
        numeric_values = [np.nan if not isinstance(val, (int, float)) else val for val in item[1:]]
        numerical_data.append(numeric_values)
    
    # Calculate the mean for each position
    means = []
    for position in range(len(numerical_data[0])):
        column_data = [row[position] for row in numerical_data]
        mean_value = np.nanmean(column_data)
        means.append(mean_value)
    
    # Write the results to the specified text file
    with open(file_name, 'w') as file:
        for i, mean in enumerate(means, start=1):
            file.write(f'Position {i}: {mean}\n')
    
    return means