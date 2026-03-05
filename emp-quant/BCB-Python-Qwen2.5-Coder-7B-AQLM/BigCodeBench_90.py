
import numpy as np
import math

def task_func(data, target, k):
    # Constants
    R = 6371  # Radius of the Earth in kilometers

    # Validate k
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer")

    # Convert target coordinates to radians
    target_lat_rad = math.radians(target[0])
    target_lon_rad = math.radians(target[1])

    # Calculate distances using the Haversine formula
    distances = []
    for point in data:
        lat_rad = math.radians(point[0])
        lon_rad = math.radians(point[1])
        dlat = lat_rad - target_lat_rad
        dlon = lon_rad - target_lon_rad
        a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(target_lat_rad) * math.cos(lat_rad) * math.sin(dlon / 2) * math.sin(dlon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        distances.append((distance, point))

    # Sort distances and get the k nearest neighbors
    nearest_neighbors = sorted(distances)[:k]

    # Extract the coordinates of the nearest neighbors
    result = [neighbor[1] for neighbor in nearest_neighbors]

    return result