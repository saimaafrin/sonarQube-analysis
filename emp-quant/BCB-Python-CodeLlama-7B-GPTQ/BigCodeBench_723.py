import urllib.request
from bs4 import BeautifulSoup
import csv
import os
CSV_FILE_PATH = 'scraped_data.csv'
def task_func(url):
    # Create a CSV writer
    with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Scrape data from the given URL
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Extract the data from the HTML
        data = []
        for row in soup.find_all('tr'):
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append(cols)

        # Write the data to the CSV file
        for row in data:
            csvwriter.writerow(row)

    # Return the path of the CSV file
    return CSV_FILE_PATH
url = 'https://www.example.com'