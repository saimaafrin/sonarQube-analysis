
import numpy as np
from scipy.stats import mode

def task_func(list_of_lists):
    # Merge the lists into a single array
    merged_array = np.concatenate(list_of_lists)

    # Find the mode of the merged array
    mode_value, mode_count = mode(merged_array)

    # Return the mode and count as a tuple
    return (mode_value, mode_count)

print(task_func(list_of_lists))