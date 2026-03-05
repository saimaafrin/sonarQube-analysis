import json
import requests
def task_func(API_URL, endpoint, PREFIX):
    try:
        # Construct the full API URL
        full_url = f"{API_URL}/{endpoint}"
        
        # Fetch data from the API
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the JSON data
        json_data = response.json()
        
        # Generate the filename
        filename = f"{PREFIX}_{endpoint}.json"
        
        # Write the JSON data to a file
        with open(filename, 'w') as file:
            json.dump(json_data, file, indent=4)
        
        # Return the filename
        return filename
    except Exception as e:
        # Raise a RuntimeError with the error message
        raise RuntimeError(f"Error fetching data from API or writing to file: {e}")