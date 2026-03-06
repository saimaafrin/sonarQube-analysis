
import requests
import json
from bs4 import BeautifulSoup

def task_func(url: str, file_name: str = "Output.txt") -> str:
    # Send a request to the specified URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title element in the HTML
    title_element = soup.find('title')

    # If the title element is found, extract the text content
    if title_element:
        title = title_element.text.strip()
    else:
        title = None

    # Create a JSON object with the title and save it to the file
    json_data = {'title': title}
    with open(file_name, 'a') as f:
        json.dump(json_data, f)

    # Return the file path where the data was saved
    return file_name