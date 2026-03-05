import numpy as np
import random
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
def task_func(l=None):
    if l is None:
        l = [random.choice(ELEMENTS) for _ in range(10)]
    
    # Convert list to numpy array
    arr = np.array(l)
    
    # Move the first 3 elements to the end
    arr = np.concatenate((arr[3:], arr[:3]))
    
    return arr