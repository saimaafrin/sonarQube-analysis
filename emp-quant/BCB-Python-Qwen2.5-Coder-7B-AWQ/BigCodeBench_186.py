from geopy.distance import geodesic
import folium
def task_func(dic):
    if not dic:
        raise ValueError("Input dictionary is empty")
    
    # Create a Folium map centered at the average latitude and longitude
    latitudes = [location['latitude'] for location in dic.values()]
    longitudes = [location['longitude'] for location in dic.values()]
    avg_lat = sum(latitudes) / len(latitudes)
    avg_lng = sum(longitudes) / len(longitudes)
    m = folium.Map(location=[avg_lat, avg_lng], zoom_start=5)
    
    # Add markers for each location
    for name, location in dic.items():
        folium.Marker([location['latitude'], location['longitude']], popup=name).add_to(m)
    
    # Calculate geodesic distances between each pair of locations
    distances = {}
    for name1, location1 in dic.items():
        for name2, location2 in dic.items():
            if name1 != name2:
                distance = geodesic((location1['latitude'], location1['longitude']),
                                    (location2['latitude'], location2['longitude'])).kilometers
                distances[(name1, name2)] = distance
    
    return m, distances