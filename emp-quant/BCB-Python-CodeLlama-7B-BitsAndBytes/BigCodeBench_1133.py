
import json
import requests

def task_func(API_URL, endpoint, PREFIX):
    try:
        # Fetch data from API
        response = requests.get(API_URL + endpoint)
        data = response.json()

        # Write data to file
        filename = PREFIX + endpoint + '.json'
        with open(filename, 'w') as f:
            json.dump(data, f)

        return filename

    except Exception as e:
        raise RuntimeError(f'Error fetching data from API or writing to file: {e}')