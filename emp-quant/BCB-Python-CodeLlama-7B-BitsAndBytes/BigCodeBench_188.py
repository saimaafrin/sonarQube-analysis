
import pandas as pd
import folium
from geopy.geocoders import Photon

def task_func(dic):
    # Create a Folium map
    m = folium.Map(location=[45.5236, -122.6750], zoom_start=12)

    # Iterate over the dictionary of locations
    for key, value in dic.items():
        # If the value is a string, use Photon to resolve the address
        if isinstance(value, str):
            location = Photon(user_agent="geoapiExercises").geocode(value)
            lat, lon = location.latitude, location.longitude
        # If the value is a tuple, use the tuple as the location
        else:
            lat, lon = value

        # Add a marker to the map for the location
        folium.Marker(location=[lat, lon], popup=key).add_to(m)

    return m