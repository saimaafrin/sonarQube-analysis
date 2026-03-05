
import requests
from bs4 import BeautifulSoup
import pandas as pd

def task_func(url='http://example.com'):
    # Get the HTML content of the web page
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the first table on the page
        table = soup.find('table')
        if table is not None:
            # Get the table headers
            headers = [th.text.strip() for th in table.find('tr').findall('th')]
            # Get the table data
            data = [[td.text.strip() for td in tr.findall('td')] for tr in table.findall('tr')]
            # Create a DataFrame
            df = pd.DataFrame(data, columns=headers)
            return df
    else:
        raise requests.HTTPError('Could not connect to the URL')