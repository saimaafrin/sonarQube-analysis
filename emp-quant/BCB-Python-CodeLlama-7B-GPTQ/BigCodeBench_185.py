import pandas as pd
import numpy as np
import folium
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    """
    Create a map with markers for a list of cities, where the coordinates are randomly generated within given ranges.
    """
    # Check if 'Lon' and 'Lat' keys are present in the dictionary and their values are tuples
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("'Lon' and 'Lat' keys must be tuples")

    # Generate random coordinates within the given ranges
    lon_range = dic['Lon'][1] - dic['Lon'][0]
    lat_range = dic['Lat'][1] - dic['Lat'][0]
    coords = [(np.random.uniform(dic['Lon'][0], dic['Lon'][1]), np.random.uniform(dic['Lat'][0], dic['Lat'][1])) for _ in range(len(cities))]

    # Create a DataFrame with city names, longitudes, and latitudes
    df = pd.DataFrame({'City': cities, 'Longitude': [coord[0] for coord in coords], 'Latitude': [coord[1] for coord in coords]})

    # Create a map with markers for each city
    map = folium.Map(location=[0, 0], zoom_start=1)
    for city, coord in zip(cities, coords):
        folium.Marker(location=coord, popup=city).add_to(map)

    return map, df