
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def task_func(url, table_id):
    # Send an HTTP request to the specified URL
    response = requests.get(url)

    # Check if the HTTP request was successful
    if response.status_code != 200:
        raise requests.exceptions.HTTPError(f"HTTP request failed with status code {response.status_code}")

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the specified ID
    table = soup.find('table', {'id': table_id})

    # Check if the table was found
    if table is None:
        raise ValueError(f"Table with ID '{table_id}' not found on webpage")

    # Extract the data from the table
    data = []
    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text.strip())
        data.append(row_data)

    # Create a Pandas DataFrame from the data
    df = pd.DataFrame(data, columns=['Column 1', 'Column 2', 'Column 3'])

    # Return the DataFrame
    return df