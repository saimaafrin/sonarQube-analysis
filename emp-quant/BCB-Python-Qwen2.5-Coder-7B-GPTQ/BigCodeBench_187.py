import numpy as np
import geopandas as gpd
from shapely.geometry import Point
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys are present and their values are tuples
    if 'Lon' not in dic or 'Lat' not in dic or not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("Invalid dictionary format. 'Lon' and 'Lat' keys must be present and their values must be tuples.")
    
    # Generate random coordinates within the specified ranges
    lon = np.random.uniform(dic['Lon'][0], dic['Lon'][1], size=len(cities))
    lat = np.random.uniform(dic['Lat'][0], dic['Lat'][1], size=len(cities))
    
    # Create a list of Point objects
    coordinates = [Point(lon[i], lat[i]) for i in range(len(cities))]
    
    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame({'City': cities, 'Coordinates': coordinates})
    
    return gdf