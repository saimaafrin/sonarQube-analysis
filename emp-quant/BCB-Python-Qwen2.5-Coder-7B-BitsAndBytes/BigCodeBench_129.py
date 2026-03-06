
import requests
from bs4 import BeautifulSoup
import pandas as pd

def task_func(url='http://example.com'):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Raise an exception if the HTTP request failed
        response.raise_for_status()
        
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the first table in the parsed HTML
        table = soup.find('table')
        
        # Check if a table was found
        if not table:
            raise ValueError("No table data found on the page.")
        
        # Extract the headers from the table
        headers = [header.text.strip() for header in table.find_all('th')]
        
        # Extract the rows from the table
        rows = []
        for row in table.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            rows.append([cell.text.strip() for cell in cells])
        
        # Create a DataFrame from the extracted data
        df = pd.DataFrame(rows[1:], columns=headers if headers else None)
        
        return df
    
    except requests.ConnectionError as e:
        raise ConnectionError(f"Failed to connect to {url}: {e}")
    
    except requests.HTTPError as e:
        raise requests.HTTPError(f"HTTP error occurred while fetching {url}: {e}")
    
    except Exception as e:
        raise ValueError(f"An unexpected error occurred: {e}")