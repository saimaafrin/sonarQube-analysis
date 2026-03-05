import unicodedata
import requests
URL = 'https://api.github.com/users/'
def task_func(username):
    """
    Retrieves user information from the GitHub API for a given username, normalizes all string data to ASCII, and returns a dictionary of the normalized data.
    This function demonstrates data retrieval from a web API and handling of Unicode data normalization.
    """
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
        raise e