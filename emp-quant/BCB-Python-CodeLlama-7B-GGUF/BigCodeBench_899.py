
import numpy as np
import random

def task_func(length=10000, seed=0):
    if length < 0:
        raise ValueError("Length must be non-negative")

    random.seed(seed)
    positions = np.zeros(length)
    positions[0] = 0

    for i in range(1, length):
        step = random.choice([1, -1])
        positions[i] = positions[i-1] + step

    return positions