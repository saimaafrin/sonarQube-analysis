
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv

def task_func(
    url: str,
    base_url: str = "https://www.example.com",
    csv_file: str = "scraped_data.csv",
) -> int:
    # Send a GET request to the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was unsuccessful

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the anchor tags
    links = soup.find_all('a', href=True)

    # Extract the absolute URLs
    absolute_links = [urljoin(base_url, link['href']) for link in links if 'href' in link]

    # Write the absolute URLs to a CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Absolute URL'])
        writer.writerows([[link] for link in absolute_links])

    # Return the number of unique absolute links
    return len(set(absolute_links))