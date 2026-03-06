
import numpy as np
from scipy.stats import mode
from scipy.stats import entropy

def task_func(numbers):
    if not numbers:
        raise ValueError("Input list 'numbers' cannot be empty")
    
    arr = np.array(numbers)
    arr_mode = mode(arr).mode[0]
    arr_entropy = entropy(np.unique(arr, return_counts=True)[1], base=2)
    
    result_dict = {
        'mode': arr_mode,
        'entropy': arr_entropy
    }
    
    return result_dict