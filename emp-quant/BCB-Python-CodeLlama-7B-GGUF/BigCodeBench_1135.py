
import collections
import json
import requests

def task_func(user, API_URL = 'https://api.github.com/users/'):
    # Query the GitHub API for the specified user's repositories
    response = requests.get(API_URL + user + '/repos')
    # Parse the response as JSON
    repos = json.loads(response.text)
    # Create a list to store the repository names and creation dates
    repo_names = []
    for repo in repos:
        # Extract the repository name and creation date
        name = repo['name']
        created_at = repo['created_at']
        # Add the repository name and creation date to the list
        repo_names.append((name, created_at))
    # Sort the list by the creation date
    repo_names.sort(key=lambda x: x[1])
    # Return the sorted list of repository names
    return [x[0] for x in repo_names]