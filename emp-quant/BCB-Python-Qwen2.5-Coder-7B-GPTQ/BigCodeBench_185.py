import pandas as pd
import numpy as np
import folium
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys are present and their values are tuples
    if 'Lon' not in dic or 'Lat' not in dic or not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("Missing 'Lon' or 'Lat' keys or their values are not tuples")
    
    # Generate random coordinates within the specified ranges
    lon_range = dic['Lon']
    lat_range = dic['Lat']
    lon = np.random.uniform(lon_range[0], lon_range[1], len(cities))
    lat = np.random.uniform(lat_range[0], lat_range[1], len(cities))
    
    # Create a DataFrame with city names and their corresponding coordinates
    df = pd.DataFrame({'City': cities, 'Longitude': lon, 'Latitude': lat})
    
    # Create a map centered at the mean of the generated coordinates
    map_center = [np.mean(lat), np.mean(lon)]
    m = folium.Map(location=map_center, zoom_start=2)
    
    # Add markers for each city on the map
    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['City']).add_to(m)
    
    return (m, df)