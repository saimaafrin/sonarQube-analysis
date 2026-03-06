
import requests
import logging

def task_func(repo_url: str) -> dict:
    """
    Fetches and returns information about a GitHub repository using its API URL.
    """
    try:
        # Make an HTTP GET request to the provided repository URL
        response = requests.get(repo_url)

        # Check for API rate limit exceeded
        if response.status_code == 403:
            logging.warning("API rate limit exceeded")
            return None

        # Check for other HTTP errors
        if response.status_code != 200:
            logging.error("HTTP error: %s", response.status_code)
            return None

        # Check for general request issues
        if response.text == "":
            logging.error("Empty response")
            return None

        # Parse the response as JSON
        data = response.json()

        # Check for large number of open issues
        if len(data["open_issues"]) > 100:
            logging.warning("Large number of open issues: %d", len(data["open_issues"]))

        # Return the repository information
        return data

    except requests.exceptions.HTTPError as e:
        logging.error("HTTP error: %s", e)
        return None

    except requests.exceptions.RequestException as e:
        logging.error("Request error: %s", e)
        return None