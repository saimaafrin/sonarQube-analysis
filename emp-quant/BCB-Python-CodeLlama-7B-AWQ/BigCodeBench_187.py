import numpy as np
import geopandas as gpd
from shapely.geometry import Point
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    """
    Create a GeoPandas DataFrame for a list of cities with randomly generated coordinates based on specified ranges.
    """
    # Check if 'Lon' and 'Lat' keys are in the dictionary and their values are tuples
    if not ('Lon' in dic and 'Lat' in dic and isinstance(dic['Lon'], tuple) and isinstance(dic['Lat'], tuple)):
        raise ValueError("'Lon' and 'Lat' keys must be in the dictionary and their values must be tuples")

    # Generate random coordinates within the specified ranges
    lon_range = dic['Lon']
    lat_range = dic['Lat']
    coords = [(np.random.uniform(lon_range[0], lon_range[1]), np.random.uniform(lat_range[0], lat_range[1])) for _ in range(len(cities))]

    # Create a GeoDataFrame with 'City' and 'Coordinates' (Point objects)
    gdf = gpd.GeoDataFrame({'City': cities, 'Coordinates': [Point(x, y) for x, y in coords]})

    return gdf
dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']