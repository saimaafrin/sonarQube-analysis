
import mechanize
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def task_func(url):
    # Create a new mechanize browser object
    br = mechanize.Browser()

    # Set the base URL for the browser
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0')]
    br.open(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(br.response().read(), 'html.parser')

    # Find all hyperlinks on the page
    links = soup.find_all('a')

    # Create a list to store the hyperlinks
    hyperlinks = []

    # Iterate over the links and extract the href attribute
    for link in links:
        href = link.get('href')

        # Check if the href attribute is not None
        if href is not None:
            # Combine the base URL with the href attribute
            absolute_url = urljoin(url, href)

            # Add the absolute URL to the list of hyperlinks
            hyperlinks.append(absolute_url)

    # Return the list of hyperlinks
    return hyperlinks