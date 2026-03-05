
from geopy.distance import geodesic
import folium

def task_func(dic):
    if not dic:
        raise ValueError("Input dictionary is empty")
    
    # Create a Folium map centered at the first location
    if len(dic) > 0:
        first_location = next(iter(dic.values()))
        map_center = (first_location['latitude'], first_location['longitude'])
        folium_map = folium.Map(location=map_center, zoom_start=5)
    else:
        folium_map = folium.Map(location=[0, 0], zoom_start=2)
    
    # Add markers for each location
    for name, location in dic.items():
        folium.Marker([location['latitude'], location['longitude']], popup=name).add_to(folium_map)
    
    # Calculate geodesic distances between each pair of locations
    distances = {}
    for name1, location1 in dic.items():
        for name2, location2 in dic.items():
            if name1 != name2:
                distance = geodesic((location1['latitude'], location1['longitude']), (location2['latitude'], location2['longitude'])).kilometers
                distances[(name1, name2)] = distance
    
    return (folium_map, distances)