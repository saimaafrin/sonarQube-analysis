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
    table = soup.find('table')
    
    if not table:
        raise ValueError("No table found on the page")
    
    headers = [header.text for header in table.find_all('th')]
    rows = table.find_all('tr')
    data = []
    
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Remove empty values
    
    if headers:
        df = pd.DataFrame(data, columns=headers)
    else:
        df = pd.DataFrame(data)
    
    return df