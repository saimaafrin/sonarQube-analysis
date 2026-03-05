
import json
import requests

def task_func(API_URL, endpoint, PREFIX):
    try:
        # Construct the full API URL
        full_url = f"{API_URL}/{endpoint}"
        
        # Fetch data from the API
        response = requests.get(full_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Parse the JSON data from the response
        data = response.json()
        
        # Generate the filename
        filename = f"{PREFIX}_{endpoint}.json"
        
        # Write the JSON data to a file
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        
        # Return the filename
        return filename
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching data from API: {e}")
    except Exception as e:
        raise RuntimeError(f"Error writing to file: {e}")