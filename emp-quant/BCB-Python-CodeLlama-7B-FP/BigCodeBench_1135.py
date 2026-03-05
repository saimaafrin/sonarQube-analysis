import collections
import json
import requests
def task_func(user, API_URL = 'https://api.github.com/users/'):
    """
    Retrieves the names of the repositories of a specified GitHub user, sorted in ascending order by their creation date.
    The function queries the GitHub API for all repositories of a given user, parses the response to extract the names and creation dates, and returns the repository names sorted by the date they were created.
    """
    # Query the GitHub API for all repositories of the specified user
    response = requests.get(API_URL + user)
    # Parse the response to extract the repository names and creation dates
    data = json.loads(response.text)
    repositories = data['repositories']
    repository_names = [repository['name'] for repository in repositories]
    repository_creation_dates = [repository['created_at'] for repository in repositories]
    # Sort the repository names and creation dates by the creation dates
    sorted_repository_names = sorted(repository_names, key=lambda x: repository_creation_dates[repository_names.index(x)])
    # Return the sorted repository names
    return sorted_repository_names
user = 'octocat'