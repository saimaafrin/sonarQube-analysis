
from geopy.distance import geodesic
import folium

def task_func(dic):
    if not dic:
        raise ValueError("Input dictionary is empty")

    # Create a Folium map
    m = folium.Map(location=[45.5236, -122.6750], zoom_start=12)

    # Add markers for each location
    for location in dic:
        folium.Marker(location=location, popup=location).add_to(m)

    # Calculate geodesic distances between each pair of locations
    distances = {}
    for i in range(len(dic)):
        for j in range(i+1, len(dic)):
            distances[(dic[i], dic[j])] = geodesic(dic[i], dic[j]).km

    return m, distances

# Print the distances
print(distances)