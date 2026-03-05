import numpy as np
import math
def task_func(data, target, k):
    # Constants
    EARTH_RADIUS = 6371  # Radius of the Earth in kilometers

    # Validate input
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer")

    # Calculate distances from target to each point in the dataset
    distances = []
    for point in data:
        lat1, lon1 = target
        lat2, lon2 = point
        # Convert degrees to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = EARTH_RADIUS * c
        distances.append((point, distance))

    # Sort distances and get the k nearest neighbors
    sorted_distances = sorted(distances, key=lambda x: x[1])
    nearest_neighbors = [point for point, distance in sorted_distances[:k]]

    return nearest_neighbors