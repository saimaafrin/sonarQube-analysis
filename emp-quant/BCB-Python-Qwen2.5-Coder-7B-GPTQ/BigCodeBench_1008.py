import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
def task_func(url, table_id):
    try:
        # Send HTTP request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful HTTP requests

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table by its ID
        table = soup.find('table', {'id': table_id})

        if not table:
            raise ValueError("Table with the specified ID not found.")

        # Extract the headers from the table
        headers = [header.text.strip() for header in table.find_all('th')]

        # Extract the rows from the table
        rows = []
        for row in table.find_all('tr'):
            cols = row.find_all(['td', 'th'])
            cols = [ele.text.strip() for ele in cols]
            rows.append([ele for ele in cols if ele])

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(rows, columns=headers)

        return df

    except requests.exceptions.HTTPError as e:
        raise e
    except ValueError as e:
        raise e