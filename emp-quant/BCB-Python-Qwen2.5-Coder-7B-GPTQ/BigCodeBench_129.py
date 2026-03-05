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

        # Find the first table in the parsed HTML
        table = soup.find('table')

        if not table:
            raise ValueError("No table data found on the page")

        # Extract the headers from the table
        headers = [header.text.strip() for header in table.find_all('th')]

        # Extract the rows from the table
        rows = []
        for row in table.find_all('tr'):
            cells = [cell.text.strip() for cell in row.find_all(['td', 'th'])]
            rows.append(cells)

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(rows, columns=headers)

        return df

    except ConnectionError as e:
        raise ConnectionError("Failed to connect to the URL") from e
    except requests.HTTPError as e:
        raise requests.HTTPError("HTTP request failed") from e
    except Exception as e:
        raise ValueError("An error occurred while parsing the page content") from e