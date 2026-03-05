import bs4
import requests
import re
import json
def task_func(url: str, output_path: str) -> list:
    """
    Extracts phone numbers from a given URL or local file and saves them to a specified file in JSON format.

    Args:
        url (str): The URL or local file path to extract phone numbers from.
        output_path (str): The path to save the extracted phone numbers to.

    Returns:
        list: A list of strings, each representing a found phone number.
    """
    # Check if the input is a URL or a local file path
    if url.startswith('http'):
        # Download the HTML content from the URL
        response = requests.get(url)
        html = response.content
    else:
        # Open the local file
        with open(url, 'r') as f:
            html = f.read()

    # Create a BeautifulSoup object from the HTML content
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Find all phone numbers in the HTML content
    phone_numbers = soup.find_all('span', {'class': 'phone-number'})

    # Extract the phone numbers from the HTML content
    extracted_phone_numbers = []
    for phone_number in phone_numbers:
        extracted_phone_numbers.append(phone_number.text.strip())

    # Save the extracted phone numbers to a JSON file
    with open(output_path, 'w') as f:
        json.dump(extracted_phone_numbers, f)

    return extracted_phone_numbers
url = 'https://www.example.com'
output_path = 'phone_numbers.json'