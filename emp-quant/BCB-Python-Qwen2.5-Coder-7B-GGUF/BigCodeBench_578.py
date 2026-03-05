
import unicodedata
import requests

URL = 'https://api.github.com/users/'

def task_func(username):
    try:
        response = requests.get(URL + username)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        user_data = response.json()
        normalized_data = {key: unicodedata.normalize('NFKD', str(value)).encode('ascii', 'ignore').decode('ascii') for key, value in user_data.items() if isinstance(value, (str, int))}
        return normalized_data

    except requests.exceptions.HTTPError as e:
        raise e