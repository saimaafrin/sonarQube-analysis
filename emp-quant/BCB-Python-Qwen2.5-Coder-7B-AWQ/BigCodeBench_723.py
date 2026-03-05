import urllib.request
from bs4 import BeautifulSoup
import csv
import os
CSV_FILE_PATH = 'scraped_data.csv'
def task_func(url):
    # Send a GET request to the URL
    response = urllib.request.urlopen(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response, 'html.parser')
    # Find all the data rows in the table
    rows = soup.find_all('tr')
    # Open a CSV file for writing
    with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow([th.text for th in rows[0].find_all('th')])
        # Write the data rows
        for row in rows[1:]:
            writer.writerow([td.text for td in row.find_all('td')])
    # Return the path of the CSV file
    return CSV_FILE_PATH