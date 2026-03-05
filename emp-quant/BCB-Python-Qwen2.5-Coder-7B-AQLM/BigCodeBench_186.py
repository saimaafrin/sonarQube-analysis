
from geopy.distance import geodesic
import folium

def task_func(dic):
    if not dic:
        raise ValueError("Input dictionary is empty")
    
    # Create a Folium map centered at the average latitude and longitude
    avg_lat = sum(location[0] for location in dic.values()) / len(dic)
    avg_lng = sum(location[1] for location in dic.values()) / len(dic)
    folium_map = folium.Map(location=[avg_lat, avg_lng], zoom_start=5)
    
    # Dictionary to store distances
    distances = {}
    
    # Add markers to the map and calculate distances
    for name1, (lat1, lng1) in dic.items():
        for name2, (lat2, lng2) in dic.items():
            if name1 != name2:
                distance_km = geodesic((lat1, lng1), (lat2, lng2)).kilometers
                distances[(name1, name2)] = distance_km
                folium.Marker([lat1, lng1], popup=name1).add_to(folium_map)
                folium.Marker([lat2, lng2], popup=name2).add_to(folium_map)
                folium.PolyLine([[lat1, lng1], [lat2, lng2]], color='blue', weight=2.5, opacity=1).add_to(folium_map)
    
    return folium_map, distances