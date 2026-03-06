from geopy.distance import geodesic
import folium
def task_func(dic):
    """
    Generates a Folium map with markers for specified locations and calculates the geodesic
    distances between each pair of locations.

    Parameters:
        dic (dict): A dictionary with location names as keys and their latitudes and longitudes
                    as values (e.g., {'Location': {'Lat': latitude, 'Lon': longitude}}).

    Returns:
        tuple: A tuple containing a Folium map object and a dictionary with pairs of location
               names as keys and their distances in kilometers as values.

    Raises:
        ValueError: If the input dictionary is empty.

    Requirements:
    - geopy.distance.geodesic
    - folium

    Examples:
    >>> result = task_func({'Place1': {'Lat': 0, 'Lon': 0}, 'Place2': {'Lat': 0, 'Lon': 1}})
    >>> isinstance(result, tuple) and len(result) == 2
    True
    >>> isinstance(result[0], folium.folium.Map) and isinstance(result[1], dict)
    True
    """
    if not dic:
        raise ValueError('The input dictionary is empty.')

    # Create a Folium map object.
    m = folium.Map(location=[0, 0], zoom_start=1)

    # Create a dictionary with pairs of location names as keys and their distances in kilometers
    # as values.
    distances = {}

    # Add markers for each location.
    for location in dic:
        folium.Marker(location=[dic[location]['Lat'], dic[location]['Lon']],
                      popup=location).add_to(m)

    # Calculate the geodesic distances between each pair of locations.
    for location1 in dic:
        for location2 in dic:
            if location1 != location2:
                distances[(location1, location2)] = geodesic(
                    (dic[location1]['Lat'], dic[location1]['Lon']),
                    (dic[location2]['Lat'], dic[location2]['Lon'])).km

    return m, distances