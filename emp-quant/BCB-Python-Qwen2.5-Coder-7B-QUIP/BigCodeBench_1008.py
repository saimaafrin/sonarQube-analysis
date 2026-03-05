
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
from requests.exceptions import HTTPError

def task_func(url, table_id):
    try:
        # Send an HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful HTTP requests

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table with the specified ID
        table = soup.find('table', {'id': table_id})

        # Check if the table is found
        if table is None:
            raise ValueError("Table with the specified ID not found.")

        # Extract the table headers
        headers = [header.text.strip() for header in table.find_all('th')]

        # Extract the table rows
        rows = table.find_all('tr')

        # Check if there are any data rows
        if not rows:
            return pd.DataFrame(columns=headers)

        # Extract the data rows
        data = [[cell.text.strip() for cell in row.find_all('td')] for row in rows[1:]]

        # Create a DataFrame from the data
        df = pd.DataFrame(data, columns=headers)

        return df

    except HTTPError as e:
        raise HTTPError(f"HTTP error occurred: {e}")