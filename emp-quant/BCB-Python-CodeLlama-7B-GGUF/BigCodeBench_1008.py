
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def task_func(url, table_id):
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        raise requests.exceptions.HTTPError(f"HTTP request failed with status code {response.status_code}")

    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table with the specified ID
    table = soup.find('table', attrs={'id': table_id})

    # Check if the table was found
    if table is None:
        raise ValueError(f"Table with ID '{table_id}' not found on webpage")

    # Extract the table data into a list of lists
    table_data = []
    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text.strip())
        table_data.append(row_data)

    # Convert the list of lists into a Pandas DataFrame
    df = pd.read_csv(StringIO(str(table_data)), header=None)

    # Return the DataFrame
    return df