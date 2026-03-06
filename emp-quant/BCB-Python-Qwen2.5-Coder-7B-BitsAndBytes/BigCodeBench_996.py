
import requests
import json
from bs4 import BeautifulSoup

def task_func(url: str, file_name: str = "Output.txt") -> str:
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the title tag
        title_tag = soup.find('title')
        
        # Get the text of the title or None if no title tag is found
        title = title_tag.string if title_tag else None
        
        # Create a dictionary to store the title
        data = {'title': title}
        
        # Open the file in append mode
        with open(file_name, 'a') as file:
            # Convert the dictionary to a JSON string and write to the file
            json.dump(data, file)
            file.write('\n')  # Add a newline for the next entry
        
        # Return the file path
        return file_name
    else:
        raise Exception(f"Failed to retrieve the webpage. Status code: {response.status_code}")