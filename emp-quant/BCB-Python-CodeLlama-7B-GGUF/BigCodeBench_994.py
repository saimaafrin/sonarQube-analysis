
import requests
import pandas as pd
from bs4 import BeautifulSoup

def task_func(url: str, csv_file_path: str) -> list:
    """
    Extracts title, date, and author information from a webpage and writes the data to a CSV file.

    Args:
        url (str): URL of the webpage to extract data from.
        csv_file_path (str): Path to the CSV file to write the extracted data to.

    Returns:
        list: A list of tuples containing the (title, date, author) extracted from the webpage.
            Default placeholders are used for missing information.

    Raises:
        RuntimeError: If the URL is incorrect or the server is down.
    """
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')

        containers = soup.find_all('div', {'class': 'container'})
        data = []
        for container in containers:
            title = container.find('h1').text.strip() or 'No Title'
            date = container.find('span', {'class': 'date'}).text.strip() or 'No Date'
            author = container.find('span', {'class': 'author'}).text.strip() or 'No Author'
            data.append((title, date, author))

        df = pd.DataFrame(data, columns=['Title', 'Date', 'Author'])
        df.to_csv(csv_file_path, index=False)

        return data
    except requests.RequestException as e:
        raise RuntimeError(f'Error fetching URL: {e}') from e