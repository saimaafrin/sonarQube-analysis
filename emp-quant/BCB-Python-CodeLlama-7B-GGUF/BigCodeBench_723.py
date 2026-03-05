
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

    # Find the table in the HTML content
    table = soup.find('table')

    # Extract the data from the table
    data = []
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    # Write the data to a CSV file
    with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    # Return the path of the CSV file
    return CSV_FILE_PATH