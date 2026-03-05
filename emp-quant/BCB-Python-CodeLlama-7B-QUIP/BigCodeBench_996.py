
import requests
import json
from bs4 import BeautifulSoup

def task_func(url: str, file_name: str = "Output.txt") -> str:
    # Get the HTML content of the web page
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Get the title of the web page
        title = soup.title.string if soup.title else "None"

        # Create a JSON object with the title
        json_data = {
            "title": title
        }

        # Open the file in append mode if it exists
        with open(file_name, "a") as f:
            # Write the JSON data to the file
            f.write(json.dumps(json_data) + "\n")

        # Return the file path where the scraped title is saved
        return file_name
    else:
        raise Exception("Could not retrieve the web page")