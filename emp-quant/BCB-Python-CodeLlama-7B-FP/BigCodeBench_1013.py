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
    # Send a request to the URL and get the HTML response
    response = requests.get(url)
    html = response.text

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Find all hyperlinks on the page
    links = soup.find_all("a")

    # Create a set to store the unique links
    unique_links = set()

    # Loop through each link and add it to the set
    for link in links:
        # Get the link URL
        link_url = link.get("href")

        # If the link is not None and is not already in the set, add it
        if link_url is not None and link_url not in unique_links:
            unique_links.add(link_url)

    # Join the base URL with each link to get the absolute URL
    absolute_links = [urljoin(base_url, link) for link in unique_links]

    # Write the absolute links to a CSV file
    with open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Link"])
        for link in absolute_links:
            writer.writerow([link])

    # Return the number of unique links scraped
    return len(unique_links)
url = "https://www.example.com"
base_url = "https://www.example.com"
csv_file = "scraped_data.csv"