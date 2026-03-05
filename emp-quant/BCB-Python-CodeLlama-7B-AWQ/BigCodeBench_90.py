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
    distances = []
    for i in range(len(data)):
        lat1, lon1 = data[i]
        lat2, lon2 = target
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        distances.append(c * 6371)

    # Sort the distances and return the 'k' nearest neighbors
    sorted_distances = sorted(distances)
    return [data[i] for i in range(k)]
data = [(37.7749, -122.4194), (37.7566, -122.4253), (37.7554, -122.4240), (37.7538, -122.4232)]
target = (37.7749, -122.4194)
k = 2