import numpy as np
import geopandas as gpd
from shapely.geometry import Point
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    """
    Create a GeoPandas DataFrame for a list of cities with randomly generated coordinates based on specified ranges.
    """
    # Check if 'Lon' and 'Lat' keys are present in the dictionary and their values are tuples
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("'Lon' and 'Lat' keys must be tuples")

    # Generate random coordinates within the specified ranges
    lon_range = dic['Lon'][1] - dic['Lon'][0]
    lat_range = dic['Lat'][1] - dic['Lat'][0]
    coords = [(np.random.uniform(dic['Lon'][0], dic['Lon'][1]), np.random.uniform(dic['Lat'][0], dic['Lat'][1])) for _ in range(len(cities))]

    # Create a GeoPandas DataFrame with 'City' and 'Coordinates' (Point objects)
    df = gpd.GeoDataFrame(cities, geometry=[Point(x, y) for x, y in coords])

    return df