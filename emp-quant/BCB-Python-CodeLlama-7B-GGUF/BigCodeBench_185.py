
import pandas as pd
import numpy as np
import folium

def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    """
    Create a map with markers for a list of cities, where the coordinates are randomly generated within given ranges.

    Parameters:
    dic (dict): A dictionary containing the ranges for the longitude and latitude coordinates.
    cities (list): A list of city names.

    Returns:
    tuple: A tuple containing (folium.Map, pandas.DataFrame).
    The DataFrame contains 'City', 'Longitude', and 'Latitude' columns.

    Raises:
    ValueError: If 'Lon' or 'Lat' keys are missing in the dictionary, or if their values are not tuples.
    """
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError("'Lon' and 'Lat' keys must be present in the dictionary.")
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError("'Lon' and 'Lat' values must be tuples.")

    # Generate random coordinates within the given ranges
    lon_range = dic['Lon']
    lat_range = dic['Lat']
    lon_coords = np.random.uniform(low=lon_range[0], high=lon_range[1], size=len(cities))
    lat_coords = np.random.uniform(low=lat_range[0], high=lat_range[1], size=len(cities))

    # Create a DataFrame with the city names and coordinates
    df = pd.DataFrame({'City': cities, 'Longitude': lon_coords, 'Latitude': lat_coords})

    # Create a map with markers for the cities
    map = folium.Map(location=[0, 0], zoom_start=1)
    for i, city in enumerate(cities):
        folium.Marker(location=[lat_coords[i], lon_coords[i]], popup=city).add_to(map)

    return map, df