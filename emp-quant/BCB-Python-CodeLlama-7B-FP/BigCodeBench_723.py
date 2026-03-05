import urllib.request
from bs4 import BeautifulSoup
import csv
import os
CSV_FILE_PATH = 'scraped_data.csv'
def task_func(url):
    # Create a CSV file if it does not exist
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
            fieldnames = ['title', 'price', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    # Scrape data from the given URL
    with urllib.request.urlopen(url) as response:
        soup = BeautifulSoup(response.read(), 'html.parser')

    # Extract data from the HTML
    titles = [title.text.strip() for title in soup.find_all('h1')]
    prices = [price.text.strip() for price in soup.find_all('span', {'class': 'price'})]
    descriptions = [description.text.strip() for description in soup.find_all('p')]

    # Write data to the CSV file
    with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
        fieldnames = ['title', 'price', 'description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for title, price, description in zip(titles, prices, descriptions):
            writer.writerow({'title': title, 'price': price, 'description': description})

    # Return the path of the CSV file
    return CSV_FILE_PATH
url = 'https://www.example.com'