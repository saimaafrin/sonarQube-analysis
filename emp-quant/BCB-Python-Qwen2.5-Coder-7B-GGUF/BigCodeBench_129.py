
import requests
from bs4 import BeautifulSoup
import pandas as pd

def task_func(url='http://example.com'):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Raise an exception if the HTTP request fails
        response.raise_for_status()
    except requests.ConnectionError:
        raise ConnectionError("Failed to connect to the URL")
    except requests.HTTPError:
        raise requests.HTTPError("HTTP request failed with status code: {}".format(response.status_code))
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first table in the HTML
    table = soup.find('table')
    if not table:
        raise ValueError("No table found on the page")
    
    # Extract the headers from the table
    headers = [header.text.strip() for header in table.find_all('th')]
    
    # Extract the rows from the table
    rows = []
    for row in table.find_all('tr'):
        # Extract the data from each cell in the row
        cells = [cell.text.strip() for cell in row.find_all(['td', 'th'])]
        rows.append(cells)
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(rows, columns=headers)
    
    return df