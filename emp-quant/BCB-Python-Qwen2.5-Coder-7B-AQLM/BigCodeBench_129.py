
import requests
from bs4 import BeautifulSoup
import pandas as pd

def task_func(url='http://example.com'):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.ConnectionError:
        raise ConnectionError("Failed to connect to the URL")
    except requests.HTTPError as e:
        raise requests.HTTPError(f"HTTP error occurred: {e}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    
    if not tables:
        raise ValueError("No table data found on the page")
    
    table = tables[0]
    headers = [header.text.strip() for header in table.find_all('th')]
    rows = []
    
    for row in table.find_all('tr'):
        cells = row.find_all(['td', 'th'])
        rows.append([cell.text.strip() for cell in cells])
    
    if headers:
        df = pd.DataFrame(rows, columns=headers)
    else:
        df = pd.DataFrame(rows)
    
    return df