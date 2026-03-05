import unicodedata
import requests
URL = 'https://api.github.com/users/'
def task_func(username):
    """
    Retrieves user information from the GitHub API for a given username, normalizes all string data to ASCII, and returns a dictionary of the normalized data.
    
    Args:
    username (str): The GitHub username to retrieve information for.
    
    Returns:
    dict: A dictionary with the user's data, where all string values are normalized to ASCII.
    
    Raises:
    requests.exceptions.HTTPError: For any HTTP response indicating an error.
    """
    response = requests.get(URL + username)
    response.raise_for_status()  # Raises an HTTPError for bad responses

    user_data = response.json()
    normalized_data = {key: unicodedata.normalize('NFKD', str(value)).encode('ascii', 'ignore').decode('ascii') for key, value in user_data.items() if isinstance(value, (str, int))}
    return normalized_data