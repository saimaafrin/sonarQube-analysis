
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

    headers = [header.text for header in table.find_all('th')]
    rows = table.find_all('tr')

    if not rows:
        return pd.DataFrame(columns=headers)

    data = []
    for row in rows[1:]:  # Skip the header row
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Filter out any empty values

    df = pd.DataFrame(data, columns=headers)
    return df