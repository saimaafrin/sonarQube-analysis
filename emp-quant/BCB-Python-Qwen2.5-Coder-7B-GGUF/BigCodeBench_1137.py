
import bs4
import requests
import re
import json

def task_func(url: str, output_path: str) -> list:
    # Regular expression pattern to match phone numbers
    phone_pattern = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')

    # Fetch the content from the URL
    if url.startswith('http'):
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        content = response.text
    else:
        with open(url, 'r') as file:
            content = file.read()

    # Use BeautifulSoup to parse the HTML content
    soup = bs4.BeautifulSoup(content, 'html.parser')

    # Extract text from the parsed HTML
    text = soup.get_text()

    # Find all phone numbers in the text
    phone_numbers = phone_pattern.findall(text)

    # Save the phone numbers to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(phone_numbers, json_file, indent=4)

    return phone_numbers