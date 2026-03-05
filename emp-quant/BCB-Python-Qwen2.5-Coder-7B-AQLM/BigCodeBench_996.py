
import requests
import json
from bs4 import BeautifulSoup

def task_func(url: str, file_name: str = "Output.txt") -> str:
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the title of the page
        title = soup.title.string if soup.title else None

        # Create a dictionary to store the title
        data = {'title': title}

        # Open the file in append mode or create it if it doesn't exist
        with open(file_name, 'a') as file:
            # Convert the dictionary to a JSON string and write it to the file
            json.dump(data, file)
            file.write('\n')  # Append a newline character

        return file_name
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None