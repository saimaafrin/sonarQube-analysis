
import numpy as np
import random

def task_func(length=10000, seed=0):
    if length < 0:
        raise ValueError("Length must be non-negative")
    random_walk = np.array([0])
    for i in range(length):
        random_walk = np.append(random_walk, random.choice([-1, 1]))
    return random_walk