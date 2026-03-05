
import unicodedata
import requests

URL = 'https://api.github.com/users/'

def task_func(username):
    try:
        response = requests.get(URL + username)
        response.raise_for_status()
        data = response.json()
        normalized_data = {}
        for key, value in data.items():
            if isinstance(value, str):
                normalized_data[key] = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
            else:
                normalized_data[key] = value
        return normalized_data
    except requests.exceptions.HTTPError as e:
        print(f'HTTP error occurred: {e}')
        return None