
import numpy as np
from scipy.stats import mode

def task_func(list_of_lists):
    # Merge the predefined sets of lists into a single list
    merged_list = np.concatenate(list_of_lists)

    # Find the mode of the merged list
    mode_value, mode_count = mode(merged_list)

    # Return the mode and count as a tuple
    return (mode_value, mode_count)