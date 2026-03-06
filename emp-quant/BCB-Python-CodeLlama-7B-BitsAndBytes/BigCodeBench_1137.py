
import bs4
import requests
import re
import json

def task_func(url: str, output_path: str) -> list:
    # Make a request to the URL and get the HTML response
    response = requests.get(url)
    html = response.content

    # Parse the HTML content using BeautifulSoup
    soup = bs4.BeautifulSoup(html, 'html.parser')

    # Find all the phone numbers in the HTML content
    phone_numbers = soup.find_all('span', {'class': 'phone-number'})

    # Extract the phone numbers from the HTML elements
    phone_numbers = [phone_number.text.strip() for phone_number in phone_numbers]

    # Save the phone numbers to a JSON file
    with open(output_path, 'w') as f:
        json.dump(phone_numbers, f)

    return phone_numbers