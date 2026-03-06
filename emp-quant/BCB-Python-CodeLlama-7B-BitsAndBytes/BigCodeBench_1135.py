
import collections
import json
import requests

def task_func(user, API_URL = 'https://api.github.com/users/'):
    # Query the GitHub API for the user's repositories
    response = requests.get(API_URL + user + '/repos')
    # Parse the response as JSON
    data = json.loads(response.text)
    # Extract the repository names and creation dates
    repos = [repo['name'] for repo in data]
    dates = [repo['created_at'] for repo in data]
    # Sort the repositories by creation date
    sorted_repos = sorted(repos, key=lambda x: dates[repos.index(x)])
    # Return the sorted repository names
    return sorted_repos