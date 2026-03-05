import numpy as np
import math
def task_func(data, target, k):
    # Check if k is a non-negative integer
    if not isinstance(k, int) or k < 0:
        raise ValueError("k must be a non-negative integer")
    
    # Radius of the Earth in kilometers
    R = 6371
    
    # Convert target coordinates to radians
    lat_target, lon_target = np.radians(target)
    
    # Calculate distances from target to each point in the dataset
    distances = []
    for point in data:
        lat, lon = np.radians(point)
        dlat = lat - lat_target
        dlon = lon - lon_target
        a = math.sin(dlat/2)**2 + math.cos(lat_target) * math.cos(lat) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c
        distances.append((point, distance))
    
    # Sort the points by distance
    sorted_points = sorted(distances, key=lambda x: x[1])
    
    # Return the 'k' nearest neighbors
    return [point for point, _ in sorted_points[:k]]
data = [[51.5074, -0.1278], [40.7128, -74.0060], [34.0522, -118.2437], [48.8566, 2.3522]]
target = [48.8566, 2.3522]
k = 2