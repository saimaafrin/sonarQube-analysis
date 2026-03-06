
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv

def task_func(url, base_url="https://www.example.com", csv_file="scraped_data.csv"):
    # Send a request to the URL and get the HTML response
    response = requests.get(url)
    html = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all the hyperlinks on the page
    links = soup.find_all("a")

    # Create a set to store the unique absolute URLs
    unique_links = set()

    # Loop through each link and extract the absolute URL
    for link in links:
        href = link.get("href")
        if href is not None:
            absolute_url = urljoin(base_url, href)
            unique_links.add(absolute_url)

    # Write the unique absolute URLs to a CSV file
    with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for link in unique_links:
            writer.writerow([link])

    # Return the number of unique absolute links scraped
    return len(unique_links)