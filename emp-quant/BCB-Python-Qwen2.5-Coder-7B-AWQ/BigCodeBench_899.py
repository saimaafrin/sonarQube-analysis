import numpy as np
import random
def task_func(length=10000, seed=0):
    """
    Generates a random walk of a specified length.

    Parameters:
    length (int): The number of steps in the random walk. Must be non-negative.
    seed (int): The seed for the random number generator.

    Returns:
    np.array: A numpy array representing the positions of the walk at each step. Starts at 0.

    Raises:
    ValueError: If `length` is negative.
    """
    if length < 0:
        raise ValueError("Length must be non-negative.")
    
    # Set the seed for the random number generator
    random.seed(seed)
    
    # Initialize the position array with the starting position at 0
    positions = np.zeros(length + 1, dtype=int)
    
    # Generate the random walk
    for i in range(1, length + 1):
        step = random.choice([-1, 1])
        positions[i] = positions[i - 1] + step
    
    return positions