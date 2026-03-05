
import numpy as np
from scipy.stats import mode

def task_func(list_of_lists):
    merged_list = np.concatenate(list_of_lists)
    mode_value, mode_count = mode(merged_list)
    return (mode_value, mode_count, merged_list)