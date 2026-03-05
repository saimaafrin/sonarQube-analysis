import numpy as np
import math
def task_func(data, target, k):
    """
    Calculate the 'k' nearest neighbors by geographic coordinates using a dataset and a target data point.
    The function returns a list of the 'k' nearest neighbors, sorted in ascending order of their distances from the target.
    Constants: radius of earth is 6371 km
    """
    if k < 0 or not k.is_integer():
        raise ValueError("'k' must be a positive integer")

    # Calculate the distances between the target point and all points in the dataset
    distances = np.sqrt(np.square(data[:, 0] - target[0]) + np.square(data[:, 1] - target[1]))

    # Sort the distances in ascending order
    sorted_distances = np.sort(distances)

    # Select the 'k' nearest neighbors
    nearest_neighbors = sorted_distances[:k]

    # Return the list of nearest neighbors
    return nearest_neighbors