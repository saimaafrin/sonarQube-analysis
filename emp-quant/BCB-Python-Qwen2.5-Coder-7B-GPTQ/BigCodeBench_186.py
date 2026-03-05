from geopy.distance import geodesic
import folium
def task_func(dic):
    if not dic:
        raise ValueError("Input dictionary is empty")
    
    # Create a Folium map centered at the average latitude and longitude
    latitudes = [location['latitude'] for location in dic.values()]
    longitudes = [location['longitude'] for location in dic.values()]
    avg_lat = sum(latitudes) / len(latitudes)
    avg_lon = sum(longitudes) / len(longitudes)
    folium_map = folium.Map(location=[avg_lat, avg_lon], zoom_start=5)
    
    # Calculate distances and add markers to the map
    distances = {}
    for name1, location1 in dic.items():
        for name2, location2 in dic.items():
            if name1 != name2:
                distance = geodesic((location1['latitude'], location1['longitude']),
                                    (location2['latitude'], location2['longitude'])).kilometers
                distances[(name1, name2)] = distance
                folium.Marker([location1['latitude'], location1['longitude']], popup=name1).add_to(folium_map)
                folium.Marker([location2['latitude'], location2['longitude']], popup=name2).add_to(folium_map)
                folium.PolyLine([[location1['latitude'], location1['longitude']], [location2['latitude'], location2['longitude']]], color='blue').add_to(folium_map)
    
    return folium_map, distances