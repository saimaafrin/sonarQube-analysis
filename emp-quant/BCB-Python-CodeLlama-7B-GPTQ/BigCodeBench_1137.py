import bs4
import requests
import re
import json
def task_func(url: str, output_path: str) -> list:
    """
    Extracts phone numbers from a given URL or local file and saves them to a specified file in JSON format.
    """
    # Get the HTML content of the URL or file
    if url:
        response = requests.get(url)
    else:
        with open(url, 'r') as f:
            response = f.read()

    # Use BeautifulSoup to parse the HTML content
    soup = bs4.BeautifulSoup(response, 'html.parser')

    # Find all phone numbers in the HTML content
    phone_numbers = []
    for phone_number in soup.find_all('span', {'class': 'phone-number'}):
        phone_numbers.append(phone_number.text.strip())

    # Save the phone numbers to a JSON file
    with open(output_path, 'w') as f:
        json.dump(phone_numbers, f)

    return phone_numbers
url = 'https://www.example.com'
output_path = 'phone_numbers.json'