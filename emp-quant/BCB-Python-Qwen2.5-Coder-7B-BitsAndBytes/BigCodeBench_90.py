
import numpy as np
import math

def calculate_distance(lat1, lon1, lat2, lon2):
    # Haversine formula to calculate distance between two points on the Earth
    R = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def task_func(data, target, k):
    if not isinstance(k, int) or k < 0:
        raise ValueError("The value of 'k' must be a non-negative integer.")
    
    if len(data) == 0:
        raise ValueError("The dataset cannot be empty.")
    
    if len(target) != 2:
        raise ValueError("The target data point must have exactly two elements (latitude and longitude).")
    
    # Calculate distances from target to all points in the dataset
    distances = []
    for point in data:
        dist = calculate_distance(target[0], target[1], point[0], point[1])
        distances.append((point, dist))
    
    # Sort the points based on their distances from the target
    sorted_points = sorted(distances, key=lambda x: x[1])
    
    # Extract the first 'k' points
    nearest_neighbors = [point[0] for point in sorted_points[:k]]
    
    return nearest_neighbors

try:
    result = task_func(data, target, k)
    print(result)
except ValueError as e:
    print(e)