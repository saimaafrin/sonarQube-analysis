import unicodedata
import requests
URL = 'https://api.github.com/users/'
def normalize_string(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s) if unicodedata.category(c) != 'Mn')
def task_func(username):
    response = requests.get(URL + username)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    user_data = response.json()
    normalized_data = {key: normalize_string(value) if isinstance(value, str) else value for key, value in user_data.items()}
    return normalized_data