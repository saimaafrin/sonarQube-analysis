
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv

def task_func(url, base_url="https://www.example.com", csv_file="scraped_data.csv"):
    # Send a request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all hyperlinks on the page
    links = soup.find_all("a")

    # Create a set to store unique links
    unique_links = set()

    # Iterate over the links and extract the absolute URL
    for link in links:
        href = link.get("href")
        if href:
            absolute_url = urljoin(base_url, href)
            unique_links.add(absolute_url)

    # Write the unique links to a CSV file
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for link in unique_links:
            writer.writerow([link])

    # Return the number of unique links scraped
    return len(unique_links)