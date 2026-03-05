import pandas as pd
import numpy as np
import folium
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    """
    Create a map with markers for a list of cities, where the coordinates are randomly generated within given ranges.
    The function should raise the exception for:
        ValueError: If 'Lon' or 'Lat' keys are missing in the dictionary, or if their values are not tuples.
    The function should output with:
        tuple: A tuple containing (folium.Map, pandas.DataFrame).
        The DataFrame contains 'City', 'Longitude', and 'Latitude' columns.
    """
    # Check if 'Lon' and 'Lat' keys are in the dictionary and their values are tuples
    if not ('Lon' in dic and 'Lat' in dic and isinstance(dic['Lon'], tuple) and isinstance(dic['Lat'], tuple)):
        raise ValueError("'Lon' and 'Lat' keys must be in the dictionary and their values must be tuples")

    # Generate random coordinates within the given ranges
    lon_range = dic['Lon'][0], dic['Lon'][1]
    lat_range = dic['Lat'][0], dic['Lat'][1]
    coords = np.random.rand(len(cities), 2)
    coords[:, 0] = np.random.uniform(lon_range[0], lon_range[1], size=len(cities))
    coords[:, 1] = np.random.uniform(lat_range[0], lat_range[1], size=len(cities))

    # Create a DataFrame with the coordinates and cities
    df = pd.DataFrame({'City': cities, 'Longitude': coords[:, 0], 'Latitude': coords[:, 1]})

    # Create a map with markers for the cities
    m = folium.Map(location=[0, 0], zoom_start=2)
    for i, city in enumerate(cities):
        folium.Marker(location=coords[i], popup=city).add_to(m)

    return m, df