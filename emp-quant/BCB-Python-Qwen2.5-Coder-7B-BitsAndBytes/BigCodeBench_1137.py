
import bs4
import requests
import re
import json

def extract_phone_numbers(text):
    # Regular expression pattern for matching phone numbers
    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    return re.findall(phone_pattern, text)

def task_func(url: str, output_path: str) -> list:
    if url.startswith('http'):
        # Fetch content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        text = response.text
    else:
        # Read content from the local file
        with open(url, 'r') as file:
            text = file.read()
    
    # Extract phone numbers
    phone_numbers = extract_phone_numbers(text)
    
    # Save phone numbers to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(phone_numbers, json_file, indent=4)
    
    return phone_numbers