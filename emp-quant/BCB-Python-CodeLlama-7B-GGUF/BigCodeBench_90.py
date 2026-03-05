
import numpy as np
import math

def task_func(data, target, k):
    """
    Calculate the 'k' nearest neighbors by geographic coordinates using a dataset and a target data point.
    The function returns a list of the 'k' nearest neighbors, sorted in ascending order of their distances from the target.
    Constants: radius of earth is 6371 km
    """
    if not isinstance(k, int) or k < 0:
        raise ValueError("'k' must be a positive integer")

    # Calculate the distances between the target point and all other points in the dataset
    distances = []
    for i in range(len(data)):
        lat1, lon1 = data[i][0], data[i][1]
        lat2, lon2 = target[0], target[1]
        d = haversine_distance(lat1, lon1, lat2, lon2)
        distances.append((i, d))

    # Sort the distances in ascending order
    distances.sort(key=lambda x: x[1])

    # Return the 'k' nearest neighbors
    return [data[i] for i, _ in distances[:k]]

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the haversine distance between two points on the surface of the Earth.
    Constants: radius of earth is 6371 km
    """
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    return 6371 * c