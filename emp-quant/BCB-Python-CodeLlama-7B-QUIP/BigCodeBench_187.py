
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("'Lon' and 'Lat' keys are missing in the dictionary")
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("'Lon' and 'Lat' values must be tuples")

    cities_coords = []
    for city in cities:
        lon_range = dic['Lon']
        lat_range = dic['Lat']
        lon = np.random.uniform(low=lon_range[0], high=lon_range[1])
        lat = np.random.uniform(low=lat_range[0], high=lat_range[1])
        point = Point(lon, lat)
        cities_coords.append(point)

    gdf = gpd.GeoDataFrame(cities_coords, crs=gpd.GeoSeries(crs="EPSG:4326"), geometry=gpd.GeoSeries(crs="EPSG:4326"))
    gdf.rename(columns={0: 'Coordinates'}, inplace=True)
    gdf.rename(columns={1: 'City'}, inplace=True)
    return gdf