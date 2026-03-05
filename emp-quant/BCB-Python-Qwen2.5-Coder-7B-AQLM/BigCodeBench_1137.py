
import bs4
import requests
import re
import json

def task_func(url: str, output_path: str) -> list:
    # Function to extract phone numbers from a given URL or local file
    def extract_phone_numbers(text):
        phone_regex = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')
        return phone_regex.findall(text)

    # Function to fetch text from a URL
    def fetch_text_from_url(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    # Function to fetch text from a local file
    def fetch_text_from_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    # Fetch text based on the URL type
    if url.startswith('http'):
        text = fetch_text_from_url(url)
    else:
        text = fetch_text_from_file(url)

    # Extract phone numbers
    phone_numbers = extract_phone_numbers(text)

    # Save phone numbers to a JSON file
    with open(output_path, 'w') as json_file:
        json.dump(phone_numbers, json_file)

    return phone_numbers