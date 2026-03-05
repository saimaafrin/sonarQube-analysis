import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
def task_func(url, table_id):
    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        # Re-raise the exception with a custom message
        raise ValueError(f"HTTP error occurred: {e}")

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the table with the specified ID
    table = soup.find('table', {'id': table_id})

    if not table:
        # Raise an error if no table with the specified ID is found
        raise ValueError("Table with the specified ID not found.")

    # Extract the headers from the table
    headers = [header.text for header in table.find_all('th')]
    # Extract the rows from the table
    rows = table.find_all('tr')

    # Check if there are any data rows in the table
    if not rows:
        # Return an empty DataFrame if no data rows are found
        return pd.DataFrame(columns=headers)

    # Extract the data from the rows
    data = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all(['td', 'th'])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Remove empty values

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data, columns=headers)
    return df