
import requests
import json
from bs4 import BeautifulSoup

def task_func(url: str, file_name: str = "Output.txt") -> str:
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the title tag in the HTML content
    title_tag = soup.find("title")

    # Extract the title text from the title tag
    title = title_tag.text.strip() if title_tag else None

    # Create a JSON object with the title and URL
    json_data = {"title": title, "url": url}

    # Open the file in append mode if it exists, or create a new file if it doesn't
    with open(file_name, "a") as f:
        # Write the JSON data to the file
        f.write(json.dumps(json_data) + "\n")

    # Return the file path where the scraped title is saved
    return file_name