
import mechanize
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def task_func(url):
    # Create a new mechanize browser object
    br = mechanize.Browser()

    # Set the base URL
    base_url = url

    # Navigate to the URL
    br.open(base_url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(br.response().read(), 'html.parser')

    # Find all hyperlinks on the page
    links = soup.find_all('a')

    # Create a list to store the hyperlinks
    hyperlinks = []

    # Iterate over the links and extract the href attributes
    for link in links:
        # Get the href attribute
        href = link.get('href')

        # Check if the href attribute is not empty
        if href:
            # Combine the base URL with the href attribute
            absolute_url = urljoin(base_url, href)

            # Add the absolute URL to the list of hyperlinks
            hyperlinks.append(absolute_url)

    # Return the list of hyperlinks
    return hyperlinks