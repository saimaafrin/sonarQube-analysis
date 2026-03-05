import collections
import json
import requests
def task_func(user, API_URL = 'https://api.github.com/users/'):
    """
    Retrieves the names of the repositories of a specified GitHub user, sorted in ascending order by their creation date.
    The function queries the GitHub API for all repositories of a given user, parses the response to extract the names and creation dates, and returns the repository names sorted by the date they were created.
    """
    # Query the GitHub API for the user's repositories
    response = requests.get(API_URL + user + '/repos')
    # Parse the response as JSON
    repos = json.loads(response.content)
    # Extract the repository names and creation dates
    names = [repo['name'] for repo in repos]
    dates = [repo['created_at'] for repo in repos]
    # Sort the repository names by their creation dates
    sorted_names = sorted(names, key=lambda x: dates[names.index(x)])
    return sorted_names
user = 'octocat'