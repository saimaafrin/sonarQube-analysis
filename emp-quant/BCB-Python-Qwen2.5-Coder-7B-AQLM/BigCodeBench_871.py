
import numpy as np
import itertools

def task_func(data_list, file_name):
    if not data_list:
        with open(file_name, 'w') as file:
            pass
        return []
    
    # Initialize a list to store the means
    means = []
    
    # Iterate over the data using itertools.zip_longest to handle missing values
    for position, values in enumerate(itertools.zip_longest(*data_list, fillvalue=np.nan)):
        # Filter out the first value of each tuple (string) and convert the rest to float
        numeric_values = [float(value) for value in values[1:] if isinstance(value, (int, float))]
        
        # Calculate the mean of the numeric values, ignoring NaNs
        mean_value = np.nanmean(numeric_values)
        
        # Append the mean value to the list
        means.append(mean_value)
        
        # Write the result to the file
        with open(file_name, 'a') as file:
            file.write(f'Position {position + 1}: {mean_value}\n')
    
    return means