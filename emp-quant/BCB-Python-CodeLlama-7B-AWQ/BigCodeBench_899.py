import numpy as np
import random
def task_func(length=10000, seed=0):
    """
    Generates a random walk of a specified length.

    Args:
        length (int): The length of the walk.
        seed (int): The seed for the random number generator.

    Returns:
        np.array: A numpy array representing the positions of the walk at each step. Starts at 0.

    Raises:
        ValueError: If `length` is negative.
    """
    if length < 0:
        raise ValueError("Length must be non-negative.")

    # Initialize the walk at 0
    walk = np.array([0])

    # Generate the walk
    for i in range(length):
        step = random.choice([1, -1])
        walk = np.append(walk, walk[-1] + step)

    return walk