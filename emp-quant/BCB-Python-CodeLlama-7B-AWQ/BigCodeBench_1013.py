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
        csv_file (str, optional): The path to the CSV file to write the scraped links to. Defaults to "scraped_data.csv".

    Returns:
        int: The number of unique absolute links scraped from the webpage.
    """
    # Send a request to the webpage
    response = requests.get(url)

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, "html.parser")

    # Create a set to store the unique links
    links = set()

    # Iterate over all links on the webpage
    for link in soup.find_all("a"):
        # Get the absolute URL of the link
        link_url = urljoin(base_url, link.get("href"))

        # Add the link to the set
        links.add(link_url)

    # Open the CSV file in write mode
    with open(csv_file, "w", newline="") as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(["Link"])

        # Write each link to the CSV file
        for link in links:
            csv_writer.writerow([link])

    # Return the number of unique links scraped
    return len(links)