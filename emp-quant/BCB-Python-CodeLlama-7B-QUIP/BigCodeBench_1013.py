
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv

def task_func(url, base_url="https://www.example.com", csv_file="scraped_data.csv"):
    # Create a BeautifulSoup object from the webpage
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    # Create a list to store the unique absolute links
    links = set()

    # Iterate over the links in the webpage
    for link in soup.find_all("a"):
        # Get the absolute URL of the link
        absolute_url = urljoin(base_url, link.get("href"))

        # Add the absolute URL to the list of unique links
        links.add(absolute_url)

    # Write the unique absolute links to a CSV file
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(links)

    return len(links)