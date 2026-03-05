
import pandas as pd
import folium
from geopy.geocoders import Photon

def task_func(dic):
    # Initialize the Photon geolocator
    geolocator = Photon(user_agent="geoapiExercises")
    
    # Create a list to hold the locations
    locations = []
    
    # Iterate over the dictionary items
    for key, value in dic.items():
        # Check if the value is a list (indicating a location)
        if isinstance(value, list):
            # Check if the list contains two elements (latitude and longitude)
            if len(value) == 2:
                locations.append((key, value[0], value[1]))
            else:
                # If not, assume it's an address and resolve it
                location = geolocator.geocode(value)
                if location:
                    locations.append((key, location.latitude, location.longitude))
                else:
                    print(f"Warning: Could not resolve address for {value}")
        else:
            print(f"Warning: Invalid value type for {key}")
    
    # Create a Folium map centered at the average of the locations
    if locations:
        latitudes = [loc[1] for loc in locations]
        longitudes = [loc[2] for loc in locations]
        avg_lat = sum(latitudes) / len(latitudes)
        avg_lon = sum(longitudes) / len(longitudes)
        m = folium.Map(location=[avg_lat, avg_lon], zoom_start=10)
        
        # Add markers to the map
        for loc in locations:
            folium.Marker([loc[1], loc[2]], popup=loc[0]).add_to(m)
        
        return m
    else:
        print("No valid locations found.")
        return None