
import numpy as np
import random

def task_func(length=10000, seed=0):
    if length < 0:
        raise ValueError("Length must be non-negative")

    # Initialize the array to store the positions of the walk
    positions = np.zeros(length)

    # Set the random seed for reproducibility
    random.seed(seed)

    # Perform the random walk
    for i in range(length):
        # Choose a random step size
        step_size = random.choice([-1, 1])

        # Update the position
        positions[i] = positions[i-1] + step_size

    return positions