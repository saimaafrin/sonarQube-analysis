import pandas as pd
import requests
from io import StringIO
def task_func(csv_url, sort_by_column="title"):
    """
    Fetches data from a given CSV URL and returns a pandas DataFrame sorted based on the specified column.

    Args:
        csv_url (str): The URL of the CSV file.
        sort_by_column (str, optional): The column to sort the DataFrame by. Defaults to "title".

    Returns:
        pandas.DataFrame: The sorted pandas DataFrame.

    Raises:
        Exception: If the response status code is not 200.
    """
    response = requests.get(csv_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from {csv_url}.")
    data = StringIO(response.text)
    df = pd.read_csv(data)
    return df.sort_values(by=sort_by_column)