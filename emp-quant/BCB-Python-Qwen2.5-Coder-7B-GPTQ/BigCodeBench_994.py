import requests
import pandas as pd
from bs4 import BeautifulSoup
def task_func(url: str, csv_file_path: str) -> list:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises an HTTPError for bad responses
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching URL: {e}")

    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    for container in soup.find_all('div', class_='container'):
        title = container.find('h1').text.strip() if container.find('h1') else 'No Title'
        date = container.find('span', class_='date').text.strip() if container.find('span', class_='date') else 'No Date'
        author = container.find('span', class_='author').text.strip() if container.find('span', class_='author') else 'No Author'
        data.append((title, date, author))

    df = pd.DataFrame(data, columns=['Title', 'Date', 'Author'])
    df.to_csv(csv_file_path, index=False)

    return data