
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("'Lon' and 'Lat' keys are missing in the dictionary")
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("'Lon' and 'Lat' values must be tuples")

    lon_range = dic['Lon']
    lat_range = dic['Lat']

    coordinates = []
    for city in cities:
        lon = np.random.uniform(lon_range[0], lon_range[1])
        lat = np.random.uniform(lat_range[0], lat_range[1])
        coordinates.append(Point(lon, lat))

    gdf = gpd.GeoDataFrame({'City': cities, 'Coordinates': coordinates})
    return gdf