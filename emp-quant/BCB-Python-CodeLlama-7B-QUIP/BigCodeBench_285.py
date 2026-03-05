
import mechanize
from bs4 import BeautifulSoup

def task_func(url, form_id, data):
    # Initialize the browser
    br = mechanize.Browser()

    # Navigate to the page
    br.open(url)

    # Find the form
    form = br.get_forms()[form_id]

    # Submit the form
    response = br.submit(form, data)

    # Parse the response page
    soup = BeautifulSoup(response, "html.parser")

    # Find the title of the page
    title = soup.title.string

    # Return the title
    return title