
import unicodedata
import requests
URL = 'https://api.github.com/users/'

def task_func(username):
    try:
        response = requests.get(URL + username)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        user_data = response.json()
        
        # Normalize all string data to ASCII
        normalized_data = {key: unicodedata.normalize('NFD', value).encode('ascii', 'ignore').decode() for key, value in user_data.items()}
        
        return normalized_data
    except requests.exceptions.HTTPError as e:
        raise e