
import numpy as np
import random

def task_func(length=10000, seed=0):
    if length < 0:
        raise ValueError("Length cannot be negative")
    
    random.seed(seed)
    walk = [0]  # Starting at position 0
    for _ in range(length):
        step = random.choice([-1, 1])
        walk.append(walk[-1] + step)
    
    return np.array(walk)