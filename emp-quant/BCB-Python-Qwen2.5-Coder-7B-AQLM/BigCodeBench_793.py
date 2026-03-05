
import numpy as np
import random
# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def task_func(l=None):
    if l is None:
        l = [random.choice(ELEMENTS) for _ in range(10)]
    
    arr = np.array(l)
    first_three = arr[:3]
    remaining = arr[3:]
    result = np.concatenate((remaining, first_three))
    
    return result