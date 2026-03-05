import numpy as np
import math
def task_func(data, target, k):
    """
    Calculate the 'k' nearest neighbors by geographic coordinates using a dataset and a target data point.
    The function returns a list of the 'k' nearest neighbors, sorted in ascending order of their distances from the target.
    Constants: radius of earth is 6371 km
    """
    if k < 0 or not isinstance(k, int):
        raise ValueError("'k' must be a positive integer")

    # Calculate the distances between the target point and all points in the dataset
    distances = np.array([haversine(target, point) for point in data])

    # Sort the distances in ascending order
    sorted_distances = np.sort(distances)

    # Return the 'k' nearest neighbors
    return data[np.argsort(distances)[:k]]
def haversine(point1, point2):
    """
    Calculate the haversine distance between two points on the surface of the Earth.
    """
    # Convert the points to radians
    point1_rad = np.radians(point1)
    point2_rad = np.radians(point2)

    # Calculate the difference between the points in radians
    dlat = point2_rad[0] - point1_rad[0]
    dlon = point2_rad[1] - point1_rad[1]

    # Calculate the haversine distance
    a = np.sin(dlat / 2) ** 2 + np.cos(point1_rad[0]) * np.cos(point2_rad[0]) * np.sin(dlon / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    # Return the haversine distance in kilometers
    return 6371 * c
data = np.array([[37.7749, -122.4194], [37.7566, -122.4253], [37.7554, -122.4240], [37.7606, -122.4179]])
target = np.array([37.7749, -122.4194])
k = 2