import json
import requests
def task_func(API_URL, endpoint, PREFIX):
    try:
        # Construct the full URL for the API endpoint
        full_url = f"{API_URL}/{endpoint}"
        
        # Send a GET request to the API endpoint
        response = requests.get(full_url)
        
        # Check if the request was successful
        if response.status_code != 200:
            raise RuntimeError(f"Failed to fetch data from {full_url}")
        
        # Parse the JSON data from the response
        json_data = response.json()
        
        # Generate the filename by concatenating the prefix with the endpoint name and adding '.json'
        filename = f"{PREFIX}_{endpoint}.json"
        
        # Write the JSON data to a file
        with open(filename, 'w') as file:
            json.dump(json_data, file, indent=4)
        
        # Return the filename
        return filename
    except Exception as e:
        # Raise a RuntimeError with the error message
        raise RuntimeError(f"An error occurred: {e}")