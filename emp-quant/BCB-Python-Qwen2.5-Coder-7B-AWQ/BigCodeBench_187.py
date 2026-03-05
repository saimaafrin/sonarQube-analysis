import numpy as np
import geopandas as gpd
from shapely.geometry import Point
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys are present and their values are tuples
    if 'Lon' not in dic or 'Lat' not in dic or not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("The dictionary must contain 'Lon' and 'Lat' keys with tuple values.")
    
    # Generate random coordinates within the specified ranges
    lons = np.random.uniform(dic['Lon'][0], dic['Lon'][1], len(cities))
    lats = np.random.uniform(dic['Lat'][0], dic['Lat'][1], len(cities))
    
    # Create a list of Point objects
    points = [Point(lon, lat) for lon, lat in zip(lons, lats)]
    
    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame({'City': cities, 'Coordinates': points})
    
    return gdf