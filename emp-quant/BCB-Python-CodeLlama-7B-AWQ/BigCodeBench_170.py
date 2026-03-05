import pandas as pd
import requests
from io import StringIO
def task_func(csv_url, sort_by_column="title"):
    """
    Fetches data from a given CSV URL and returns a pandas DataFrame sorted based on the specified column.

    Parameters
    ----------
    csv_url : str
        The URL of the CSV file to fetch.
    sort_by_column : str, optional
        The column to sort the DataFrame by. Defaults to "title".

    Returns
    -------
    DataFrame
        The pandas DataFrame that sorted based on the specified column.

    Raises
    ------
    Exception
        If the response status code is not 200.
    """
    # Fetch the CSV file
    response = requests.get(csv_url)

    # Check the response status code
    if response.status_code != 200:
        raise Exception(f"Failed to fetch CSV file from {csv_url}. Status code: {response.status_code}")

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(StringIO(response.text))

    # Sort the DataFrame by the specified column
    df = df.sort_values(by=sort_by_column)

    return df
csv_url = "http://example.com/data.csv"
sort_by_column = "price"