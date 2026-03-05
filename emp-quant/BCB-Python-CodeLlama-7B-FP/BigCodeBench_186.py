from geopy.distance import geodesic
import folium
def task_func(dic):
    """
    Generates a Folium map with markers for specified locations and calculates the geodesic distances between each pair of locations.
    The function should raise the exception for: ValueError: If the input dictionary is empty.
    The function should output with:
        tuple: A tuple containing a Folium map object and a dictionary with pairs of location
        names as keys and their distances in kilometers as values.
    """
    if not dic:
        raise ValueError("Input dictionary is empty.")

    # Create a Folium map object
    m = folium.Map(location=[45.5236, -122.6750], zoom_start=12)

    # Create a dictionary to store the distances between locations
    distances = {}

    # Iterate over the dictionary of locations
    for location_1, location_2 in dic.items():
        # Calculate the geodesic distance between the two locations
        distance = geodesic(location_1, location_2).km

        # Add the distance to the dictionary
        distances[location_1, location_2] = distance

        # Add a marker for each location to the map
        folium.Marker(location=location_1, popup=location_1).add_to(m)
        folium.Marker(location=location_2, popup=location_2).add_to(m)

    return m, distances
dic = {"Seattle": {"Portland": 100, "San Francisco": 200},
       "Portland": {"Seattle": 100, "Vancouver": 50},
       "San Francisco": {"Seattle": 200, "Los Angeles": 100},
       "Los Angeles": {"San Francisco": 100, "Phoenix": 200},
       "Phoenix": {"Los Angeles": 200, "Tucson": 100},
       "Tucson": {"Phoenix": 100, "Albuquerque": 50}}