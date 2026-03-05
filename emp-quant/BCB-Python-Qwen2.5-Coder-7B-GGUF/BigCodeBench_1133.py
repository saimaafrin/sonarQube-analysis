
import json
import requests

def task_func(API_URL, endpoint, PREFIX):
    try:
        # Construct the full URL by combining the API URL and the endpoint
        full_url = f"{API_URL}/{endpoint}"
        
        # Send a GET request to the API endpoint
        response = requests.get(full_url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON data from the response
        json_data = response.json()
        
        # Construct the filename by concatenating the prefix, endpoint, and '.json'
        filename = f"{PREFIX}_{endpoint}.json"
        
        # Write the JSON data to a file with the constructed filename
        with open(filename, 'w') as file:
            json.dump(json_data, file, indent=4)
        
        # Return the filename
        return filename
    
    except requests.exceptions.RequestException as e:
        # Raise a RuntimeError if there is an error fetching data from the API
        raise RuntimeError(f"Error fetching data from API: {e}")
    
    except Exception as e:
        # Raise a RuntimeError if there is an error writing to the file
        raise RuntimeError(f"Error writing to file: {e}")