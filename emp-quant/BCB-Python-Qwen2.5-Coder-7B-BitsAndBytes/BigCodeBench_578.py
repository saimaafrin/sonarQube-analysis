
import unicodedata
import requests

URL = 'https://api.github.com/users/'

def normalize_string(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def task_func(username):
    try:
        response = requests.get(URL + username)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        user_data = response.json()
        
        normalized_user_data = {key: normalize_string(value) if isinstance(value, str) else value for key, value in user_data.items()}
        
        return normalized_user_data
    
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error occurred: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise