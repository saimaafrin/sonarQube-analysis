
import numpy as np
from scipy.stats import mode

def task_func(list_of_lists):
    # Merge the list of lists into a single list
    merged_list = []
    for sublist in list_of_lists:
        merged_list.extend(sublist)
    
    # Convert the merged list to a numpy array
    merged_array = np.array(merged_list)
    
    # Find the mode of the merged array
    mode_value, mode_count = mode(merged_array)
    
    # Return the mode and count as a tuple
    return (mode_value, mode_count)