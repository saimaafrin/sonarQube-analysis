
from geopy.distance import geodesic
import folium

def task_func(dic):
    if not dic:
        raise ValueError("Input dictionary is empty")

    map = folium.Map(location=[45.5236, -122.6750], zoom_start=12)

    for location in dic:
        map.add_child(folium.Marker(location=location, popup=location))

    distances = {}
    for i in range(len(dic)):
        for j in range(i+1, len(dic)):
            distances[(dic[i], dic[j])] = geodesic(dic[i], dic[j]).km

    return map, distances