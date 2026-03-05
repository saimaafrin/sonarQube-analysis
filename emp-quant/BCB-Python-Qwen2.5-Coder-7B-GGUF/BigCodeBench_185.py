
import pandas as pd
import numpy as np
import folium

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys are present and their values are tuples
    if 'Lon' not in dic or 'Lat' not in dic or not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("Missing 'Lon' or 'Lat' keys or their values are not tuples")
    
    # Generate random coordinates within the specified ranges
    lons = np.random.uniform(dic['Lon'][0], dic['Lon'][1], len(cities))
    lats = np.random.uniform(dic['Lat'][0], dic['Lat'][1], len(cities))
    
    # Create a DataFrame with city names and their corresponding coordinates
    df = pd.DataFrame({'City': cities, 'Longitude': lons, 'Latitude': lats})
    
    # Create a folium map centered at the mean of the generated coordinates
    map_center = [np.mean(lats), np.mean(lons)]
    m = folium.Map(location=map_center, zoom_start=2)
    
    # Add markers to the map for each city
    for index, row in df.iterrows():
        folium.Marker([row['Latitude'], row['Longitude']], popup=row['City']).add_to(m)
    
    return (m, df)