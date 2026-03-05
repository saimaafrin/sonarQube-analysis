
import numpy as np
from scipy.stats import mode
from scipy.stats import entropy

def task_func(numbers):
    # Convert the list to a numpy array
    arr = np.array(numbers)

    # Calculate the mode and entropy of the array
    mode_val = mode(arr)
    entropy_val = entropy(arr, base=2)

    # Create a dictionary with the mode and entropy
    result = {'mode': mode_val, 'entropy': entropy_val}

    # Return the dictionary
    return result