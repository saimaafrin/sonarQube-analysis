
import numpy as np
import random

def task_func(length=10000, seed=0):
    if length < 0:
        raise ValueError("Length cannot be negative")
    
    random.seed(seed)
    walk = np.zeros(length + 1)
    
    for i in range(1, length + 1):
        step = random.choice([-1, 1])
        walk[i] = walk[i - 1] + step
    
    return walk