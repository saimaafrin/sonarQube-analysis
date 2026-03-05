
import collections
import json
import requests

def task_func(user, API_URL = 'https://api.github.com/users/'):
    # Construct the URL to access the user's repositories
    url = f"{API_URL}{user}/repos"
    
    # Set the headers to accept JSON response
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Make the GET request to the GitHub API
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        repositories = json.loads(response.text)
        
        # Create a list of tuples containing repository name and creation date
        repo_list = [(repo['name'], repo['created_at']) for repo in repositories]
        
        # Sort the list of tuples by the creation date
        sorted_repo_list = sorted(repo_list, key=lambda x: x[1])
        
        # Extract the sorted repository names
        sorted_repo_names = [repo[0] for repo in sorted_repo_list]
        
        return sorted_repo_names
    else:
        # Return an empty list if the request was not successful
        return []