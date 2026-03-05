
import bs4
import requests
import re
import csv

def task_func(url="http://example.com", csv_path="emails.csv", 
              regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
              headers={'User-Agent': 'Mozilla/5.0'}):
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes

    # Parse the HTML content of the page
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # Find all text in the page
    text = soup.get_text()

    # Use regular expression to find all email addresses
    emails = re.findall(regex, text)

    # Write the emails to a CSV file
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Emails'])
        writer.writerow(emails)

    return csv_path