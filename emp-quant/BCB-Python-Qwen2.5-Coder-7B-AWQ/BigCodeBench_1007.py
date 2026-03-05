import requests
import pandas as pd
from requests.exceptions import RequestException
def task_func(url: str) -> pd.DataFrame:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        json_data = response.json()
        return pd.DataFrame(json_data)
    except RequestException as e:
        raise SystemError(f"Network error: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid JSON format: {e}")
url = "https://api.example.com/data"