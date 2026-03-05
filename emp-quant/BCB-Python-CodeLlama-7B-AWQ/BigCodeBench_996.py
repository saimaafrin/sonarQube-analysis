import requests
import json
from bs4 import BeautifulSoup
def task_func(url: str, file_name: str = "Output.txt") -> str:
    """
    Scrape the 'title' from a specified web page, save it in JSON format to a given file, and append to the file if it exists.
    """
    # Send a request to the specified URL
    response = requests.get(url)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the title from the HTML content
    title = soup.title.string

    # If the title is not found, set it to None
    if title is None:
        title = 'None'

    # Convert the title to JSON format
    json_title = json.dumps(title)

    # Open the file in append mode if it exists, otherwise create a new file
    with open(file_name, 'a') as f:
        # Write the JSON title to the file
        f.write(json_title + '\n')

    # Return the file path where the scraped title is saved
    return file_name
url = 'https://www.example.com'
file_name = 'Output.txt'