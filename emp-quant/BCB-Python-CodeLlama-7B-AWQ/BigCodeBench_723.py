import urllib.request
from bs4 import BeautifulSoup
import csv
import os
CSV_FILE_PATH = 'scraped_data.csv'
def task_func(url):
    # Create a CSV file if it does not exist
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['title', 'description', 'price'])

    # Scrape data from the given URL
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all('div', {'class': 'product'})

    # Write scraped data to the CSV file
    with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for product in products:
            title = product.find('h2', {'class': 'title'}).text.strip()
            description = product.find('p', {'class': 'description'}).text.strip()
            price = product.find('span', {'class': 'price'}).text.strip()
            writer.writerow([title, description, price])

    return CSV_FILE_PATH
url = 'https://example.com'