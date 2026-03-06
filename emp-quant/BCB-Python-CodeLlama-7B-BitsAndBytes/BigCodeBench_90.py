
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

    # Calculate the distances between the target point and all points in the dataset
    distances = np.array([haversine_distance(target, point) for point in data])

    # Sort the distances and get the 'k' nearest neighbors
    nearest_neighbors = np.argsort(distances)[:k]

    # Return the nearest neighbors as [Latitude, Longitude]
    return np.array([data[neighbor][1:3] for neighbor in nearest_neighbors])

def haversine_distance(point1, point2):
    """
    Calculate the haversine distance between two points on the surface of a sphere (in this case, the Earth)
    """
    lat1, lon1 = point1
    lat2, lon2 = point2
    radius = 6371 # radius of earth in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius * c