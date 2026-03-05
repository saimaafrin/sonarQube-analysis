import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import csv
def task_func(
    url: str,
    base_url: str = "https://www.example.com",
    csv_file: str = "scraped_data.csv",
) -> int:
    """
    Scrapes a webpage for all hyperlinks and saves them as absolute URLs to a CSV file.

    Args:
        url (str): The URL of the webpage to scrape.
        base_url (str, optional): The base URL to use for relative links. Defaults to "https://www.example.com".
        csv_file (str, optional): The file path to save the scraped data to. Defaults to "scraped_data.csv".

    Returns:
        int: The number of unique absolute links scraped from the webpage.
    """
    # Send a request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all hyperlinks on the page
    links = soup.find_all("a")

    # Create a set to store unique links
    unique_links = set()

    # Loop through each link and add it to the set
    for link in links:
        # Get the absolute URL of the link
        absolute_url = urljoin(base_url, link.get("href"))

        # Add the link to the set
        unique_links.add(absolute_url)

    # Write the unique links to a CSV file
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for link in unique_links:
            writer.writerow([link])

    # Return the number of unique links scraped
    return len(unique_links)
url = "https://www.example.com"
base_url = "https://www.example.com"
csv_file = "scraped_data.csv"