import collections
import json
import requests
def task_func(user, API_URL = 'https://api.github.com/users/'):
    """Retrieves the names of the repositories of a specified GitHub user, sorted in ascending order by their creation date.

    Args:
        user (str): The GitHub username of the user whose repositories to retrieve.
        API_URL (str, optional): The base URL of the GitHub API. Defaults to 'https://api.github.com/users/'.

    Returns:
        list of str: A list of repository names, sorted by their creation dates from oldest to newest.
    """
    # Query the GitHub API for all repositories of the specified user
    response = requests.get(f'{API_URL}{user}/repos')
    # Parse the response to extract the names and creation dates of the repositories
    repos = json.loads(response.content)
    # Create a list of tuples containing the repository names and creation dates
    repo_data = [(repo['name'], repo['created_at']) for repo in repos]
    # Sort the list of tuples by the creation dates
    sorted_repos = sorted(repo_data, key=lambda x: x[1])
    # Return the sorted list of repository names
    return [repo[0] for repo in sorted_repos]
user = 'octocat'