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
    # Check if 'Lon' and 'Lat' keys are present in the dictionary and their values are tuples
    if not (('Lon' in dic) and ('Lat' in dic) and (type(dic['Lon']) == tuple) and (type(dic['Lat']) == tuple)):
        raise ValueError("'Lon' and 'Lat' keys must be present in the dictionary and their values must be tuples")

    # Generate random coordinates within the given ranges
    lon_range = dic['Lon'][1] - dic['Lon'][0]
    lat_range = dic['Lat'][1] - dic['Lat'][0]
    lon_coords = np.random.uniform(low=dic['Lon'][0], high=dic['Lon'][1], size=len(cities))
    lat_coords = np.random.uniform(low=dic['Lat'][0], high=dic['Lat'][1], size=len(cities))

    # Create a DataFrame with the coordinates and cities
    df = pd.DataFrame({'City': cities, 'Longitude': lon_coords, 'Latitude': lat_coords})

    # Create a map with markers for the cities
    map = folium.Map(location=[0, 0], zoom_start=2)
    for i, city in enumerate(cities):
        folium.Marker(location=[lat_coords[i], lon_coords[i]], popup=city).add_to(map)

    return (map, df)
dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']