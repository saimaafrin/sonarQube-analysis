
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("Missing 'Lon' or 'Lat' keys in the dictionary.")
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("Values for 'Lon' and 'Lat' should be tuples.")
    
    lon_range, lat_range = dic['Lon'], dic['Lat']
    cities = {city: (np.random.uniform(lon_range[0], lon_range[1]), np.random.uniform(lat_range[0], lat_range[1])) for city in cities}
    
    gdf = gpd.DataFrame(list(cities.items()), columns=['City', 'Coordinates'])
    gdf['Coordinates'] = gdf['Coordinates'].apply(lambda x: Point(x))
    
    return gdf