
import pandas as pd
import numpy as np
import folium

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys are present in the dictionary
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("Missing 'Lon' or 'Lat' keys in the dictionary")
    
    # Check if the values of 'Lon' and 'Lat' are tuples
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("Values of 'Lon' and 'Lat' should be tuples")
    
    # Generate random coordinates within the specified ranges
    lon_range = dic['Lon']
    lat_range = dic['Lat']
    lons = np.random.uniform(lon_range[0], lon_range[1], size=len(cities))
    lats = np.random.uniform(lat_range[0], lat_range[1], size=len(cities))
    
    # Create a DataFrame with cities and their corresponding coordinates
    df = pd.DataFrame({'City': cities, 'Longitude': lons, 'Latitude': lats})
    
    # Create a Folium map and add markers for each city
    map_obj = folium.Map()
    for _, row in df.iterrows():
        folium.Marker(row['City'], location=[row['Latitude'], row['Longitude']], popup=row['City']).add_to(map_obj)
    
    return map_obj, df