import bs4
import requests
import re
import csv
def task_func(url="http://example.com", csv_path="emails.csv", 
              regex=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", 
              headers={'User-Agent': 'Mozilla/5.0'}):
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    # Parse the HTML content of the page
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # Find all text in the page
    text = soup.get_text()
    # Find all email addresses using the specified regular expression
    emails = re.findall(regex, text)
    # Write the email addresses to a CSV file
    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Emails'])
        for email in emails:
            writer.writerow([email])
    # Return the path to the CSV file
    return csv_path