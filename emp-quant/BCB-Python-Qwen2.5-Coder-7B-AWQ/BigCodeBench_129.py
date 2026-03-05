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
    except requests.HTTPError as e:
        raise HTTPError(f"HTTP error occurred: {e}")
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first table in the parsed HTML
    table = soup.find('table')
    
    # Raise an exception if no table is found
    if not table:
        raise ValueError("No table found on the page")
    
    # Extract the headers from the table
    headers = [header.text for header in table.find('tr').find_all('th')]
    
    # Extract the data from the table rows
    data = []
    for row in table.find_all('tr')[1:]:
        row_data = [cell.text for cell in row.find_all(['td', 'th'])]
        data.append(row_data)
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data, columns=headers)
    
    return df