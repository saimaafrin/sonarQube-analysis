
import requests
import logging

def task_func(repo_url: str) -> dict:
    # Set up logging
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger()

    # Function to check the number of open issues
    def check_open_issues(repo_url):
        response = requests.get(f"{repo_url}/issues")
        if response.status_code == 200:
            return response.json()
        else:
            logger.warning(f"Failed to fetch open issues: {response.status_code}")
            return None

    try:
        # Make the HTTP GET request to the repository URL
        response = requests.get(repo_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Check if the rate limit is exceeded
        if response.status_code == 403 and 'rate limit' in response.text:
            raise Exception("Rate limit exceeded")

        # Parse the JSON response
        repo_info = response.json()

        # Check the number of open issues
        open_issues = check_open_issues(repo_url)
        if open_issues and len(open_issues) > 100:
            logger.warning(f"Warning: Large number of open issues: {len(open_issues)}")

        return repo_info
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors
        logger.error(f"HTTP error occurred: {e}")
        raise
    except requests.exceptions.RequestException as e:
        # Handle other request exceptions
        logger.error(f"Request error occurred: {e}")
        raise