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
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all hyperlinks on the page
    links = soup.find_all('a')
    # Set to store unique absolute URLs
    unique_links = set()
    
    # Iterate over all links
    for link in links:
        href = link.get('href')
        # Join the href with the base URL to get an absolute URL
        absolute_url = urljoin(base_url, href)
        # Add the absolute URL to the set of unique links
        unique_links.add(absolute_url)
    
    # Write the unique absolute links to a CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for link in unique_links:
            writer.writerow([link])
    
    # Return the number of unique absolute links
    return len(unique_links)