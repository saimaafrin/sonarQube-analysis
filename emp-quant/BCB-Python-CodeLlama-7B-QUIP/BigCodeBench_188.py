
import pandas as pd
import folium
from geopy.geocoders import Photon

def task_func(dic):
    # Create a Folium map object
    m = folium.Map(location=[40.74, -73.98], zoom=10)

    # Create a list of markers for each location
    markers = []
    for location in dic:
        # If the location is a string, use the Photon geolocation service to convert it to latitude and longitude
        if isinstance(location, str):
            location = Photon(location).latlng
        # Create a marker for the location
        markers.append(folium.Marker(location=location, popup=location))

    # Add the markers to the map
    for marker in markers:
        m.add_marker(marker)

    return m