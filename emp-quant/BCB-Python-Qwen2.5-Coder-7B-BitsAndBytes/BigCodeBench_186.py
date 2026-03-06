
from geopy.distance import geodesic
import folium

def task_func(dic):
    if not dic:
        raise ValueError("Input dictionary is empty")
    
    # Create a Folium map centered at the first location's coordinates
    center_lat = list(dic.values())[0][0]
    center_lon = list(dic.values())[0][1]
    m = folium.Map(location=[center_lat, center_lon], zoom_start=5)
    
    # Dictionary to store distances
    distances = {}
    
    # Add markers for each location
    for name, (lat, lon) in dic.items():
        folium.Marker([lat, lon], popup=name).add_to(m)
        
        # Calculate distances from this location to all other locations
        for other_name, (other_lat, other_lon) in dic.items():
            if name != other_name:
                distance_km = geodesic((lat, lon), (other_lat, other_lon)).kilometers
                distances[(name, other_name)] = distance_km
    
    return m, distances