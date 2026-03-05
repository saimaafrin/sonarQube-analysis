
import pandas as pd
import folium
from geopy.geocoders import Photon

def task_func(dic):
    # Create a Folium map
    m = folium.Map(location=[47.6062, -122.3321], zoom_start=12)

    # Iterate over the locations in the dictionary
    for location in dic.values():
        # Check if the location is a string
        if isinstance(location, str):
            # Use the Photon geolocator to resolve the address to latitude and longitude
            geolocator = Photon(user_agent="geoapiExercises")
            location = geolocator.geocode(location)

        # Add a marker to the map for the current location
        folium.Marker(location=location, popup=location).add_to(m)

    return m