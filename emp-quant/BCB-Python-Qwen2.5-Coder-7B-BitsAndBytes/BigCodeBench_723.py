
import urllib.request
from bs4 import BeautifulSoup
import csv
import os

# Constants
CSV_FILE_PATH = 'scraped_data.csv'

def task_func(url):
    # Send HTTP request to the URL
    response = urllib.request.urlopen(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.read(), 'html.parser')
    
    # Find all the table rows in the HTML
    rows = soup.find_all('tr')
    
    # Open a CSV file for writing
    with open(CSV_FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write each row to the CSV file
        for row in rows:
            writer.writerow([cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])])
    
    return CSV_FILE_PATH