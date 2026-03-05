
import bs4
import requests
import re
import json

def task_func(url: str, output_path: str) -> list:
    # Function to extract phone numbers from a given URL or local file
    def extract_phone_numbers(text):
        # Regular expression to find phone numbers
        phone_regex = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')
        return re.findall(phone_regex, text)

    # Function to read text from URL or file
    def read_text(source):
        if source.startswith('http'):
            # Fetch text from URL
            response = requests.get(source)
            text = response.text
        else:
            # Read text from local file
            with open(source, 'r') as file:
                text = file.read()
        return text

    # Read text from the source
    text = read_text(url)

    # Extract phone numbers
    phone_numbers = extract_phone_numbers(text)

    # Save the list of phone numbers to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(phone_numbers, json_file, indent=4)

    # Return the list of phone numbers
    return phone_numbers