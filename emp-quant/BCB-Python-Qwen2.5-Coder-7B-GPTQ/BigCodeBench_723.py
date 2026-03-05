import urllib.request
from bs4 import BeautifulSoup
import csv
import os
CSV_FILE_PATH = 'scraped_data.csv'
def task_func(url):
    # Send a request to the URL
    response = urllib.request.urlopen(url)
    html = response.read()
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all the data you want to scrape (e.g., all <p> tags)
    data = soup.find_all('p')
    
    # Open a CSV file to write the scraped data
    with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(['Data'])
        
        # Write the scraped data to the CSV file
        for item in data:
            writer.writerow([item.get_text()])
    
    # Return the path of the CSV file
    return CSV_FILE_PATH