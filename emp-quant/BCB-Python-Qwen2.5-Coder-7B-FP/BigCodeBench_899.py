import numpy as np
import random
def task_func(length=10000, seed=0):
    """
    Generates a random walk of a specified length.

    Parameters:
    - length (int): The number of steps in the random walk. Must be non-negative.
    - seed (int): The seed for the random number generator for reproducibility.

    Returns:
    - np.array: A numpy array representing the positions of the walk at each step, starting at 0.

    Raises:
    - ValueError: If `length` is negative.
    """
    if length < 0:
        raise ValueError("Length must be non-negative.")
    
    random.seed(seed)
    walk = np.zeros(length + 1)
    for i in range(1, length + 1):
        step = random.choice([-1, 1])
        walk[i] = walk[i - 1] + step
    
    return walk