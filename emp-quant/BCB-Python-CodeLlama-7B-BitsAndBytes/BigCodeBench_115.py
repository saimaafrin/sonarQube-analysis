
import numpy as np
from scipy.stats import mode
from scipy.stats import entropy

def task_func(numbers):
    if not numbers:
        raise ValueError("Input list is empty")

    numbers_array = np.array(numbers)
    mode_value = mode(numbers_array)
    entropy_value = entropy(numbers_array, base=2)

    return {'mode': mode_value, 'entropy': entropy_value}