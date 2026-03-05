import collections
import json
import requests
def task_func(user, API_URL = 'https://api.github.com/users/'):
    # Construct the full URL to access the user's repositories
    url = f"{API_URL}{user}/repos"
    
    # Send a GET request to the GitHub API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        repositories = json.loads(response.text)
        
        # Create a list of tuples (creation date, repository name)
        repo_dates = [(repo['created_at'], repo['name']) for repo in repositories]
        
        # Sort the list of tuples by the creation date
        sorted_repos = sorted(repo_dates)
        
        # Extract the sorted repository names
        sorted_repo_names = [repo[1] for repo in sorted_repos]
        
        return sorted_repo_names
    else:
        # Return an empty list if the request failed
        return []