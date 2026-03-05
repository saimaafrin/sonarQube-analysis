
from geopy.distance import geodesic
import folium

def task_func(dic):
    map = folium.Map()
    distances = {}
    for i in range(len(dic)):
        for j in range(i+1, len(dic)):
            distances[dic[i] + " to " + dic[j]] = geodesic(dic[i][0], dic[i][1], dic[j][0], dic[j][1])
    return map, distances