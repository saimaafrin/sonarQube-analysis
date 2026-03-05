
import pandas as pd
import numpy as np
import folium

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("Dictionary must contain 'Lon' and 'Lat' keys.")
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("Values for 'Lon' and 'Lat' keys must be tuples.")
    
    lon_range = dic['Lon']
    lat_range = dic['Lat']
    
    data = {
        'City': cities,
        'Longitude': [np.random.uniform(lon_range[0], lon_range[1]) for _ in cities],
        'Latitude': [np.random.uniform(lat_range[0], lat_range[1]) for _ in cities]
    }
    
    df = pd.DataFrame(data)
    
    map_obj = folium.Map(location=[np.mean(df['Latitude']), np.mean(df['Longitude'])], zoom_start=2)
    
    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['City']).add_to(map_obj)
    
    return (map_obj, df)