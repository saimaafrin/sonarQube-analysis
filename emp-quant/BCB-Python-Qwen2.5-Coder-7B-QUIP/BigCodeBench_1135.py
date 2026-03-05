
import collections
import json
import requests

def task_func(user, API_URL = 'https://api.github.com/users/'):
    # Construct the full URL for the user's repositories
    url = f"{API_URL}{user}/repos"
    
    # Initialize an empty list to store repository names
    repo_names = []
    
    # Make the API request to get the list of repositories
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        repos_data = response.json()
        
        # Extract the names and creation dates of the repositories
        for repo in repos_data:
            repo_names.append((repo['name'], repo['created_at']))
        
        # Sort the list of tuples by the creation date
        repo_names.sort(key=lambda x: x[1])
        
        # Extract and return only the repository names
        return [name for name, date in repo_names]
    else:
        # Return an empty list if the request was not successful
        return []