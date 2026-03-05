
import urllib.request
from bs4 import BeautifulSoup
import csv
import os
# Constants
CSV_FILE_PATH = 'scraped_data.csv'

def task_func(url):
    # Get the HTML content of the page
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(), 'html.parser')

    # Create a CSV file
    with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write the header row
        csvwriter.writerow(['Title', 'Description', 'Price'])

        # Iterate over the rows and write them to the CSV file
        for row in soup.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 3:
                csvwriter.writerow([cells[0].text, cells[1].text, cells[2].text])

    # Return the path of the CSV file
    return CSV_FILE_PATH