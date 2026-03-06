
import requests
from bs4 import BeautifulSoup
import pandas as pd

def task_func(url='http://example.com'):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        raise ConnectionError("Error connecting to URL: {}".format(url))

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the first table on the page
    table = soup.find('table')

    # Check if a table was found
    if table is None:
        raise ValueError("No table data found on page: {}".format(url))

    # Extract the table data into a list of lists
    table_data = []
    for row in table.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text.strip())
        table_data.append(row_data)

    # Create a DataFrame from the table data
    df = pd.DataFrame(table_data, columns=table.find_all('th'))

    # Return the DataFrame
    return df