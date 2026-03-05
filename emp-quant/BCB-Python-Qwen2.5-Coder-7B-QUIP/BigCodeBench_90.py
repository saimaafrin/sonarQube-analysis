
import numpy as np
import math

def task_func(data, target, k):
    # Check if k is a valid integer
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer")
    
    # Calculate the distance between the target and each point in the dataset
    distances = np.sqrt((data[:, 0] - target[0])**2 + (data[:, 1] - target[1])**2)
    
    # Get the indices of the k nearest neighbors
    nearest_indices = np.argsort(distances)[:k]
    
    # Return the k nearest neighbors
    nearest_neighbors = data[nearest_indices].tolist()
    
    return nearest_neighbors