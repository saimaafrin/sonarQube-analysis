
import json
import requests

def task_func(API_URL, endpoint, PREFIX):
    """
    Retrieves JSON data from a specified API endpoint and writes it to a file.

    Args:
        API_URL (str): The base URL of the API.
        endpoint (str): The name of the endpoint to retrieve data from.
        PREFIX (str): The prefix to use for the filename.

    Returns:
        str: The filename into which the JSON data was written.

    Raises:
        RuntimeError: If there is an error fetching data from the API or writing to the file.
    """
    try:
        # Fetch data from API
        response = requests.get(f"{API_URL}/{endpoint}")
        if response.status_code != 200:
            raise RuntimeError(f"Error fetching data from API: {response.text}")

        # Write data to file
        filename = f"{PREFIX}{endpoint}.json"
        with open(filename, "w") as f:
            json.dump(response.json(), f)

        return filename
    except RuntimeError as e:
        raise RuntimeError(f"Error writing data to file: {e}")