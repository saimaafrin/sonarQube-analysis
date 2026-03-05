import unicodedata
import requests
URL = 'https://api.github.com/users/'
def task_func(username):
    """
    Retrieves user information from the GitHub API for a given username, normalizes all string data to ASCII, and returns a dictionary of the normalized data.
    This function demonstrates data retrieval from a web API and handling of Unicode data normalization.
    The function should raise the exception for: requests.exceptions.HTTPError: For any HTTP response indicating an error.
    The function should output with:
        dict: A dictionary with the user's data, where all string values are normalized to ASCII.
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
        print(f'Error: {e}')
        return None