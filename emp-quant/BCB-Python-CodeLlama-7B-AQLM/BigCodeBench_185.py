import pandas as pd
import numpy as np
import folium
def task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']):
    """
    Create a map with markers for a list of cities, where the coordinates are randomly generated within given ranges.

    Parameters:
    dic (dict): Dictionary with 'Lon' and 'Lat' keys, each a tuple (min, max) for coordinate range. 
                Default: {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities (list): List of city names. Default: ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']

    Returns:
    tuple: A tuple containing (folium.Map, pandas.DataFrame).
           The DataFrame contains 'City', 'Longitude', and 'Latitude' columns.

    Raises:
    ValueError: If 'Lon' or 'Lat' keys are missing in the dictionary, or if their values are not tuples.

    Requirements:
    - pandas
    - numpy
    - folium

    Example:
    >>> dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    >>> map_obj, city_data = task_func(dic)
    """
    if 'Lon' not in dic or 'Lat' not in dic:
        raise ValueError('The dictionary must contain "Lon" and "Lat" keys.')
    if not isinstance(dic['Lon'], tuple) or not isinstance(dic['Lat'], tuple):
        raise ValueError('The values of "Lon" and "Lat" keys must be tuples.')

    # Generate random coordinates within given ranges
    city_data = pd.DataFrame(columns=['City', 'Longitude', 'Latitude'])
    for city in cities:
        city_data = city_data.append({'City': city, 'Longitude': np.random.randint(dic['Lon'][0], dic['Lon'][1]), 'Latitude': np.random.randint(dic['Lat'][0], dic['Lat'][1])}, ignore_index=True)

    # Create a map
    map_obj = folium.Map(location=[dic['Lat'][0], dic['Lon'][0]], zoom_start=2)

    # Add markers
    for i in range(len(city_data)):
        folium.Marker(location=[city_data['Latitude'][i], city_data['Longitude'][i]], popup=city_data['City'][i]).add_to(map_obj)

    return map_obj, city_data