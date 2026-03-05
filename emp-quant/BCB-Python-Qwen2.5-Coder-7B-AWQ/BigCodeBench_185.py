import pandas as pd
import numpy as np
import folium
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys are present and their values are tuples
    if 'Lon' not in dic or 'Lat' not in dic or not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("Missing 'Lon' or 'Lat' keys or their values are not tuples.")
    
    # Generate random coordinates within the specified ranges
    lon_range = dic['Lon']
    lat_range = dic['Lat']
    longitudes = np.random.uniform(lon_range[0], lon_range[1], len(cities))
    latitudes = np.random.uniform(lat_range[0], lat_range[1], len(cities))
    
    # Create a DataFrame with city names and their corresponding coordinates
    data = {'City': cities, 'Longitude': longitudes, 'Latitude': latitudes}
    df = pd.DataFrame(data)
    
    # Create a folium map and add markers for each city
    map_obj = folium.Map(location=[np.mean(latitudes), np.mean(longitudes)], zoom_start=2)
    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['City']).add_to(map_obj)
    
    return (map_obj, df)