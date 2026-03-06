
import pandas as pd
import numpy as np
import folium

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys exist and have valid tuple values
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("Missing 'Lon' or 'Lat' key in the dictionary.")
    
    lon_range = dic['Lon']
    lat_range = dic['Lat']
    
    if not isinstance(lon_range, tuple) or not isinstance(lat_range, tuple):
        raise ValueError("'Lon' and 'Lat' values must be tuples.")
    
    if len(lon_range) != 2 or len(lat_range) != 2:
        raise ValueError("Tuples must contain exactly two elements.")
    
    # Generate random coordinates within the specified ranges
    lons = np.random.uniform(lon_range[0], lon_range[1], size=len(cities))
    lats = np.random.uniform(lat_range[0], lat_range[1], size=len(cities))
    
    # Create a DataFrame to store city names and their corresponding coordinates
    data = {'City': cities, 'Longitude': lons, 'Latitude': lats}
    df = pd.DataFrame(data)
    
    # Create a Folium map centered at the average coordinates
    avg_lon = np.mean(lons)
    avg_lat = np.mean(lats)
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=4)
    
    # Add markers for each city on the map
    for _, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['City']).add_to(m)
    
    return m, df