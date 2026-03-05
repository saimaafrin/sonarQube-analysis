
import numpy as np
from scipy.stats import mode

def task_func(list_of_lists):
    # Merge the list of lists into a single list
    merged_list = [item for sublist in list_of_lists for item in sublist]
    
    # Convert the merged list to a numpy array
    merged_array = np.array(merged_list)
    
    # Calculate the mode using scipy's mode function
    mode_result = mode(merged_array)
    
    # Extract the mode value and count
    mode_value = mode_result.mode[0]
    mode_count = mode_result.count[0]
    
    # Return the results as a tuple and numpy array
    return (mode_value, mode_count), mode_value, mode_count