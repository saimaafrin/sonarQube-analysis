import numpy as np
from scipy.stats import mode
def task_func(list_of_lists):
    # Merge the list of lists into a single list
    merged_list = [item for sublist in list_of_lists for item in sublist]
    
    # Convert the merged list into a numpy array
    merged_array = np.array(merged_list)
    
    # Calculate the mode using scipy's mode function
    mode_result = mode(merged_array)
    
    # Extract the mode value and count from the result
    mode_value = mode_result.mode[0]
    mode_count = mode_result.count[0]
    
    # Return the mode value and count as a tuple
    return (mode_value, mode_count)
list_of_lists = [[1, 2, 3], [2, 3, 4], [2, 3, 5]]