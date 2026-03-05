
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def task_func(url, table_id):
    # Make an HTTP request to the specified URL
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError(f"HTTP request failed with status {response.status_code}")

    # Parse the HTML content of the response with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table with the specified ID
    table = soup.find("table", {"id": table_id})
    if table is None:
        raise ValueError(f"Table with ID {table_id} not found")

    # Extract the data from the table
    rows = table.find_all("tr")
    if len(rows) == 0:
        return pd.DataFrame()

    # Create a DataFrame from the extracted data
    df = pd.read_html(StringIO(str(rows)))

    return df