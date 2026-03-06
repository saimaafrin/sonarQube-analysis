
import urllib.request
from bs4 import BeautifulSoup
import csv
import os

# Constants
CSV_FILE_PATH = 'scraped_data.csv'

def task_func(url):
    # Open the URL and read the HTML content
    with urllib.request.urlopen(url) as response:
        html = response.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the table on the page
    table = soup.find('table')

    # Create a CSV writer
    with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row
        writer.writerow(['Name', 'Age', 'Gender'])

        # Iterate over the rows in the table
        for row in table.find_all('tr'):
            # Get the columns for this row
            columns = row.find_all('td')

            # Write the data for this row to the CSV file
            writer.writerow([columns[0].text.strip(), columns[1].text.strip(), columns[2].text.strip()])

# Call the function with the URL to scrape
task_func('https://www.example.com')