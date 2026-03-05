
import requests
import logging

def task_func(repo_url: str) -> dict:
    """
    Fetches and returns information about a GitHub repository using its API URL.

    Parameters
    ----------
    repo_url : str
        The API URL of the GitHub repository.

    Returns
    -------
    dict
        A dictionary containing information about the GitHub repository.

    Raises
    ------
    requests.exceptions.HTTPError
        If an HTTP error occurs, particularly when the GitHub API rate limit is exceeded.
    requests.exceptions.RequestException
        For other general issues encountered during the API request, such as network problems, invalid responses, or timeouts.
    """
    try:
        response = requests.get(repo_url)
        response.raise_for_status()
        data = response.json()
        if data["open_issues"] > 100:
            logging.warning(f"Repository {repo_url} has {data['open_issues']} open issues.")
        return data
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP error occurred while fetching repository information: {e}")
        raise
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error occurred while fetching repository information: {e}")
        raise