
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
    
    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all anchor tags
    links = soup.find_all('a', href=True)
    
    # Extract absolute URLs
    absolute_links = set()
    for link in links:
        absolute_link = urljoin(base_url, link['href'])
        absolute_links.add(absolute_link)
    
    # Save the absolute links to a CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for link in absolute_links:
            writer.writerow([link])
    
    # Return the number of unique absolute links
    return len(absolute_links)