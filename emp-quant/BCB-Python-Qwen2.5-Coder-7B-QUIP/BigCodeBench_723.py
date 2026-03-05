
import urllib.request
from bs4 import BeautifulSoup
import csv
import os
# Constants
CSV_FILE_PATH = 'scraped_data.csv'
def task_func(url):
    # Send a GET request to the URL
    with urllib.request.urlopen(url) as response:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response, 'html.parser')
        
        # Extract data from the page (this is a simple example, you may need to adjust based on the website's structure)
        data = []
        for row in soup.find_all('tr'):
            cells = row.find_all('td')
            if len(cells) == 2:
                data.append([cell.text.strip() for cell in cells])
        
        # Write the data to a CSV file
        with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        
        # Return the path of the CSV file
        return CSV_FILE_PATH