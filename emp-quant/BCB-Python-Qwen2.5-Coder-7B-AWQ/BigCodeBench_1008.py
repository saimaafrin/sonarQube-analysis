import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
def task_func(url, table_id):
    try:
        # Send HTTP request to the URL
        response = requests.get(url)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Raise a ValueError with a custom message if the table is not found
        raise ValueError("Table with the specified ID not found.") from e

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the table by its ID
    table = soup.find('table', {'id': table_id})

    # Check if the table exists
    if not table:
        raise ValueError("Table with the specified ID not found.")

    # Extract the headers from the table
    headers = [header.text for header in table.find_all('th')]
    # Extract the rows from the table
    rows = table.find_all('tr')

    # Check if there are any data rows
    if not rows:
        return pd.DataFrame(columns=headers)

    # Extract the data from the rows
    data = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all(['td', 'th'])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=headers)
    return df