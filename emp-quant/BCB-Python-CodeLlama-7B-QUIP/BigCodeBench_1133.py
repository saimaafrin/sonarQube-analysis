
import json
import requests

def task_func(API_URL, endpoint, PREFIX):
    try:
        # Fetch data from API
        response = requests.get(API_URL + endpoint)
        if response.status_code == 200:
            # Write data to file
            with open(PREFIX + endpoint + '.json', 'w') as f:
                f.write(response.text)
                return PREFIX + endpoint + '.json'
        else:
            raise RuntimeError("Error fetching data from API")
    except requests.exceptions.RequestException as e:
        raise RuntimeError("Error fetching data from API")