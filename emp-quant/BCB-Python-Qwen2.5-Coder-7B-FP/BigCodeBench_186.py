from geopy.distance import geodesic
import folium
def task_func(dic):
    if not dic:
        raise ValueError("Input dictionary is empty")
    
    # Create a Folium map centered at the average latitude and longitude
    avg_lat = sum(loc['lat'] for loc in dic.values()) / len(dic)
    avg_lng = sum(loc['lng'] for loc in dic.values()) / len(dic)
    m = folium.Map(location=[avg_lat, avg_lng], zoom_start=5)
    
    # Dictionary to store distances
    distances = {}
    
    # Add markers and calculate distances
    for name1, loc1 in dic.items():
        folium.Marker([loc1['lat'], loc1['lng']], popup=name1).add_to(m)
        for name2, loc2 in dic.items():
            if name1 != name2:
                distance_km = geodesic((loc1['lat'], loc1['lng']), (loc2['lat'], loc2['lng'])).kilometers
                distances[(name1, name2)] = distance_km
    
    return m, distances