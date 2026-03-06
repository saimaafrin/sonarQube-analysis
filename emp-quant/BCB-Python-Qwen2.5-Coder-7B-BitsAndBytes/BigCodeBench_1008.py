
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def task_func(url, table_id):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.exceptions.HTTPError as e:
        raise e

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': table_id})

    if not table:
        raise ValueError("Table with the specified ID not found.")

    headers = [header.text.strip() for header in table.find_all('th')]
    rows = table.find_all('tr')[1:]  # Skip the header row

    data = []
    for row in rows:
        cols = row.find_all(['td', 'th'])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Remove empty strings

    if not data:
        return pd.DataFrame(columns=headers)

    return pd.read_csv(StringIO('\n'.join([','.join(row) for row in data])), names=headers)