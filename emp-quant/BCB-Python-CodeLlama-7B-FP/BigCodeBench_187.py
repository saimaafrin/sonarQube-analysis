import numpy as np
import geopandas as gpd
from shapely.geometry import Point
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    """
    Create a GeoPandas DataFrame for a list of cities with randomly generated coordinates based on specified ranges.
    """
    # Check if 'Lon' and 'Lat' keys are present in the dictionary and their values are tuples
    if not isinstance(dic.get('Lon'), tuple) or not isinstance(dic.get('Lat'), tuple):
        raise ValueError("'Lon' and 'Lat' keys must be present in the dictionary and their values must be tuples")

    # Generate random coordinates within the specified ranges
    lon_range = dic['Lon']
    lat_range = dic['Lat']
    lon_coords = np.random.uniform(low=lon_range[0], high=lon_range[1], size=len(cities))
    lat_coords = np.random.uniform(low=lat_range[0], high=lat_range[1], size=len(cities))

    # Create a list of Point objects
    points = [Point(x, y) for x, y in zip(lon_coords, lat_coords)]

    # Create a GeoDataFrame with 'City' and 'Coordinates' columns
    gdf = gpd.GeoDataFrame({'City': cities, 'Coordinates': points})

    return gdf
dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']