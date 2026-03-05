
from geopy.distance import geodesic
import folium

def task_func(dic):
    if not dic:
        raise ValueError("Input dictionary is empty")
    
    # Create a Folium map
    map_obj = folium.Map(location=[0, 0], zoom_start=2)
    
    # Add markers for each location
    for location, coordinates in dic.items():
        folium.Marker([coordinates[0], coordinates[1]], popup=location).add_to(map_obj)
    
    # Calculate and store distances between each pair of locations
    distances = {}
    for i, (name1, coords1) in enumerate(dic.items()):
        for name2, coords2 in dic.items():
            if name1 != name2:
                distance = geodesic(coords1, coords2).kilometers
                distances[(name1, name2)] = distance
    
    return map_obj, distances