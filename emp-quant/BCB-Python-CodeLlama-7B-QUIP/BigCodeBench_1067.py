
import requests
import logging

def task_func(repo_url: str) -> dict:
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Fetching information for repository: {repo_url}")
    try:
        response = requests.get(repo_url)
        if response.status_code == 200:
            repo_info = response.json()
            logging.info(f"Successfully fetched information for repository: {repo_url}")
            return repo_info
        else:
            logging.error(f"Failed to fetch information for repository: {repo_url}")
            raise requests.exceptions.HTTPError(f"Failed to fetch information for repository: {repo_url}")
    except requests.exceptions.HTTPError as e:
        logging.error(f"Failed to fetch information for repository: {repo_url}")
        raise e
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch information for repository: {repo_url}")
        raise e
    except Exception as e:
        logging.error(f"Failed to fetch information for repository: {repo_url}")
        raise e