
import collections
import json
import requests

def task_func(user, API_URL = 'https://api.github.com/users/'):
    # Query the GitHub API for the user's repositories
    response = requests.get(API_URL + user + '/repos')
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        repos = json.loads(response.content)
        # Extract the repository names and creation dates
        repo_names = [repo['name'] for repo in repos]
        repo_dates = [repo['created_at'] for repo in repos]
        # Sort the repository names and creation dates by creation date
        sorted_repo_names = sorted(repo_names, key=lambda x: repo_dates.index(x))
        return sorted_repo_names
    else:
        return None