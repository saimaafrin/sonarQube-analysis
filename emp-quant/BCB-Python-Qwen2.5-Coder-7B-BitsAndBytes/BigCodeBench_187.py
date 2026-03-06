
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys exist and have tuple values
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("Both 'Lon' and 'Lat' keys must be present in the dictionary.")
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("'Lon' and 'Lat' values must be tuples.")

    # Generate random coordinates within the specified ranges
    lon_range = dic['Lon']
    lat_range = dic['Lat']
    lons = np.random.uniform(lon_range[0], lon_range[1], len(cities))
    lats = np.random.uniform(lat_range[0], lat_range[1], len(cities))

    # Create a list of Point objects from the generated coordinates
    points = [Point(lon, lat) for lon, lat in zip(lons, lats)]

    # Create a GeoDataFrame with 'City' and 'Coordinates' columns
    data = {'City': cities, 'Coordinates': points}
    gdf = gpd.GeoDataFrame(data)

    return gdf