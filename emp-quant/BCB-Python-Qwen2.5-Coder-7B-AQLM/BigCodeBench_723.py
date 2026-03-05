
import urllib.request
from bs4 import BeautifulSoup
import csv
import os

# Constants
CSV_FILE_PATH = 'scraped_data.csv'

def task_func(url):
    # Send a request to the URL
    response = urllib.request.urlopen(url)
    html = response.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the data you want to scrape (e.g., all <p> tags)
    data = soup.find_all('p')

    # Write the scraped data to a CSV file
    with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Scraped Data'])  # Write the header
        for item in data:
            writer.writerow([item.get_text()])  # Write each item as a row

    return CSV_FILE_PATH