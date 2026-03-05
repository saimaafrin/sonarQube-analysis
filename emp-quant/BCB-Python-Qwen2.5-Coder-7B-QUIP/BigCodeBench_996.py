
import requests
import json
from bs4 import BeautifulSoup

def task_func(url: str, file_name: str = "Output.txt") -> str:
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the title tag
        title_tag = soup.find('title')
        # Get the text of the title tag, or 'None' if it doesn't exist
        title = title_tag.text.strip() if title_tag else 'None'
        # Create a dictionary with the title
        data = {'title': title}
        # Open the file in append mode
        with open(file_name, 'a') as f:
            # Write the JSON data to the file
            f.write(json.dumps(data) + '\n')
        # Return the file path
        return file_name
    else:
        # Return None if the request was not successful
        return None