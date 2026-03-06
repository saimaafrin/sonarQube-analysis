
import pandas as pd
import numpy as np
import folium

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    # Check if 'Lon' and 'Lat' keys are present in the dictionary and their values are tuples
    if 'Lon' not in dic or 'Lat' not in dic or not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("Invalid input. 'Lon' and 'Lat' keys must be present in the dictionary and their values must be tuples.")

    # Generate random coordinates within the given ranges
    lon_range = dic['Lon'][1] - dic['Lon'][0]
    lat_range = dic['Lat'][1] - dic['Lat'][0]
    lon_coords = np.random.uniform(low=dic['Lon'][0], high=dic['Lon'][1], size=len(cities))
    lat_coords = np.random.uniform(low=dic['Lat'][0], high=dic['Lat'][1], size=len(cities))

    # Create a DataFrame with the cities and their coordinates
    df = pd.DataFrame({'City': cities, 'Longitude': lon_coords, 'Latitude': lat_coords})

    # Create a folium map with the markers
    m = folium.Map(location=[np.mean(lat_coords), np.mean(lon_coords)], zoom_start=4)
    for i, city in enumerate(cities):
        folium.Marker(location=[lat_coords[i], lon_coords[i]], popup=city).add_to(m)

    return m, df