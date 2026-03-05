
import pandas as pd
import numpy as np
import folium

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("'Lon' and 'Lat' keys are missing in the dictionary")
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("'Lon' and 'Lat' values are not tuples")

    map = folium.Map(location=[dic['Lon'][0], dic['Lat'][0]], zoom_start=10)
    df = pd.DataFrame({'City': cities, 'Longitude': np.random.uniform(dic['Lon'][0], dic['Lon'][1], len(cities)), 'Latitude': np.random.uniform(dic['Lat'][0], dic['Lat'][1], len(cities))})

    return map, df