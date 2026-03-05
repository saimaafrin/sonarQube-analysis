import requests
import json
from bs4 import BeautifulSoup
def task_func(url: str, file_name: str = "Output.txt") -> str:
    # Send a GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the title tag
        title_tag = soup.find('title')
        
        # Extract the text from the title tag, or use 'None' if not found
        title = title_tag.text if title_tag else 'None'
        
        # Create a dictionary to store the title
        data = {'title': title}
        
        # Open the file in append mode
        with open(file_name, 'a') as file:
            # Convert the dictionary to a JSON string and write to the file
            json.dump(data, file)
            file.write('\n')  # Add a new line after each entry
        
        # Return the file path
        return file_name
    else:
        # Return an error message if the request was not successful
        return f"Failed to retrieve the webpage. Status code: {response.status_code}"