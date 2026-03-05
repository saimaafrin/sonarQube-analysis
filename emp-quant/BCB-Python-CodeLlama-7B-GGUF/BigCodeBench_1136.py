
import bs4
import requests
import re
import csv

def task_func(url="http://example.com", csv_path="emails.csv", 
          regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
          headers={'User-Agent': 'Mozilla/5.0'}):
    # Send a request to the URL and get the HTML response
    response = requests.get(url, headers=headers)
    # Parse the HTML content using BeautifulSoup
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    # Find all the email addresses in the HTML content
    emails = re.findall(regex, soup.text)
    # Create a CSV file with the header "Emails"
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Emails'])
        for email in emails:
            writer.writerow([email])
    return csv_path