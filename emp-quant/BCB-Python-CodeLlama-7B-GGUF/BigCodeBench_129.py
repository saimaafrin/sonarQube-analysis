
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_table(url):
    """
    Scrape the first table from a web page and extract data into a Pandas DataFrame.

    Args:
        url (str): URL of the web page to scrape.

    Returns:
        pd.DataFrame: A DataFrame containing the scraped table data, with rows corresponding to table rows and
        columns named after the table headers, if available.

    Raises:
        ConnectionError: If there is an issue connecting to the URL.
        requests.HTTPError: If the HTTP request to the URL fails.
        ValueError: If no table data is found on the page or if the page content cannot be parsed.
    """
    try:
        response = requests.get(url)
    except requests.ConnectionError:
        raise ConnectionError(f"Error connecting to {url}")
    except requests.HTTPError:
        raise requests.HTTPError(f"HTTP error occurred while connecting to {url}")

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')

    if not table:
        raise ValueError(f"No table data found on {url}")

    headers = [th.text.strip() for th in table.find_all('th')]
    rows = [tr.find_all('td') for tr in table.find_all('tr')]

    df = pd.DataFrame(rows, columns=headers)

    return df