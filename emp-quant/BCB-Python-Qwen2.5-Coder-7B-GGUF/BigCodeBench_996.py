
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
        
        # Get the text of the title tag or None if it doesn't exist
        title = title_tag.text if title_tag else None
        
        # Create a dictionary with the title
        data = {'title': title}
        
        # Open the file in append mode
        with open(file_name, 'a') as file:
            # Convert the dictionary to a JSON string and write it to the file
            json.dump(data, file)
            file.write('\n')  # Append a newline character for each title
    
    # Return the file path where the scraped title is saved
    return file_name