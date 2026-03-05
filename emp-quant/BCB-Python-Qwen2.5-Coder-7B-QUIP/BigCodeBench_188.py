
import pandas as pd
import folium
from geopy.geocoders import Photon

def task_func(dic):
    # Initialize the geolocator
    geolocator = Photon(user_agent="geoapiExercises")

    # Create a Folium map
    map_ = folium.Map(location=[0, 0], zoom_start=2)

    # Function to get latitude and longitude from address
    def get_lat_lon(address):
        location = geolocator.geocode(address, exactly_one=True, timeout=10)
        if location:
            return (location.latitude, location.longitude)
        else:
            raise ValueError(f"Address {address} not found")

    # Add markers to the map
    for key, value in dic.items():
        if isinstance(value, str):
            lat, lon = get_lat_lon(value)
        elif isinstance(value, list) and len(value) == 2:
            lat, lon = value
        else:
            raise ValueError(f"Invalid value for {key}")
        folium.Marker([lat, lon], popup=key).add_to(map_)

    return map_