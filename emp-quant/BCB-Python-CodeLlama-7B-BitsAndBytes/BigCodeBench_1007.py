
import requests
import pandas as pd

def task_func(url: str) -> pd.DataFrame:
    """
    Fetches JSON data from a specified URL and converts it into a Pandas DataFrame.

    Parameters
    ----------
    url : str
        The URL to fetch the JSON data from.

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
        # Send a GET request to the URL with a 5-second timeout
        response = requests.get(url, timeout=5)

        # Check the HTTP response status and raise an HTTPError for unsuccessful status codes
        response.raise_for_status()

        # Directly convert the HTTP response to JSON and then to a DataFrame, without intermediate processing
        data = response.json()
        df = pd.DataFrame(data)

        return df
    except requests.RequestException as e:
        # Re-raise the exception with a more specific error message
        raise SystemError(f"Network error: {e}")
    except ValueError as e:
        # Raise a ValueError with a more specific error message
        raise ValueError(f"Invalid JSON format: {e}")