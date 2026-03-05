
from typing import List, Union
import numpy as np
import scipy.fft

def task_func(data: List[Union[int, str]], repetitions: int = 1):
    if not data or repetitions <= 0:
        return {'mode': np.array([]), 'count': np.array([])}

    # Repeat the data the specified number of times
    repeated_data = data * repetitions

    # Calculate the mode(s)
    mode, count = np.unique(repeated_data, return_counts=True)

    # Sort the mode(s) in ascending order
    sorted_mode = np.sort(mode)

    # Return the result as a dictionary
    return {'mode': sorted_mode, 'count': count[sorted_mode.argsort()]}