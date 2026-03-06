
import json
import requests

def task_func(API_URL, endpoint, PREFIX):
    try:
        # Construct the full URL for the API request
        url = f"{API_URL}/{endpoint}"
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON data from the response
        data = response.json()
        
        # Generate the filename using the provided prefix and endpoint
        filename = f"{PREFIX}_{endpoint}.json"
        
        # Write the JSON data to a file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        
        # Return the filename
        return filename
    
    except (requests.RequestException, json.JSONDecodeError) as e:
        # Raise a RuntimeError with the error message
        raise RuntimeError(f"Error fetching data from API or writing to file: {e}")