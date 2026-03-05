
import requests
from bs4 import BeautifulSoup
import pandas as pd

def task_func(url='http://example.com'):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the first table in the HTML
        table = soup.find('table')

        # Check if a table was found
        if not table:
            raise ValueError("No table data found on the page")

        # Extract the headers and data from the table
        headers = [header.text.strip() for header in table.find('tr').find_all('th')]
        data = []
        for row in table.find_all('tr')[1:]:
            data.append([cell.text.strip() for cell in row.find_all('td')])

        # Create a DataFrame from the data
        df = pd.DataFrame(data, columns=headers)

        return df

    except requests.ConnectionError as e:
        raise ConnectionError(f"Connection error: {e}")
    except requests.HTTPError as e:
        raise HTTPError(f"HTTP error: {e}")
    except ValueError as e:
        raise ValueError(f"Value error: {e}")