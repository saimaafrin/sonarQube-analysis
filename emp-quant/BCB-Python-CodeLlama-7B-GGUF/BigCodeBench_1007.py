
import requests
import pandas as pd

def fetch_json_data(url: str) -> pd.DataFrame:
    """
    Fetches JSON data from a specified URL and converts it into a Pandas DataFrame.

    Parameters
    ----------
    url : str
        The URL from which to fetch the JSON data.

    Returns
    -------
    pd.DataFrame
        A DataFrame constructed from the JSON data fetched from the URL.

    Raises
    ------
    SystemError
        If there is a network-related issue such as a connection error, timeout, or if the server responded with an unsuccessful status code (like 404 or 500).
    ValueError
        If the fetched data is not in a valid JSON format that can be converted into a DataFrame.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        return df
    except requests.RequestException as e:
        raise SystemError(f"Network error: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid JSON format: {e}")