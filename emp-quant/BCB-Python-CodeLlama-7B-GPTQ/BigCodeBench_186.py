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
    map = folium.Map(location=[47.6062, -122.3321], zoom_start=12)

    # Create a dictionary to store the distances between locations
    distances = {}

    # Iterate over the dictionary of locations
    for location_name, location in dic.items():
        # Add a marker for the current location to the map
        folium.Marker(location=location, popup=location_name).add_to(map)

        # Calculate the geodesic distance between the current location and all other locations
        for other_location_name, other_location in dic.items():
            # Skip the current location
            if other_location_name == location_name:
                continue

            # Calculate the geodesic distance between the current location and the other location
            distance = geodesic(location, other_location).km

            # Add the distance to the dictionary
            distances[location_name, other_location_name] = distance

    # Return the map and the dictionary of distances
    return map, distances